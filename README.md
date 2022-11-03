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
- /videos/?video_search=Cat
- /categories/ **[GET/POST]**
- /categories/{id} **[GET/DELETE/PUT/PATCH]**
- /categories/{categories.id}/videos **[GET]**
- /categories/?category_search=Documentary

## Request Example

### Video

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
    "The video title alrealdy exist"
]
```

### Category

```python
[
    {
      "title": "CATEGORY",
      "color": "#ffffff"
    }
]
```
## Bad Request
```python
[
    "The category title alrealdy exist"
]
```