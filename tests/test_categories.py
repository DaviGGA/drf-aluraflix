from urllib import request
from django.urls import reverse
from unittest import TestCase
import pytest
from rest_framework.test import APIClient
from api.models import Video, Category

class CategoriesTestCase(TestCase):
    
    def setUp(self):
        
        self.client = APIClient()
    
        self.category_free = Category.objects.create(
        title = 'FREE',
        color = '#ffffff',
        )

        self.category_test = Category.objects.create(
        title = 'Test',
        color = '#fdfdfd',
        id = 2
        )
        self.video_test = Video.objects.create(
        title = 'Video Test Case',
        description = 'Test case description',
        url = 'https://www.youtube.com/',
        category = self.category_test
        )



    @pytest.mark.django_db
    def test_get_category(self):
        url = reverse('categories')
        
        response = self.client.get(url)
        assert response.status_code == 200

    @pytest.mark.django_db
    def test_get_by_id_category(self):
        url = f'/categories/{self.category_test.id}/'
        
        response = self.client.get(url)
        assert response.status_code == 200
    
    @pytest.mark.django_db
    def test_get_video_by_id_category(self):
        url = f'/categories/{self.category_test.id}/videos'
        
        response = self.client.get(url)
        assert response.status_code == 200
    
    @pytest.mark.django_db
    def test_get_by_id_category_that_doesnt_exist(self):
        url = '/categories/999/'
        
        response = self.client.get(url)
        assert response.status_code == 404

    @pytest.mark.django_db
    def test_post_category(self):
        url = reverse('categories')
        data = {
            'title' : 'New category',
            'color' : '#fdfdfd',
        }
        
        response = self.client.post(url, data)
        assert response.status_code == 201

    @pytest.mark.django_db
    def test_post_category_with_repeated_title(self):
        url = reverse('categories')
        data = {
            'title' : 'Test',
            'color' : '#fdfdfd',
        }

        response = self.client.post(url,data)
        assert response.status_code == 400

    @pytest.mark.django_db
    def test_put_category(self):
        url = f'/categories/{self.category_test.id}/'
        data = {
            'title' : 'New PUT Category',
            'color' : '#000000',
        }
        
        response = self.client.put(url, data)
        assert response.status_code == 200
   
    @pytest.mark.django_db
    def test_put_category_when_his_title_alrealdy_exist(self):
        url = f'/categories/{self.category_test.id}/'
        data = {
            'title' : 'Test',
            'description' : 'changed using PUT method',
            'url' : 'https://www.youtube.com/'
        }
        
        response = self.client.put(url, data)
        assert response.status_code == 400

    @pytest.mark.django_db
    def test_patch_category(self):
        url = f'/categories/{self.category_test.id}/'
        data = {
            'title' : ' PATCH Test',
            'description' : 'Test case description',
            'url' : 'https://www.youtube.com/'
        }
        
        response = self.client.patch(url, data)
        assert response.status_code == 200

    @pytest.mark.django_db
    def test_delete_category(self):
        url = f'/videos/{self.video_test.id}/'
        data = self.client.get(url).data
        
        response = self.client.delete(url, data)
        assert response.status_code == 204


    