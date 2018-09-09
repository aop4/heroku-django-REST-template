from rest_framework import serializers
from rest_api.models import Student

# Define a serializer that serves as an interface to the Student
# class, allowing its instances to be created, retrieved, and updated
# with various formats (JSON, XML, probably things I don't know about)
# See some documentation on serializers here: http://www.django-rest-framework.org/tutorial/1-serialization/
# AND PLEASE please please if you read that, look at the section Model Serializers--
# that will save you loads of time and is used below
class DataModelSerializer(serializers.ModelSerializer):
    class Meta:
        model = Student
        fields = ('uuid', 'name', 'id') # you can explicitly define the 
                                  # fields to include in serialized model
        # fields = '__all__' # you can also say "__all__", but this may 
                             # expose data you don't want exposed by giving
                             # access to all model fields
