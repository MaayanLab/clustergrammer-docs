.. _clustergrammer_js:

Clustergrammer-JS
-----------------
|npm-version|
|license|

Clustergrammer-JS is the front-end JavaScript library that builds the interactive heatmap visualization in `SVG`_ using the visualization library `D3.js`_


Dependencies
============

- `D3.js`_
- `JQuery`_
- `Underscore`_

Installation
============
Clustergrammer.js can be installed using node package manager (`npm package`_) with the following:
::

  npm install clustergrammer

or the source code and library, ``clustergrammer.js``, can be obtained from the `clustergrammer`_ GitHub repo.

.. _javascript_workflow_example:

JavaScript Workflow Example
============================
This workflow shows how to make a visualization using a JSON produced by Clustergrammer.py
::

  // load visualization JSON to network_data
  var args = {
    'root': '#id_of_container',
    'network_data': 'network_data'
  }

  var cgm = Clustergrammer(args);

The ``id`` of the container where the visualization will be made is passed as ``root`` (this root container must be made by the user). The :ref:`visualization_json` contains the information necessary to make the visualization and is passed as ``network_data``. See the :ref:`clustergrammer_js_api` for additional arguments that can be passed to Clustergrammer.js.

.. _example_pages:

Example Pages
=============
The `clustergrammer`_ contains several example pages demonstrating how to make a webpage with a Clustergrammer heatmap. The page `index.html`_ and corresponding script `load_clustergram.js`_ show how to make a full-screen resizable visualization.

The page `multiple_clust.html`_ and corresponding script `load_multiple_clustergrams.js`_ show how to visualize multiple clustergrams on one page. Note that each heatmap requires its own container.

.. _clustergrammer_js_api:

Clustergrammer-JS API
=====================

.. js:class:: Clustergrammer(args)

  The Clustergrammer JavaScript object takes the ``args`` object and produces a visualization on the page.

  This ``args`` object has two required arguments, ``network_data`` and ``root``:

    .. js:attribute:: args.network_data

      This required attribute is where the visualization JSON should be passed as a JavaScript object.

    .. js:attribute:: args.root

      This required attribute is the ``id`` (passed as a string) of the container where Clustergrammer will be built. Each Clustergrammer visualization in a page should be passed a unique ``id``.

    .. js:attribute:: args.about

      This attribute is a string (which can include HTML) that will produce a small about section at the top of the sidebar. This can be used to provide a quick description about the data or visualization.

    .. js:attribute:: args.row_tip_callback

      Users can pass a callback function that will run when mousing over row labels.

    .. js:attribute:: args.col_tip_callback

      Users can pass a callback function that will run when mousing over col labels.

    .. js:attribute:: args.tile_tip_callback

      Users can pass a callback function that will run when mousing over a matrix-cell (e.g. matrix tile).

    .. js:attribute:: args.dendro_callback

      Users can pass a callback function that will run when mousing over a dendrogram cluster (e.g. gray trapezoid)

    .. js:attribute:: args.matrix_update_callback

      Users can pass a callback function that will run anytime the matrix has been updated, for instance when filtering/un-filtering, cropping, etc.

    .. js:attribute:: args.sidebar_width:

      Users can modify the width of the sidebar by specifying the width of the sidebar in pixels as a number.

    .. js:attribute:: args.ini_view

      Users can initialize the 'view' of their matrix, e.g. a initialize the matrix at a particular row filtering level.

  Clustergrammer's attributes and functions are listed below:

  .. js:function:: update_cats(row_data)

    Update the visualization row categories.

    :param row_data: The row category data that will be used to ...

    :param resize_viz: Call this function to resize the visualization to fit in its resized container (if the user has resized the container).



.. _visualization_json:

Visualization-JSON
==================
The visualization-JSON format required for Clustergrammer.js is described here:


Users can also generate the visualization-JSON using their own scripts as long as they adhere to the above format.

.. _clustergrammer_js_dev:

Clustergrammer-JS Development
=============================
Clustergrammer-JS' source code can be found in the `clustergrammer`_ GihHub repo. The Clustergrammer-JS library is utilized by the :ref:`clustergrammer_web` and the :ref:`clustergrammer_widget`. Clustergrammer-JS is built with `Webpack Module Bundler`_ from the source files in the `src`_ directory.

Please :ref:`contact` Nicolas Fernandez or Avi Ma'ayan with questions or use the GitHub `issues`_ feature to raise an issue.

.. _`SVG`: https://en.wikipedia.org/wiki/Scalable_Vector_Graphics
.. _`clustergrammer`: https://github.com/MaayanLab/clustergrammer
.. _`npm package`: https://www.npmjs.com/package/clustergrammer
.. _`index.html`: https://github.com/MaayanLab/clustergrammer/blob/master/index.html
.. _`load_clustergram.js`: https://github.com/MaayanLab/clustergrammer/blob/master/js/load_clustergram.js
.. _`multiple_clust.html`: https://github.com/MaayanLab/clustergrammer/blob/master/multiple_clustergrams.html
.. _`load_multiple_clustergrams.js`: https://github.com/MaayanLab/clustergrammer/blob/master/js/load_multiple_clustergrams.js
.. _`D3.js`: https://d3js.org/
.. _`JQuery`: https://jquery.com/
.. _`Underscore`: http://underscorejs.org/
.. _`Webpack Module Bundler`: https://webpack.github.io/
.. _`src`: https://github.com/MaayanLab/clustergrammer/tree/master/src
.. _`issues`: https://github.com/MaayanLab/clustergrammer/issues

.. |npm-version| image:: https://img.shields.io/npm/v/clustergrammer.svg
    :alt: version
    :scale: 100%
    :target: https://www.npmjs.com/package/clustergrammer

.. |license| image:: https://img.shields.io/npm/l/clustergrammer.svg
    :alt: license
    :scale: 100%
    :target: https://github.com/MaayanLab/clustergrammer/blob/master/LICENSES/LICENSE