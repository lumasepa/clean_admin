from django.db import models


class ForeingModel(models.Model):
    icon = "fa-cogs"

    name = models.CharField(
        max_length=500,
        help_text="write something"
    )

    def __unicode__(self):
        return self.name


class ManyToManyModel(models.Model):
    name = models.CharField(
        max_length=500,
        help_text="write something"
    )

    def __unicode__(self):
        return self.name


class OneToOneModel(models.Model):
    name = models.CharField(
        max_length=500,
        help_text="write something"
    )

    def __unicode__(self):
        return self.name


class AllFieldsModel(models.Model):
    char_field = models.CharField(
        max_length=500,
        help_text="write something"
    )

    int_field = models.IntegerField(
        help_text="Put a number, magic number"
    )

    text_field = models.TextField(
        help_text="Put a large test here"
    )

    big_integer_field = models.BigIntegerField(
        help_text="An big integer field"
    )

    binary_field = models.BinaryField(
        help_text="A binary field"
    )

    date_field = models.DateField(
        help_text="A date field"
    )

    datetime_field = models.DateTimeField(
        help_text="A datetime field"
    )

    boolean_field = models.BooleanField(
        help_text="A boolean field"
    )

    comma_separated_integer_field = models.CommaSeparatedIntegerField(
        max_length=200,
        help_text="A comma sepparated integer field"
    )

    decimal_field = models.DecimalField(
        decimal_places=10,
        max_digits=100,
        help_text="A decimal field"
    )

    duration_field = models.DurationField(
        help_text="A duration field"
    )

    email_field = models.EmailField(
        help_text="A email field"
    )

    file_field = models.FileField(
        help_text="A file field"
    )

    file_path_field = models.FilePathField(
        help_text="A file path field"
    )

    float_field = models.FloatField(
        help_text="A float field"
    )

    foreign_key_field = models.ForeignKey(
        ForeingModel,
        help_text="A foreign_key field"
    )

    generic_ip_addr_field = models.GenericIPAddressField(
        help_text="A generic ip addr field"
    )

    image_field = models.ImageField(
        help_text="A image field"
    )

    many_to_many_field = models.ManyToManyField(
        ManyToManyModel,
        help_text="A many to many field"
    )

    one_to_one_field = models.OneToOneField(
        OneToOneModel,
        help_text="A one to one field"
    )

    null_boolean_field = models.NullBooleanField(
        help_text="A null boolean field"
    )

    positive_integer_field = models.PositiveIntegerField(
        help_text="A positive integer"
    )

    positive_small_integer_field = models.PositiveSmallIntegerField(
        help_text="A positive small integer field"
    )

    slug_field = models.SlugField(
        help_text="A slug field"
    )

    small_integer_field = models.SmallIntegerField(
        help_text="A small integer field"
    )

    time_field = models.TimeField(
        help_text="A time field"
    )

    url_field = models.URLField(
        help_text="A url field"
    )

    uuid_field = models.UUIDField(
        help_text="A uuid field"
    )

    def __unicode__(self):
        return self.char_field
