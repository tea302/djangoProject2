# Generated by Django 4.2.2 on 2023-06-20 12:07

from django.db import migrations, models
import django.db.models.deletion
import phonenumber_field.modelfields


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Author',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created', models.DateTimeField(auto_now_add=True, verbose_name='Дата добавления')),
                ('updated', models.DateTimeField(auto_now=True, verbose_name='Дата редактирования')),
                ('first_name', models.CharField(max_length=50, verbose_name='имя автора')),
                ('last_name', models.CharField(max_length=50, verbose_name='фамилия автора')),
                ('photo', models.ImageField(upload_to='photos/')),
            ],
            options={
                'verbose_name': 'Автор',
                'verbose_name_plural': 'Авторы',
                'unique_together': {('first_name', 'last_name')},
            },
        ),
        migrations.CreateModel(
            name='Book',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created', models.DateTimeField(auto_now_add=True, verbose_name='Дата добавления')),
                ('updated', models.DateTimeField(auto_now=True, verbose_name='Дата редактирования')),
                ('name', models.CharField(max_length=100, verbose_name='название книги')),
                ('description', models.TextField(verbose_name='описание')),
                ('total_page', models.PositiveIntegerField()),
                ('total_instances', models.PositiveIntegerField()),
                ('author', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, related_name='books', to='library.author')),
            ],
            options={
                'verbose_name': 'Книга',
                'verbose_name_plural': 'Киниги',
            },
        ),
        migrations.CreateModel(
            name='Reader',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created', models.DateTimeField(auto_now_add=True, verbose_name='Дата добавления')),
                ('updated', models.DateTimeField(auto_now=True, verbose_name='Дата редактирования')),
                ('first_name', models.CharField(max_length=50, verbose_name='имя читателя')),
                ('last_name', models.CharField(max_length=50, verbose_name='фамилия читателя')),
                ('phone_number', phonenumber_field.modelfields.PhoneNumberField(max_length=128, region=None, unique=True)),
                ('status', models.CharField(choices=[('активен', 'Is Active'), ('не активен', 'Not Active')], default='активен', max_length=10)),
                ('active_books', models.ManyToManyField(max_length=3, to='library.book')),
            ],
            options={
                'verbose_name': 'Читатель',
                'verbose_name_plural': 'Читатели',
            },
        ),
    ]
