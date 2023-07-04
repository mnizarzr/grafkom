function bresenhamCircle(xc, yc, r) {
    let x = 0, y = r;
    let d = 3 - 2 * r;
    while (y >= x) {
        drawCircle(xc, yc, x, y);
        x++;
        if (d > 0) {
            y--;
            d = d + 4 * (x - y) + 10;
        } else {
            d = d + 4 * x + 6;
        }
        drawCircle(xc, yc, x, y);
    }
}

function drawCircle(xc, yc, x, y) {
    console.log(`xc + x = ${xc + x} || yc + y = ${yc + y}`);
    console.log(`yc + x = ${yc + x} || xc + y = ${xc + y}`);
    console.log(`-yc + x = ${-yc + x} || xc + y = ${xc + y}`);
    console.log(`-xc + x = ${-xc + x} || yc + y = ${yc + y}`);
    console.log(`-xc + x = ${-xc + x} || -yc + y = ${-yc + y}`);
    console.log(`-yc + x = ${-yc + x} || -xc + y = ${-xc + y}`);
    console.log(`yc + x = ${yc + x} || -xc + y = ${-xc + y}`);
    console.log(`xc + x = ${xc + x} || -yc - y = ${-yc - y}`);
    console.log();
}

bresenhamCircle(0, 0, 10);

