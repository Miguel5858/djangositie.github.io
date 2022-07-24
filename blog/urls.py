from django.urls import path
from .views import render_posts, post_detail, post_sale, post_confirm

app_name = 'blog'

urlpatterns = [
    path('', render_posts, name='posts'),
    path("<int:post_id>", post_detail, name="post_detail"),
    path("<int:post_id>>", post_sale, name="post_sale"),
     path("<int:post_id>>>", post_confirm, name="post_confirm"),
   
    
]
