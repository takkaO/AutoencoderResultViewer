import eel
import numpy as np
import tensorflow as tf
import base64
import io
from PIL import Image

decoder = tf.keras.models.load_model("decoder.h5")

default = np.array([
    [0,  11.234877,   1.8221463, 12.184746,   5.210108,   5.7688284,
     7.117953,   4.66948, 6.3518763, 2.8289835, 10.993784,  5.3251004,
     4.4222527,  2.8173194, 6.0845437, 7.998674, 5.941929,  3.2750404,
     4.5753427,  2.7305543, 3.2396033, 1.7854958, 5.951744,  3.8232558,
     3.9120317,  8.740001, 15.583646, 5.3138685, 4.793798,  4.6253824,
     5.177718,   4.845586]])

@eel.expose
def decodeImage(values):
	encoded_img = np.array([values])
	#print(encoded_img)
	decoded_img = decoder.predict(encoded_img)
	
	decoded_img = Image.fromarray((decoded_img[0].reshape(28, 28)*255).astype(np.uint8))
	bin_img = io.BytesIO()

	if decoded_img.mode != 'RGB':
		decoded_img = decoded_img.convert('RGB')
	decoded_img.save(bin_img, format="JPEG")
	send_img = bin_img.getvalue()
	
	send_img = base64.b64encode(send_img).decode("utf-8")
	return send_img 
	#print(decoded_img[0].reshape(28, 28))
	#cv2.imshow("img", decoded_img[0].reshape(28, 28))
	#cv2.waitKey(0)

@eel.expose
def resetImage():
	eel.setParameters(default[0].tolist())
	eel.setImage(decodeImage(default[0]))

def main():

	eel.init("web")
	try:
		eel.setParameters(default[0].tolist())
		eel.setImage(decodeImage(default[0]))
		eel.start('index.html')
	except (SystemExit, MemoryError, KeyboardInterrupt):
    	# We can do something here if needed
    	# But if we don't catch these safely, the script will crash
		print("close window")
		pass 

if __name__ == "__main__":
	main()
