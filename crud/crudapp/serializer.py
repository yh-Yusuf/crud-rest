from rest_framework import serializers
from .models import post
import requests



class post_serializer(serializers.ModelSerializer):
    class Meta:
        model = post
        fields = ['title', 'content', 'words', 'created_on']

        def validate_title(self, data):
            if data['title'] == '':
                raise serializers.ValidationError("Invalid Data")

        def validate_words(self, data):
            if len(data["words"]) < 3:
                raise serializers.ValidationError("Length less")


            # print(validated_data["words"])

            # words_obj = validated_data['words']
            # if len(words_obj) < 20:
            #     raise serializers.ValidationError("lenght less than 20")
            #
            # if validated_data.get('title'):
            #     title_obj = validated_data['title']
            #     regex = re.compile('[@_!#$%^&*()<>?/\|}{~:]')
            #
            #     if not regex.search(title_obj) == None:
            #         raise serializers.ValidationError("Title contains special characters")
            #
            # return validated_data

