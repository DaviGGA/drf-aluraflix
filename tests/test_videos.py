from urllib import request
from django.contrib.auth.models import User
from rest_framework_simplejwt.tokens import RefreshToken
from django.urls import reverse
from unittest import TestCase
import pytest
from rest_framework.test import APIClient
from api.models import Video, Category



class VideosTestCase(TestCase):

    def setUp(self):

        self.test_user = User.objects.create_user(
            username = 'TestUser',
            password = '123'
        )

        self.client = APIClient()

        self.category_free = Category.objects.create(
            title = 'FREE',
            color = '#ffffff',
        )
       
        self.video_test = Video.objects.create(
            title = 'Video Test Case',
            description = 'Test case description',
            url = 'https://www.youtube.com/'
        )
        self.video_test2 = Video.objects.create(
            title = 'Video Test Case 2',
            description = 'Test case description 2',
            url = 'https://www.youtube.com/'
        )

    @pytest.mark.django_db
    def get_token(self):
        token_url = "/token/"
        payload = {'username' : 'TestUser', 'password' : '123'}
        response_token =self.client.post(token_url,payload)
        token = response_token.data
    
        return token

    @pytest.mark.django_db
    def test_get_video(self):
        token = self.get_token()
        header = f"Bearer {token['access']}"
        
        url = reverse('videos')
        response = self.client.get(url,HTTP_AUTHORIZATION=header, format='json')
    
        assert response.status_code == 200

    @pytest.mark.django_db
    def test_get_by_id_video(self):
        token = self.get_token()
        header = f"Bearer {token['access']}"

        url = f'/videos/{self.video_test.id}/'
        response = self.client.get(url,HTTP_AUTHORIZATION=header, format='json')
        
        assert response.status_code == 200
    
    @pytest.mark.django_db
    def test_get_by_id_video_that_doesnt_exist(self):
        token = self.get_token()
        header = f"Bearer {token['access']}"
        
        url = '/videos/999/'
        response = self.client.get(url,HTTP_AUTHORIZATION=header, format='json')

        assert response.status_code == 404
    
    @pytest.mark.django_db
    def test_post_video(self):
        token = self.get_token()
        header = f"Bearer {token['access']}"
        
        url = reverse('videos')
        data = {
            'title' : 'Test video',
            'description' : 'Funny test video',
            'url' : 'https://www.youtube.com/'
        }
        
        response = self.client.post(url, data, HTTP_AUTHORIZATION=header, format='json')
        assert response.status_code == 201

    @pytest.mark.django_db
    def test_post_video_with_repeated_title(self):
        token = self.get_token()
        header = f"Bearer {token['access']}"
        url = reverse('videos')
        data = {
            'title' : 'Video Test Case',
            'description' : 'test desc',
            'url' : 'https://www.youtube.com/'
        }

        response = self.client.post(url, data, HTTP_AUTHORIZATION=header, format='json')
        assert response.status_code == 400

    @pytest.mark.django_db
    def test_put_video(self):
        token = self.get_token()
        header = f"Bearer {token['access']}"

        url = f'/videos/{self.video_test.id}/'
        data = {
            'title' : 'New Video Test Case',
            'description' : 'changed using PUT method',
            'url' : 'https://www.youtube.com/'
        }
        
        response = self.client.put(url, data, HTTP_AUTHORIZATION=header, format='json')
        assert response.status_code == 200
   
    @pytest.mark.django_db
    def test_put_video_when_his_title_alrealdy_exist(self):
        token = self.get_token()
        header = f"Bearer {token['access']}"
        
        url = f'/videos/{self.video_test.id}/'
        data = {
            'title' : 'Video Test Case 2',
            'description' : 'changed using PUT method',
            'url' : 'https://www.youtube.com/'
        }
        
        response = self.client.put(url, data, HTTP_AUTHORIZATION=header, format='json')
       
        assert response.status_code == 400

    @pytest.mark.django_db
    def test_patch_video(self):
        token = self.get_token()
        header = f"Bearer {token['access']}"

        url = f'/videos/{self.video_test.id}/'
        data = {
            'title' : 'New Video Test Case',
            'description' : 'Test case description',
            'url' : 'https://www.youtube.com/'
        }
        
        response = self.client.patch(url, data, HTTP_AUTHORIZATION=header, format='json')
        assert response.status_code == 200

    @pytest.mark.django_db
    def test_delete_video(self):
        token = self.get_token()
        header = f"Bearer {token['access']}"
        
        url = f'/videos/{self.video_test.id}/'
        data = self.client.get(url).data
        
        response = self.client.delete(url, data, HTTP_AUTHORIZATION=header, format='json')
        assert response.status_code == 204

    



   