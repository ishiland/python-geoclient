.. _errors:


Error Handling
--------------

`python-geoclient` will raise a ``GeoclientError`` when the Geoclient API returns an error code. Sometimes there is more information
returned, in which case the exception will have a ``result`` dictionary.

.. code-block:: python

    from geoclient import GeoclientError

    try:
        g.address(125, 'wort st', 1)

    except GeoclientError as e:
        print(e) # 'WORT STREET' NOT RECOGNIZED. THERE ARE 010 SIMILAR NAMES.
        print(e.result['streetName1']) # WORTH SQUARE

You can easily iterate all `similar names`:

.. code-block:: python

    from geoclient import GeoclientError

    try:
        g.address(125, 'wort st', 1)

    except GeoclientError as e:
        print(e) # 'WORT STREET' NOT RECOGNIZED. THERE ARE 010 SIMILAR NAMES.
        print(e.result['numberOfStreetCodesAndNamesInList']) # 10

        # iterate similar names
        for x in range(int(e.result['numberOfStreetCodesAndNamesInList'])):
            print(e.result['streetName{}'.format(x + 1)])

**Note:** The ``GeoclientError`` will not be raised when using the ``search`` method.