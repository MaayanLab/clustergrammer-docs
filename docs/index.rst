.. sphinx-autobuild . _build_html

Welcome to Clustergrammer's Documentation!
------------------------------------------
Clustergrammer is a web-based tool for visualizing and analyzing high-dimensional data as interactive and shareable hierarchically clustered heatmaps (see :ref:`intro_heatmap_clustergram`). Clustergrammer's front end (:ref:`clustergrammer_js`) is built using `D3.js`_ and its back end (:ref:`clustergrammer_py`) is built using `Python`_. Clustergrammer produces highly interactive visualizations that enable intuitive exploration of high-dimensional data and has several optional biology-specific features (e.g. enrichment analysis; see :ref:`biology_specific_features`) to facilitate the exploration of gene-level biological data. The project is free and open-source and can be found on `GitHub`_.

.. raw:: html

         <iframe id='iframe_preview' src="https://amp.pharm.mssm.edu/clustergrammer/demo/" frameBorder="0" style='height: 495px; width:730px; margin-bottom:20px;'></iframe>

Press play or interact with the gene-expression demo above to see some of Clustergrammer's interactive features and refer to :ref:`interacting_with_viz` for more information.

JupyterCon 2018
===============

.. raw:: html

         <div style="position: relative; padding-bottom: 10px; height: 0; overflow: hidden; max-width: 100%; height: auto;">

         <iframe width="560" height="315" src="https://www.youtube.com/embed/82epZkmfkrE" frameborder="0" allow="autoplay; encrypted-media" allowfullscreen></iframe>
         </div>

The Clustergrammer-Widget was recently presented at JupyterCon 2018.

What's New?
===========
Clustergrammer is currently being re-built using the WebGL library `regl`_:

* `Clustergrammer-GL`_: WebGL JavaScript Library
* `Clustergrammer2`_: WebGL Jupyter Widget

Try running Clustergrammer2 on mybinder

|intro-notebook|

|ccle-notebook|

and see `Clustergrammer2-Examples`_

Using Clustergrammer
====================

The easiest ways to use Clustergrammer to produce an interactive visualization of your data are to:

- upload a tab-separated matrix file using the Clustergrammer web app: `https://amp.pharm.mssm.edu/clustergrammer/`_
- or use the :ref:`clustergrammer_widget` within a `Jupyter`_ notebook and share using `nbviewer`_ (see `example notebook`_)

The :ref:`clustergrammer_web` is the quickest way to generate an interactive and shareable visualization (see `example visualization`_ and :ref:`getting started Web-app<getting_started_web_app>`). For users who want to visualize their data within a Jupyter notebook, the :ref:`clustergrammer_widget` enables visualizations to be embedded into shareable Jupyter notebooks (see `example notebook`_ and :ref:`Getting Started Widget <getting_started_widget>`).

Web developers can use Clustergrammer's core libraries, :ref:`clustergrammer_js` and :ref:`clustergrammer_py`, or the :ref:`clustergrammer_web_api` to dynamically generate visualizations for their own web applications (see examples in :ref:`app_integration`).

Please read the :doc:`getting_started` guide for more information.

Case Studies and Examples
=========================
Clustergrammer was developed to visualize high-dimensional biological data (e.g. genome-wide expression data), but it can also generally be applied to any high-dimensional data. Please refer to the :ref:`case_studies` and links below for more information:

- `CCLE Explorer`_ (and the `CCLE Jupyter Notebook`_)
- `Lung Cancer PTM and Gene Expression Regulation`_
- `Single-Cell CyTOF Data`_
- `Kinase Substrate Similarity Network`_
- `MNIST Notebook`_
- `Iris Flower Dataset`_
- `USDA Nutrient Dataset`_

.. _contact:

Contact
=======
Please contact Nicolas Fernandez (nicolas.fernandez@mssm.edu) and Avi Ma'ayan (avi.maayan@mssm.edu) for support, comments, and suggestions.

Citing Clustergrammer
=====================
Please consider supporting Clustergrammer by citing our publication:

Fernandez, N. F. et al. Clustergrammer, a web-based heatmap visualization and analysis tool for high-dimensional biological data. Sci. Data 4:170151 doi: `10.1038/sdata.2017.151`_ (2017).

Funding
=======
Clustergrammer is being developed by the `Ma'ayan Lab`_ and the `Human Immune Monitoring Center`_ at the `Icahn School of Medicine at Mount Sinai`_ for the `BD2K-LINCS DCIC`_ and the `KMC-IDG`_.

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

.. _`Clustergrammer2-Examples`: https://github.com/ismms-himc/clustergrammer2-examples
.. _`Clustergrammer2`: https://github.com/ismms-himc/clustergrammer2
.. _`Clustergrammer-GL`: https://github.com/ismms-himc/clustergrammer-gl
.. _`regl`: http://regl.party/
.. _`GitHub`: https://github.com/MaayanLab/clustergrammer
.. _`https://amp.pharm.mssm.edu/clustergrammer/`: https://amp.pharm.mssm.edu/clustergrammer/
.. _`D3.js`: https://d3js.org/
.. _`Python`: https://www.python.org/
.. _`nbviewer`: http://nbviewer.jupyter.org/
.. _`Jupyter`: http://jupyter.org/
.. _`example visualization`: http://amp.pharm.mssm.edu/clustergrammer/viz_sim_mats/58a492b4a63cb826f0be6476/rc_two_cats.txt
.. _`example notebook`: http://nbviewer.jupyter.org/github/MaayanLab/clustergrammer-widget/blob/master/Running_clustergrammer_widget.ipynb
.. _`10.1038/sdata.2017.151`: https://www.nature.com/articles/sdata2017151

.. _`USDA Nutrient Dataset`: http://nbviewer.jupyter.org/github/MaayanLab/USDA_Nutrients_Viz/blob/master/USDA_Nutrients.ipynb

.. _`CCLE Jupyter Notebook`: http://nbviewer.jupyter.org/github/MaayanLab/CCLE_Clustergrammer/blob/master/notebooks/Clustergrammer_CCLE_Notebook.ipynb

.. _`Single-Cell CyTOF Data`: http://nbviewer.jupyter.org/github/MaayanLab/Cytof_Plasma_PMA/blob/master/notebooks/Plasma_vs_PMA_Phosphorylation.ipynb
.. _`Lung Cancer PTM and Gene Expression Regulation`: http://nbviewer.jupyter.org/github/MaayanLab/CST_Lung_Cancer_Viz/blob/master/notebooks/CST_Data_Viz.ipynb
.. _`CCLE Explorer`: http://amp.pharm.mssm.edu/clustergrammer/CCLE/
.. _`Iris Flower Dataset`: http://nbviewer.jupyter.org/github/MaayanLab/iris_clustergrammer_visualization/blob/master/Iris%20Dataset.ipynb


.. _`Kinase Substrate Similarity Network`: https://maayanlab.github.io/kinase_substrate_similarity_network/


.. _`MNIST Notebook`: http://nbviewer.jupyter.org/github/MaayanLab/MNIST_heatmaps/blob/master/notebooks/MNIST_Notebook.ipynb

.. _`USDA Nutrient Dataset`: http://nbviewer.jupyter.org/github/MaayanLab/USDA_Nutrients_Viz/blob/master/USDA_Nutrients.ipynb

.. _`Ma'ayan Lab`: http://labs.icahn.mssm.edu/maayanlab/
.. _`Human Immune Monitoring Center`: https://icahn.mssm.edu/research/human-immune-monitoring-center
.. _`Icahn School of Medicine at Mount Sinai`: http://icahn.mssm.edu/
.. _`BD2K-LINCS DCIC`: http://lincs-dcic.org/
.. _`KMC-IDG`: http://commonfund.nih.gov/idg/overview
.. _`example notebook`: http://nbviewer.jupyter.org/github/MaayanLab/clustergrammer-widget/blob/master/Running_clustergrammer_widget.ipynb

.. |intro-notebook| image:: https://img.shields.io/badge/launch-1.0%20Example%20notebook-579ACA.svg?logo=data:image/png;base64,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
    :alt: version
    :scale: 100%
    :target: https://mybinder.org/v2/gh/ismms-himc/clustergrammer2-examples/master?filepath=notebooks%2F1.0_Clustergrammer2_Example_Notebook.ipynb

.. |ccle-notebook| image:: https://img.shields.io/badge/launch-2.0%20CCLE%20Gene%20Expression-579ACA.svg?logo=data:image/png;base64,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
    :alt: version
    :scale: 100%
    :target: https://mybinder.org/v2/gh/ismms-himc/clustergrammer2_examples/master?filepath=notebooks%2F2.0_CCLE_Gene_Expression.ipynb

