# Django Rest Framework API

## Getting started

### Run Locally
 
 - Install all required packages:
```
pip install -r requirements.txt
```
- Run in your localhost server:
```
python manage.py runserver
```

### Access via URL

- https://davigga-aluraflix.up.railway.app/

### JWT Authentication

- Create your account in /user/register/
- Do a POST request in /token/ to get your token

## Endpoints

- https://davigga-aluraflix.up.railway.app/

### Search params

- /videos/?video_search=
- /categories/?categories_search=

### Pagination

- /videos/?page=
- /categories/?page=

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
### Bad Request
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
### Bad Request
```python
[
    "The category title alrealdy exist"
]
```
