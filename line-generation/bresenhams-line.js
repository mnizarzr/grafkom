function bresenhamLine(x1, y1, x2, y2) {

    let m = (y2 - y1) / (x2 - x1);
    let dx = Math.abs(x2 - x1);
    let dy = Math.abs(y2 - y1);
    let x = x1, y = y1;
    let i = 1;
    console.log(`X = ${x} || Y = ${y}`);

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
            console.log(`X = ${x} || Y = ${y}`);
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
            console.log(`X = ${x} || Y = ${y}`);
            i++
        }
    }

}


bresenhamLine(1, 1, 30, 20);
