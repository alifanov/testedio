import ast
from astmonkey import transformers
from django.core.management.base import BaseCommand
from app.models import (CodeItem)
from app.core import DepthVisitor


class Command(BaseCommand):
    def handle(self, *args, **options):
        for code in CodeItem.objects.all():
            dv = DepthVisitor()
            tree = ast.parse(code.source_code)
            tree = transformers.ParentNodeTransformer().visit(tree)
            dv.visit(tree)
            code.source_depth = dv.depth
            code.save()
