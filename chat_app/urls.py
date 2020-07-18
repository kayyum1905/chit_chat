from django.urls import path, re_path, include
from django.contrib.auth import views as auth_views
from django.conf.urls.static import static
from django.conf import settings

from chat_app.views import ChatPageView, chat_json

from chit_chat import settings_base as settings

app_name = 'chat_app'

urlpatterns = [
    path('', ChatPageView.as_view(), name='chat'),
    path('json_chat/', chat_json, name='chat_json')
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
