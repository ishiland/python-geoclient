.. _config:

Using a Configuration File
--------------------------
You can optionally use a configuration file that stores your API `ID` and `Key` in addition to any proxies you may need to use.

`python-geoclient` will look for a file called ``.nyc-developer.ini`` in your home directory.
If on a windows machine, this directory is typically located in ``C:\Users\<MY-USERNAME>\``.

A sample ``.nyc-developer.ini`` looks like this:

.. code-block:: ini

   [GEOCLIENT]
   id = my-app-id
   key = my-app-key

   [PROXIES]
   http = http://user:password@host:port
   https = http://user:password@host:port



Now using a ``Geoclient`` object is a little easier:

.. code-block:: python

   from geoclient import Geoclient
   g = Geoclient()

   g.address('1500', 'Madison Ave', 'Manhattan')
