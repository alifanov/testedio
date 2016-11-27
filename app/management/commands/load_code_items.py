from astmonkey import transformers
import ast
import csv
import inspect
from django.core.management.base import BaseCommand, CommandError
import imp
from app.models import (CodeTestItem, CodeItem, TestItem, ProcessedLine)
from django.conf import settings
import os
import sys
import astor
import astunparse

# sys.path.insert(0, os.path.join(settings.BASE_DIR, 'django-rest-framework'))
from rest_framework import filters, generics, serializers, status
from rest_framework.compat import django_filters, reverse
from app.management.commands.validate import remove_explicit_indent
from app.management.commands.test_astor import SourceNodeVisitor
# from smother.python import PythonFile, Visitor


class DepthVisitor(ast.NodeVisitor):
    depth = 0

    def __init__(self):
        self.depth = 0

    def generic_visit(self, node):
        parent = node.parent
        if parent:
            while parent:
                self.depth += 1
                parent = parent.parent
        ast.NodeVisitor.generic_visit(self, node)


class Command(BaseCommand):

    def get_source_code(self, line, separator=':'):
        # if 'migrations' in line: return None
        # if '.test' in line: return None
        if not separator in line: return None
        fname, context = line.split(separator)
        fname = os.path.join('django-registration', fname.replace('.', '/') + '.py')
        code = open(fname).read()
        tree = ast.parse(code)
        v = SourceNodeVisitor(prefix='')
        v.visit(tree)
        nodes = v.nodes
        items = context.split('.')
        if len(items) > 2:
            return ''
        method = items[-1]
        try:
            source_code = nodes[method]
        except KeyError:
            return None
        # print(sc_fname)
        # pf = PythonFile(sc_fname, prefix='')
        # context = line.split(separator)[1]
        # context_range = pf.context_range(context)
        # lines = open(sc_fname).readlines()
        # source_code = lines[context_range[0] - 1:context_range[1]]
        # source_code = ''.join(source_code)
        return source_code

    def get_test_code(self, line, separator='.py'):
        if not separator in line: return None
        fname, context = line.split(separator)
        if '()' in line:
            line = line.replace('::()', '')
        # fname = os.path.join('django-registration', fname.replace('.', '/') + '.py')
        fname = os.path.join(fname.replace('.', '/') + '.py')

        code = open(fname).read()
        tree = ast.parse(code)
        v = SourceNodeVisitor(prefix='')
        v.visit(tree)
        nodes = v.nodes
        method = context.split('::')[-1]
        try:
            source_code = nodes[method]
        except KeyError:
            return None
        # print(line)
        # print(sc_fname)
        # pf = PythonFile(sc_fname, prefix='')
        # context = line.split(separator)[1].split('::')
        # context = context[1:]
        # context = '.'.join(context)
        # context_range = pf.context_range(context)
        # print(sc_fname)
        # print(context_range)
        # v = Visitor(prefix='')
        # tree = ast.parse(open(sc_fname).read())
        # code = astunparse.unparse(tree).splitlines()
        # v.visit(tree)
        # print(v.lines)
        # for i, l in enumerate(v.lines):
        #     print(i, l)
        # lines = open(sc_fname).readlines()
        # print(context, context_range)
        # lines = pf.source.splitlines()
        # source_code = code[context_range[0]:context_range[1]]
        # source_code = '\n'.join(source_code)
        # for ctx, line in zip(v.lines, code):
        #     print(line)
        # for i, l in enumerate(source_code.splitlines()):
        #     print(i+708, l)
        return source_code

    def handle(self, *args, **options):
        smother_name = 'reg_smother.csv'
        reader = csv.DictReader(open(os.path.join(settings.BASE_DIR, smother_name)))
        for row in reader:
            passed = True
            if not ProcessedLine.objects.filter(
                smother_name=smother_name,
                line_source=row['source_context'],
                line_test=row[' test_context']
            ).exists():
                for s in ['.test', 'migrations', 'tests']:
                    if row['source_context'].startswith(s):
                        passed = False
                if not passed or not row[' test_context']:
                    continue

                source_code = self.get_source_code(row['source_context'])
                test_code = self.get_test_code(row[' test_context'])

                if source_code and test_code:
                    source_code = remove_explicit_indent(source_code)
                    test_code = remove_explicit_indent(test_code)
                    # print('Source: ')
                    # print(source_code)
                    # print('Test: ')
                    # print(test_code)

                    hv = DepthVisitor()
                    try:
                        tree = ast.parse(source_code)
                    except SyntaxError:
                        print(source_code)
                        continue
                    tree = transformers.ParentNodeTransformer().visit(tree)
                    hv.visit(tree)
                    source_depth = hv.depth

                    hv = DepthVisitor()
                    tree = ast.parse(test_code)
                    tree = transformers.ParentNodeTransformer().visit(tree)
                    hv.visit(tree)
                    test_depth = hv.depth

                    code, _ = CodeItem.objects.get_or_create(
                        source_code=source_code,
                        source_depth=source_depth
                    )
                    test, _ = TestItem.objects.get_or_create(
                        test_code=test_code,
                        test_depth=test_depth
                    )
                    CodeTestItem.objects.get_or_create(
                        source_code=code,
                        test_code=test
                    )
                ProcessedLine.objects.create(
                    smother_name=smother_name,
                    line_source=row['source_context'],
                    line_test=row[' test_context']
                )
