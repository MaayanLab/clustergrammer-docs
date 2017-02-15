.. _interacting_with_viz:

Interacting with the Visualization
----------------------------------
Data visualizations benefit enormously from user interactions that allow users to explore and generate new views of their data. Clustergrammer produces highly interactive heatmaps that enable users to intuitively explore and perform complex transformations on their data. This section will cover the types of interactions available to the user.

Introduction to Clustergrams/Heatmaps
=====================================
Clustergrammer visualizes high-dimensional data as a hierarchically clustered matrix with colored tiles (red for positive numbers and blue for negative numbers) and row and column labels, commonly referred to as a heatmap or clustergram (this documentation uses heatmap and clustergram interchangeably, see `Eisen et al., 1998`_ for an early example using biological data). Clustergrams also typically have `dendrogram trees`_ to depict the hierarchy of row and column clusters formed from hierarchical clustering.

Heatmaps are a powerful visualization tool that enables users to directly visualize high-dimensional data without the loss of information and interpretability associated with dimensionality reduction techniques (e.g. `t-SNE`_). For instance, columns can depict measurements (e.g. data-points) and rows can depict dimensions (e.g. measured variables). In this way heatmaps can visualize thousands of data-points in thousands of dimensions. However, static heatmaps are of limited use for visualizing large datasets (where matrix cells and labels become too small to read). Furthermore, static heatmaps prevent users from interactively exploring their data, e.g. reordering rows/columns.

Zooming and Panning
===================

Mouseover Interactions
======================

Row and Column Reordering
=========================

Dimensionality Reduction (Row Filtering)
========================================

Interactive Dendrogram
======================

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

.. _`Eisen et al., 1998`: http://www.pnas.org/content/95/25/14863.full
.. _`dendrogram trees`: https://en.wikipedia.org/wiki/Dendrogram
.. _`t-SNE`: https://lvdmaaten.github.io/tsne/