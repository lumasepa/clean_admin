from django.contrib import admin
from django.contrib.admin import StackedInline, TabularInline, ModelAdmin
from second_app.models import AllFieldsModel, ForeingModel, ManyToManyModel, ForeingModeltoForeingModel
from nested_admin.nested import NestedStackedInline, NestedModelAdmin, NestedTabularInline


class ForeingInlineAdmin(StackedInline):
    model = ForeingModel
    extra = 0
    pass


class ForeignTabularInlineAdmin(TabularInline):
    model = ForeingModel
    extra = 0
    pass


#@admin.register(AllFieldsModel)
class AllFieldsAdmin(ModelAdmin):
    inlines = [ForeignTabularInlineAdmin]
    filter_horizontal = ['many_to_many_field']
    pass


class FKtoFKNested(NestedStackedInline):
    model = ForeingModeltoForeingModel
    extra = 1


class FKNested(NestedStackedInline):
    inlines = [FKtoFKNested]
    model = ForeingModel
    extra = 1


class FKtoFKTabularNested(NestedTabularInline):
    model = ForeingModeltoForeingModel
    extra = 1


class FKNestedTabular(NestedTabularInline):
    inlines = [FKtoFKTabularNested]
    model = ForeingModel
    extra = 1



class AllFieldsAdminNested(NestedModelAdmin):
    inlines = [FKNested]
    filter_horizontal = ['many_to_many_field']
    pass

admin.site.register(AllFieldsModel, AllFieldsAdminNested)
