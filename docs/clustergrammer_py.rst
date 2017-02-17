.. _clustergrammer_py:

Clustergrammer-PY
-----------------
|pypi-version|

Clustergrammer-PY is the back-end Python library that is used to hierarchically cluster the data and generate the :ref:`visualization_json` for the front-end :ref:`clustergrammer_js` visualization library. Clustergrammer-PY is compatible with Python 2 and 3.

Dependencies
============

- `Numpy`_
- `SciPy`_
- `Pandas`_

Installation
============
Clustergrammer-PY can be installed using pip (`package index`_) with the following:
::

  pip install clustergrammer

or the source code can be obtained from the `GitHub repo`_.

.. _clustergrammer_py_workflow:

Python Workflow Example
=======================
This workflow shows how to cluster a matrix of data from a file or DataFrame (see :ref:`matrix_format_io`) and generate a :ref:`visualization_json` (for use by :ref:`clustergrammer_js`):
::

  # make network object and load file
  from clustergrammer import Network
  net = Network()

  # load matrix from file
  net.load_file('your_matrix.txt')

  # or load matrix from DataFrame
  net.load_df(df)

  # calculate clustering using default parameters
  net.make_clust()

  # save visualization JSON to file
  net.write_json_to_file('viz', 'mult_view.json')

The file ``mult_view.json`` will be loaded by the front-end and used to build the interactive visualization. See `make_clustergrammer.py`_ for an additional example.

.. _clustergrammer_py_api:

Clustergrammer-PY API
=====================
Clustergrammer-PY generates a Network object (see `Network class definition`_), which is used to load a matrix (e.g. from a Pandas `DataFrame`_), optionally normalize or filter the matrix, cluster the matrix, and finally generate the visualization JSON for the front-end Clustergrammer.js.

When a matrix is loaded into an instance of ``Network`` (e.g. ``net``) it is stored in the data, ``dat``, attribute. Normalization and filtering will modify the ``dat`` representation of the matrix. When the matrix is clustered (by calling :ref:`make_clust`)

.. automodule:: clustergrammer_py

.. autoclass:: Network
    :members:


.. _clustergrammer_py_dev:

Clustergrammer-PY Development
=============================
Clustergrammer-PY's source code can be found in the `clustergrammer-py`_ GitHub repo. The Clustergrammer-PY library is utilized by the :ref:`clustergrammer_web` and the :ref:`clustergrammer_widget`.

Please :ref:`contact` Nicolas Fernandez or Avi Ma'ayan with questions or use the GitHub `issues`_ feature to raise an issue.

.. _`GitHub repo`: http://github.com/MaayanLab/clustergrammer-py
.. _`package index`: https://pypi.python.org/pypi?:action=display&name=clustergrammer
.. _`clustergrammer-py`: https://github.com/MaayanLab/clustergrammer-py
.. _`issues`: https://github.com/MaayanLab/clustergrammer-py/issues
.. _`Pandas`: http://pandas.pydata.org/
.. _`Numpy`: http://www.numpy.org/
.. _`SciPy`: https://www.scipy.org/
.. _`Network class definition`: https://github.com/MaayanLab/clustergrammer-py/blob/master/clustergrammer/__init__.py
.. _`DataFrame`: http://pandas.pydata.org/pandas-docs/stable/generated/pandas.DataFrame.html
.. _`make_clustergrammer.py`: https://github.com/MaayanLab/clustergrammer-py/blob/master/make_clustergrammer.py

.. |pypi-version| image:: https://img.shields.io/pypi/v/clustergrammer.svg
    :alt: version
    :scale: 100%
    :target: https://pypi.python.org/pypi?:action=display&name=clustergrammer