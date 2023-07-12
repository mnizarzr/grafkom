function createPixel(x, y, color) {
  const pixel = document.createElement("div");
  pixel.className = "pixel";
  pixel.style.top = y + 'px';
  pixel.style.left = x + "px";
  if (color !== undefined) {
    pixel.style.backgroundColor = color;
  }
  // pixel.style.bottom = y - 1 + "px";
  console.log(pixel);
  return pixel;
}

const isWithinRange = (range, n) => n >= range.min && n <= range.max;

class Canvas {
  constructor(graph) {
    this.graph = graph;
  }

  get pixelSize() {
    return getComputedStyle(document.documentElement).getPropertyValue(
      "--pixel-size"
    );
  }

  set pixelSize(size) {
    document.documentElement.style.setProperty("--pixel-size", size + "px");
  }

  get center() {
    const pixelSize = this.pixelSize.replace("px", "");
    const wh = this.graphSize / pixelSize;
    return wh / 2;
  }

  get graphSize() {
    return this.graph.clientHeight;
  }

  drawPixel(x, y, color) {
    const pixelSize = this.pixelSize.replace("px", "");

    const range = { min: 1, max: this.graphSize / pixelSize };
    if (!(isWithinRange(range, x) && isWithinRange(range, y))) return;

    const _x = (x - 1) * pixelSize + 1;
    const _y = (y - 1) * pixelSize + 1;
    if (color !== undefined) {
      return this.graph.appendChild(createPixel(_x, _y, color));
    }
    return this.graph.appendChild(createPixel(_x, _y));
  }

  clear() {
    document.querySelectorAll(".pixel").forEach((ele) => ele.remove());
  }
}

export default Canvas;
