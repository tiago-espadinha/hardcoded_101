#include <iostream>
#include <vector>
#include <string>

// 1. Stack<T> using std::vector internally
template <typename T>
class Stack {
private:
    std::vector<T> elements;
public:
    void push(T const& elem) { elements.push_back(elem); }
    void pop() {
        if (elements.empty()) throw std::out_of_range("Stack<>::pop(): empty stack");
        elements.pop_back();
    }
    T top() const {
        if (elements.empty()) throw std::out_of_range("Stack<>::top(): empty stack");
        return elements.back();
    }
    bool empty() const { return elements.empty(); }
};

// 2. Node<T> for linked lists
template <typename T>
struct Node {
    T value;
    Node* next;
    Node(T v) : value(std::move(v)), next(nullptr) {}
};

// 3. Variadic template: print_all
void print_all() { std::cout << std::endl; } // Base case

template <typename T, typename... Args>
void print_all(T first, Args... args) {
    std::cout << first << " ";
    print_all(args...);
}

int main() {
    std::cout << "--- Testing Stack<int> ---" << std::endl;
    Stack<int> s;
    s.push(10);
    s.push(20);
    std::cout << "Top: " << s.top() << std::endl;

    std::cout << "\n--- Testing Node<string> ---" << std::endl;
    Node<std::string> n("Hello");
    std::cout << "Node value: " << n.value << std::endl;

    std::cout << "\n--- Testing print_all (Variadic Template) ---" << std::endl;
    print_all(1, 2.5, "Hello", 'A', std::string("C++17"));

    return 0;
}
