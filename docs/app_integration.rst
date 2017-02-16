.. _app_integration:

App Integration Examples
------------------------
Clustergrammer can be integrated into other web applications and is being utilized to visualize data for the following `Ma'ayan lab`_ web applications:

Enrichr
=======
The enrichment analysis tool, `Enrichr`_, uses the :ref:`clustergrammer_web`'s API to produce dynamic heatmaps of enriched terms as columns and user lists as rows. This helps users understand the relationships between their input genes and the returned enriched terms.

GEN3VA
======
The gene signature analysis and visualization tool, `GEN3VA`_, uses Clustergrammer's core libraries, :ref:`clustergrammer_js` and :ref:`clustergrammer_py`, to dynamically visualize collections of gene expression signatures collected by users from `GEO`_ as interactive heatmaps. GEN3VA also uses Clustergrammer to visualize enrichment analysis results (obtained from `Enrichr`_) and perturbations that reverse or mimic gene expression signatures (obtained from `L1000CDS2`_)

L1000CDS2
=========
`L1000CDS2`_ uses the :ref:`clustergrammer_web`'s API to produce interactive heatmaps of perturbagen gene signatures that mimic or reverse an input gene signature. This can be useful for users that are interested in the specific genes that are differentially regulated by the identified perturbagens.

Harmonizome
===========
The `Harmonizome`_ uses :ref:`clustergrammer_web`'s API to generate visualize of curated biological datasets as heatmaps and adjacency matrices (to depict networks). The Harmonizome also uses the Clustergrammer to visualize the amount of biological information that is available for different families of genes in the `Harmonogram`_

.. _`Enrichr`: http://amp.pharm.mssm.edu/Enrichr/
.. _`GEN3VA`: http://amp.pharm.mssm.edu/gen3va/
.. _`L1000CDS2`: http://amp.pharm.mssm.edu/l1000cds2/
.. _`GEO2Enrichr`: http://amp.pharm.mssm.edu/g2e/
.. _`Harmonizome`: http://amp.pharm.mssm.edu/Harmonizome/
.. _`GEO`: https://www.ncbi.nlm.nih.gov/geo/
.. _`L1000CDS2': http://amp.pharm.mssm.edu/l1000cds2/#/index
.. _`Harmonogram`: http://amp.pharm.mssm.edu/harmonogram/
.. _`Ma'ayan lab`: http://labs.icahn.mssm.edu/maayanlab/