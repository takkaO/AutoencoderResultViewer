import tensorflow as tf
import numpy as np
import matplotlib.pyplot as plt
import cv2

def getMnist():
	(x_train, l), (x_test, _) = tf.keras.datasets.mnist.load_data()
	print(l.shape)
	
	x_train = x_train.astype('float32') / 255
	x_test = x_test.astype('float32') / 255
	x_train = x_train.reshape(60000, 784)
	x_test = x_test.reshape(10000, 784)
	
	return x_train, x_test
	

def main():
	encoding_dim = 32
	train_img, test_img = getMnist()
	
	decoder = tf.keras.models.load_model("decoder.h5")
	encoded_img = np.load("encoded.npy")
	
	print(encoded_img.shape)

	encoded_img = np.array([[0,       11.234877,   1.8221463, 12.184746,   5.210108,   5.7688284,
                         7.117953,   4.66948   , 6.3518763  ,2.8289835, 10.993784 ,  5.3251004,
                         4.4222527,  2.8173194  ,6.0845437  ,7.998674  , 5.941929 ,  3.2750404,
                         4.5753427,  2.7305543  ,3.2396033  ,1.7854958  ,5.951744 ,  3.8232558,
                         3.9120317,  8.740001  ,15.583646   ,5.3138685  ,4.793798 ,  4.6253824,
                         5.177718,   4.845586]])

	print(encoded_img.shape)
	decoded_img = decoder.predict(encoded_img)
	print(decoded_img[0].reshape(28, 28).shape)
	cv2.imshow("img", decoded_img[0].reshape(28, 28))
	cv2.waitKey(0)

	"""
	n = 10
	plt.figure(figsize=(20, 4))
	for i in range(n):
		ax = plt.subplot(2, n, i+1)
		plt.imshow(test_img[i].reshape(28, 28))
		plt.gray()
		ax.get_xaxis().set_visible(False)
		ax.get_yaxis().set_visible(False)

		ax = plt.subplot(2, n, i+1+n)
		plt.imshow(decoded_img[i].reshape(28, 28))
		plt.gray()
		ax.get_xaxis().set_visible(False)
		ax.get_yaxis().set_visible(False)
	plt.show()
	"""
	
if __name__ == "__main__":
	main()
