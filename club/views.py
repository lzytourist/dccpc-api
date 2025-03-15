from rest_framework.generics import CreateAPIView, ListAPIView, RetrieveAPIView

from club.models import (
    Member,
    Gallery,
    PanelMember,
    Event,
    ContactRequest,
    Notice
)
from club.serializers import (
    MemberSerializer,
    GallerySerializer,
    PanelMemberSerializer,
    EventSerializer,
    ContactRequestSerializer,
    NoticeSerializer
)


class MemberCreateAPIView(CreateAPIView):
    serializer_class = MemberSerializer
    queryset = Member.objects.all()


class GalleryListAPIView(ListAPIView):
    serializer_class = GallerySerializer
    queryset = Gallery.objects.all()


class PanelMemberListAPIView(ListAPIView):
    serializer_class = PanelMemberSerializer
    queryset = PanelMember.objects.all()


class EventListAPIView(ListAPIView):
    serializer_class = EventSerializer
    queryset = Event.objects.all()


class EventRetrieveAPIView(RetrieveAPIView):
    serializer_class = EventSerializer
    queryset = Event.objects.all()


class ContactCreateAPIView(CreateAPIView):
    serializer_class = ContactRequestSerializer
    queryset = ContactRequest.objects.all()


class NoticeListAPIView(ListAPIView):
    queryset = Notice.objects.all()
    serializer_class = NoticeSerializer


class NoticeRetrieveAPIView(RetrieveAPIView):
    queryset = Notice.objects.all()
    serializer_class = NoticeSerializer
