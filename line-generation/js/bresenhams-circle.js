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
    coordinates.push({ x: xc + x, y: yc + y });
    coordinates.push({ x: xc - x, y: yc + y });
    coordinates.push({ x: xc + x, y: yc - y });
    coordinates.push({ x: xc - x, y: yc - y });
    coordinates.push({ x: xc + y, y: yc + x });
    coordinates.push({ x: xc - y, y: yc + x });
    coordinates.push({ x: xc + y, y: yc - x });
    coordinates.push({ x: xc - y, y: yc - x });
}

export default bresenhamCircle;
