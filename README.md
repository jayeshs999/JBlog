# JBlog
A Blog app where users can create, edit and delete posts with ease.
The backend for the blog as been written in Django 3.0.4 using Python3.
The blog also uses a third-party application called crispy forms.
The Blog has views for login,post creation, post deletion, registering using both custom as well as generic views.


Steps to run the blog application

1.Download the repository and cd into the directory where you have downloaded the repository

2.Install the requirements.txt file

```python
pip install -r requirements_dev.txt
```
3.Install Django crispy forms using pip

```python
pip install django-crispy-forms
```

3. Make migratios and then start the server

```python
python3 manage.py makemigrations
python3 manage.py migrate
python3 manage.py runserver
```
4.The blog application will start running at localhost:8000.
Go to the url localhost:8000/blog/home.
