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

        res = self.client.get(reverse('task-detail', args=(task.id,)))
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

    def test_create_task(self):
        """
        タスクを１つ作成できる
        """
        data = {
            'name': '作成テスト',
            'expirationDm': '2020-08-30',
            'status': 'OPEN'
        }
        res = self.client.post(
            reverse('task-list'),
            json.dumps(data),
            content_type='application/json'
        )

        actual = Task.objects.get(name='作成テスト')
        self.assertEqual(Task.objects.count(), 1)
        self.assertEqual(actual.name, '作成テスト')

    def test_update_task(self):
        """
        タスクを更新できる
        """
        task = Task.objects.create(
            name = '更新テスト',
            expiration_dm = '2020-08-30',
            status = 'OPEN'
        )

        res = self.client.put(
            reverse('task-detail', args=(task.id,)),
            json.dumps({
                'id': task.id,
                'name': '更新済み',
                'expirationDm': task.expiration_dm,
                'status': 'CLOSED',
            }),
            content_type='application/json'
        )

        task.refresh_from_db()
        self.assertEqual(Task.objects.count(), 1)
        self.assertEqual(Task.objects.get().name, '更新済み')
        self.assertEqual(Task.objects.get().status, 'CLOSED')

    def test_delete_task(self):
        """
        タスクを削除できる
        """
        task = Task.objects.create(
            name = '削除テスト',
            expiration_dm = '2020-08-30',
            status = 'OPEN'
        )

        res = self.client.delete(
            reverse("task-detail", args=(task.id,)),
            json.dumps({ 'id': task.id }),
            content_type='application/json'
        )
        self.assertEqual(Task.objects.count(), 0)

    def test_404_task(self):
        """
        タスクが見つからなかったとき404を返す
        """
        task = Task.objects.create(
            name = '404テスト',
            expiration_dm = '2020-08-27',
            status = 'OPEN'
        )

        res = self.client.get(reverse('task-detail', args=(9999,)))
        self.assertEqual(res.status_code, 404)
