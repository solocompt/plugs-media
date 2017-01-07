=====
Usage
=====

To use Plugs Media in a project, add it to your `INSTALLED_APPS`:

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
