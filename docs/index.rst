.. sphinx-autobuild . _build_html

Welcome to Clustergrammer's Documentation!
------------------------------------------
The Clustergrammer project consists of web-based tools for visualizing and analyzing high-dimensional data as interactive and shareable hierarchically clustered heatmaps (see :ref:`intro_heatmap_clustergram`). Clustergrammer produces highly interactive visualizations that enable intuitive exploration of high-dimensional data and has several optional biology-specific features (e.g. enrichment analysis; see :ref:`biology_specific_features`) to facilitate the exploration of gene-level biological data. The project is free, open-source (all code is available on GitHub), and being actively developed at the `Human Immune Monitoring Center`_ and the `Ma'ayan Lab`_ at the `Icahn School of Medicine at Mount Sinai`_.

What's New
--------------

Visium Spatial Transcriptomics Data from 10X Genomics
====================================================================
|visium-clustergrammer2|

.. raw:: html

         <div style="position: relative; padding-bottom: 10px; height: 0; overflow: hidden; max-width: 100%; height: auto;">

         <iframe width="560" height="315" src="https://www.youtube.com/embed/eGDZA-xm_oc" frameborder="0" allow="autoplay; encrypted-media" allowfullscreen></iframe>
         </div>

We used :ref:`clustergrammer2`, the plotting library `bqplot`_, the Jupyter dashboard library `voila`_, and the Jupyter notebook hosting service `Binder`_ to build an interactive data explroation dashboard for `Visium`_ data from the mouse brain from `10X Genomics`_ (try dashboard: `Visium-Clustergrammer2 Dashboard`_, code: `https://github.com/ismms-himc/visium-clustergrammer2`_). This dashboard generates linked views of spatial tissue data and high-dimensional gene expression data - see GitHub repo `https://github.com/ismms-himc/visium-clustergrammer2`_ for more information.



Single Cell Immune Profiling of Atherosclerotic Plaques
===============================================================


Our collaborators in the `Giannarelli Lab`_ used single-cell proteomics and transcriptomics to investigate the immune landscape of atheroscelerotic plaques (`Fernandez et al.`_) and identify features of T cells and macrophages that were associated with clinical symptomatic disease state (see :ref:`athero_plaques`). We used Clustergrammer2 to analyze scRNA-seq and CITE-seq data as well as infer cell-cell communication pathways.


Clustergrammer2
===============
|MyBinder-scRNA-seq| |NBViewer-scRNA-seq|

.. raw:: html

         <div style="position: relative; padding-bottom: 10px; height: 0; overflow: hidden; max-width: 100%; height: auto;">

         <iframe width="560" height="315" src="https://www.youtube.com/embed/BEPspcC7vIY" frameborder="0" allow="autoplay; encrypted-media" allowfullscreen></iframe>
         </div>

Clustergrammer2 is a WebGL (specifically `regl`_) visualization tool that enables researchers to easily visualize and explore large high-dimensional single-cell datasets (e.g. scRNA-seq data) without the need for traditional dimensionality reduction methods (e.g. t-SNE or UMAP). Please see the tutorial video above and :ref:`case_studies` for more information.

Case Studies and Examples
=========================
Clustergrammer was developed to visualize high-dimensional biological data (e.g. genome-wide expression data), but it can also generally be applied to any high-dimensional data. Please refer to the :ref:`case_studies` and links below for more information:

-  :ref:`athero_plaques`
-  :ref:`clustergrammer2_2700`
-  :ref:`clustergrammer2_citeseq_7800`
-  :ref:`clustergrammer2_CCLE`
- `Lung Cancer PTM and Gene Expression Regulation`_
- `Single-Cell CyTOF Data`_
- `Kinase Substrate Similarity Network`_
- `MNIST Notebook`_
- `Iris Flower Dataset`_
- `USDA Nutrient Dataset`_


JupyterCon 2018
===============

.. raw:: html

         <div style="position: relative; padding-bottom: 10px; height: 0; overflow: hidden; max-width: 100%; height: auto;">

         <iframe width="560" height="315" src="https://www.youtube.com/embed/82epZkmfkrE" frameborder="0" allow="autoplay; encrypted-media" allowfullscreen></iframe>
         </div>

The Clustergrammer-Widget was presented at JupyterCon 2018.

.. _contact:

Contact
=======
Please contact Nicolas Fernandez (nicolas.fernandez@mssm.edu) and Avi Ma'ayan (avi.maayan@mssm.edu) for support, comments, and suggestions. Users can also visit the discussion forum `Clustergrammer2-Gitter`_.

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
   case_studies
   clustergrammer2
   clustergrammer_web
   interacting_with_viz
   biology_specific_features
   matrix_format_io
   building_webpage
   clustergrammer_widget
   clustergrammer_js
   clustergrammer_gl
   clustergrammer_py
   app_integration
   developing_with_clustergrammer
   license

.. _`Clustergrammer2`: https://github.com/ismms-himc/clustergrammer2
.. _`regl`: http://regl.party/
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
.. _`Clustergrammer2-Gitter`: https://gitter.im/clustergrammer2



.. _`Giannarelli Lab`: http://labs.icahn.mssm.edu/giannarellilab/
.. _`Fernandez et al.`: https://www.nature.com/articles/s41591-019-0590-4
.. _`Single-Cell-Immune-Profiling-of-Atherosclerotic-Plaques`: https://github.com/giannarelli-lab/Single-Cell-Immune-Profiling-of-Atherosclerotic-Plaques

.. _`bqplot`: https://github.com/bloomberg/bqplot
.. _`voila`: https://github.com/voila-dashboards/voila
.. _`Binder`: https://mybinder.org/
.. _`https://github.com/ismms-himc/visium-clustergrammer2`: https://github.com/ismms-himc/visium-clustergrammer2
.. _`Visium`: https://www.10xgenomics.com/spatial-transcriptomics/
.. _`10X Genomics`: https://www.10xgenomics.com/
.. _`Visium-Clustergrammer2 Dashboard`: http://bit.ly/visium-clustergrammer2


.. |MyBinder-scRNA-seq| image:: https://img.shields.io/badge/launch-3.0_2700_PBMC_scRNAseq-579ACA.svg?logo=data:image/png;base64,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
    :alt: MyBinder-scRNA-seq
    :scale: 100%
    :target: https://mybinder.org/v2/gh/ismms-himc/clustergrammer2-notebooks/master?filepath=notebooks%2F3.0_2700_PBMC_scRNA-seq.ipynb

.. |NBViewer-scRNA-seq| image:: https://img.shields.io/badge/jupyter_notebooks-nbviewer-purple.svg?style=flat
    :alt: NBViewer-scRNA-seq
    :scale: 100%
    :target: https://nbviewer.jupyter.org/github/ismms-himc/clustergrammer2-notebooks/blob/master/notebooks/3.0_2700_PBMC_scRNA-seq.ipynb


.. |visium-clustergrammer2| image:: https://mybinder.org/badge_logo.svg?style=flat
    :alt: visium-clustergrammer2
    :scale: 100%
    :target: http://bit.ly/visium-clustergrammer2