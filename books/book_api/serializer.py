    
from rest_framework import serializers
from book_api.models import Book
from django.forms import ValidationError
        
class BookSerializer(serializers.ModelSerializer):
    description = serializers.SerializerMethodField()
    class Meta:
        model = Book
        fields = "__all__"
        
    def validate_title(self, value):
        if value == "Suicide":
            raise ValidationError("Suicide banned")
        return value
    
    def validate(self, data):
        if data["number_of_pages"] > 200 and data["quantity"] > 200:
            raise ValidationError("Too bulky")
        return data
     
    def get_description(self, data):
        return "This book is called " + data.title + "and it is " + str(data.number_of_pages) + " long"
            