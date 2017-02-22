.. sphinx-autobuild . _build_html

Welcome to Clustergrammer's Documentation!
------------------------------------------
Clustergrammer is a web-based tool for visualizing high-dimensional data (e.g. a matrix) as an interactive and shareable hierarchically clustered heatmap. Clustergrammer's front-end (:ref:`clustergrammer_js`) is built using `D3.js`_ and its back-end (:ref:`clustergrammer_py`) is built using `Python`_. Clustergrammer produces highly interactive visualizations that enable intuitive exploration of high-dimensional data and has several optional biology-specific features (e.g. enrichment analysis, see :ref:`biology_specific_features`) to facilitate the exploration of gene-level biological data. Press play or interact with the gene-expression demo below to see some of Clustergrammer's interactive features and see :ref:`interacting_with_viz` for more information:

.. raw:: html

         <iframe id='iframe_preview' src="http://amp.pharm.mssm.edu/clustergrammer/demo/" frameBorder="0" style='height: 495px; width:730px; margin-bottom:20px;'></iframe>

Using Clustergrammer
====================

The easiest ways to use Clustergrammer to produce an interactive visualization of your data are:

- upload a tab-separated matrix file using the Clustergrammer web app `homepage`_
- or use the :ref:`clustergrammer_widget` within a `Jupyter`_ notebook and share using `nbviewer`_

The :ref:`clustergrammer_web` is the quickest way to generate an interactive and shareable visualization (see `example visualization`_ and :ref:`getting started Web-app<getting_started_web_app>`). For users that want to visualize their data within a notebook workflow, the :ref:`clustergrammer_widget` enables visualizations to be built within Jupyter notebooks and shared through Jupyter's `nbviewer`_ (see `example notebook`_ and :ref:`getting started Widget <getting_started_widget>`).

Web developers can use Clustergrammer's core libraries (:ref:`clustergrammer_js` and :ref:`clustergrammer_py`) or the :ref:`clustergrammer_web_api` to dynamically generate visualizations for their own web applications (see examples in :ref:`app_integration`).

Please read the :doc:`getting_started` guide for more information.

Use Cases
=========
Clustergrammer was built to visualize biological data but is applicable for visualizing high-dimensional data in general. Below are links to several example use cases (see :ref:`case_studies` for more information):

- `Cancer Cell Line Encyclopedia Gene Expression Data`_
- `Single Cell RNA-seq Data Visualization`_
- `Zika Virus RNA-seq Data Visualization`_
- `Kinase Substrate Similarity Network`_
- `Iris flower dataset`_
- `MNIST Handwritten Digit Dataset`_

.. _contact:

Contact
=======
Please contact Avi Ma'ayan (avi.maayan@mssm.edu) and Nicolas Fernandez (nicolas.fernandez@mssm.edu) for support, comments, and suggestions.



Contents:
=========

.. toctree::
   :maxdepth: 2

   getting_started
   clustergrammer_web
   clustergrammer_widget
   interacting_with_viz
   biology_specific_features
   case_studies
   matrix_format_io
   building_webpage
   clustergrammer_js
   clustergrammer_py
   app_integration
   developing_with_clustergrammer
   license

.. _`homepage`: http://amp.pharm.mssm.edu/clustergrammer/
.. _`D3.js`: https://d3js.org/
.. _`Python`: https://www.python.org/
.. _`nbviewer`: http://nbviewer.jupyter.org/
.. _`Jupyter`: http://jupyter.org/
.. _`example visualization`: http://amp.pharm.mssm.edu/clustergrammer/viz_sim_mats/58a492b4a63cb826f0be6476/rc_two_cats.txt
.. _`example notebook`: http://nbviewer.jupyter.org/github/MaayanLab/clustergrammer-widget/blob/master/Running_clustergrammer_widget.ipynb

.. _`Cancer Cell Line Encyclopedia Gene Expression Data`: http://amp.pharm.mssm.edu/clustergrammer/CCLE/
.. _`Zika Virus RNA-seq Data Visualization`: http://nbviewer.jupyter.org/github/maayanlab/Zika-RNAseq-Pipeline/blob/master/Zika.ipynb
.. _`Iris flower dataset`: http://nbviewer.jupyter.org/github/MaayanLab/iris_clustergrammer_visualization/blob/master/Iris%20Dataset.ipynb
.. _`MNIST Handwritten Digit Dataset`: https://maayanlab.github.io/MNIST_heatmaps/
.. _`Single Cell RNA-seq Data Visualization`: http://nbviewer.jupyter.org/github/MaayanLab/single_cell_RNAseq_Visualization/blob/master/Single%20Cell%20RNAseq%20Visualization%20Example.ipynb
.. _`Kinase Substrate Similarity Network`: https://maayanlab.github.io/kinase_substrate_similarity_network/