from collections import Counter
from astmonkey import transformers
from app.management.commands.visit_ast_for_items import remove_explicit_indent
from app.models import (CodeItem, FreqRelationCodeItem)
import ast


class DepthVisitor(ast.NodeVisitor):
    connections = []
    depth = 0
    body_length = 0

    def generic_visit(self, node):
        start_type = node.__class__.__name__
        if node.__class__.__name__ == 'FunctionDef':
            self.body_length = len(node.body)
        parent = node.parent
        depth = 0
        if parent:
            end_type = node.parent.__class__.__name__
            link_type = node.parent_field
            self.connections.append({
                'start_type': start_type,
                'link_type': link_type,
                'end_type': end_type
            })
            while parent:
                depth += 1
                parent = parent.parent
            self.depth = max(self.depth, depth)
        ast.NodeVisitor.generic_visit(self, node)


def get_most_frequent(ids, num=1):
    counter = Counter(ids)
    return counter.most_common(num)


def get_similar_code_items(source_code, count=1):
    source_code = remove_explicit_indent(source_code)
    hv = DepthVisitor()
    tree = ast.parse(source_code)
    tree = transformers.ParentNodeTransformer().visit(tree)
    hv.visit(tree)
    freq_connections = []
    for conn in hv.connections:
        conn['freq'] = hv.connections.count(conn)
        freq_connections.append(conn)
    matched_ids = []
    for fc in freq_connections:
        matched_ids.extend(FreqRelationCodeItem.objects.filter(
            start_type=fc['start_type'],
            link_type=fc['link_type'],
            end_type=fc['end_type'],
            freq=fc['freq']
        )
        .filter(
            code_test_item__source_code__source_depth=hv.depth,
            code_test_item__source_code__body_length=hv.body_length,
            # code_test_item__source_code__body_length__gte=hv.body_length-2,
            # code_test_item__source_code__body_length__lte=hv.body_length+2,
        )
        .values_list('code_test_item__source_code__id', flat=True))
    if count == 1:
        best_matched_id, best_rank = get_most_frequent(matched_ids)[0]
        best_matched_code = CodeItem.objects.get(pk=best_matched_id)
        return best_matched_code
    else:
        return [item for item in get_most_frequent(matched_ids, 100)]
