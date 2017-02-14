.. _building_web_page:

Building a Webpage
------------------
Clustergrammer can be used by developers to add interactive heatmap visualizations to their web pages and web applications.

Embedding Clustergrammer
========================


Clustergrammer Web Page
=======================
The Clustergrammer-JS library can be used to generate an interactive visualization in your webpage. Simply include the ``clustergrammer.js`` script in your page and load the pre-calculated :ref:`Clustergrammer-JSON <clustergrammer_json>` to generate a visualization.


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



or upload their data using the web app API.



Clustergrammer Web App
======================