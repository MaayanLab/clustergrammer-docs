.. _biology_specific_features:

Biology-Specific Features
-------------------------
Clustergrammer was built to visualize high-dimensional biological data (e.g. genome-wide expression data), but can be generally applied to any high-dimensional data (e.g. any matrix). Clustergrammer has several biology-specific features that faciliate analysis of gene-level biological data, such as: gene-expression data, proteomics-data, etc. To take advantage of these feaatures gene-level data (e.g. dimensions) must be given as rows. See `CCLE Explorer`_ for examples of gene-expression data.

Mouseover Gene Name and Description
===================================
The human genome consists of over 20,000 genes and modern high-throughput measurements are capable of making mesurements across the entire genome (e.g. genome-wide expression studies). Human genes have been given official gene symbols (e.g. EGFR) and these are frequently used to label genes in these datasets. Since no biologist can be knowledgable about every gene in the genome a common task for biologists is looking up the names and descriptions of genes in a dataset or visualization. To streamline this, Clustergrammer automatically gives the full name and description of a gene (provided by data aggregated through the `Harmonizome`_) as a tooltip when a user mouses over a gene label. This simple feature speeds up analysis of large gene-level datasets.

The JavaScript file `hzome_functions.js`_ provides this functionality by utilizing `Harmonizome`_'s RESTful API to obtain gene names and descriptions on mouseover events. `hzome_functions.js`_ is passed to :ref:`clustergrammer_js` as a callback function. See `load_clustergram.js`_ for an example use case.

Enrichment Analysis
===================
The field of biology has amassed an enormous amount of information about the genes in living organisms such as: function, disease-association, up-stream regulators, protein-level binding partners, etc. Integration of this information can help biologists understand patterns in their data. For instance, enrichment analysis a popular method to identify biological information specific to a list of genes - e.g. a biologist may use enrichment analysis to identify up-stream regulatory transcription factors that specifically target their measured set of up-regulated genes and thereby form hypotheses about potential up-stream regulators in their system.

When a user visualizes a matrix with genes as rows, Clustergrammer automatically enables intergration with the enrichment analysis tool `Enrichr`_. Users can export their genes of interest to Enrichr using the interactive dendrogram or import enrichment results from Enrichr using the Enrichr tool on the top left.

The JavaScript file `Enrichrgram.js`_ provides this functionality using `Enrichr`_'s RESTful API to generate enrichment results from a list of input genes. `Enrichrgram.js`_ works with the :ref:`clustergrammer_js` API to depict enriched terms and their associated genes as row categories by adding/removing row categories.

.. _`Enrichrgram.js`: https://github.com/MaayanLab/clustergrammer/blob/master/js/Enrichrgram.js
.. _`hzome_functions.js`: https://github.com/MaayanLab/clustergrammer/blob/master/js/hzome_functions.js
.. _`load_clustergram.js`: https://github.com/MaayanLab/clustergrammer/blob/master/js/load_clustergram.js
.. _`CCLE Explorer`: http://amp.pharm.mssm.edu/clustergrammer/CCLE/
.. _`Harmonizome`: http://amp.pharm.mssm.edu/Harmonizome/
.. _`Enrichr`: http://amp.pharm.mssm.edu/Enrichr/