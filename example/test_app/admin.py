from django.contrib import admin
from test_app.models import AllFieldsModel, ForeingModel, OneToOneModel, ManyToManyModel


@admin.register(ForeingModel)
class ForeingAdmin(admin.ModelAdmin):
    search_fields = ("name",)
    pass


@admin.register(ManyToManyModel)
class ManyToManyAdmin(admin.ModelAdmin):
    pass


@admin.register(OneToOneModel)
class OneToOneAdmin(admin.ModelAdmin):
    pass


@admin.register(AllFieldsModel)
class AllFieldsAdmin(admin.ModelAdmin):
    pass
