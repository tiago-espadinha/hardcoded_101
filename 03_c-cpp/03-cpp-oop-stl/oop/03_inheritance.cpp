#include <iostream>
#include <vector>
#include <memory>
#include <string>
#include <cmath>

class Shape {
public:
    // Virtual destructor is crucial for correct cleanup of derived objects through base pointers
    virtual ~Shape() {
        std::cout << "[LOG] Shape Destructor" << std::endl;
    }

    virtual double area() const = 0;       // Pure virtual
    virtual double perimeter() const = 0;  // Pure virtual
    virtual std::string toString() const = 0;
};

class Circle : public Shape {
private:
    double radius;
public:
    Circle(double r) : radius(r) {}
    ~Circle() override { std::cout << "[LOG] Circle Destructor" << std::endl; }

    double area() const override { return M_PI * radius * radius; }
    double perimeter() const override { return 2 * M_PI * radius; }
    std::string toString() const override { return "Circle (radius: " + std::to_string(radius) + ")"; }
};

class Rectangle : public Shape {
private:
    double width, height;
public:
    Rectangle(double w, double h) : width(w), height(h) {}
    ~Rectangle() override { std::cout << "[LOG] Rectangle Destructor" << std::endl; }

    double area() const override { return width * height; }
    double perimeter() const override { return 2 * (width + height); }
    std::string toString() const override { return "Rectangle (" + std::to_string(width) + "x" + std::to_string(height) + ")"; }
};

int main() {
    std::vector<std::unique_ptr<Shape>> shapes;

    shapes.push_back(std::make_unique<Circle>(5.0));
    shapes.push_back(std::make_unique<Rectangle>(4.0, 6.0));

    std::cout << "--- Polymorphism in Action ---" << std::endl;
    for (const auto& shape : shapes) {
        std::cout << shape->toString() << ":" << std::endl;
        std::cout << "  Area: " << shape->area() << std::endl;
        std::cout << "  Perimeter: " << shape->perimeter() << std::endl;
    }

    std::cout << "\n--- Destruction Phase ---" << std::endl;
    // unique_ptrs go out of scope, calling virtual destructors correctly
    return 0;
}
