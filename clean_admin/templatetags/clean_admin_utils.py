from importlib import import_module

from django import template
from django.conf import settings
from django.template.loader import render_to_string

register = template.Library()
CUSTOM_FIELD_RENDERER = getattr(settings, 'DAB_FIELD_RENDERER', False)
MAX_LENGTH_BOOTSTRAP_COLUMN = 12


def css_classes_for_field(field, custom_classes):
    orig_class = field.field.widget.attrs.get('class', '')
    required = 'required' if field.field.required else ''
    classes = field.css_classes(' '.join([orig_class, custom_classes, required]))
    return classes


@register.filter()
def get_label(field, custom_classes=''):
    classes = css_classes_for_field(field, custom_classes)
    return field.label_tag(attrs={'class': classes}, label_suffix='')

@register.filter()
def add_class(field, custom_classes=''):
    classes = css_classes_for_field(field, custom_classes)
    try:
        # For widgets like SelectMultiple, checkboxselectmultiple
        field.field.widget.widget.attrs.update({'class': classes})
    except:
        field.field.widget.attrs.update({'class': classes})
    return field


@register.filter()
def widget_type(field):
    if isinstance(field, dict):
        return 'adminreadonlyfield'
    try:
        # For widgets like SelectMultiple, checkboxselectmultiple
        widget_type = field.field.widget.widget.__class__.__name__.lower()
    except:
        widget_type = field.field.widget.__class__.__name__.lower()
    return widget_type


@register.filter()
def placeholder(field, placeholder=''):
    field.field.widget.attrs.update({'placeholder': placeholder})
    return field


@register.filter()
def class_for_field_boxes(line):
    size_column = MAX_LENGTH_BOOTSTRAP_COLUMN / len(line.fields)
    return 'col-sm-{0}'.format(size_column or 1)  # if '0' replace with 1


@register.simple_tag(takes_context=True, name="dab_field_rendering")
def custom_field_rendering(context, field, *args, **kwargs):
    """ Wrapper for rendering the field via an external renderer """
    if CUSTOM_FIELD_RENDERER:
        mod, cls = CUSTOM_FIELD_RENDERER.rsplit(".", 1)
        field_renderer = getattr(import_module(mod), cls)
        if field_renderer:
            return field_renderer(field, **kwargs).render()
    return field


@register.simple_tag(takes_context=True)
def render_app_description(context, app, fallback="", template="/admin_app_description.html"):
    """ Render the application description using the default template name. If it cannot find a
        template matching the given path, fallback to the fallback argument.
    """
    try:
        template = app['app_label'] + template
        text = render_to_string(template, context)
    except:
        text = fallback
    return text


@register.simple_tag(takes_context=True)
def render_app_label(context, app, fallback=""):
    """ Render the application label.
    """
    try:
        text = app['app_label']
    except KeyError:
        text = fallback
    except TypeError:
        text = app
    return text

@register.simple_tag(takes_context=True)
def render_app_name(context, app, template="/admin_app_name.html"):
    """ Render the application name using the default template name. If it cannot find a
        template matching the given path, fallback to the application name.
    """
    try:
        template = app['app_label'] + template
        text = render_to_string(template, context)
    except:
        text = app['name']
    return text

@register.simple_tag(takes_context=True)
def render_with_template_if_exist(context, template, fallback):
    text = fallback
    try:
        text = render_to_string(template, context)
    except:
        pass
    return text


@register.filter(name='form_fieldset_column_width')
def form_fieldset_column_width(form):
    def max_line(fieldset):
        try:
            return max([len(list(line)) for line in fieldset])
        # This ValueError is for case that fieldset has no line.
        except ValueError:
            return 0

    try:
        width = max([max_line(fieldset) for fieldset in form])
        return 12 // width
    except (ValueError, ZeroDivisionError):
        return 12

if settings.DEBUG:
    # for breakpoint and inspection
    @register.filter()
    def inspect(thing):
        print(thing)
        return thing
