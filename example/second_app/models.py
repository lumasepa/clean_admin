from django.core.exceptions import ValidationError
from django.db import models


class ManyToManyModel(models.Model):
    name = models.CharField(
        max_length=500,
        help_text="write something"
    )


class AllFieldsModel(models.Model):
    char_field = models.CharField(
        max_length=500,
        help_text="write something",
        null=True,
        blank=True
    )

    int_field = models.IntegerField(
        help_text="Put a number, magic number",
        null=True,
        blank=True
    )

    text_field = models.TextField(
        help_text="Put a large test here",
        null=True,
        blank=True
    )

    big_integer_field = models.BigIntegerField(
        help_text="An big integer field",
        null=True,
        blank=True
    )

    binary_field = models.BinaryField(
        help_text="A binary field",
        null=True,
        blank=True
    )

    date_field = models.DateField(
        help_text="A date field",
        null=True,
        blank=True
    )

    datetime_field = models.DateTimeField(
        help_text="A datetime field",
        null=True,
        blank=True
    )

    boolean_field = models.BooleanField(
        help_text="A boolean field",
    )

    comma_separated_integer_field = models.CommaSeparatedIntegerField(
        max_length=200,
        help_text="A comma sepparated integer field",
        null=True,
        blank=True
    )

    decimal_field = models.DecimalField(
        decimal_places=10,
        max_digits=100,
        help_text="A decimal field",
        null=True,
        blank=True
    )

    duration_field = models.DurationField(
        help_text="A duration field",
        null=True,
        blank=True
    )

    email_field = models.EmailField(
        help_text="A email field",
        null=True,
        blank=True
    )

    file_field = models.FileField(
        help_text="A file field",
        null=True,
        blank=True
    )

    file_path_field = models.FilePathField(
        help_text="A file path field",
        null=True,
        blank=True
    )

    float_field = models.FloatField(
        help_text="A float field",
        null=True,
        blank=True
    )

    generic_ip_addr_field = models.GenericIPAddressField(
        help_text="A generic ip addr field",
        null=True,
        blank=True
    )

    image_field = models.ImageField(
        help_text="A image field",
        null=True,
        blank=True
    )

    null_boolean_field = models.NullBooleanField(
        help_text="A null boolean field",
        null=True,
        blank=True
    )

    positive_integer_field = models.PositiveIntegerField(
        help_text="A positive integer",
        null=True,
        blank=True
    )

    positive_small_integer_field = models.PositiveSmallIntegerField(
        help_text="A positive small integer field",
        null=True,
        blank=True
    )

    slug_field = models.SlugField(
        help_text="A slug field",
        null=True,
        blank=True
    )

    small_integer_field = models.SmallIntegerField(
        help_text="A small integer field",
        null=True,
        blank=True
    )

    time_field = models.TimeField(
        help_text="A time field",
        null=True,
        blank=True
    )

    url_field = models.URLField(
        help_text="A url field",
        null=True,
        blank=True
    )

    uuid_field = models.UUIDField(
        help_text="A uuid field",
        null=True,
        blank=True
    )

    many_to_many_field = models.ManyToManyField(
        ManyToManyModel,
        help_text="A many to many field",
        null=True,
        blank=True
    )


class ForeingModel(models.Model):
    name = models.CharField(
        max_length=500,
        choices=(("a", "1"),
                 ("b", "2"),
                 ("c", "3")),
        help_text="write something"
    )

    age = models.PositiveSmallIntegerField()

    birthday = models.DateField()

    foreign_key_field = models.ForeignKey(
        AllFieldsModel,
        help_text="A foreign_key field"
    )

    def clean(self):
        if self.age > 100:
            raise ValidationError("Age must be under 100")


class ForeingModeltoForeingModel(models.Model):
    inner_name = models.CharField(
        max_length=500,
        choices=(("a", "1"),
                 ("b", "2"),
                 ("c", "3")),
        help_text="write something"
    )

    foreign_key_field = models.ForeignKey(
        ForeingModel,
        help_text="A foreign_key field"
    )
