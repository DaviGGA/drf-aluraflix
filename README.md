# Django Rest Framework API

## Getting started
 
 - Install all required packages:
```
pip install -r requirements.txt
```
- Run in your localhost server:
```
python manage.py runserver
```

## Endpoints

- /videos/ **[GET/POST]**
- /videos/{id}/ **[GET/DELETE/PUT/PATCH]**

## Request Example

```python
[
    {
      "title": "VIDEO",
      "description": "SOME VIDEO",
      "url": "https://github.com/DaviGGA"
    }
]
```
## Bad Request
```python
[
    "The video {video.title} alrealdy exist"
]
```
