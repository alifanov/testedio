from astmonkey import transformers
import ast
from django.core.management.base import BaseCommand, CommandError
from app.models import (CodeTestItem, RelationCodeItem, FreqRelationCodeItem, FreqRelationTestItem)
from app.core import get_similar_code_items


class Command(BaseCommand):
    def handle(self, *args, **options):
        for item in CodeTestItem.objects.all()[:10]:
            print(item.source_code.source_code)
            matched = get_similar_code_items(item.source_code.source_code)
            assert matched.pk == item.source_code.pk
        print('Validating passed')