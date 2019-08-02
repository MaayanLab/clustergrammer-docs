.. _clustergrammer2:

Clustergrammer2
---------------

Clustergrammer2 is an interactive heatmap Jupyter widget built using the widget-ts-cookiecutter library and the WebGL library `regl`_. Clustergrammer2 is built to help researchers interactively explore single cell data (e.g. scRNA-seq). Please see Case Studies and Tutorials for examples.

Single Cell Gene Expression 2,700 PBMC
=======================================

|MyBinder-scRNA-seq| |NBViewer-scRNA-seq|

.. raw:: html

         <div style="position: relative; padding-bottom: 10px; height: 0; overflow: hidden; max-width: 100%; height: auto;">

         <iframe width="560" height="315" src="https://www.youtube.com/embed/BEPspcC7vIY" frameborder="0" allow="autoplay; encrypted-media" allowfullscreen></iframe>
         </div>

Single cell RNA-seq (scRNA-seq) is a powerful method to interrogate gene expression across thousands of single cells. This method provides thousands of measurements (single cells) across thousands of dimensions (genes). Clustergrammer2 is used to interactively explore an example dataset of 2,700 PBMCs obtained from `10X Genomics`_. Bulk gene expression signatures of cell types obtained from `CIBERSORT`_ were used to obtain a tentative cell type for each cell. The data and code can be found on GitHub at `clustergrammer2-notebooks`_ and the notebook can be viewed and re-run on the cloud - see below.



.. _clustergrammer2_dev:

Clustergrammer2 Development
===================================
Clustergrammer2's source code can be found in the `Clustergrammer2 GitHub repo`_. Clustergrammer2 is built using the jupyter-widgets framework (using the `cookie cutter`_ template).

Please :ref:`contact` Nicolas Fernandez and Avi Ma'ayan with questions or use the GitHub `issues`_ feature to report an issue.


.. _`Clustergrammer2 GitHub repo`: https://github.com/ismms-himc/clustergrammer2
.. _`cookie cutter`: https://github.com/jupyter-widgets/widget-ts-cookiecutter
.. _`regl`: http://regl.party/

.. _`10X Genomics`: https://www.10xgenomics.com/resources/datasets/
.. _`CIBERSORT`: https://cibersort.stanford.edu/
.. _`clustergrammer2-notebooks`: https://github.com/ismms-himc/clustergrammer2-notebooks
.. _`MyBinder`: https://gke.mybinder.org/

.. _`MyBinder scRNA-seq 2700`: https://mybinder.org/v2/gh/ismms-himc/clustergrammer2-notebooks/master?filepath=notebooks%2F3.0_2700_PBMC_scRNA-seq.ipynb
.. _`NBViewer scRNA-seq 2700`: https://nbviewer.jupyter.org/github/ismms-himc/clustergrammer2-notebooks/blob/master/notebooks/3.0_10X_Genomics_2700_Dataset_NBViewer.ipynb


.. |MyBinder-scRNA-seq| image:: https://img.shields.io/badge/launch-3.0_2700_PBMC_scRNAseq-579ACA.svg?logo=data:image/png;base64,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
    :alt: MyBinder-scRNA-seq
    :scale: 100%
    :target: https://mybinder.org/v2/gh/ismms-himc/clustergrammer2-notebooks/master?filepath=notebooks%2F3.0_2700_PBMC_scRNA-seq.ipynb

.. |NBViewer-scRNA-seq| image:: https://img.shields.io/badge/jupyter_notebooks-nbviewer-purple.svg?style=flat
    :alt: NBViewer-scRNA-seq
    :scale: 100%
    :target: https://nbviewer.jupyter.org/github/ismms-himc/clustergrammer2-notebooks/blob/master/notebooks/3.0_2700_PBMC_scRNA-seq.ipynb