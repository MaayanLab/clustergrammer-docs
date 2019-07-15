.. _building_web_page:

Web-Development
---------------
Clustergrammer can be used by developers to add interactive heatmap visualizations to their web pages and web applications (see :ref:`app_integration`).

Embedding Clustergrammer
========================

The Clustergrammer web app can be used to produce visualizations that are embedded into another page using an IFrame; see below:
::

  <iframe id="iframe_preview" src="https://amp.pharm.mssm.edu/clustergrammer/viz/5734a7399fee36034aeb787e/rc_two_cats.txt" frameborder="0"></iframe>

Users can obtain a permanent link to their visualization by manually uploading their data  using the Upload section of Clustergrammer-Web's `homepage`_ and copying the URL to the full-screen version of their visualization. Alternatively users can programmatically upload their data using the :ref:`clustergrammer_web_api` and obtain their permanent links through the API.


Adding Clustergrammer to a Page
===============================
In addition to embedding a visualization hosted by the :ref:`clustergrammer_web` application developers add a Clustergrammer to directly their own page using the core libraries:

**Clustergrammer-JS**: The front-end :ref:`clustergrammer_js` JavaScript library generates the interactive visualization and can be installed via npm: ``npm install Clustergrammer``. See the :ref:`example_pages` for templates to build a site with your visualization

**Clustergrammer-PY**: The back-end :ref:`clustergrammer_py` Python library clusters a matrix of data and makes the JSON for the front end and can be installed using pip: ``pip install --upgrade clustergrammer``. See the :ref:`clustergrammer_py_workflow` for examples of how cluster your matrix and generate the :ref:`visualization_json`

To make a page, simply include the :ref:`clustergrammer_js` script in your page and load the pre-calculated :ref:`visualization-JSON <visualization_json>` to generate a visualization (use :ref:`clustergrammer_py` to generate this JSON).

:ref:`clustergrammer_js` can also be included as a node module (see `Clustergrammer-Widget source code`_ for an example with Webpack), or can be used with `RequireJS`_ (see `Clustergrammer RequireJS example`_).


Jupyter Notebook Webpages
=========================

The :ref:`clustergrammer_widget` can also be used in combination with `nbviewer`_ to share static Jupyter notebook web pages with embedded interactive Clustergrammer visualizations. This is one of the easiest ways to generate a web page with Clustergrammer visualizations and several of the :ref:`case_studies` are Jupyter notebooks.

.. _`nbviewer`: http://nbviewer.jupyter.org/
.. _`homepage`: http://amp.pharm.mssm.edu/clustergrammer
.. _`Clustergrammer-Widget source code`: https://github.com/MaayanLab/clustergrammer-widget
.. _`RequireJS`: http://requirejs.org/
.. _`Clustergrammer RequireJS example`: https://github.com/MaayanLab/clustergrammer_requirejs