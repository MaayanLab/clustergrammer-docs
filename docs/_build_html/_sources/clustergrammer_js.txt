.. _clustergrammer_js:

Clustergrammer-JS
-----------------
|npm-version|
|license|

Clustergrammer-JS is the front-end JavaScript library that builds the interactive heatmap visualization in `SVG`_ using the visualization library `D3.js`_

.. _clustergrammer_js_dependencies:

Clustergrammer-JS Dependencies
==============================

- `D3.js`_
- `JQuery`_
- `Underscore`_
- `Bootstrap`_

Installation
============
Clustergrammer.js can be installed using node package manager (`npm package`_) with the following:
::

  npm install clustergrammer

or the source code and library, ``clustergrammer.js``, can be obtained from the `Clustergrammer GitHub repo`_.

.. _javascript_workflow_example:

JavaScript Workflow Example
============================
This workflow shows how to generate a visualization using the JSON produced by Clustergrammer.py
::

  // load visualization JSON to network_data
  var args = {
    'root': '#id_of_container',
    'network_data': 'network_data'
  }

  var cgm = Clustergrammer(args);

The ``id`` of the container where the visualization will be made is passed as ``root`` (this root container must be made by the user). The :ref:`visualization_json` contains the information necessary to generate the visualization and is passed as ``network_data``. See the :ref:`clustergrammer_js_api` for additional arguments that can be passed to Clustergrammer.js.

.. _example_pages:

Example Pages
=============
The `Clustergrammer GitHub repo`_ contains several example pages demonstrating how to build a webpage with a Clustergrammer heatmap. The page `index.html`_ and corresponding script `load_clustergram.js`_ show how to make a full-screen resizable visualization. The page `multiple_clust.html`_ and corresponding script `load_multiple_clustergrams.js`_ show how to visualize multiple clustergrams on one page. Note that each heatmap requires its own container.

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

    .. js:attribute:: args.row_label, args.col_label

      Pass strings that will be used as 'super-labels' for rows and columns.

    .. js:attribute:: args.row_label_scale, args.col_label_scale.

      Scaling factor to increase/decrease the size of the rows and column labels.

    .. js:attribute:: args.super_label_scale

      Scaling factor to increase/decrease the size of the row/column 'super-labels'.

    .. js:attribute:: args.opacity_scale

      Name of the scaling function, e.g. `linear`, `log`, used to map matrix cell values to cell opacity. The default is `linear`.

    .. js:attribute:: args.input_domain

      The `input_domain` defines the maximum absolute value of matrix cells that are mapped to the maximum opacity of 1. The default `input_domain` is defined using the maximum absolute value of the matrix. Lowering the `input_domain` value increases the opacity of the overall visualization by setting a cutoff.

    .. js:attribute:: args.do_zoom

      This boolean value turns on or off zooming. The default is `true`.

    .. js:attribute:: args.tile_colors

      Set the positive and negative colors in the heatmap using an array with color names or hexcode, e.g. ``['#ED9124','#1C86EE']``. The default is `red` and `blue` for positive and negative, respectively.

    .. js:attribute:: args.row_order, args.col_order

      Set the initial ordering for rows and columns. The default is `clust` and the options are:

        * `alpha`: order based on names
        * `clust`: order based on clustering
        * `rank`: order based on sum
        * `rank_var`: order based on variance

    .. js:attribute:: args.ini_view

      Load clustergram using an initial filtered `view`.

    .. :js:attribute:: args.max_allow_fs

      This sets th emaximum allowed font-size. The default is set to 16px.

    .. js:attribute:: args.about

      This attribute is a string (which can include HTML) that will produce a small About section at the top of the sidebar. This can be used to provide a quick description about the data or visualization.

    .. js:attribute:: args.row_tip_callback

      Users can pass a callback function that will run when mousing over row labels.

    .. js:attribute:: args.col_tip_callback

      Users can pass a callback function that will run when mousing over column labels.

    .. js:attribute:: args.tile_tip_callback

      Users can pass a callback function that will run when mousing over a matrix-cell (e.g. matrix tile).

    .. js:attribute:: args.dendro_callback

      Users can pass a callback function that will run when mousing over a dendrogram cluster (e.g. gray trapezoid)

    .. js:attribute:: args.dendro_click_callback

      Users can pass a callback function that will run when clicking a dendrogram cluster (e.g. gray trapezoid)

    .. js:attribute:: args.matrix_update_callback

      Users can pass a callback function that will run anytime the matrix has been updated, for instance when filtering/un-filtering, cropping, etc.

    .. js:attribute:: args.ini_expand

      Initialize the visualization in 'expanded' mode where the sidebar is not visible. The sidebar can be shown by clicking the menu button on the top left of the visualization.

    .. js:attribute:: args.sidebar_width:

      Users can modify the width of the sidebar by specifying the width of the sidebar in pixels as a number.

    .. js:attribute:: args.ini_view

      Users can initialize the 'view' of their matrix, e.g. initialize the matrix at a particular row filtering level.

    .. js:attribute:: args.make_modals

      This boolean option gives users have the option to not make any Bootstrap modals (e.g. dendrogram group modals) and the default is ``true``.




  Clustergrammer's attributes and functions are listed below:

  .. js:attribute:: params

    The Clustergrammer parameters object, which contains all the parameters necessary to generate the visualization.

  .. js:function:: update_cats(row_data)

    Update the visualization row categories.

    :param row_data: Row category data.

  .. js:function:: reset_cats()

    Reset the row categories to their original state.

  .. js:function:: resize_viz:

    Call this function to resize the visualization to fit in its resized container (if the user has resized the container).

  .. js:function:: d3_tip_custom

    Generate a D3 tooltip for SVG elements.

  .. js:function:: update_view(filter_type, inst_state)

    Update the heatmap with a specified row filter 'view'.

    :param filter_type: The available filter types sum or variance: e.g. N_row_sum, N_row_var

    :param inst_state: The value of the row filter, e.g. 500

  .. js:function:: filter_viz_using_names(names)

    Update the visualization to show the row and column names specified in the ``names`` object.

    :param names: Object with ``row`` and/or ``col`` attributes that specify the row and column names that will be visible after updating. Row and column names should be given as a list. Users can include only one attribute, e.g. filter rows only by including no ``col`` attribute, to only filter rows or columns (or users can specify an empty list to not filter).

  .. js:function:: filter_viz_using_nodes(nodes)

    Update the visualization to show the row and column names specified in the ``nodes`` object.

    :param names: Object with ``row`` and ``col`` attributes that specify the row and column nodes that will be visible after updating.

  .. js:function:: zoom(pan_x, pan_y, zoom)

    Zoom and pan into the visualization.

    :param pan_x: Panning in the `x` direction

    :param pan_y: Panning in the `y` direction

    :param zoom: The zoom level applied to the visualization.

  .. js:function:: export_matrix()

    Save the current matrix (e.g. after cropping) as a tab-separated file.


.. _visualization_json:

Visualization-JSON
==================
The visualization-JSON is calculated by :ref:`clustergrammer_py` and encodes everything needed for the front-end Clustergrammer-JS to produce the visualization. The visualization-JSON format is described here (see `clustergrammer_example.json`_ for an example file). An overview of the format is shown below (note that the group arrays are not shown):
::

  {
    "row_nodes":[
       {
        "name": "ATF7",
        "clust": 67,
        "rank": 66,
        "rankvar": 10,
        "group": []
      }
    ],
    "col_nodes":[
      {
        "name": "Col-0",
        "clust": 4,
        "rank": 10,
        "rankvar": 120,
        "group": []
      }
    ],
    "mat":[
      [1, 2],
      [3, 4],
      [5, 6]
    ],
    "links":[
      {
        "source": 0,
        "target": 0,
        "value": 0.023
      }
    ]
  }

Optional 'views' of the matrix (e.g. row-filtered views) are encoded into the ``views`` attribute at the base level of the object. These views are used to store a filtered version of the matrix. Only the row and column names are stored in these views since all views share the same matrix cells. The view attributes are stored in the view object (e.g. ``N_row_sum``):
::

  "views":[
    {
      "N_row_sum": "all",
      "dist": "cos",
      "nodes":{
        "row_nodes": [],
        "col_nodes": []
      }
    }

There are three required properties for the Visualization-JSON: ``row_nodes``, ``col_nodes``, and ``mat`` (``links`` can be used in place of ``mat`` and will continue to be supported, but the default format will use ``mat``). Each of these properties is an array of objects and these objects are discussed below.

**Nodes**

``row_nodes`` and ``col_nodes`` objects are required to have three properties: ``name``, ``clust``, ``rank``. ``name`` specifies the name given to the row or column. ``clust`` and ``rank`` give the ordering of the row or column in the clustergram. Two optional properties are ``group`` and ``value``. ``group`` is an array that contains group-membership of the row/column at different dendrogram distance cutoffs and is necessary for displaying a dendrogram. If nodes have the ``value`` property, then semi-transparent bars will be displayed behind the labels to represent this value.

**Mat**

``mat`` is an JavaScript array that stores the matrix data. The ``source`` and ``target`` of each value (row and column) are inferred from the position of the data in the two-dimensional array.

**Links**

Note: ``mat`` will be used by default instead of ``links``, but both formats will be supported (``mat`` is usually a more compact format). ``links`` have three properties: ``source``, ``target``, and ``value``. ``source`` and ``target`` give the integer value of the row and column of the matrix-cell in the visualization. ``value`` specifies the opacity and color of the matrix-cell, where positive/negative values results in red/blue matrix-cells in the visualization. The optional properties ``value_up`` and ``value_dn`` allow the user to have a split matrix-cell that has an up-triangle and a down-triangle.


Users can also generate the visualization-JSON using their own scripts provided that they adhere to the above format.

.. _clustergrammer_js_dev:

Clustergrammer-JS Development
=============================
The Clustergrammer-JS source code can be found in the `Clustergrammer GitHub repo`_. The Clustergrammer-JS library is utilized by the :ref:`clustergrammer_web` and the :ref:`clustergrammer_widget`. Clustergrammer-JS is built with `Webpack Module Bundler`_ from the source files in the `src`_ directory.

Please :ref:`contact` Nicolas Fernandez and Avi Ma'ayan with questions or use the GitHub `issues`_ feature to report an issue.

.. _`SVG`: https://en.wikipedia.org/wiki/Scalable_Vector_Graphics
.. _`Clustergrammer GitHub repo`: https://github.com/MaayanLab/clustergrammer
.. _`npm package`: https://www.npmjs.com/package/clustergrammer
.. _`index.html`: https://github.com/MaayanLab/clustergrammer/blob/master/index.html
.. _`load_clustergram.js`: https://github.com/MaayanLab/clustergrammer/blob/master/js/load_clustergram.js
.. _`multiple_clust.html`: https://github.com/MaayanLab/clustergrammer/blob/master/multiple_clustergrams.html
.. _`load_multiple_clustergrams.js`: https://github.com/MaayanLab/clustergrammer/blob/master/js/load_multiple_clustergrams.js
.. _`D3.js`: https://d3js.org/
.. _`JQuery`: https://jquery.com/
.. _`Underscore`: http://underscorejs.org/
.. _`Bootstrap`: http://getbootstrap.com/
.. _`Webpack Module Bundler`: https://webpack.github.io/
.. _`src`: https://github.com/MaayanLab/clustergrammer/tree/master/src
.. _`issues`: https://github.com/MaayanLab/clustergrammer/issues

.. _`clustergrammer_example.json`: https://github.com/MaayanLab/clustergrammer-json/blob/master/clustergrammer_example.json

.. |npm-version| image:: https://img.shields.io/npm/v/clustergrammer.svg
    :alt: version
    :scale: 100%
    :target: https://www.npmjs.com/package/clustergrammer

.. |license| image:: https://img.shields.io/npm/l/clustergrammer.svg
    :alt: license
    :scale: 100%
    :target: https://github.com/MaayanLab/clustergrammer/blob/master/LICENSES/LICENSE