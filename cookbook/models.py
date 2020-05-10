from django.db import models


class Batch(models.Model):
    gene = models.ForeignKey('Gene', models.DO_NOTHING, blank=True, null=True)
    quantity = models.IntegerField(blank=True, null=True, default=0)
    date_created = models.DateTimeField(blank=True, null=True)
    date_modified = models.CharField(max_length=45, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'batch'

    def __str__(self):
        return self.gene.name + ' X ' + str(self.quantity)


class BatchItem(models.Model):
    batch = models.ForeignKey(Batch, models.CASCADE, blank=True, null=True)
    ingredient = models.ForeignKey('Ingredient', models.DO_NOTHING, blank=True, null=True)
    computed_vol = models.FloatField(blank=True, null=True)
    is_manual = models.IntegerField(blank=True, null=True)
    manager = models.Manager()

    class Meta:
        managed = False
        db_table = 'batch_item'

    def __str__(self):
        return self.batch.gene.name + ' ' + self.ingredient.name


class Gene(models.Model):
    name = models.CharField(max_length=32, blank=True, null=True)
    description = models.TextField(blank=True, null=True)
    recipe = models.ForeignKey('Recipe', models.DO_NOTHING, blank=True, null=True)
    program = models.ForeignKey('Program', models.DO_NOTHING, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'gene'

    def __str__(self):
        return self.name


class Ingredient(models.Model):
    name = models.CharField(max_length=64, blank=True, null=True)
    description = models.TextField(blank=True, null=True)
    nature = models.ForeignKey('Nature', models.DO_NOTHING, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'ingredient'

    def __str__(self):
        return self.name


class Nature(models.Model):
    name = models.CharField(max_length=16, blank=True, null=True)
    description = models.TextField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'nature'

    def __str__(self):
        return self.name


class Program(models.Model):
    name = models.CharField(max_length=64, blank=True, null=True)
    description = models.TextField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'program'

    def __str__(self):
        return self.name


class Recipe(models.Model):
    name = models.CharField(max_length=32, blank=True, null=True)
    description = models.TextField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'recipe'

    def __str__(self):
        return self.name


class RecipeItem(models.Model):
    recipe = models.ForeignKey(Recipe, models.DO_NOTHING, blank=True, null=True)
    ingredient = models.ForeignKey(Ingredient, models.DO_NOTHING, blank=True, null=True)
    volume = models.FloatField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'recipe_item'

    def __str__(self):
        return self.ingredient.name
