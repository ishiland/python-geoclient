.. _proxy:

Using a Proxy
-------------
If you are behind a proxy server, you can pass a proxies dictionary to the ``Geoclient`` object:

.. code-block:: python

    proxies = {
        'http': 'http://user:password@host:port',
        'https': 'http://user:password@host:port',
        }
    g = Geoclient('my app ID', 'my app key', proxies)

See the |requests_link| documentation for more info on using proxies.

.. |requests_link| raw:: html

   <a href="http://docs.python-requests.org/en/master/user/advanced/#proxies" target="_blank">Requests</a>
