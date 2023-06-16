from django.contrib import admin
from django.core.exceptions import ValidationError

from djangoProject2.library.models import Author, Book, Reader

# admin.site.register(Author)
# admin.site.register(Book)
# admin.site.register(Reader)


@admin.register(Author)
class AuthorAdmin(admin.ModelAdmin):
    pass
#     list_display = ('id', 'title', 'author', 'quantity')
#     search_fields = ('title', 'description')
#     list_filter = ('author', )


@admin.register(Book)
class BookAdmin(admin.ModelAdmin):
    pass


@admin.register(Reader)
class ReaderAdmin(admin.ModelAdmin):

    def save_model(self, request, obj, form, change):
        if len(form.cleaned_data["active_books"]) > 3:
            from django.contrib import messages
            messages.add_message(request, messages.ERROR, 'Maximum active books to save must 3')
            raise ValidationError('Maximum active books to save must 3')
        else:
            super().save_model(request, obj, form, change)
