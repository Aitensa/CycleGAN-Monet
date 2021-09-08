import argparse
import tensorflow as tf
from tensorflow.core.framework import graph_pb2
tf.compat.v1.disable_eager_execution()

if __name__ == '__main__':
   input_pb = "east_int8.pb"
   output_pbtxt = "eastok.pbtxt"
   with tf.compat.v1.Session()  as sess:
     with tf.compat.v1.gfile.FastGFile(input_pb, 'rb') as f:
       graph_def = graph_pb2.GraphDef()
       graph_def.ParseFromString(f.read())
       #tf.import_graph_def(graph_def)
     tf.train.write_graph(graph_def, './', output_pbtxt, as_text=True)
