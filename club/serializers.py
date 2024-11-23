from rest_framework import serializers

from club.models import Member, Gallery, PanelMember


class MemberSerializer(serializers.ModelSerializer):
    class Meta:
        model = Member
        fields = '__all__'


class GallerySerializer(serializers.ModelSerializer):
    class Meta:
        model = Gallery
        fields = '__all__'


class PanelMemberSerializer(serializers.ModelSerializer):
    class Meta:
        model = PanelMember
        fields = '__all__'

