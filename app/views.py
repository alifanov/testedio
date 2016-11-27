from astmonkey import transformers
import ast
from django.views.generic import View, TemplateView
from django.http import HttpResponse
from django.shortcuts import render
import ujson
from app.models import (RelationCodeItem, FreqRelationCodeItem, CodeTestItem, FreqRelationTestItem, CodeItem)
from app.core import Counter, DepthVisitor, remove_explicit_indent, get_similar_code_items


# Create your views here.


class FindCodeView(View):
    def post(self, request, *args, **kwargs):
        data = []
        origin_code = ujson.loads(request.body)['data']
        code = remove_explicit_indent(origin_code)
        code_items = get_similar_code_items(code, 10)

        # filtered_common = [cm for cm in counter.most_common(100) if abs(CodeItem.objects.get(pk=cm[0]).source_depth - depth) < 10]
        for item in code_items:
            code_item = CodeItem.objects.get(pk=item[0])
            data.append({
                'rank': item[1],
                'code': code_item.source_code,
                'depth': code_item.source_depth,
                'body_length': code_item.body_length,
                'tests': [{
                    'name': ct.test_code.get_test_name(),
                    'test': ct.test_code.test_code
                } for ct in CodeTestItem.objects.filter(source_code=code_item)]
            })
        return HttpResponse(ujson.dumps(data), content_type='application/json')


class FindTestView(View):
    def post(self, request, *args, **kwargs):
        data = []
        origin_code = ujson.loads(request.body)['data']
        code = remove_explicit_indent(origin_code)
        hv = DepthVisitor(code)
        tree = ast.parse(code)
        tree = transformers.ParentNodeTransformer().visit(tree)
        hv.visit(tree)
        depth = hv.depth
        freq_connections = []
        for conn in hv.connections:
            conn['freq'] = hv.connections.count(conn)
            freq_connections.append(conn.copy())
        matched_ids = []
        for fc in freq_connections:
            matched_ids.extend(FreqRelationTestItem.objects.filter(
                start_type=fc['start_type'],
                link_type=fc['link_type'],
                end_type=fc['end_type'],
                freq=fc['freq']
            ).values_list('code_test_item_id', flat=True))

        counter = Counter(matched_ids)
        filtered_common = [cm for cm in counter.most_common(10) if
                           abs(CodeTestItem.objects.get(pk=cm[0]).test_depth - depth) < 3]
        for item in filtered_common:
            code_item = CodeTestItem.objects.get(pk=item[0])
            data.append({
                'rank': item[1],
                'code': remove_explicit_indent(code_item.source_code),
                'test': remove_explicit_indent(code_item.test_code)
            })
        return HttpResponse(ujson.dumps(data), content_type='application/json')


def add(a, b):
    return a + b


def max_in_list(l):
    return max(l)


def min_in_list(l):
    return min(l)


def fact(a):
    if a == 0: return 1
    return a * fact(a - 1)


def hello(name, suffix='!'):
    return 'Hello, {}{}'.format(name, suffix)


class IndexView(View):
    def get(self, request, *args, **kwargs):
        return HttpResponse('OK')


class SortView(View):
    def get(self, request, *args, **kwargs):
        data = [2, 1, 3, 5, 6, 7, 8, 9, 10, 4]
        sort = self.request.GET.get('sort')
        if sort == 'up':
            data = sorted(data)
        if sort == 'down':
            data = sorted(data, reverse=True)
        return HttpResponse(ujson.dumps(data),
                            content_type='application/json')
