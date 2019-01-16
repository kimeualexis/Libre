from django.urls import path
from .views import MemberListView, MemberCreateView, MemberUpdateView
from . import views

app_name = 'users'


urlpatterns = [
	path('', MemberListView.as_view(), name='libre-index'),
	path('add-member/', MemberCreateView.as_view(), name='add-member'),
	path('<int:pk>/update-member/', MemberUpdateView.as_view(), name='update-member'),
	path('(?P<m_id>[0-9]+)/', views.detail, name='detail-member'),
	]