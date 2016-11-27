from astmonkey import transformers
import ast
import ujson
from django.core.management.base import BaseCommand
from app.models import (CodeTestItem, RelationCodeItem, FreqRelationCodeItem)
from app.management.commands.validate import remove_explicit_indent
from app.management.commands.load_code_items import DepthVisitor


class Command(BaseCommand):
    def handle(self, *args, **options):
        data = ujson.loads(open('drf_smother.json').read())
        for d in data:
            source_code = remove_explicit_indent(d['source_code'])
            test_code = remove_explicit_indent(d['test_code'])

            print(source_code)
            print(test_code)

            hv = DepthVisitor()
            tree = ast.parse(source_code)
            tree = transformers.ParentNodeTransformer().visit(tree)
            hv.visit(tree)
            source_depth = hv.depth

            hv = DepthVisitor()
            tree = ast.parse(test_code)
            tree = transformers.ParentNodeTransformer().visit(tree)
            hv.visit(tree)
            test_depth = hv.depth

            CodeTestItem.objects.get_or_create(
                source_code=source_code,
                test_code=test_code,
                source_depth=source_depth,
                test_depth=test_depth
            )
