from __future__ import unicode_literals

from importlib import import_module

import six
from django import template
from django.apps import apps
from django.conf import settings
from django.core.exceptions import ImproperlyConfigured
from django.core.urlresolvers import reverse, NoReverseMatch
from django.template.defaultfilters import capfirst

register = template.Library()


class AdminAppsNode(template.Node):
    def __init__(self, varname):
        self.varname = varname

    def __repr__(self):
        return "<GetAdminLog Node>"

    def render(self, context):
        try:
            request = context["request"]
        except KeyError:
            raise ImproperlyConfigured("clean_admin needs the context procesor 'django.core.context_processors.request'")

        if hasattr(settings, "CLEAN_ADMIN_SITES"):
            try:
                if hasattr(request, "current_app"):
                    site_dot_path = settings.CLEAN_ADMIN_SITES[request.current_app]
                    module_dot_path = ".".join(site_dot_path.split(".")[:-1])
                    obj_name = site_dot_path.split(".")[-1:][0]
                    module = import_module(module_dot_path)
                    site = getattr(module, obj_name)
                else:  # no hay current_app asi que se retorna vacio para compatibilidad con plugins del admin mal hechos
                    context[self.varname] = []
                    return ''
            except KeyError:
                raise ImproperlyConfigured("clean_admin site {} not found in CLEAN_ADMIN_SITES".format(request.current_app))
        else:
            from django.contrib import admin
            site = admin.site

        app_dict = {}

        for model, model_admin in site._registry.items():
            app_label = model._meta.app_label
            has_module_perms = model_admin.has_module_permission(request)

            if has_module_perms:
                perms = model_admin.get_model_perms(request)

                # Check whether user has any perm for this module.
                # If so, add the module to the model_list.
                if True in perms.values():
                    info = (app_label, model._meta.model_name)
                    model_dict = {
                        'name': capfirst(model._meta.verbose_name_plural),
                        'object_name': model._meta.object_name,
                        'perms': perms,
                        'icon': getattr(model, "icon", "")
                    }
                    if perms.get('change', False):
                        try:
                            model_dict['admin_url'] = reverse('admin:%s_%s_changelist' % info, current_app=site.name)
                        except NoReverseMatch:
                            pass
                    if perms.get('add', False):
                        try:
                            model_dict['add_url'] = reverse('admin:%s_%s_add' % info, current_app=site.name)
                        except NoReverseMatch:
                            pass
                    if app_label in app_dict:
                        app_dict[app_label]['models'].append(model_dict)
                    else:
                        app_dict[app_label] = {
                            'name': apps.get_app_config(app_label).verbose_name,
                            'app_label': app_label,
                            'app_url': reverse(
                                'admin:app_list',
                                kwargs={'app_label': app_label},
                                current_app=site.name,
                            ),
                            'has_module_perms': has_module_perms,
                            'models': [model_dict],
                        }

        # Sort the apps alphabetically.
        app_list = list(six.itervalues(app_dict))
        app_list.sort(key=lambda x: x['name'].lower())

        # Sort the models alphabetically within each app.
        for app in app_list:
            app['models'].sort(key=lambda x: x['name'])

        context[self.varname] = app_list
        return ''


@register.tag
def get_apps(parser, token):
    """
    Populates a template variable with the apps
    Usage::
        {% get_apps as [varname] %}
    """
    tokens = token.contents.split()
    if len(tokens) > 3:
        raise template.TemplateSyntaxError(
            "'get_apps' statements require one arguments")
    if tokens[1] != 'as':
        raise template.TemplateSyntaxError(
            "first argument to 'get_apps' must be 'as'")

    return AdminAppsNode(varname=tokens[2])


