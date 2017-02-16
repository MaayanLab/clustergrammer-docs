.. _clustergrammer_py:

Clustergrammer-PY
-----------------
|pypi-version|

Clustergrammer-PY is the back-end Python library that is used to hierarchically cluster the data and generate the :ref:`visualization_json` for the front-end Clustergrammer.js visualization library. Clustergrammer-PY is compatible with Python 2 and 3.

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
This workflow shows how to cluster a matrix of data and generate a visualization JSON (for use by Clustergrammer.js) from a matrix file:
::

  # make network object
  from clustergrammer import Network
  net = Network()

  # load matrix file
  net.load_file('your_matrix.txt')

  # calculate clustering using default parameters
  net.make_clust()

  # write visualization JSON to file
  net.write_json_to_file('viz', 'mult_view.json')

The file ``mult_view.json`` will be loaded by the front-end and used to build the interactive visualization.

.. _clustergrammer_py_api:

Clustergrammer-PY API
=====================
Clustergrammer-PY generates a Network object (see `Network class definition`_), which is used to load a matrix (e.g. from a Pandas `DataFrame`_), optionally normalize or filter the matrix, cluster the matrix, and finally generate the visualization JSON for the front-end Clustergrammer.js.

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

.. |pypi-version| image:: https://img.shields.io/pypi/v/clustergrammer.svg
    :alt: version
    :scale: 100%
    :target: https://pypi.python.org/pypi?:action=display&name=clustergrammer