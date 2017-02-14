Getting Started
---------------

Introduction
============
Clustergrammer is an interactive web-based tool for visualizing high-dimensional data as hierarchically clustered heatmap. Clustergrammer can be used in three main ways: 1) web application, Jupyter notebook interactive widget, and JavaScript and Python libraries. This section will provide quick instructions on how to

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
Clustergrammer is built to enable users to intuitively explore/analyze high-dimensional datasets and has many interactive features including:

- zooming/panning
- row and column reordering (e.g. reorder based on sum)
- interactive dendrogram
- dimensionality reduction (e.g. filter rows based on variance)a
- interactive row/column categories
- cropping

Clustergrammer also have biology-specific features including:

- mouseover gene (row) names to show the full name and description of a gene (through `Harmonizome`_)
- find biological information (e.g. up-stream transcription factors) specific to your gene list using enrichment analysis through `Enrichr`_


.. _getting_started_web_development:

Clustergrammer.js Web Development
=================================
Clustergrammer can be used to generate interactive visualizations for your own web application by: using the Clustergrammer.js library on your site, or embedding a visualization provided by the Clustergrammer web app.


*Webpage Examples*

The easiest way to generate a visualize of your own data on a webpage is to:

#. follow the :ref:`python_workflow_example` to cluster your matrix and generate the front-end JSON
#. then use the :ref:`example_pages` workflow to visualize your calculated JSON

These examples require Clustergrammer's JavaScript and Python libraries:

#. the front-end Clustergrammer.js JavaScript library makes the interactive visualization
#. the back-end Clustergrammer.py Python library clusters a matrix of data and makes the JSON for the front-end

These libraries can be installed npm, ``npm install Clustergrammer``, and pip, ``pip install clustergrammer``, respectively.

*Embedding Information*

The Clustergrammer web app can be used to produce visualizations that are embedded into another page using an IFrame - see below:
::

  <iframe id="iframe_preview" src="http://amp.pharm.mssm.edu/clustergrammer/viz/5734a7399fee36034aeb787e/rc_two_cats.txt" frameborder="0"></iframe>

Users can upload their data using the upload section of the web app `homepage`_

.. _`Enrichr`: http://amp.pharm.mssm.edu/Enrichr/
.. _`Harmonizome`: http://amp.pharm.mssm.edu/Harmonizome/
.. _`homepage`: http://amp.pharm.mssm.edu/clustergrammer

or upload their data using the web app API.d