Getting Started
---------------

Introduction
============
Clustergrammer is a web-based tool for visualizing high-dimensional data as interactive and shareable hierarchically clustered heatmaps. Clustergrammer can be used in three main ways:

#. :ref:`clustergrammer_web`
#. :ref:`clustergrammer_widget`
#. :ref:`clustergrammer_js` and :ref:`clustergrammer_py` libraries

This section will provide instructions on how to quickly generate a visualization from a matrix of data using the :ref:`clustergrammer_web` and the :ref:`clustergrammer_widget` as well as instructions on how to interact with the visualization. For developers interested in building their own web page using Clustergrammer, please see the :ref:`building_web_page` section.

.. _getting_started_web_app:

Clustergrammer-Web
==================
Instructions for using the web application...

.. _getting_started_widget:

Clustergrammer-Widget
=====================
Here is a link to a notebook with an example interactive widget hosted on nbviewer:
`Interactive Widget <http://nbviewer.jupyter.org/github/MaayanLab/clustergrammer-widget/blob/master/Running_clustergrammer_widget.ipynb>`_

Interacting with Clustergrammer
===============================
Clustergrammer produces highly interactive visualizations that enable intuitive exploration of high-dimensional data including:

- :ref:`zooming_and_panning`
- :ref:`row_col_reordering` (e.g. reorder based on sum)
- :ref:`interactive_dendrogram`
- :ref:`interactive_dim_reduction` (e.g. filter rows based on variance)a
- :ref:`interactive_categories`
- :ref:`cropping`
- :ref:`search`

Press play or interact with the demo (see :ref:`interacting_with_viz` for more information):

.. raw:: html

         <iframe id='iframe_preview' src="http://amp.pharm.mssm.edu/clustergrammer/demo/" frameBorder="0" style='height: 495px; width:730px; margin-bottom:15px;'></iframe>

Clustergrammer also has biology-specific features for working with gene-level data including:

- mouseover gene names and description look-up (using `Harmonizome`_)
- enrichment analysis to find biological information (e.g. up-stream transcription factors) specific to your set of genes (using `Enrichr`_)

See :ref:`biology_specific_features` for more information.

.. _`Enrichr`: http://amp.pharm.mssm.edu/Enrichr/
.. _`Harmonizome`: http://amp.pharm.mssm.edu/Harmonizome/