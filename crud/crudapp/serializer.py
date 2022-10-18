from rest_framework import serializers
from .models import post
import requests



class post_serializer(serializers.ModelSerializer):
    class Meta:
        model = post
        fields = ['title', 'content', 'keywords', 'created_on']

        def validate_title(self, data):
            if (data.get('title') == ""):
                raise serializers.ValidationError("Invalid Data")
            else:
                return data

        def validate_words(self, data):
            if len(data["keywords"]) < 3:
                raise serializers.ValidationError("Length less")
            return data

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

