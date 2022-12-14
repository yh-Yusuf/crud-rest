from rest_framework import serializers
from .models import post
import requests



class post_serializer(serializers.ModelSerializer):

    def validate(self, data):
        if (data['title'] == ""):
            raise serializers.ValidationError("Invalid Data")
        else:
            return data

    def validate(self, data):
        if len(data["keywords"]) < 10:
            raise serializers.ValidationError("Invalid Data")
        else:
            return data
    
    # def validate(self, data):
    #     if len(data["content"]) < 10 and len(data["content"]) > 100:
    #         raise serializers.ValidationError("Invalid Data")
    #     else:
    #         return data

    class Meta:
        model = post
        fields = ['title', 'content', 'keywords', 'created_on']



        '''To check the string contains special character or not'''
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

