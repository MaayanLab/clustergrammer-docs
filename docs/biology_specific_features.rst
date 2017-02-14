Biology Specific Features
-------------------------
Clustergrammer was built to visualize high-dimensional biological data (e.g. genome-wide expression data), but can be generally applied to any high-dimensional data (e.g. any matrix). Clustergrammer has several biology-specific features that faciliate analysis of gene-level biological data, such as: gene-expression data, proteomics-data, etc. To take advantage of these feaatures gene-level data (e.g. dimensions) must be given as rows. See `CCLE Explorer`_ for examples of gene-expression data.

Mouseover Gene Name and Description
===================================
The human genome consists of over 20,000 genes and modern high-throughput measurements are capable of making mesurements across the entire genome (e.g. genome-wide expression studies). Human genes have been given official gene symbols (e.g. EGFR) and these are usually used to label genes in these datasets. Since no biologist can be knowledgable about every gene in the genome a common task for biologists is looking up the names and descriptions of genes in a dataset or visualization. To streamline this, Clustergrammer automatically gives the full name and description of a gene (provided by data aggregated through the `Harmonizome`_) as a tooltip when a user mouses over a gene label. This simple feature speeds up analysis of big gene-level data.

Enrichment Analysis
===================

.. _`CCLE Explorer`: http://amp.pharm.mssm.edu/clustergrammer/CCLE/
.. _`Harmonizome`: http://amp.pharm.mssm.edu/Harmonizome/