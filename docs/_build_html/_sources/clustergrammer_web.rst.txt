.. _clustergrammer_web:

Clustergrammer-Web
----------------------
|github-version|

The `Web App`_ (`http://amp.pharm.mssm.edu/clustergrammer`_) enables users to easily generate interactive and shareable heatmap visualizations by uploading their data as a tab-separated file.

.. _clustergrammer_web_upload:

Uploading Data using the Web App Homepage
=========================================

Users can easily generate an interactive and shareable heatmap visualization using the :ref:`clustergrammer_web` (see upload section screenshot below). Simply upload a tab-separated matrix file (see :ref:`matrix_format_io` for more information) at the `homepage`_ to be redirected to a permanent and shareable visualization of your data.


.. figure:: _static/clustergrammer_web_upload.png
  :width: 900px
  :align: left
  :alt: Clustergrammer Web
  :target: http://amp.pharm.mssm.edu/clustergrammer/

  Users can upload their data using the web app `homepage`_. Simply choose your file and upload to be redirected to your permanent and shareable visualization.


.. _clustergrammer_web_viz:

Clustergrammer-Web Visualization
================================
Uploading a matrix to the `Web App`_ will redirect the user to a new permanent and shareable page with three views of their data:

- Heatmap view of their matrix
- Similarity matrix of the columns in their original matrix
- Similarity matrix of the rows in their original matrix

See the screenshots below and the `example visualization`_ for an example `Web App`_ visualization page.

**Heatmap View**

.. figure:: _static/web_app_heatmap.png
  :width: 800px
  :align: left
  :alt: Web application heatmap
  :target: http://amp.pharm.mssm.edu/clustergrammer/viz_sim_mats/58a492b4a63cb826f0be6476/rc_two_cats.txt

  Above is an example clustergram visualization produced by the `Web App`_. Clustergrammer produces three views of your data and the clustered heatmap view is shown above.

**Similarity Matrix View**

.. figure:: _static/web_app_sim_mat.png
  :width: 800px
  :align: left
  :alt: Web application sim-mat
  :target: http://amp.pharm.mssm.edu/clustergrammer/viz_sim_mats/58a492b4a63cb826f0be6476/rc_two_cats.txt

  The `Web App`_ produces similarity matrices of rows and columns to provide additional perspectives on a user's data. Above is an example column similarity matrix.

Users can view the heatmap/similarity-matrices in full screen by clicking the blue link under the visualizations. All visualizations are permanent and shareable, which enables sharing with collaborators. See :ref:`interacting_with_viz` for more information.

.. _clustergrammer_web_api:

Clustergrammer-Web API
======================
Clustergrammer-Web's RESTful API enables users to programmatically generate visualizations. The API can be convenient for users that need to generate many clustergrams or developers who need to automatically generate visualizations for their own Web application.

*Matrix Upload*

Users can post a matrix file to Clustergrammer-Web using the endpoint
::

  http://amp.pharm.mssm.edu/clustergrammer/matrix_upload/

and receive a permanent link to their visualization. Below is an example in Python 2.7 showing the post request and how to obtain the link from the response object:
::

  import requests

  filename = 'example_matrix.txt'
  upload_url = 'http://amp.pharm.mssm.edu/clustergrammer/matrix_upload/'

  r = requests.post(upload_url, files={'file': open(filename, 'rb')})

  link = r.text

.. _clustergrammer_web_dev:

Clustergrammer-Web Development
==============================
Clustergrammer-Web is a `dockerized`_ Web application built using the Python library `Flask`_ and `MongoDB`_ database. Clustergrammer-Web uses the :ref:`clustergrammer_js` and :ref:`clustergrammer_py` libraries and the source code can be found in the `clustergrammer-web`_ GitHub repo.


.. _`Web App`: http://amp.pharm.mssm.edu/clustergrammer/
.. _`Flask`: http://flask.pocoo.org/
.. _`dockerized`: https://docs.docker.com/
.. _`clustergrammer-web`: https://github.com/MaayanLab/clustergrammer-web/
.. _`MongoDB`: https://www.mongodb.com/
.. _`example visualization`: http://amp.pharm.mssm.edu/clustergrammer/viz_sim_mats/58a492b4a63cb826f0be6476/rc_two_cats.txt
.. _`http://amp.pharm.mssm.edu/clustergrammer`: http://amp.pharm.mssm.edu/clustergrammer/
.. _`homepage`: http://amp.pharm.mssm.edu/clustergrammer/

.. |github-version| image:: https://img.shields.io/github/release/MaayanLab/clustergrammer-web.svg
    :alt: version
    :scale: 100%
    :target: https://github.com/MaayanLab/clustergrammer-web