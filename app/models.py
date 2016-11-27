from __future__ import unicode_literals
import json

from django.db import models


# Create your models here.
class ProcessedLine(models.Model):
    smother_name = models.CharField(max_length=100)
    line_source = models.TextField()
    line_test = models.TextField()


class CodeItem(models.Model):
    source_code = models.TextField()
    source_depth = models.IntegerField(default=0)
    body_length = models.IntegerField(default=0)


class TestItem(models.Model):
    test_code = models.TextField()
    test_depth = models.IntegerField(default=0)

    def get_test_name(self):
        line = self.test_code.splitlines()[0]
        if '@' in line:
            line = self.test_code.splitlines()[1]
        func = line.split('def ')[1]
        name = func.split('(')[0]
        return name


class CodeTestItem(models.Model):
    source_code = models.ForeignKey(CodeItem)
    test_code = models.ForeignKey(TestItem)
    # source_code = models.TextField()
    # test_code = models.TextField()
    # source_depth = models.IntegerField(default=0)
    # test_depth = models.IntegerField(default=0)


class RelationCodeItem(models.Model):
    start_type = models.CharField(max_length=100)
    end_type = models.CharField(max_length=100)
    link_type = models.CharField(max_length=100)
    code_test_item = models.ForeignKey(CodeTestItem)


class FreqRelationCodeItem(models.Model):
    start_type = models.CharField(max_length=100)
    end_type = models.CharField(max_length=100)
    link_type = models.CharField(max_length=100)
    freq = models.BigIntegerField(default=0)
    code_test_item = models.ForeignKey(CodeTestItem)


class RelationTestItem(models.Model):
    start_type = models.CharField(max_length=100)
    end_type = models.CharField(max_length=100)
    link_type = models.CharField(max_length=100)
    code_test_item = models.ForeignKey(CodeTestItem)


class FreqRelationTestItem(models.Model):
    start_type = models.CharField(max_length=100)
    end_type = models.CharField(max_length=100)
    link_type = models.CharField(max_length=100)
    freq = models.BigIntegerField(default=0)
    code_test_item = models.ForeignKey(CodeTestItem)


class MatrixTestItem(models.Model):
    test_code = models.TextField()
    matrix = models.TextField(default='[]')
    matrix_size = models.IntegerField(default=1)

    def set_matrix(self, m):
        self.matrix = json.dumps(m)

    def get_matrix(self):
        return json.loads(self.matrix)
