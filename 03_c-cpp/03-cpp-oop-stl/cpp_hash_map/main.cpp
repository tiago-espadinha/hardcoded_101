#include <iostream>
#include <string>
#include "HashMap.hpp"

int main() {
    HashMap<std::string, int> ageMap;
    ageMap.insert("Alice", 25);
    ageMap.insert("Bob", 30);
    ageMap["Charlie"] = 35;

    std::cout << "Alice's age: " << ageMap.get("Alice").value_or(-1) << std::endl;
    std::cout << "Charlie's age: " << ageMap["Charlie"] << std::endl;
    std::cout << "Map size: " << ageMap.size() << std::endl;

    return 0;
}
