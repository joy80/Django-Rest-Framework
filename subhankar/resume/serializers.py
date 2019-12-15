from rest_framework import serializers
from .models import Profile


class ProfileSerializer(serializers.ModelSerializer):
	file = serializers.FileField(required=True)

	class Meta:
		model = Profile
		fields = '__all__'
		# read_only_fields = ('name', 'email', 'phone', 'skill')