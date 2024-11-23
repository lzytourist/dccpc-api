from django.urls import path

from .views import MemberCreateAPIView, GalleryListAPIView, PanelMemberListAPIView

urlpatterns = [
    path('members/', MemberCreateAPIView.as_view(), name='member-create'),
    path('gallery/', GalleryListAPIView.as_view(), name='gallery-list'),
    path('panel-members/', PanelMemberListAPIView.as_view(), name='panel-list'),
]
