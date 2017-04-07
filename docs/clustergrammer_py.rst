.. _clustergrammer_py:

Clustergrammer-PY
-----------------
|pypi-version|

Clustergrammer-PY is the back-end Python library that is used to hierarchically cluster the data and generate the :ref:`visualization_json` for the front end :ref:`clustergrammer_js` visualization library. Clustergrammer-PY is compatible with Python 2 and 3.

.. _clustergrammer_py_dependencies:

Clustergrammer-PY Dependencies
==============================

- `Numpy`_
- `SciPy`_
- `Pandas`_
- `scikit-learn`_

Installation
============
Clustergrammer-PY can be installed using pip (`package index`_) with the following:
::

  pip install --upgrade clustergrammer

or the source code can be obtained from the `GitHub repo`_.

.. _clustergrammer_py_workflow:

Python Workflow Examples
========================
This workflow shows how to cluster a matrix of data from a file (see :ref:`matrix_format_io`) and generate a :ref:`visualization_json` (for use by :ref:`clustergrammer_js`):
::

  # make network object and load file
  from clustergrammer import Network
  net = Network()
  net.load_file('your_matrix.txt')

  # calculate clustering using default parameters
  net.cluster()

  # save visualization JSON to file for use by front-end
  net.write_json_to_file('viz', 'mult_view.json')

The file ``mult_view.json`` will be loaded by the front-end and used to build the interactive visualization. See `clusterergrammer.py`_ for an additional example.

Clustergrammer can also load data from a Pandas DataFrame and perform normalization and filtering. In this example, we will load data from a DataFrame, normalize the rows, and filter the columns:
::

  # make network object and load DataFrame, df
  net = Network()
  net.load_df(df)

  # Z-score normalize the rows
  net.normalize(axis='row', norm_type='zscore', keep_orig=True)

  # filter for the top 100 columns based on their absolute value sum
  net.filter_N_top('col', 100, 'sum')

  # cluster using default parameters
  net.cluster()

  # save visualization JSON to file for use by front-end
  net.write_json_to_file('viz', 'mult_view.json')

Note that filtering done on the ``Network`` object before clustering is permanent, unlike the filtering done within ``cluster`` which can be toggled on and off in the front-end visualization. The ``keep_orig`` parameter in the ``normalize`` function allows us to show un-normalized data a user mouses over a matrix-cell in the visualization. See the :ref:`clustergrammer_py_api` documentation below for more information.

.. _clustergrammer_py_api:

Clustergrammer-PY API
=====================
Clustergrammer-PY generates a Network object (see `Network class definition`_), which is used to load a matrix (e.g. from a Pandas `DataFrame`_), optionally normalize or filter the matrix, cluster the matrix, and finally generate the visualization JSON for the front-end Clustergrammer.js.

When a matrix is loaded into an instance of ``Network`` (e.g. ``net.load_file('your_file.txt')``) it is stored in the data, ``dat``, attribute. Normalization and filtering will permanently modify the ``dat`` representation of the matrix. When the matrix is clustered (by calling ``cluster``) this produces the :ref:`visualization_json`, which is stored in the ``viz`` attribute. This JSON can then be exported as a string using ``net.export_net_json('viz')`` or saved to a file using ``net.write_json_to_file('viz', filename)``.

The function ``cluster`` calculates hierarchical clustering of your data and hierarchical clustering of successive-row-filtered versions of your data. These alternate filtered-views are stored as ``views`` within the :ref:`visualization_json`.

.. automodule:: clustergrammer_py

.. autoclass:: Network
    :members:


.. _clustergrammer_py_dev:

Clustergrammer-PY Development
=============================
Clustergrammer-PY's source code can be found in the `clustergrammer-py`_ GitHub repo. The Clustergrammer-PY library is utilized by the :ref:`clustergrammer_web` and the :ref:`clustergrammer_widget`.

Please :ref:`contact` Nicolas Fernandez and Avi Ma'ayan with questions or use the GitHub `issues`_ feature to report an issue.

.. _`GitHub repo`: http://github.com/MaayanLab/clustergrammer-py
.. _`package index`: https://pypi.python.org/pypi?:action=display&name=clustergrammer
.. _`clustergrammer-py`: https://github.com/MaayanLab/clustergrammer-py
.. _`issues`: https://github.com/MaayanLab/clustergrammer-py/issues
.. _`Pandas`: http://pandas.pydata.org/
.. _`Numpy`: http://www.numpy.org/
.. _`SciPy`: https://www.scipy.org/
.. _`Network class definition`: https://github.com/MaayanLab/clustergrammer-py/blob/master/clustergrammer/__init__.py
.. _`DataFrame`: http://pandas.pydata.org/pandas-docs/stable/generated/pandas.DataFrame.html
.. _`clusterergrammer.py`: https://github.com/MaayanLab/clustergrammer-py/blob/master/clusterergrammer.py
.. _`scikit-learn`: http://scikit-learn.org/stable/

.. |pypi-version| image:: https://img.shields.io/pypi/v/clustergrammer.svg
    :alt: version
    :scale: 100%
    :target: https://pypi.python.org/pypi?:action=display&name=clustergrammer