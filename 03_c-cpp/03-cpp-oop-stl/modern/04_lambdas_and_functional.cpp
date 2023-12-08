#include <iostream>
#include <functional>
#include <vector>
#include <string>

// Functional composition: compose(f, g) -> f(g(x))
template <typename F, typename G>
auto compose(F f, G g) {
    return [f, g](auto x) { return f(g(x)); };
}

int main() {
    std::cout << "--- Lambda Captures ---" << std::endl;
    int x = 10;
    auto val_capture = [x]() { return x; };
    auto ref_capture = [&x]() { return ++x; };
    
    std::cout << "Value capture: " << val_capture() << std::endl;
    std::cout << "Reference capture (modifies original): " << ref_capture() << std::endl;
    std::cout << "Original x: " << x << std::endl;

    std::cout << "\n--- Functional Composition ---" << std::endl;
    auto add1 = [](int n) { return n + 1; };
    auto square = [](int n) { return n * n; };

    auto add1ThenSquare = compose(square, add1); // (x+1)^2
    std::cout << "compose(square, add1)(5) = (5+1)^2 = " << add1ThenSquare(5) << std::endl;

    std::cout << "\n--- std::function Wrapper ---" << std::endl;
    std::vector<std::function<void()>> actions;
    actions.push_back([]() { std::cout << "Action 1: Hello!" << std::endl; });
    actions.push_back([]() { std::cout << "Action 2: Functional C++!" << std::endl; });

    for (const auto& action : actions) action();

    return 0;
}
