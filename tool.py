#-*- coding : utf-8-*-
# coding: utf-8
import tensorflow as tf
from tensorflow.core.framework import graph_pb2
from google.protobuf import text_format



if __name__ == '__main__':
   input_pbtxt = "east_int8.pbtxt"
   output_pb = "east_int8_sbc.pb"
   with tf.compat.v1.Session() as sess:
     with tf.compat.v1.gfile.FastGFile(input_pbtxt, 'rb') as f:
       graph_def = graph_pb2.GraphDef()
       new_graph_def=text_format.Merge(f.read(), graph_def)
     tf.train.write_graph(new_graph_def, './', output_pb, as_text=False)

