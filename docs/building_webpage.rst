.. _building_web_page:

Web-Development with Clustergrammer
-----------------------------------
Clustergrammer can be used by developers to add interactive heatmap visualizations to their web pages and web applications (see :ref:`app_integration`).

Embedding Clustergrammer
========================

The Clustergrammer web app can be used to produce visualizations that are embedded into another page using an IFrame - see below:
::

  <iframe id="iframe_preview" src="http://amp.pharm.mssm.edu/clustergrammer/viz/5734a7399fee36034aeb787e/rc_two_cats.txt" frameborder="0"></iframe>

Users can obtain a permanent link to their visualization by manually uploading their data  using the upload section of Clustergrammer-Web's `homepage`_ and copying the URL to the full-screen version of their visualization. Alternatively users can programmatically upload their data using the :ref:`clustergrammer_web_api` and receive their permanent links through the API.


Adding Clustergrammer to a Page
===============================
The :ref:`clustergrammer_js` library can be used to generate an interactive visualization in your webpage. Simply include the :ref:`clustergrammer_js` script in your page and load the pre-calculated :ref:`visualization-JSON <visualization_json>` to generate a visualization. Alternatively, :ref:`clustergrammer_js` can also be included as a node module.


Clustergrammer can be used to generate interactive visualizations for your own web application by: using the :ref:`clustergrammer_js` library on your site, or embedding a visualization provided by the :ref:`clustergrammer_web`.


The easiest way to generate a visualize of your own data on a webpage is to:

#. Follow the :ref:`clustergrammer_py_workflow` to cluster your matrix and generate the :ref:`visualization_json`
#. Then use the :ref:`example_pages` as templates to build a site with your visualization

These examples require Clustergrammer's JavaScript and Python libraries:

#. the front-end :ref:`clustergrammer_js` JavaScript library makes the interactive visualization
#. the back-end :ref:`clustergrammer_py` Python library clusters a matrix of data and makes the JSON for the front-end

These libraries can be installed npm, ``npm install Clustergrammer``, and pip, ``pip install clustergrammer``, respectively.

.. _`homepage`: http://amp.pharm.mssm.edu/clustergrammer