from django.contrib.auth.models import User, Group
from rest_framework import serializers

class UserSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = User
        fields = ('url','username','email','id')

class AdminSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Admin
        fields = ('url','id','user_id','board')
        # userids don't need to be unique (one person can admin multiple boards) but boards DO need to be unique. One admin per board

class BoardSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Admin
        field = ('url','id','user_id','board')

class GateSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Gate
        fields = ('name', 'type', 'id')

class EventSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Event
        fields = ('name','type','id','body')
