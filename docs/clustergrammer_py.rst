.. _clustergrammer_py:

Clustergrammer-PY
-----------------
Clustergrammer-PY is the back-end Python library that is used to hierarchically cluster the data and generate the JSON for the front-end Clustergrammer.js visualization library.

Dependencies
============

- Numpy
- Pandas
- SciPy

Installation
============
Clustergrammer-PY can be installed using pip (`package index`_) with the following:
::

  pip install clustergrammer

or the source code can be obtained from the `GitHub repo`_.

.. _python_workflow_example:

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


Clustergrammer-PY API
=====================
Clustergrammer-PY generates a Network object, which is used to load a matrix (e.g. from a Pandas DataFrame), normalize/filter the matrix, cluster the matrix, and finally generate the visualization JSON for the front-end Clustergrammer.js.

Developing Clustergrammer-PY
=============================
Clustergrammer-PY's source code can be found in the `clustergrammer-py`_ Github repo. The Clustergrammer-PY library is utilized by the :ref:`clustergrammer_web` and the :ref:`clustergrammer_widget`.

.. _`GitHub repo`: http://github.com/MaayanLab/clustergrammer-py
.. _`package index`: https://pypi.python.org/pypi?:action=display&name=clustergrammer
.. _`clustergrammer-py`: https://github.com/MaayanLab/clustergrammer-py