.. _interacting_with_viz:

Interacting with the Visualization
----------------------------------
Data visualizations benefit enormously from user interactions that allow users to explore and generate new views of their data. Clustergrammer produces highly interactive heatmaps that enable users to intuitively explore and perform complex transformations on their data. Clustergrammer visualizations are consistent across the :ref:`clustergrammer_web` and the :ref:`clustergrammer_widget` and are built using :ref:`clustergrammer_js`. This section will cover the types of interactions available to the user.

Introduction to Clustergrams/Heatmaps
=====================================
Clustergrammer visualizes high-dimensional data as a hierarchically clustered matrix with colored tiles (red for positive numbers and blue for negative numbers) and row/column labels, commonly referred to as a heatmap or clustergram (this documentation uses heatmap and clustergram interchangeably, see `Eisen et al., 1998`_ for an early example using biological data). Clustergrams also typically have `dendrogram trees`_ to depict the hierarchy of row and column clusters produced by `hierarchical clustering`_.

Heatmaps are a powerful visualizations that enable users to directly visualize high-dimensional data without the loss of information and interpretability associated with dimensionality reduction techniques (e.g. `t-SNE`_). For instance, columns can depict measurements (e.g. data-points) and rows can depict dimensions (e.g. measured variables). In this way, heatmaps can visualize thousands of data-points in thousands of dimensions. However, static heatmaps are of limited use for visualizing large datasets (e.g. matrix cells and labels become too small to read). Furthermore, static heatmaps prevent users from interactively exploring their data, e.g. reordering rows/columns.

Zooming and Panning
===================
Clustergrammer allows users to zoom and pan by scrolling and dragging. This is useful for working with large datasets (where labels are not readable wihouth zooming) and for zooming into regions of interest of your data.

Zooming occurs in two stages. First zooming/panning occurs in the direction that matrix cells have been more compressed (e.g. if there are more more rows than columns, then matrix cells will be compressed in the vertical direction and will be wide). Once zooming has de-compressed matrix cells (e.g. matrix cells are now squares) then zooming/panning occurs in both directions. For instance, when visualizing a matrix with many more columns than rows zooming/panning will occur in the horizontal direction first until matrix cells have equal width and height, then zooming/panning will be allowed in the vertical and horizontal direction.

Mouseover Interactions
======================
Mousing over visualization elements brings up more information in tooltips. For instance, mousing over matrix cells brings up a tooltip with the row name, column name, and value of the matrix cell.

  **<add-screenshot of mouseover tooltip>**

See :ref:`clustergrammer_js_api` for information about adding callback functions to mouseover events and :ref:`hzome_gene_info` for biology specific mouseover behavior.

.. _row_col_reordering:

Row and Column Reordering
=========================
Clustergrammer allows users to order rows and columns based on:

- sum or variance
- hierarchical clustering order
- label order

by using the reordering-buttons on the sidebar. This can be useful for identifying broad patterns in your data. Users can also reorder their matrix based on the values in a single row/column by double-clicking the row/column labels. Similarly, users can reorder based on categorical information by double-clicking the category labels (see :ref:`interactive_categories`). For small matrices reordering events are animated to help users visually track the effects of the transformation.

.. _interactive_dim_reduction:

Interactive Dimensionality Reduction
====================================
Dimensionality reduction is a useful data analysis technique (e.g. `PCA`_ , `t-SNE`_) that is often used to reduce the dimensionality of high-dimensional datasets (e.g. hundreds-thousands of dimensions) down to a number that can be easily be analyzed and visualized (e.g. two-three dimensions). Heatmaps are capable of directly visualizing high-dimensional data, but can also benefit from dimensionality reduction.

Clustergrammer enables users to interactively perform dimensionality reduction by filtering rows based on sum or variance and instantaneously observe the effects of this dimensionality reduction on clustering (where matrix rows represent dimensions, see :ref:`matrix_format_io`). Users can filter for the top rows based on sum or variance using the row-filter-sliders in the sidebar. The sliders allow users to select their top 500, 250, 100, 50, 20, and 10 rows (clustered views of the filtered matrices are pre-calculated by :ref:`clustergrammer_py`). This can be useful for filtering out dimensions that are not of interest (e.g. dimensions with low sum may not be of interest) and determining the effect of these dimensions on clustering.

  **<addscreenshot of sidebar filters>**

For small matrices dimensionality reduction is animated to help the user visualize the effects this transformation. Clustergrammer employs the concept of `object constancy`_ by using animations to help the user visually follow changes to their data. Filtering out dimensions (rows) occurs in two steps: 1) filtered rows fade out, then the remaining rows rearrange themselves into their new order (e.g. clustering order). Adding back in dimensions (rows) occurs in two steps: the current rows rearrange themselves into their new positions, then the new rows fade into view.

Interactive Dendrogram
======================

.. _interactive_categories:

Interactive Categories
======================

Dendrogram Cropping
===================

Brush-Cropping
==============

Downloading Data to File
========================

Taking a Snapshot of the Visualization
======================================

Changing the Opacity
====================

Row Searching
=============

Expanding
=========

Biology Specific Interactions
=============================

Row Downsampling
================

.. _`Eisen et al., 1998`: http://www.pnas.org/content/95/25/14863.full
.. _`dendrogram trees`: https://en.wikipedia.org/wiki/Dendrogram
.. _`t-SNE`: https://lvdmaaten.github.io/tsne/
.. _`hierarchical clustering`: https://docs.scipy.org/doc/scipy-0.18.1/reference/cluster.hierarchy.html
.. _`PCA`: https://en.wikipedia.org/wiki/Principal_component_analysis
.. _`object constancy`: https://bost.ocks.org/mike/constancy/