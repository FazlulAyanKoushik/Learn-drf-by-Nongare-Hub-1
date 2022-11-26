from rest_framework import serializers
from .models import Profile


class ProfileSerializer(serializers.ModelSerializer):
    class Meta:
        model = Profile
        fields = ['name', 'email', 'phoneNumber']
        
        

# class ProfileSerializer(serializers.Serializer):
#     name = serializers.CharField(max_length=255)
#     email = serializers.EmailField(max_length=255)
#     phoneNumber = serializers.CharField(max_length=13)
    
    
#     def create(self, validated_data):
#         """
#         Create and return a new `profile` instance, given the validated data.
#         """
#         return Profile.objects.create(**validated_data)
    

#     def update(self, instance, validated_data):
#         """
#         Update and return an existing `Snippet` instance, given the validated data.
#         """
#         instance.name = validated_data.get('name', instance.name)
#         instance.email = validated_data.get('email', instance.email)
#         instance.phoneNumber = validated_data.get('phoneNumber', instance.phoneNumber)
#         instance.save()
#         return instance