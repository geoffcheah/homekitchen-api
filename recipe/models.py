from django.db import models


class Recipe(models.Model):
    name = models.CharField(
        max_length=64,
        null=False,
        blank=False,
        default="",
        unique=True,
        db_index=True
    )
    author_name = models.CharField(
        max_length=64,
        null=False,
        blank=False,
        default="",
        db_index=True
    )
    slug = models.CharField(
        max_length=64,
        null=False,
        blank=False,
        default="",
        db_index=True
    )

    def __str__(self):
        return self.name

    def save(self, *args, **kwargs):
        slugged_author_name = self.author_name.replace(" ", "-").lower()
        slugged_recipe_name = self.name.replace(" ", "-").lower()
        self.slug = f"{slugged_author_name}-{slugged_recipe_name}"
        super().save(*args, **kwargs)

