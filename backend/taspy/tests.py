from django.test import TestCase
from django.urls import reverse

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

        res = self.client.get(reverse('task-list'))
        self.assertContains(res, 'テスト')
        self.assertContains(res, '2020-08-27')
        self.assertContains(res, 'OPEN')
