function bresenhamCircle(xc, yc, r) {
    var x = 0, y = r;
    var d = 3 - 2 * r;
    var coordinates = [];

    while (y >= x) {
        addCoordinates(coordinates, { xc, yc, x, y });

        x++;

        if (d > 0) {
            y--;
            d = d + 4 * (x - y) + 10;
        } else {
            d = d + 4 * x + 6;
        }

        addCoordinates(coordinates, { xc, yc, x, y });
    }

    return coordinates;
}

function addCoordinates(coordinates, { xc, yc, x, y }) {
    coordinates.push({ x: xc + x, y: yc + y, color: '#EC407A' });
    coordinates.push({ x: xc - x, y: yc + y, color: '#2196F3' });
    coordinates.push({ x: xc + x, y: yc - y, color: '#9C27B0' });
    coordinates.push({ x: xc - x, y: yc - y, color: '#FF9800' });
    coordinates.push({ x: xc + y, y: yc + x, color: '#00BCD4' });
    coordinates.push({ x: xc - y, y: yc + x, color: '#009688' });
    coordinates.push({ x: xc + y, y: yc - x, color: '#FF5722' });
    coordinates.push({ x: xc - y, y: yc - x, color: '#FFC107' });
}

export default bresenhamCircle;
