from rest_framework import serializers
from .models import SpellCheck
from textblob import TextBlob


class SpellCheckSerializer(serializers.ModelSerializer):
    correct = serializers.SerializerMethodField(method_name='check')

    def check(self, spell_check: SpellCheck):
        text = spell_check.text
        correct = TextBlob(text)
        return str(correct.correct())

    class Meta:
        model = SpellCheck
        fields = ['text', 'correct']
