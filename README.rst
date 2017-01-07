=============================
Plugs Media
=============================

.. image:: https://badge.fury.io/py/plugs-media.png
    :target: https://badge.fury.io/py/plugs-media

.. image:: https://travis-ci.org/ricardolobo/plugs-media.png?branch=master
    :target: https://travis-ci.org/ricardolobo/plugs-media

Your project description goes here

Documentation
-------------

The full documentation is at https://plugs-media.readthedocs.io.

Quickstart
----------

Install Plugs Media::

    pip install plugs-media

Add it to your `INSTALLED_APPS`:

.. code-block:: python

    INSTALLED_APPS = (
        ...
        'plugs_media.apps.PlugsMediaConfig',
        ...
    )

Add Plugs Media's URL patterns:

.. code-block:: python

    from plugs_media import urls as plugs_media_urls


    urlpatterns = [
        ...
        url(r'^', include(plugs_media_urls)),
        ...
    ]

Features
--------

* TODO

Running Tests
-------------

Does the code actually work?

::

    source <YOURVIRTUALENV>/bin/activate
    (myenv) $ pip install tox
    (myenv) $ tox

Credits
-------

Tools used in rendering this package:

*  Cookiecutter_
*  `cookiecutter-djangopackage`_

.. _Cookiecutter: https://github.com/audreyr/cookiecutter
.. _`cookiecutter-djangopackage`: https://github.com/pydanny/cookiecutter-djangopackage
