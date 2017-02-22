.. _clustergrammer_widget:

Clustergrammer Jupyter Widget
-----------------------------
|pypi-version|
|npm-version|

Clustergrammer can be used within a `Jupyter`_ notebook as an interactive HTML widget, Clustergrammer-Widget, and shared with collaborators using `nbviewer`_. Clustergrammer-Widget can be used to visualize a matrix of data from a file or from a `Pandas`_ DataFrame (see :ref:`matrix_format_io` for more information).

.. figure:: _static/jupyter_widget_nbviewer.png
  :width: 900px
  :align: center
  :alt: Jupyter Widget NBViewer
  :target: http://nbviewer.jupyter.org/github/MaayanLab/clustergrammer-widget/blob/master/Running_clustergrammer_widget.ipynb

  Clustergrammer can be used as an interactive widget within a Jupyter notebook and shared using nbviewer (see `Running_clustergrammer_widget.ipynb`_ example).

Dependencies
============

- `Numpy`_
- `SciPy`_
- `Pandas`_
- `ipywidgets`_

Clustergrammer-Widget works with Python 2 and 3.

Installation
============
Clustergrammer-Widget can be installed (with pip) and enabled using the following commands:

::

  pip install clustergrammer_widget
  jupyter nbextension enable --py --sys-prefix widgetsnbextension
  jupyter nbextension enable --py --sys-prefix clustergrammer_widget

To enable rendering interactive widgets on `nbviewer`_ you must have `ipywidgets version 6`_  or later installed and use the "Save Notebook with Widgets" action in the Widgets menu in the Jupyter notebook (for more information, see ipywidgets documentation on `Rendering Interactive Widgets on nbviewer`_).

.. _clustergrammer_widget_workflow:

Clustergrammer-Widget Workflow Example
======================================
The Jupyter notebook `Running_clustergrammer_widget.ipynb`_ (which is rendered using `nbviewer`_) shows how to visualize a matrix from a file and a `Pandas`_ DataFrame. The following examples are taken from this notebook.

Visualizing a matrix of gene expression data from a tab-separated file:
::

  # import clustergrammer_widgets and initialize network object
  from clustergrammer_widget import *
  net = Network()

  # load matrix file
  net.load_file('rc_two_cats.txt')

  # cluster using default parameters
  net.make_clust()

  # make interactive widget
  clustergrammer_widget(network=net.widget())

Clustergrammer-Widget can also be used as a general purpose `Pandas`_ D/ataFrame viewer. Below is an example of how to visualize a Pandas Dataframe, ``df``, by loading it into the same ``net`` object from above:
::

  # load DataFrame
  net.load_df(df)

  # cluster using default parameters
  net.make_clust()

  # make interactive widget
  clustergrammer_widget(network=net.widget())

The ``net`` object can also be used to filter and normalize your data before visualizing. The example below performs Z-score normalization on the columns and filter to keep the top 200 rows based on their absolute value sum:
::

  # Z-score normalize columns
  net.normalize(axis='col', norm_type='zscore', keep_orig=True)

  # filter for the top 200 rows based on their absolute value sum
  net.filter_N_top('row', 200, 'sum')

  # make interactive widget
  clustergrammer_widget(network=net.widget())

For more information about the ``Network`` object see the :ref:`clustergrammer_py_api`.

.. _clustergrammer_widget_dev:

Clustergrammer-Widget Development
=================================
Clustergrammer-Widget's source code can be found in the `clustergrammer-widget`_ GitHub repo. Clustergrammer-Widget is built using the `ipywidgets`_ framework (using the `cookie cutter`_ template).

Please :ref:`contact` Nicolas Fernandez or Avi Ma'ayan with questions or use the GitHub `issues`_ feature to raise an issue.

.. _`ipywidgets version 6`: https://github.com/ipython/ipywidgets/releases
.. _`ipywidgets`: http://ipywidgets.readthedocs.io/en/latest/
.. _`cookie cutter`: https://github.com/jupyter/widget-cookiecutter
.. _`issues`: https://github.com/MaayanLab/clustergrammer-widget/issues
.. _`clustergrammer-widget`: https://github.com/MaayanLab/clustergrammer-widget
.. _`nbviewer`: http://nbviewer.jupyter.org/
.. _`Rendering Interactive Widgets on nbviewer`: http://ipywidgets.readthedocs.io/en/latest/embedding.html?highlight=save#rendering-interactive-widgets-on-nbviewer
.. _`Running_clustergrammer_widget.ipynb`: http://nbviewer.jupyter.org/github/MaayanLab/clustergrammer-widget/blob/master/Running_clustergrammer_widget.ipynb
.. _`Pandas`: http://pandas.pydata.org/
.. _`Numpy`: http://www.numpy.org/
.. _`SciPy`: https://www.scipy.org/
.. _`nbviewer`: http://nbviewer.jupyter.org/
.. _`Jupyter`: http://jupyter.org/

.. |pypi-version| image:: https://img.shields.io/pypi/v/clustergrammer_widget.svg
    :alt: pypi-version
    :scale: 100%
    :target: https://pypi.python.org/pypi?:action=display&name=clustergrammer_widget

.. |npm-version| image:: https://img.shields.io/npm/v/clustergrammer_widget.svg
    :alt: npm-version
    :scale: 100%
    :target: https://www.npmjs.com/package/clustergrammer_widgt