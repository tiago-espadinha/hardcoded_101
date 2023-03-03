/**
 * Command pattern implementation for a Canvas Drawing App
 * ES2022 Node.js environment
 */

// Command Interface
class Command {
  execute() { throw new Error("Method execute() must be implemented."); }
  undo() { throw new Error("Method undo() must be implemented."); }
}

// Receiver
class Canvas {
  #shapes = [];

  addShape(shape) {
    this.#shapes.push(shape);
    console.log(`Canvas: Added ${shape.type} at (${shape.x}, ${shape.y})`);
  }

  removeLastShape() {
    const shape = this.#shapes.pop();
    if (shape) {
      console.log(`Canvas: Removed ${shape.type} from (${shape.x}, ${shape.y})`);
    }
    return shape;
  }

  draw() {
    console.log("--- Current Canvas State ---");
    this.#shapes.forEach(s => console.log(`- ${s.type} at (${s.x}, ${s.y})`));
    console.log("----------------------------");
  }
}

// Concrete Command
class DrawCircleCommand extends Command {
  #canvas;
  #circle;

  constructor(canvas, x, y, radius) {
    super();
    this.#canvas = canvas;
    this.#circle = { type: "Circle", x, y, radius };
  }

  execute() {
    this.#canvas.addShape(this.#circle);
  }

  undo() {
    this.#canvas.removeLastShape();
  }
}

class DrawSquareCommand extends Command {
  #canvas;
  #square;

  constructor(canvas, x, y, side) {
    super();
    this.#canvas = canvas;
    this.#square = { type: "Square", x, y, side };
  }

  execute() {
    this.#canvas.addShape(this.#square);
  }

  undo() {
    this.#canvas.removeLastShape();
  }
}

// Invoker
class CanvasManager {
  #history = [];
  #canvas;

  constructor(canvas) {
    this.#canvas = canvas;
  }

  execute(command) {
    command.execute();
    this.#history.push(command);
  }

  undo() {
    const command = this.#history.pop();
    if (command) {
      command.undo();
    }
  }

  showCanvas() {
    this.#canvas.draw();
  }
}

// Client Code
const myCanvas = new Canvas();
const manager = new CanvasManager(myCanvas);

manager.execute(new DrawCircleCommand(myCanvas, 10, 10, 5));
manager.execute(new DrawSquareCommand(myCanvas, 20, 20, 10));
manager.showCanvas();

console.log("Undoing last draw...");
manager.undo();
manager.showCanvas();
