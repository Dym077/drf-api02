from dj_rest_auth.serializers import UserDetailsSerializer, RegisterSerializer
from rest_framework import serializers


class CurrentUserSerializer(UserDetailsSerializer):
    profile_id = serializers.ReadOnlyField(source='profile.id')
    profile_image = serializers.ReadOnlyField(source='profile.image.url')

    class Meta(UserDetailsSerializer.Meta):
        fields = UserDetailsSerializer.Meta.fields + (
            'profile_id', 'profile_image'
        )

class CustomRegisterSerializer(RegisterSerializer):
    user_type = serializers.ChoiceField(choices=['regular', 'artist'])

    def get_cleaned_data(self):
        data = super().get_cleaned_data()
        data['user_type'] = self.validated_data.get('user_type', '')
        return data        