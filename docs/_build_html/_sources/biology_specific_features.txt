.. _biology_specific_features:

Biology-Specific Features
-------------------------
Clustergrammer was built to visualize high-dimensional biological data (e.g. genome-wide expression data), but can generally be applied to any high-dimensional data (e.g. a matrix). Clustergrammer has several biology-specific features that facilitate the analysis of gene-level biological data, such as: gene-expression data, proteomics-data, etc. To take advantage of these features, genes must be given as rows. See the `CCLE Explorer`_ for examples of gene-expression data. These optional biology-specific features are available in the :ref:`clustergrammer_web` as well as the :ref:`clustergrammer_widget` and will activate if the row-names are genes.

.. _hzome_gene_info:

Mouseover Gene Name and Description
===================================
The human genome consists of over 20,000 genes and modern high-throughput measurements are capable of making measurements across the entire genome (e.g. genome-wide expression studies). Human genes have official gene symbols (e.g. EGFR) that are frequently used to label genes in these datasets. Since no biologist can be knowledgeable about every gene in the genome a common and repetitive task for biologists is looking up the names and descriptions of genes in a dataset or visualization. To streamline this, Clustergrammer automatically gives the full name and description of a gene (provided by data aggregated through the `Harmonizome`_) as a tooltip when a user mouses over a gene label (see screenshot below). This simple feature speeds up analysis of large gene-level datasets.

.. figure:: _static/gene_info.png
  :width: 700px
  :align: center
  :alt: Gene Info

  Mousing over a gene name row brings up the full gene name and description (provided by data aggregated through the `Harmonizome`_).

The JavaScript file `hzome_functions.js`_ provides this functionality by utilizing `Harmonizome's RESTful API`_ to obtain gene names and descriptions on mouseover events. `hzome_functions.js`_ is passed to :ref:`clustergrammer_js` as a callback function. See `load_clustergram.js`_ for an example use case. Mouseover callback functions can be used by developers to extend functionality for other domain-specific problems.


Enrichment Analysis
===================
The field of biology has amassed an enormous amount of information about the genes in living organisms such as: function, disease-association, up-stream regulators, protein-level binding partners, etc. Integration of this information can help biologists understand patterns in their data. For instance, enrichment analysis a popular method to identify biological information specific to a list of genes -- e.g. a biologist may use enrichment analysis to identify up-stream regulatory transcription factors that specifically target their measured set of up-regulated genes and thereby form hypotheses about potential up-stream regulators in their system.

**Export to Enrichr**

When a user visualizes a matrix with genes as rows, Clustergrammer automatically enables integration with the enrichment analysis tool `Enrichr`_. Users can export a set of clustered genes to `Enrichr`_ using the interactive dendrogram (see screenshot) or import enriched terms into the visualization using :ref:`Enrichrgram <enrichrgram>`.

.. figure:: _static/send_to_Enrichr_modal.png
  :width: 600px
  :align: center
  :alt: Send to Enrichr Modal

  Clicking a row dendrogram cluster opens a modal with cluster information, row names, and a 'Send genes to Enrichr' link that allows users to export their gene list (e.g. cluster of row-genes) to Enrichr.

.. _enrichrgram:

**Enrichrgram**

Users can also import biological information about their genes directly into the visualization (see screenshot below). Simply click the Enrichr-logo to the top-left of the heatmap to bring up a list of libraries from Enrichr, then click on a library to obtain enriched terms for your genes of interest. For instance, clicking on 'ChEA 2016' will enrich for up-stream transcription factors. The enriched terms are shown as row categories, which enables users to see which genes are associated with each term. The row-category-titles give the enriched term name and the red-bars represent the significance of the enrichment (see `Enrichr combined score`_). Users can run enrichment analysis on specific clusters of genes by filtering the matrix to only show their genes of interest: e.g. use the dendrogram crop buttons or brush-crop to select a subset of genes for analysis.


.. figure:: _static/enrichrgram_results.png
  :width: 900px
  :align: center
  :alt: Enrichrgram Menu

  Users can perform enrichment analysis to find biological information specific to their genes (e.g. a cluster of genes). Users can select from several enrichment libraries and the top 10 enriched terms will be shown as rows categories. The combined-scores for the enriched terms will be shown as red bars behind the row category titles.

`Enrichrgram.js`_ provides this functionality and works with the :ref:`clustergrammer_js` API to depict enriched terms and their associated genes as row categories. The update-row-category functionality can be extended by developers for other domain specific problems.

.. _`Enrichrgram.js`: https://github.com/MaayanLab/clustergrammer/blob/master/js/Enrichrgram.js
.. _`hzome_functions.js`: https://github.com/MaayanLab/clustergrammer/blob/master/js/hzome_functions.js
.. _`load_clustergram.js`: https://github.com/MaayanLab/clustergrammer/blob/master/js/load_clustergram.js
.. _`CCLE Explorer`: http://amp.pharm.mssm.edu/clustergrammer/CCLE/
.. _`Harmonizome`: http://amp.pharm.mssm.edu/Harmonizome/
.. _`Enrichr`: http://amp.pharm.mssm.edu/Enrichr/
.. _`Enrichr's RESTful API`: http://amp.pharm.mssm.edu/Enrichr/help#api
.. _`Harmonizome's RESTful API`: http://amp.pharm.mssm.edu/Harmonizome/documentation

.. _`Enrichr combined score`: http://amp.pharm.mssm.edu/Enrichr/help#basics