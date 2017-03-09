import io, sys
import StringIO
import json
import pandas as pd
from . import categories
from . import proc_df_labels
from . import data_formats

def load_file(net, filename):
  # reset network when loaing file, prevents errors when loading new file
  net.__init__()

  f = open(filename, 'r')

  file_string = f.read()

  if (sys.version_info > (3, 0)):
    # python 3
    ####################
    file_string = str(file_string)
  else:
    # python 2
    ####################
    file_string = unicode(file_string)

  buff = io.StringIO(file_string)
  f.close()

  if '/' in filename:
    filename = filename.split('/')[-1]

  net.load_tsv_to_net(buff, filename)

def load_stdin(net):
  data = ''

  for line in sys.stdin:
    data = data + line

  data = StringIO.StringIO(data)

  net.load_tsv_to_net(data)

def load_tsv_to_net(net, file_buffer, filename=None):
  lines = file_buffer.getvalue().split('\n')
  num_labels = categories.check_categories(lines)

  row_arr = list(range(num_labels['row']))
  col_arr = list(range(num_labels['col']))
  tmp_df = {}

  # use header if there are col categories
  if len(col_arr) > 1:
    tmp_df['mat'] = pd.read_table(file_buffer, index_col=row_arr,
                                  header=col_arr)
  else:
    tmp_df['mat'] = pd.read_table(file_buffer, index_col=row_arr)

  tmp_df = proc_df_labels.main(tmp_df)

  net.df_to_dat(tmp_df)
  net.dat['filename'] = filename

def load_json_to_dict(filename):
  f = open(filename, 'r')
  inst_dict = json.load(f)
  f.close()
  return inst_dict

def load_gmt(filename):
  f = open(filename, 'r')
  lines = f.readlines()
  f.close()
  gmt = {}
  for i in range(len(lines)):
    inst_line = lines[i].rstrip()
    inst_term = inst_line.split('\t')[0]
    inst_elems = inst_line.split('\t')[2:]
    gmt[inst_term] = inst_elems

  return gmt

def load_data_to_net(net, inst_net):
  ''' load data into nodes and mat, also convert mat to numpy array'''
  net.dat['nodes'] = inst_net['nodes']
  net.dat['mat'] = inst_net['mat']
  data_formats.mat_to_numpy_arr(net)