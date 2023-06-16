from rest_framework import serializers
from rest_framework.exceptions import ValidationError

from djangoProject2.library.models import Author, Book, Reader


class AuthorSerializer(serializers.ModelSerializer):
    class Meta:
        model = Author
        fields = [
            'id',
            'first_name',
            'last_name',
            'photo',
        ]


class BookSerializer(serializers.ModelSerializer):

    class Meta:
        model = Book
        fields = [
            'id',
            'name',
            'description',
            'total_page',
            'author',
            'total_instances',
        ]


class ReaderSerializer(serializers.ModelSerializer):

    def validate(self, data):
        data['phone_number'] = data.get('phone_number')[1:]
        print(data['phone_number'])
        self.__validate_phone_number(data.get('phone_number'))
        self.__validate_active_books(data.get('books'))

        return super().validate(data)


@staticmethod
def __validate_phone_number(number: str):
    if not number.startswith('7'):
        raise ValidationError('Invalid phone number, startswith +7')
    if len(number[1:]) != 11:
        raise ValidationError('Invalid phone number')


@staticmethod
def __validate_active_books(books: dict):
    if len(books) > 3:
        raise ValidationError('Max active books 3')

    class Meta:
        model = Reader
        fields = [
            'id',
            'first_name',
            'last_name',
            'phone_number',
            'status',
            'active_books',
        ]
