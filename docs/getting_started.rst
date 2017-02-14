Getting Started
---------------

Introduction
============
Clustergrammer is a web-based tool for visualizing high-dimensional data as hierarchically interactive and shareable clustered heatmap. Clustergrammer can be used in three main ways:

#. :ref:`clustergrammer_web`
#. :ref:`clustergrammer_widget`
#. :ref:`clustergrammer_js` and :ref:`clustergrammer_py` libraries

This section will provide quick instructions on how to generate a visualization from a matrix of data using the :ref:`clustergrammer_web` and the :ref:`clustergrammer_widget` as well as instructions on how to interact with the visualization. For developers interested in building their own web page using Clustergrammer, please see the :ref:`building_web_page` section.

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

- zooming/panning
- row and column reordering (e.g. reorder based on sum)
- interactive dendrogram
- dimensionality reduction (e.g. filter rows based on variance)a
- interactive row/column categories
- cropping

Press play or interact with the demo to see

.. raw:: html

         <iframe id='iframe_preview' src="http://amp.pharm.mssm.edu/clustergrammer/demo/" frameBorder="0" style='height: 495px; width:730px; margin-bottom:15px;'></iframe>

For more information on interacting with the visualization please see the :ref:`viz_interaction` section. Clustergrammer also has biology-specific features including:

- mouseover gene (row) names to show the full name and description of a gene (through `Harmonizome`_)
- find biological information (e.g. up-stream transcription factors) specific to your gene list using enrichment analysis through `Enrichr`_

For more information on Clustergrammer's biology specific features please see the :ref:`biology_specific_features` section.

.. _`Enrichr`: http://amp.pharm.mssm.edu/Enrichr/
.. _`Harmonizome`: http://amp.pharm.mssm.edu/Harmonizome/
.. _`homepage`: http://amp.pharm.mssm.edu/clustergrammer