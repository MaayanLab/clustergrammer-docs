.. _clustergrammer_web:

Clustergrammer Web Application
------------------------------
The Clustergrammer web application (referred to as Clustergrammer-Web) enables users to easily generate interactive and shareable heatmap visualizations.

Uploading Data through the Homepage
====================================

Web Application API
===================
Clustergrammer-Web's RESful API enables users to programatically generate visualizations. The API can be useful for users that need to generate many clustergrams or developers that need to automatically generate visualizations for their own web application.

*Matrix Upload*
Users can post a matrix file to Clustergrammer-Web using the endpoint
::

  http://amp.pharm.mssm.edu/clustergrammer/matrix_upload/

and recieve a permanent link to their visualization. Below is an example in Python 2.7 showing the post request and how to obtain the link from the response object:
::

  import requests

  filename = 'example_matrix.txt'
  upload_url = 'http://amp.pharm.mssm.edu/clustergrammer/matrix_upload/'

  r = requests.post(upload_url, files={'file': open(filename, 'rb')})

  link = r.text

.. _clustergrammer_web_dev:

Clustergrammer-Web Development
==============================
Clustergrammer-Web is a `dockerized`_ web application built using the Python library `Flask`_. Clustergrammer-Web uses the :ref:`clustergrammer_js` and :ref:`clustergrammer_py` libraries and the source code can be found in the `clustergrammer-web`_ GitHub repo.


.. _`Flask`: http://flask.pocoo.org/
.. _`dockerized`: https://docs.docker.com/
.. _`clustergrammer-web`: https://github.com/MaayanLab/clustergrammer-web/