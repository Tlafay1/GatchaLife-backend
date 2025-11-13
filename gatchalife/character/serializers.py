from .models import Character, Variant, Attachment
from rest_framework import serializers


class AttachmentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Attachment
        fields = ["id", "name", "image"]


class VariantSerializer(serializers.ModelSerializer):
    images = AttachmentSerializer(many=True, read_only=True)

    class Meta:
        model = Variant
        fields = ["id", "name", "description", "images"]


class CharacterSerializer(serializers.ModelSerializer):
    variants = VariantSerializer(many=True, read_only=True)
    images = AttachmentSerializer(many=True, read_only=True)

    class Meta:
        model = Character
        fields = ["id", "name", "description", "images", "variants"]
