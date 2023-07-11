function bresenhamLine(coords1, coords2) {

    let x1 = coords1.x;
    let y1 = coords1.y;
    let x2 = coords2.x;
    let y2 = coords2.y;

    let m = (y2 - y1) / (x2 - x1);
    let dx = Math.abs(x2 - x1);
    let dy = Math.abs(y2 - y1);
    let x = x1, y = y1;
    let i = 1;

    let coordinates = []

    coordinates.push({ x, y })

    if (Math.abs(m) < 1) {
        let p = (2 * dy) - dx;
        while (i <= dx) {
            if (p < 0) {
                x = x + 1;
                p = p + (2 * dy);
            }
            else {
                x = x + 1;
                y = y + 1;
                p = p + (2 * dy) - (2 * dx);
            }
            coordinates.push({ x, y })
            i++
        }
    } else {
        let p = (2 * dx) - dy;
        while (i <= dy) {
            if (p < 0) {
                y = y + 1;
                p = p + (2 * dx);
            } else {
                x = x + 1;
                y = y + 1;
                p = p + (2 * dx) - (2 * dy);
            }
            coordinates.push({ x, y })
            i++
        }
    }

    return coordinates;

}

export default bresenhamLine;
