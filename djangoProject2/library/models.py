from django.db import models
from phonenumber_field.modelfields import PhoneNumberField


class BaseModel(models.Model):
    created = models.DateTimeField(verbose_name="Дата добавления", auto_now_add=True)
    updated = models.DateTimeField(verbose_name="Дата редактирования", auto_now=True)

    class Meta:
        abstract = True


class Author(BaseModel):
    first_name = models.CharField(verbose_name='имя автора', max_length=50)
    last_name = models.CharField(verbose_name='фамилия автора', max_length=50)
    photo = models.ImageField(upload_to='photos/')

    def __str__(self):
        return f'{self.first_name}, {self.last_name}'

    class Meta:
        verbose_name = 'Автор'
        verbose_name_plural = 'Авторы'
        unique_together = ('first_name', 'last_name')


class Book(BaseModel):
    name = models.CharField(verbose_name='название книги', max_length=100)
    description = models.TextField(verbose_name='описание')
    total_page = models.PositiveIntegerField()
    author = models.ForeignKey(Author, on_delete=models.PROTECT, related_name='books')
    total_instances = models.PositiveIntegerField()

    def __str__(self):
        return f'{self.name}, {self.author}'

    class Meta:
        verbose_name = 'Книга'
        verbose_name_plural = 'Киниги'


class Reader(BaseModel):
    class Status(models.TextChoices):
        is_active = 'активен'
        not_active = 'не активен'

    first_name = models.CharField(verbose_name='имя читателя', max_length=50)
    last_name = models.CharField(verbose_name='фамилия читателя', max_length=50)
    phone_number = PhoneNumberField(max_length=12, null=False, blank=False)
    status = models.CharField(max_length=10, choices=Status.choices, default=Status.is_active)
    active_books = models.ManyToManyField(Book, max_length=3)

    def __str__(self):
        return f'{self.first_name}, {self.last_name}'

    class Meta:
        verbose_name = 'Читатель'
        verbose_name_plural = 'Читатели'

