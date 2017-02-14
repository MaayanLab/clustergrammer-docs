Web Application
---------------
The Clustergrammer web application (referred to as Clustergrammer-web) enables users to easily generate interactive and shareable heatmap visualizations.

Uploading Data through Homepage
===============================

Web Application API
===================
Clustergrammer-web's RESful API enables users to programatically generate visualizations. The API can be useful for users that need to generate many clustergrams or developers that need to automatically generate visualizations for their own web application.

*Matrix Upload*
Users can post a matrix file to Clustergrammer-web using the endpoint
::

  http://amp.pharm.mssm.edu/clustergrammer/matrix_upload/

and recieve a permanent link to their visualization. Below is an example in Python 2.7 showing the post request and how to obtain the link from the response object:
::

  import requests

  filename = 'example_matrix.txt'
  upload_url = 'http://amp.pharm.mssm.edu/clustergrammer/matrix_upload/'

  r = requests.post(upload_url, files={'file': open(filename, 'rb')})

  link = r.text