#include <iostream>
#include "DoublyLinkedList.hpp"

int main() {
    DoublyLinkedList<int> list = {10, 20, 30, 40, 50};

    std::cout << "List elements (using iterators): ";
    for (int x : list) {
        std::cout << x << " ";
    }
    std::cout << "\nList size: " << list.size() << std::endl;

    return 0;
}
