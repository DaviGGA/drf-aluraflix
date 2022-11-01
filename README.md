# Django Rest Framework API

## Getting started
 
```
pip install -r requirements.txt
```
```
python manage.py runserver
```

## Endpoints

- /videos/
- /videos/{id}/

## Request Example

```
[
    {
      "title": "VIDEO",
      "description": "SOME VIDEO",
      "url": "https://github.com/DaviGGA"
    }
]
```
## Bad Request
```
[
    "The video {video.title} alrealdy exist"
]
```
