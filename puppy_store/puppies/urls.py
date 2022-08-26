from django.urls import path, re_path
from .views import get_delete_update_puppy, get_post_puppies

urlpatterns = [
    re_path(
        r'puppies/(?P<pk>[0-9]+)$', 
        get_delete_update_puppy,
        name='get_delete_update_puppy'
    ),
    re_path(
        r'puppies/$',
        get_post_puppies,
        name='get_post_puppies'
    )
]
