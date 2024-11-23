from rest_framework.generics import CreateAPIView, ListAPIView

from club.models import Member, Gallery, PanelMember
from club.serializers import MemberSerializer, GallerySerializer, PanelMemberSerializer


class MemberCreateAPIView(CreateAPIView):
    serializer_class = MemberSerializer
    queryset = Member.objects.all()


class GalleryListAPIView(ListAPIView):
    serializer_class = GallerySerializer
    queryset = Gallery.objects.all()


class PanelMemberListAPIView(ListAPIView):
    serializer_class = PanelMemberSerializer
    queryset = PanelMember.objects.all()
