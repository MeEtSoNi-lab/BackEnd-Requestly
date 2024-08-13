from rest_framework import serializers
from user.models import UserDetail

class UserSerializer(serializers.ModelSerializer):
    # password2 = serializers.CharField(write_only=True, required=True)

    class Meta:
        model = UserDetail
        fields = ['id', 'username' ,'first_name', 'last_name', 'phone','email','street_address', 'province', 'password',]
        extra_kwargs = {'password':{'write_only' : True}}

        # def validate(self, attrs):
        #     if attrs['password'] != attrs['password2']:
        #         raise serializers.ValidationError({"password": "Password fields didn't match."})
        #     return attrs

        def create(self, validated_data):
            # validated_data.pop('password2')  #Remove password2 since it's not needed for creating the user
            user = UserDetail(
                email=validated_data['email'],
                username=validated_data['username'],
                first_name=validated_data.get('first_name'),
                last_name = validated_data.get('last_name'),
                street_address=validated_data.get('address'),
                province =validated_data.get('provience')
            )
            # # Hashes the password
            user.set_password(validated_data['password'])  
            user.save()
            return user