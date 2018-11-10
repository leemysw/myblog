# from .views import CommentView
from django.urls import path, include

from .views import comment

urlpatterns = [
    path('comment/', comment, name='comment'),
    path('icon/', include('django_pydenticon.urls'))
]
