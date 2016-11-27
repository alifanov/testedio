import csv
import imp
import ast
import astdump
import inspect
from django.core.management.base import BaseCommand, CommandError
from app.models import (CodeTestItem, RelationCodeItem, RelationTestItem)
from django.conf import settings
from astmonkey import transformers
from app.utils import BUILTIN_FUNCTIONS


def remove_explicit_indent(s):
    first_line = ''
    if '\n' in s:
        lines = s.split('\n')
        first_line = lines[0]
    else:
        first_line = s
    n = 0
    for c in first_line:
        if c != ' ':
            break
        n += 1
    if '\n' in s:
        modified_lines = []
        lines = s.split('\n')
        for line in lines:
            modified_lines.append(
                line[n:]
            )
        return '\n'.join(modified_lines)
    else:
        return s[n:]


class RelationVisitor(ast.NodeVisitor):
    code = None
    model = None

    def __init__(self, code, model):
        self.code = code
        self.model = model

    def generic_visit(self, node):
        start_type = node.__class__.__name__
        parent = node.parent
        if parent:
            end_type = parent.__class__.__name__
            if start_type == 'Name':
                if node.id in BUILTIN_FUNCTIONS:
                    start_type = node.id
            if end_type == 'Name':
                if parent.id in BUILTIN_FUNCTIONS:
                    end_type = parent.id
            link_type = node.parent_field
            self.model.objects.create(
                start_type=start_type,
                end_type=end_type,
                link_type=link_type,
                code_test_item=self.code
            )
        ast.NodeVisitor.generic_visit(self, node)


class Command(BaseCommand):
    def handle(self, *args, **options):
        for c in CodeTestItem.objects.all():
            code = c.source_code.source_code
            hv = RelationVisitor(c, RelationCodeItem)
            tree = ast.parse(code)
            tree = transformers.ParentNodeTransformer().visit(tree)
            hv.visit(tree)

            code = c.test_code.test_code
            hv = RelationVisitor(c, RelationTestItem)
            tree = ast.parse(code)
            tree = transformers.ParentNodeTransformer().visit(tree)
            hv.visit(tree)

