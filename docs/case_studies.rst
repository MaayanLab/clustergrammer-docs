.. _case_studies:

Case Studies and Examples
-------------------------
Clustergrammer was developed to visualize high-dimensional biological data (e.g. genome-wide expression data), but it can also generally be applied to any high-dimensional data (e.g. a matrix). Below are links to several example case studies and examples using Clustergrammer.

Cancer Cell Line Encyclopedia Gene Expression Data
==================================================
The Cancer Cell Line Encyclopedia (`CCLE`_) is a publicly available project that has characterized (e.g. genetic characterization) over 1,000 cancer cell lines. We used Clustergrammer to re-analyze and visualize CCLE's gene expression data in the `CCLE Explorer`_. The CCLE Explorer allows users to explore the CCLE by tissue type and visualize the most commonly differentially expressed genes for each tissue type as an interactive heatmap. The `CCLE Jupyter Notebook`_ generates an overview of the CCLE gene expression data, investigates specific tissues, and explains how to use :ref:`Enrichrgram <enrichrgram>` to understand the biological functions of differentially expressed genes.

Lung Cancer Post-Translational Modification and Gene Expression Regulation
==========================================================================
Lung cancer is a complex disease that is known to be regulated at the post-translational modification (PTM) level, e.g. phosphorylation driven by kinases. Our collaborators at `Cell Signaling Technology Inc`_ used Tandem Mass Tag (TMT) mass spectrometry to measure differential phosphorylation, acetylation, and methylation in a panel of 42 lung cancer cell lines compared to non-cancerous lung tissue. Gene expression data from 37 of these lung cancer cell lines was also independently obtained from the publically available Cancer Cell Line Encyclopedia (`CCLE`_). In the Jupyter notebook `CST_Data_Viz.ipynb`_ we:

- Visualize PTM data, gene expression data, and merged PTM-Expression data
- Identify co-regulated clusters of PTMs/genes in distinct lung cancer cell line subtypes
- Perform enrichment analysis to understand the biological processes involved in PTM/expression clusters

CyTOF Data: Single Cell Immune Response to PMA Treatment
========================================================
White blood cells are a key component of the immune system and kinase signaling is known to play an imporant role in immune cell function (see `Isakov and Altman 2013`_).

Zika Virus RNA-seq Data Visualization
=====================================
Clustergrammer was used to visualize the results of an RNA-Seq data analysis pipeline within a Jupyter notebook: `An open RNA-Seq data analysis pipeline tutorial with an example of reprocessing data from a recent Zika virus study`_ (`Wang et al.`_).

Single-Cell RNA-seq Data Visualization
======================================
Clustergrammer was used to visualize published single-cell gene expression data: `Single-Cell RNA-seq Data Visualization`_ (`Olsson et al.`_). The visualization was produced using an Excel file provided alongside the figures.

Machine Learning and Miscellaneous Datasets
===========================================
Clustergrammer was used to visualize several widely used machine learning Datasets and other miscellaneous Datasets:

- `Iris Flower Dataset`_
- `MNIST Handwritten Digit Dataset`_
- `USDA Nutrient Dataset`_

These examples demonstrate the generality of heatmap visualizations and enable users to interactively explore familiar Datasets.

.. _`Isakov and Altman 2013`: https://www.ncbi.nlm.nih.gov/pmc/articles/PMC3831523/
.. _`CST_Data_Viz.ipynb`: http://nbviewer.jupyter.org/github/MaayanLab/CST_Lung_Cancer_Viz/blob/master/notebooks/CST_Data_Viz.ipynb?flush_cache=true
.. _`Cell Signaling Technology Inc`: https://www.cellsignal.com/
.. _`CCLE Explorer`: http://amp.pharm.mssm.edu/clustergrammer/CCLE/
.. _`CCLE Jupyter Notebook`: http://nbviewer.jupyter.org/github/MaayanLab/CCLE_Clustergrammer/blob/master/notebooks/Clustergrammer_CCLE_Notebook.ipynb
.. _`An open RNA-Seq data analysis pipeline tutorial with an example of reprocessing data from a recent Zika virus study`: http://nbviewer.jupyter.org/github/maayanlab/Zika-RNAseq-Pipeline/blob/master/Zika.ipynb
.. _`Iris Flower Dataset`: http://nbviewer.jupyter.org/github/MaayanLab/iris_clustergrammer_visualization/blob/master/Iris%20Dataset.ipynb
.. _`MNIST Handwritten Digit Dataset`: http://nbviewer.jupyter.org/github/MaayanLab/MNIST_heatmaps/blob/master/notebooks/MNIST_Notebook.ipynb
.. _`Single-Cell RNA-seq Data Visualization`: http://nbviewer.jupyter.org/github/MaayanLab/single_cell_RNAseq_Visualization/blob/master/Single%20Cell%20RNAseq%20Visualization%20Example.ipynb
.. _`CCLE`: https://portals.broadinstitute.org/ccle/home
.. _`Wang et al.`: https://f1000research.com/articles/5-1574/v1
.. _`Olsson et al.`: http://www.nature.com/nature/journal/v537/n7622/full/nature19348.html

.. _`USDA Nutrient Dataset`: http://nbviewer.jupyter.org/github/MaayanLab/USDA_Nutrients_Viz/blob/master/USDA_Nutrients.ipynb