=============================
clean_admin
=============================

.. image:: https://img.shields.io/badge/version-0.1.3-brightgreen.svg
    :target: https://img.shields.io/badge/version-0.1.3-brightgreen

Django Admin with the bootstrap styles

Quickstart
----------

Install clean_admin::

    pip install -e git+git@github.com/lumasepa/clean_admin#egg=clean_admin

Then use it in a project::

    Add clean_admin in INSTALLED_APPS before django admin


Features
--------
* Full rewrite of django admin with the bootstrap styles
* Icons for Models
* Support for django-nested-admin
* Support for django-admin-sortable
* Support for django-adminactions
* Support for django-reversion
* Support for django-reversion-compare
* Support for extending the navbar top and right
* Full history view
* Multiple admins support

Documentation
-------------

Install :
    To install the project just run::

        pip install -e git+git@github.com/lumasepa/clean_admin#egg=clean_admin

    and add clean_admin in INSTALLED_APPS before django admin


Extend the nav-bars :
    To add buttons or panels to the navbars overwite the admin/includes/extend/ files,
    navbar-head.html to add buttons to the head bar, and navbar-right to add panels to the
    right lateral.


Multiple admins :
    To use multiple admins fill the settings var CLEAN_ADMIN_SITES with the admin name and
    the dot path to the instance of the admin. ::

        CLEAN_ADMIN_SITES = {
            "atusu_admin": "atusu_admin.admin.atusu_admin",
            "admin": "django.contrib.admin.site"
        }


Example :
    In the example directory there is a django project to test the clean_admin templates and as a project example.


Credits
-------

Tools used in rendering this package:

*  Cookiecutter_
*  `cookiecutter-pypackage`_

.. _Cookiecutter: https://github.com/audreyr/cookiecutter
.. _`cookiecutter-pypackage`: https://github.com/pydanny/cookiecutter-djangopackage
