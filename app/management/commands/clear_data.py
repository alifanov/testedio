from django.core.management.base import BaseCommand
from app.models import (CodeTestItem, RelationCodeItem, FreqRelationCodeItem, ProcessedLine, CodeItem, TestItem, FreqRelationTestItem)


class Command(BaseCommand):
    def handle(self, *args, **options):
        for model in [RelationCodeItem, FreqRelationCodeItem, ProcessedLine, CodeTestItem, FreqRelationTestItem]:
            model.objects.all().delete()
