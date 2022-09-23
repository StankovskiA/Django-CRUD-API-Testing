from django.urls import path
from . import views

urlpatterns = [
    path('api/books/<int:pk>/', views.get_delete_update_book, name='get_delete_update_book'),
    path('api/books/$', views.get_post_books, name='get_post_books'
    )
]
