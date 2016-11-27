from django.core.management.base import BaseCommand, CommandError
from app.models import (CodeTestItem, RelationCodeItem, FreqRelationCodeItem, FreqRelationTestItem, RelationTestItem)
from django.conf import settings
from django.db.models import Count


class Command(BaseCommand):
    def handle(self, *args, **options):
        for rel in RelationCodeItem.objects.values('start_type', 'link_type', 'end_type', 'code_test_item').annotate(Count('id')):
            FreqRelationCodeItem.objects.create(
                start_type=rel['start_type'],
                end_type=rel['end_type'],
                link_type=rel['link_type'],
                code_test_item=CodeTestItem.objects.get(pk=rel['code_test_item']),
                freq=rel['id__count']
            )

        for rel in RelationTestItem.objects.values('start_type', 'link_type', 'end_type', 'code_test_item').annotate(Count('id')):
            FreqRelationTestItem.objects.create(
                start_type=rel['start_type'],
                end_type=rel['end_type'],
                link_type=rel['link_type'],
                code_test_item=CodeTestItem.objects.get(pk=rel['code_test_item']),
                freq=rel['id__count']
            )


