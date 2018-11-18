.. _case_studies:

Case Studies and Examples
-------------------------
Clustergrammer was developed to visualize high-dimensional biological data (e.g. genome-wide expression data), but it can also generally be applied to any high-dimensional data. Below are links to several case studies and examples using Clustergrammer to explore high-dimensional data. All examples are below are publically available through GitHub.

Cancer Cell Line Encyclopedia Gene Expression Data
==================================================

.. figure:: _static/CCLE_explorer.png
  :width: 800px
  :align: left
  :alt: CCLE Explorer
  :target: https://maayanlab.github.io/CCLE_Clustergrammer/

  Screenshot from the `CCLE Explorer`_ showing the tissue breakdown of the CCLE. Clicking on a tissue brings up an interactive heatmap with the top 250 most variable genes within a tissue. Also see the `CCLE Jupyter Notebook`_ for an example of how to explore the CCLE gene expression data in a Jupyter notebook.

The Cancer Cell Line Encyclopedia (`CCLE`_) is a publicly available project that has characterized (e.g. genetic characterization) over 1,000 cancer cell lines. We used Clustergrammer to re-analyze and visualize CCLE's gene expression data in the `CCLE Explorer`_. The CCLE Explorer allows users to explore the CCLE by tissue type and visualize the most commonly differentially expressed genes for each tissue type as an interactive heatmap. The `CCLE Jupyter Notebook`_ generates an overview of the CCLE gene expression data, investigates specific tissues, and explains how to use :ref:`Enrichrgram <enrichrgram>` to understand the biological functions of differentially expressed genes.

Lung Cancer Post-Translational Modification and Gene Expression Regulation
==========================================================================

.. figure:: _static/CST_screenshot.png
  :width: 450px
  :align: left
  :alt: CST Screenshot
  :target: http://nbviewer.jupyter.org/github/MaayanLab/CST_Lung_Cancer_Viz/blob/master/notebooks/CST_Data_Viz.ipynb

  Screenshot from the `CST_Data_Viz.ipynb`_ Jupyter notebook showing hierarchical clustering of differential phosphorylation, methylation, acetylation, and gene expression data across 37 lung cancer cell lines. See the interactive Jupyter notebook `CST_Data_Viz.ipynb`_ for more information.

Lung cancer is a complex disease that is known to be regulated at the post-translational modification (PTM) level, e.g. phosphorylation driven by kinases. Our collaborators at `Cell Signaling Technology Inc`_ used Tandem Mass Tag (TMT) mass spectrometry to measure differential phosphorylation, acetylation, and methylation in a panel of 42 lung cancer cell lines compared to non-cancerous lung tissue. Gene expression data from 37 of these lung cancer cell lines was also independently obtained from the publicly available Cancer Cell Line Encyclopedia (`CCLE`_). In the Jupyter notebook `CST_Data_Viz.ipynb`_ we:

- Visualize PTM data, gene expression data, and merged PTM/gene-expression data
- Identify co-regulated clusters of PTMs/genes in distinct lung cancer cell line subtypes
- Perform enrichment analysis to understand the biological processes involved in PTM/expression clusters

CyTOF Data: Single Cell Immune Response to PMA Treatment
========================================================

.. figure:: _static/CyTOF_screenshot.png
  :width: 450px
  :align: left
  :alt: CyTOF Screenshot
  :target: http://nbviewer.jupyter.org/github/MaayanLab/Cytof_Plasma_PMA/blob/master/notebooks/Plasma_vs_PMA_Phosphorylation.ipynb

  Screenshot from the `Plasma_vs_PMA_Phosphrylation.ipynb`_ Jupyter notebook showing downsampled single cell CyTOF data (K-means downsampled from 220,000 single cells to 2,000 cell-clusters). Cell-clusters are shown as rows with cell-type categories (e.g. Natural Killer cells) and phosphorylations are shown as columns. See the interactive Jupyter notebook `Plasma_vs_PMA_Phosphrylation.ipynb`_ for more information.

White blood cells are a key component of the immune system and kinase signaling is known to play an important role in immune cell function (see `Isakov and Altman 2013`_). Our collaborators in the `Giannarelli Lab`_ and the `Icahn School of Medicine Human Immune Monitoring Core`_ used Mass Cytometry, CyTOF (Fluidigm), to investigate the phosphorylation response of peripheral blood mononuclear cells (PBMC) immune cells exposed to PMA (phorbol 12-myristate 13-acetate), a tumor promoter and activator of protein kinase C (PKC). A total of 28 markers (18 surface markers and 10 phosphorylation markers) were measured in over 200,000 single cells. In the Jupyter notebook `Plasma_vs_PMA_Phosphrylation.ipynb`_ we semi-automatically identify cell types using surface markers and cluster cells based on phosphorylation to identify cell-type specific behavior at the phosphorylation level. See the `Plasma_vs_PMA_Phosphrylation.ipynb`_ Jupyter notebook for more information.

Large Network: Kinase Substrate Similarity Network
==================================================
.. figure:: _static/kinase_network_screenshot.png
  :width: 450px
  :align: left
  :alt: Kinase Network Screenshot
  :target: https://maayanlab.github.io/kinase_substrate_similarity_network/

  Screenshot from the `Kinase Substrate Similarity Network`_ example that demonstrates how Clustergrammer can be used to visualize a large network of kinases based on shared substrates.

Clustergrammer can be used to visualize large networks without the formation of 'hairballs'. In the `Kinase Substrate Similarity Network`_ example we use Clustergrammer to visualize a network kinases based on shared substrate that includes 404 kinases and 163,216 links. Kinases are shown as rows and columns. For more information see the `Kinase Substrate Similarity Network`_ example.

Machine Learning and Miscellaneous Datasets
===========================================
.. figure:: _static/MNIST_screenshot.png
  :width: 450px
  :align: left
  :alt: MNIST Screenshot
  :target: http://nbviewer.jupyter.org/github/MaayanLab/MNIST_heatmaps/blob/master/notebooks/MNIST_Notebook.ipynb#Visualize-Downsampled-Version-of-MNIST

  Screenshot from the `MNIST Notebook`_ that demonstrates how the :ref:`clustergrammer_widget` can be used to visualize the `MNIST Data`_. Downsampled handwritten digits (K-means downsampled from 70,0000 handwritten digits to 300 digit-clusters) are shown as columns with digit-type categories and pixels are shown as rows. For more information see the `MNIST Notebook`_.

Clustergrammer was used to visualize several widely used machine learning Datasets and other miscellaneous Datasets:

- `MNIST Handwritten Digit Dataset`_
- `Iris Flower Dataset`_
- `USDA Nutrient Dataset`_

These examples demonstrate the generality of heatmap visualizations and enable users to interactively explore familiar Datasets.

Zika Virus RNA-seq Data Visualization
=====================================
Clustergrammer was used to visualize the results of an RNA-Seq data analysis pipeline within a Jupyter notebook: `An open RNA-Seq data analysis pipeline tutorial with an example of reprocessing data from a recent Zika virus study`_ (`Wang et al.`_).

Single-Cell RNA-seq Data Visualization
======================================
Clustergrammer was used to visualize published single-cell gene expression data: `Single-Cell RNA-seq Data Visualization`_ (`Olsson et al.`_). The visualization was produced using an Excel file provided alongside the figures.


.. _`Kinase Substrate Similarity Network`: https://maayanlab.github.io/kinase_substrate_similarity_network/
.. _`MNIST Data`: http://yann.lecun.com/exdb/mnist/
.. _`Giannarelli Lab`: http://labs.icahn.mssm.edu/giannarellilab/
.. _`Icahn School of Medicine Human Immune Monitoring Core`: http://icahn.mssm.edu/research/portal/resources/deans-cores/human-immune-monitoring-core
.. _`Plasma_vs_PMA_Phosphrylation.ipynb`: http://nbviewer.jupyter.org/github/MaayanLab/Cytof_Plasma_PMA/blob/master/notebooks/Plasma_vs_PMA_Phosphorylation.ipynb
.. _`Isakov and Altman 2013`: https://www.ncbi.nlm.nih.gov/pmc/articles/PMC3831523/
.. _`CST_Data_Viz.ipynb`: http://nbviewer.jupyter.org/github/MaayanLab/CST_Lung_Cancer_Viz/blob/master/notebooks/CST_Data_Viz.ipynb?flush_cache=true
.. _`Cell Signaling Technology Inc`: https://www.cellsignal.com/
.. _`CCLE Explorer`: http://amp.pharm.mssm.edu/clustergrammer/CCLE/
.. _`CCLE Jupyter Notebook`: http://nbviewer.jupyter.org/github/MaayanLab/CCLE_Clustergrammer/blob/master/notebooks/Clustergrammer_CCLE_Notebook.ipynb
.. _`An open RNA-Seq data analysis pipeline tutorial with an example of reprocessing data from a recent Zika virus study`: http://nbviewer.jupyter.org/github/maayanlab/Zika-RNAseq-Pipeline/blob/master/Zika.ipynb
.. _`Iris Flower Dataset`: http://nbviewer.jupyter.org/github/MaayanLab/iris_clustergrammer_visualization/blob/master/Iris%20Dataset.ipynb
.. _`MNIST Notebook`: http://nbviewer.jupyter.org/github/MaayanLab/MNIST_heatmaps/blob/master/notebooks/MNIST_Notebook.ipynb
.. _`MNIST Handwritten Digit Dataset`: http://nbviewer.jupyter.org/github/MaayanLab/MNIST_heatmaps/blob/master/notebooks/MNIST_Notebook.ipynb
.. _`Single-Cell RNA-seq Data Visualization`: http://nbviewer.jupyter.org/github/MaayanLab/single_cell_RNAseq_Visualization/blob/master/Single%20Cell%20RNAseq%20Visualization%20Example.ipynb
.. _`CCLE`: https://portals.broadinstitute.org/ccle/home
.. _`Wang et al.`: https://f1000research.com/articles/5-1574/v1
.. _`Olsson et al.`: http://www.nature.com/nature/journal/v537/n7622/full/nature19348.html

.. _`USDA Nutrient Dataset`: http://nbviewer.jupyter.org/github/MaayanLab/USDA_Nutrients_Viz/blob/master/USDA_Nutrients.ipynb