from urllib import request
from django.urls import reverse
from unittest import TestCase
import pytest
from rest_framework.test import APIClient
from api.models import Video, Category

class VideosTestCase(TestCase):

    def setUp(self):
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
    def test_get_video(self):
        url = reverse('videos')
        
        response = self.client.get(url)
        assert response.status_code == 200

    @pytest.mark.django_db
    def test_get_by_id_video(self):
        url = f'/videos/{self.video_test.id}/'
        
        response = self.client.get(url)
        assert response.status_code == 200
    
    @pytest.mark.django_db
    def test_get_by_id_video_that_doesnt_exist(self):
        url = '/videos/999/'
        
        response = self.client.get(url)
        assert response.status_code == 404
    
    @pytest.mark.django_db
    def test_post_video(self):
        url = reverse('videos')
        data = {
            'title' : 'Test video',
            'description' : 'Funny test video',
            'url' : 'https://www.youtube.com/'
        }
        
        response = self.client.post(url, data)
        assert response.status_code == 201

    @pytest.mark.django_db
    def test_post_video_with_repeated_title(self):
        url = reverse('videos')
        data = {
            'title' : 'Video Test Case',
            'description' : 'test desc',
            'url' : 'https://www.youtube.com/'
        }

        response = self.client.post(url,data)
        assert response.status_code == 400

    @pytest.mark.django_db
    def test_put_video(self):
        url = f'/videos/{self.video_test.id}/'
        data = {
            'title' : 'New Video Test Case',
            'description' : 'changed using PUT method',
            'url' : 'https://www.youtube.com/'
        }
        
        response = self.client.put(url, data)
        assert response.status_code == 200
   
    @pytest.mark.django_db
    def test_put_video_when_his_title_alrealdy_exist(self):
        url = f'/videos/{self.video_test.id}/'
        data = {
            'title' : 'Video Test Case 2',
            'description' : 'changed using PUT method',
            'url' : 'https://www.youtube.com/'
        }
        
        response = self.client.put(url, data)
        assert response.status_code == 400

    @pytest.mark.django_db
    def test_patch_video(self):
        url = f'/videos/{self.video_test.id}/'
        data = {
            'title' : 'New Video Test Case',
            'description' : 'Test case description',
            'url' : 'https://www.youtube.com/'
        }
        
        response = self.client.patch(url, data)
        assert response.status_code == 200

    @pytest.mark.django_db
    def test_delete_video(self):
        url = f'/videos/{self.video_test.id}/'
        data = self.client.get(url).data
        
        response = self.client.delete(url, data)
        assert response.status_code == 204

    



   