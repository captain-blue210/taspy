import json

from django.test import TestCase
from django.urls import reverse
from rest_framework.test import APIRequestFactory

from taspy.models import Task


class TaskTests(TestCase):
    def test_get_task(self):
        """
        タスクを１つ取得できる
        """
        task = Task.objects.create(
            name = 'テスト',
            expiration_dm = '2020-08-27',
            status = 'OPEN'
        )

        res = self.client.get(reverse('task-detail', args=(1,)))
        self.assertContains(res, 'テスト')
        self.assertContains(res, '2020-08-27')
        self.assertContains(res, 'OPEN')

    def test_get_task_list(self):
        """
        タスクを3つ取得できる（リスト取得）
        """
        task1 = Task.objects.create(
            name = 'テスト1',
            expiration_dm = '2020-08-27',
            status = 'OPEN'
        )
        task2 = Task.objects.create(
            name = 'テスト2',
            expiration_dm = '2020-08-28',
            status = 'OPEN'
        )
        task3 = Task.objects.create(
            name = 'テスト3',
            expiration_dm = '2020-08-29',
            status = 'OPEN'
        )

        res = self.client.get(reverse('task-list'))
        data = json.dumps(res.data, ensure_ascii=False)
        data_list = json.loads(data)
        self.assertEqual(data_list[0]['name'], task1.name)
        self.assertEqual(data_list[1]['name'], task2.name)
        self.assertEqual(data_list[2]['name'], task3.name)

