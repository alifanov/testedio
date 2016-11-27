from django.test import TestCase
from app.models import CodeTestItem
from app.views import (add, hello, fact, min_in_list, max_in_list)
import ujson


# Create your tests here.
class SimpleTest(TestCase):
    def test_add(self):
        self.assertTrue(2 + 2 == 4)
        self.assertEqual(2 + 2, 4)


class MinMaxTest(TestCase):
    def test_min_in_list(self):
        self.assertTrue(min_in_list([-100, 1, 2, 3, 4, 10]) == -100)

    def test_max_in_list(self):
        self.assertTrue(max_in_list([1, 2, 3, 4, 10]) == 10)


class FunctionTest(TestCase):
    def test_add(self):
        self.assertTrue(add(2, 2) == 4)
        self.assertEqual(add(2, 2), 4)

    def test_fact(self):
        self.assertTrue(fact(0) == 1)
        self.assertTrue(fact(1) == 1)
        self.assertTrue(fact(2) == 2)
        self.assertTrue(fact(3) == 6)
        self.assertTrue(fact(4) == 24)

    def test_hello(self):
        self.assertTrue(hello('Vasya') == 'Hello, Vasya!')
        self.assertTrue(hello('') == 'Hello, !')
        self.assertTrue(hello(' ') == 'Hello,  !')
        self.assertTrue(hello(None) == 'Hello, None!')
        self.assertTrue(hello(1) == 'Hello, 1!')


class DjangoModelTestCase(TestCase):
    def test_create_model(self):
        item = CodeTestItem.objects.create(
            source_code='1+1',
            test_code='assert 1+1 == 2'
        )
        self.assertTrue(CodeTestItem.objects.count() > 0)
        self.assertTrue(CodeTestItem.objects.count() == 1)
        self.assertTrue(CodeTestItem.objects.all()[0].pk == item.pk)


class IndexTestCase(TestCase):
    def test_index(self):
        response = self.client.get('/index/')
        self.assertEqual(response.content, 'OK')


class SortTestCase(TestCase):
    def test_no_sort(self):
        response = self.client.get('/sort/')
        self.assertEqual(response.content,
                         ujson.dumps([2, 1, 3, 5, 6, 7, 8, 9, 10, 4]))

    def test_up_sort(self):
        response = self.client.get('/sort/?sort=up')
        self.assertEqual(response.content,
                         ujson.dumps([1, 2, 3, 4, 5, 6, 7, 8, 9, 10]))

    def test_down_sort(self):
        response = self.client.get('/sort/?sort=down')
        self.assertEqual(response.content,
                         ujson.dumps([10, 9, 8, 7, 6, 5, 4, 3, 2, 1]))
