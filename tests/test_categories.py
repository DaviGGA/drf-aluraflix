from urllib import request
from django.contrib.auth.models import User
from django.urls import reverse
from unittest import TestCase
import pytest
from rest_framework.test import APIClient
from api.models import Video, Category

class CategoriesTestCase(TestCase):
    
    def setUp(self):
        
        self.client = APIClient()

        self.test_user = User.objects.create_user(
            username = 'TestUser',
            password = '123'
        )
    
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
    def get_token(self):
        token_url = "/token/"
        payload = {'username' : 'TestUser', 'password' : '123'}
        response_token =self.client.post(token_url,payload)
        token = response_token.data
    
        return token


    @pytest.mark.django_db
    def test_get_category(self):
        token = self.get_token()
        header = f"Bearer {token['access']}"
       
        url = reverse('categories') 
        response = self.client.get(url,HTTP_AUTHORIZATION=header, format='json')
    
        assert response.status_code == 200

    @pytest.mark.django_db
    def test_get_by_id_category(self):
        token = self.get_token()
        header = f"Bearer {token['access']}"

        url = f'/categories/{self.category_test.id}/'
        response = self.client.get(url,HTTP_AUTHORIZATION=header, format='json')
        
        assert response.status_code == 200
    
    @pytest.mark.django_db
    def test_get_video_by_id_category(self):
        token = self.get_token()
        header = f"Bearer {token['access']}"
        
        url = f'/categories/{self.category_test.id}/videos'
        response = self.client.get(url,HTTP_AUTHORIZATION=header, format='json')
        
        assert response.status_code == 200
    
    @pytest.mark.django_db
    def test_get_by_id_category_that_doesnt_exist(self):
        token = self.get_token()
        header = f"Bearer {token['access']}"
        url = '/categories/999/'
        
        response = self.client.get(url,HTTP_AUTHORIZATION=header, format='json')
        assert response.status_code == 404

    @pytest.mark.django_db
    def test_post_category(self):
        token = self.get_token()
        header = f"Bearer {token['access']}"
        
        url = reverse('categories')
        data = {
            'title' : 'New category',
            'color' : '#fdfdfd',
        }
        
        response = self.client.post(url, data,HTTP_AUTHORIZATION=header, format='json')
        assert response.status_code == 201

    @pytest.mark.django_db
    def test_post_category_with_repeated_title(self):
        token = self.get_token()
        header = f"Bearer {token['access']}"
        
        url = reverse('categories')
        data = {
            'title' : 'Test',
            'color' : '#fdfdfd',
        }

        response = self.client.post(url, data,HTTP_AUTHORIZATION=header, format='json')
        assert response.status_code == 400

    @pytest.mark.django_db
    def test_put_category(self):
        token = self.get_token()
        header = f"Bearer {token['access']}"
       
        url = f'/categories/{self.category_test.id}/'
        data = {
            'title' : 'New PUT Category',
            'color' : '#000000',
        }
        
        response = self.client.put(url, data,HTTP_AUTHORIZATION=header, format='json')
        assert response.status_code == 200
   
    @pytest.mark.django_db
    def test_put_category_when_his_title_alrealdy_exist(self):
        token = self.get_token()
        header = f"Bearer {token['access']}"
        
        url = f'/categories/{self.category_test.id}/'
        data = {
            'title' : 'Test',
            'description' : 'changed using PUT method',
            'url' : 'https://www.youtube.com/'
        }
        
        response = self.client.put(url, data,HTTP_AUTHORIZATION=header, format='json')
        assert response.status_code == 400

    @pytest.mark.django_db
    def test_patch_category(self):
        token = self.get_token()
        header = f"Bearer {token['access']}"
        
        url = f'/categories/{self.category_test.id}/'
        data = {
            'title' : ' PATCH Test',
            'description' : 'Test case description',
            'url' : 'https://www.youtube.com/'
        }
        
        response = self.client.patch(url, data,HTTP_AUTHORIZATION=header, format='json')
        assert response.status_code == 200

    @pytest.mark.django_db
    def test_delete_category(self):
        token = self.get_token()
        header = f"Bearer {token['access']}"
        
        url = f'/videos/{self.video_test.id}/'
        data = self.client.get(url).data
        
        response = self.client.delete(url, data,HTTP_AUTHORIZATION=header, format='json')
        assert response.status_code == 204


    