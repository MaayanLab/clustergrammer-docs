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
Clustergrammer allows users to zoom and pan by scrolling and dragging. This is useful for working with large datasets (where labels are not readable without zooming) and for zooming into regions of interest of your data.

**Zooming Panning Behavior**

Zooming occurs in two stages. First zooming/panning occurs in the direction that matrix cells have been more compressed (e.g. if there are more more rows than columns, then matrix cells will be compressed in the vertical direction and will be wide). Once zooming has decompressed matrix cells (e.g. matrix cells are now squares) then zooming/panning occurs in both directions. For instance, when visualizing a matrix with many more columns than rows zooming/panning will occur in the horizontal direction first until matrix cells have equal width and height, then zooming/panning will be allowed in the vertical and horizontal direction.

**Large Matrix Behavior**

Clustergrammer is capable of visualizing matrices with ~500,000 to ~1,000,000 matrix cells, but is optimized to visualize matrices with more rows than columns. Clustergrammer uses row-downsampling to improve visualization performance with large matrices. If a user visualizes a matrix with a large number of rows (e.g. >1000-2000) such that each matrix cell is less than 1 pixel tall, then Clustergrammer will perform downsampling. When zoomed out, the user will see a downsampled version of their data. Zooming into the matrix will bring up successively less downsampled views until the original data is shown (e.g. when the original matrix cells are > 1 pixels tall). Clustergrammer will also not display row labels until their font size is above ~5 pixels and they are readable. Clustergrammer will also hide row/column labels while zooming into large matrices to improve performance.


Mouseover Interactions
======================
Mousing over visualization elements brings up more information in tooltips. For instance, mousing over matrix cells brings up a tooltip with the row name, column name, and value of the matrix cell.

  **<screenshot of mouseover tooltip>**

See :ref:`clustergrammer_js_api` for information about adding callback functions to mouseover events and :ref:`hzome_gene_info` for biology specific mouseover behavior.

.. _sidebar_interactions:

Sidebar Interactions
====================
Clustergrammer visualizations have a sidebar section that contain:

- optional about section (see :ref:`clustergrammer_js_api`)
- icon buttons: :ref:`share <share_heatmap>`, snapshot_, download_, cropping_
- row and column reordering_ buttons
- :ref:`Row Search Box <search>`
- :ref:`Opacity Slider<opacity>`
- :ref:`Row Filter Sliders <interactive_dim_reduction>`

.. _row_col_reordering:
.. _reordering:

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

**Row Filter Sliders**

Clustergrammer enables users to interactively perform dimensionality reduction by filtering rows based on sum or variance and instantaneously observe the effects of this dimensionality reduction on clustering (where matrix rows represent dimensions, see :ref:`matrix_format_io`). Users can filter for the top rows based on sum or variance using the row-filter-sliders in the sidebar. The sliders allow users to select their top 500, 250, 100, 50, 20, and 10 rows (clustered views of the filtered matrices are pre-calculated by :ref:`clustergrammer_py`). This can be useful for filtering out dimensions that are not of interest (e.g. dimensions with low sum may not be of interest) and determining the effect of these dimensions on clustering.

  **<screenshot of sidebar filters and maybe before after fiiltering>**

**Visualizing Dimensionality Reduction**

For small matrices dimensionality reduction is animated to help the user visualize the effects this transformation. Clustergrammer employs the concept of `object constancy`_ by using animations to help the user visually follow changes to their data. Filtering out dimensions (rows) occurs in two steps: 1) filtered rows fade out, then the remaining rows rearrange themselves into their new order (e.g. clustering order). Adding back in dimensions (rows) occurs in two steps: the current rows rearrange themselves into their new positions, then the new rows fade into view.

.. _interactive_dendrogram:

Dendrogram
==========
Clustergrams typically have `dendrogram trees`_ (for both rows and columns) to depict the hierarchy of row and column clusters produced by `hierarchical clustering`_. The height of the branches in the dendrogram depict how different clusters are from each other. :ref:`clustergrammer_py` calculates hierarchical clustering using `SciPy`_'s hierarchy_ clustering functions (with the default linkage type set to average, see `calc_clust.py`_) and saves ten slices of the dendrogram taken evenly across the tree.

**Visualizing Dendrogram Clusters**

Rather than visualize the dendrogram as a large branching structure which takes up a lot of space and is difficult to interact with, Clustergrammer uses a more compact and easy to interact with visual representation: only a single slice of the dendrogram tree is visualized at a time as a set of non-overlapping adjacent clusters (gray trapezoids). Different slices of the dendrogram can be toggled using the dendrogram-sliders (blue circles that move along a gray triangle). Moving the slider up or down shows slices taken higher or lower in the dendrogram tree, and thereby larger or smaller clusters respectively.

  **<screenshot of dendrogram clusters>**

**Interacting with Dendrogram Clusters**

Mousing over a dendrogram cluster (gray trapezoid) highlights the current group of rows or columns (by adding a shadows over the rows or columns not in the cluster) and brings up a tooltip with cluster information. If the rows or columns have categories, this tooltip will show a breakdown of the rows and columns into their categories, which can be useful for understanding how prior knowledge compares to clusters identified in a data-driven manner (e.g. we can ask, do columns with the same category cluster together based on the data). Clicking a dendrogram cluster brings up this same information in a pop-up window and also allows users to export the names of the rows or columns in the cluster. When a user is visualizing biological data with, where rows are official gene symbols, users have the option to export the gene list from the cluster to the enrichment analysis tool, `Enrichr`_ (see :ref:`biology_specific_features` for more information).

  **<screenshot of dendrogram cluster hover over>**
  **<screenshot of dendrogram cluster pop-up>**

**Dendrogrm Cropping**

Each dendrogram cluster has a small triangular crop button above it that allows users to crop the matrix to the rows or columns in this cluster. Clicking on the dendrogram crop button filters out the rows or columns that not in the cluster and resizes the visualization to show the remaining data. For small matrices, this transformation is animated. Dendrogram cropping can be useful for focusing in on a cluster of interest and when used in combination with :ref:`Enrichrgram <enrichrgram>` to import enrichment analysis results into the visualization (as row categories) from `Enrichr`_ for a specific cluster of genes (see :ref:`biology_specific_features` for more information).

.. _interactive_categories:

Categories
==========
Prior knowledge about our system can be represented as row and column categories in a heatmap. For instance, our columns may represent cell lines and our categories may represent the tissues of these cell lines.


*Explain why categories are useful*

*category types: string value*


*mouseover highlighting, reordering, dendrogram breakdown*


*category updating API*

.. _cropping:

Cropping
========
*brush cropping*

.. _download:

Downloading Data from the Visualization
=======================================
Obtaining the underlying data from a visualization for re-use and re-analysis can be a tedious task. To facilitate this common task, Clustergrammer's sidebar has a download icon, shown below, that allows users to download the matrix of data in the visualization. The downloaded data reflects the current state of the matrix, e.g. filtering, cropping, and reordering will be reflected in the downloaded data.

  **<screenshot of download button in sidebar>**

.. _snapshot:

Taking a Snapshot
=================
*stateful snapshots of matrix*

.. _share_heatmap:

Sharing your Interactive Heatmap
================================
Interactive heatmaps produced with the :ref:`clustergrammer_web` and the :ref:`clustergrammer_widget` (when notebooks are rendered through `nbviewer`_) can easily be shared with collaborators by sharing the URL of the visualization on the web app or the notebook. Users can also click the share button on the sidebar (see :ref:`sidebar_interactions`) sidebar to get this shareable URL.

.. _opacity:

Opacity Slider
==============
*useful for dealing with outlier values*

.. _search:

Row Searching
=============
*useful for working with large datasets, animated*

Expanding
=========
*when displaying in constrained spaces*

Biology Specific Interactions
=============================


.. _`Eisen et al., 1998`: http://www.pnas.org/content/95/25/14863.full
.. _`dendrogram trees`: https://en.wikipedia.org/wiki/Dendrogram
.. _`t-SNE`: https://lvdmaaten.github.io/tsne/
.. _`hierarchical clustering`: https://en.wikipedia.org/wiki/Hierarchical_clustering
.. _`PCA`: https://en.wikipedia.org/wiki/Principal_component_analysis
.. _`object constancy`: https://bost.ocks.org/mike/constancy/
.. _`nbviewer`: http://nbviewer.jupyter.org/
.. _`SciPy`: https://www.scipy.org/
.. _`hierarchy`: https://docs.scipy.org/doc/scipy-0.18.1/reference/cluster.hierarchy.html
.. _`calc_clust.py`: https://github.com/MaayanLab/clustergrammer-py/blob/master/clustergrammer/calc_clust.py
.. _`Enrichr`: http://amp.pharm.mssm.edu/Enrichr/