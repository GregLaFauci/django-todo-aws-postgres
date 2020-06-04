from django.urls import reverse, resolve
from django.test import RequestFactory
from tasks.models import Task
import pytest

from django.contrib.auth.models import User

from tasks import views

class TestTasks:

    def test_home_page_url(self):
        path = reverse('list')
        assert resolve(path).view_name == 'list'

    def test_update_task(self):
        path = reverse('update_task', args=[3])
        assert resolve(path).view_name == 'update_task'


    @pytest.mark.django_db
    def test_save(self):
        test_task = Task(title="Test_Task")
        test_task.save()
        assert test_task.title == "Test_Task"

    @pytest.mark.django_db
    def test_view(client):
        req = RequestFactory().get(reverse('list'))
        resp = views.index(req)
        assert resp.status_code == 200


    @pytest.mark.django_db
    def test_create_user(self):
        User.objects.create_user('john', 'lennon@thebeatles.com', 'johnpassword')
        assert User.objects.count() == 1




