from django.db import models


class Series(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField(blank=True)

    def __str__(self):
        return self.name


# An anime character, with support for multiple variants
class Character(models.Model):
    name = models.CharField(max_length=100)
    series = models.ForeignKey(
        Series, related_name="characters", on_delete=models.CASCADE
    )
    description = models.TextField(blank=True)

    images = models.ManyToManyField("Attachment", blank=True)

    def __str__(self):
        return self.name


class Variant(models.Model):
    character = models.ForeignKey(
        Character, related_name="variants", on_delete=models.CASCADE
    )
    name = models.CharField(max_length=100)
    description = models.TextField(blank=True)

    images = models.ManyToManyField("Attachment", blank=True)

    def __str__(self):
        return f"{self.character.name} - {self.name}"


class Attachment(models.Model):
    name = models.CharField(max_length=100)

    image = models.ImageField()

    def __str__(self):
        return f"{self.name}"
