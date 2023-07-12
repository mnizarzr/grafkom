import Canvas from './canvas.js';
import bresenhamLine from './bresenhams-line.js';
import bresenhamCircle from './bresenhams-circle.js';

function sleep(ms) {
    return new Promise(resolve => setTimeout(resolve, ms));
}

// New Canvas Object
const canvas = new Canvas(document.querySelector('#graph'));

// Clear Button
const clearBtn = document.querySelector('#clear');
clearBtn.addEventListener('click', canvas.clear);

// Pixel Size Change Handler
const pixelSize = document.querySelector('#pixel-size');
pixelSize.addEventListener('change', (e) => {
    canvas.clear();
    canvas.pixelSize = e.target.value;
    const maxVal = Math.round(canvas.graphSize / e.target.value);
    document.querySelector('#range-max').textContent = maxVal;

    document.getElementById("xc").value = Math.floor(canvas.center);
    document.getElementById("yc").value = Math.floor(canvas.center);
});

const blgController = document.getElementById("blg-controller");
const bcgController = document.getElementById("bcg-controller");

const selectAlgo = document.getElementById("algo");
selectAlgo.addEventListener("change", (e) => {
    let selectedOption = e.target.value;

    if (selectedOption == 'blg-algo') {
        bcgController.style.display = "none";
        blgController.style.display = "flex";
    } else if (selectedOption == 'bcg-algo') {
        blgController.style.display = "none";
        bcgController.style.display = "flex";
    }
})

// Form Submit Handler [Drawing tool]
const form = document.querySelector('#drawing-tool');
form.addEventListener('submit', (e) => {

    e.preventDefault();

    const coord1 = {
        x: Number(e.target['x1'].value),
        y: Number(e.target['y1'].value),
    };

    const coord2 = {
        x: Number(e.target['x2'].value),
        y: Number(e.target['y2'].value),
    };

    const circle = {
        xc: Number(e.target['xc'].value),
        yc: Number(e.target['yc'].value),
        r: Number(e.target['r'].value)
    }

    const algo = document.querySelector('#algo').value;

    if (algo == 'blg-algo') {
        const coords = bresenhamLine(coord1, coord2);
        coords.forEach((coord) => canvas.drawPixel(coord.x, coord.y));
    } else {
        const coords = bresenhamCircle(circle.xc, circle.yc, circle.r);
        coords.forEach((coord, index) => {
            setTimeout(() => {
                canvas.drawPixel(coord.x, coord.y, coord.color);
            }, (index + 1) * 1);
        })
    }

});
