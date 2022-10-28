from django.contrib import admin
from django.core.exceptions import ValidationError
from django.forms import BaseInlineFormSet

from .models import Article, Scope, Tag


class ScopeInlineFormset(BaseInlineFormSet):
    def clean(self):
        is_main = 0
        for form in self.forms:
            if form.cleaned_data['is_main'] == False:
                pass
            else:
                is_main += 1
        if is_main == 0:
            raise ValidationError('Укажите основной раздел')
        elif is_main >= 2:
            raise ValidationError('Основным может быть только один раздел')
        return super().clean()


class ScopeInline(admin.TabularInline):
    model = Scope
    formset = ScopeInlineFormset
    extra = 0

@admin.register(Tag)
class TagAdmin(admin.ModelAdmin):
    pass

@admin.register(Article)
class ArticleAdmin(admin.ModelAdmin):
    inlines = [ScopeInline]

