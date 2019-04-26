from rest_framework import serializers
from .models import Interest
from .models import Course
from django.contrib.auth.models import User


class InterestSerializer(serializers.ModelSerializer):

	class Meta:
		model = Interest
		fields = ('id', User.username, Course.code, 'date_created', 'date_modified')


class UserSerializer(serializers.ModelSerializer):


	class Meta:
		model = User
		fields = ('id', 'username')


class CourseSerializer(serializers.ModelSerializer):


	class Meta:
		model = Course
		fields = ('id', 'code', 'section', 'title', 'semester', 'seats', 'instructor', 'date_created', 'date_modified','appclassdash_course')

