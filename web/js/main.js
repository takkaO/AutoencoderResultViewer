"use strict"

var arrSlider = new Array();
var arrSliderValues = new Array();
for(var i=0; i<slider_num; i++){
	arrSlider.push(new Slider("#s" + String(i)));
	arrSliderValues.push(0);
	const sv = "sv" + String(i);

	arrSlider[i].on("slide", function (sliderValue) {
		document.getElementById(sv).textContent = sliderValue;
		//console.log(sliderValue);

		if (arrSliderValues[j] != sliderValue) {
			arrSliderValues[j] = sliderValue;
			//console.log(arrSliderValues);

			decodeImageJS();
		}
	});

	const j = i;
	arrSlider[i].on("slideStop", function (sliderValue) {
		document.getElementById(sv).textContent = sliderValue;
		if (arrSliderValues[j] != sliderValue) {
			arrSliderValues[j] = sliderValue;
			//console.log(arrSliderValues);

			decodeImageJS();
		}
	});
}

async function decodeImageJS() {
	let val = "data:image/jpeg;base64,"
	val += await eel.decodeImage(arrSliderValues)();
	//console.log(val);
	document.getElementById("canvas").src = val;
}

eel.expose(setImage);
function setImage (img64){
	let val = "data:image/jpeg;base64," + img64;
	document.getElementById("canvas").src = val;
}

eel.expose(setParameters);
function setParameters(values){
	//console.log(values);
	for(var i=0; i<values.length; i++){
		arrSlider[i].setValue(values[i]);
		document.getElementById("sv" + String(i)).textContent = arrSlider[i].getValue();
		arrSliderValues[i] = arrSlider[i].getValue();
	}
}

document.getElementById("reset-btn").addEventListener("click", function(){
	eel.resetImage();
});

window.addEventListener("load", function () {
	console.log("load event ok");
})