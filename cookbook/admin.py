from django.contrib import admin
from .models import Gene, Recipe, RecipeItem, Ingredient, Nature, Program, Batch, BatchItem


@admin.register(Gene)
class GeneAdmin(admin.ModelAdmin):
    pass


class RecipeItemInLine(admin.TabularInline):
    model = RecipeItem
    extra = 1


@admin.register(Recipe)
class RecipeAdmin(admin.ModelAdmin):
    inlines = [RecipeItemInLine, ]
    pass


@admin.register(RecipeItem)
class RecipeItemAdmin(admin.ModelAdmin):
    pass


@admin.register(Ingredient)
class IngredientAdmin(admin.ModelAdmin):
    pass


@admin.register(Program)
class ProgramAdmin(admin.ModelAdmin):
    pass


@admin.register(Nature)
class NatureAdmin(admin.ModelAdmin):
    pass


@admin.register(BatchItem)
class BatchItemAdmin(admin.ModelAdmin):
    pass


class BatchItemInLine(admin.TabularInline):
    model = BatchItem
    extra = 1


@admin.register(Batch)
class BatchAdmin(admin.ModelAdmin):
    inlines = [BatchItemInLine, ]
    pass
