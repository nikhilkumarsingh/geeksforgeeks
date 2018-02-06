# importing tensorflow
import tensorflow as tf
 
# creating nodes in computation graph
node1 = tf.constant(3, dtype=tf.int32)
node2 = tf.constant(5, dtype=tf.int32)
node3 = tf.add(node1, node2)
 
# create tensorflow session object
sess = tf.Session()
 
# evaluating node3 and printing the result
print("Sum of node1 and node2 is:",sess.run(node3))
 
# closing the session
sess.close()
