# AutoEncoder Result Viewer

Simple autoencoder result viewer.  

![sampleImage](https://github.com/takkaO/AutoencoderResultViewer/blob/images/sample.png?raw=true)

## Features
- Realtime rendering image
- Flexible change of the number of sliders
- Flexible change of the decoder model

## Requirement
```
python3 -m pip install eel
python3 -m pip install tensorflow
python3 -m pip install numpy
python3 -m pip install pillow
```

## How to use
1. **Edit ``` gui.py ```**
	- Change ``` decoder ``` model to yourself.
	- Edit ``` default ``` numpy array to yourself encoded values.   
	Please include the batch.
	- Edit ``` decodeImage ``` function.

2. **Edit ``` web/index.html ```**
	- Change ``` slider-num ``` to the slider-num you want to set.
	- Change ``` slider-min ``` to the minimum value you want to set.
	- Change ``` slider-max ``` to the maximum value you want to set.
	- Change ``` slider-step ``` to the step value you want to set.
3. **Run ``` python3 gui.py ```**

