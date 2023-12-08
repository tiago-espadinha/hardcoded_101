#include <catch2/catch_test_macros.hpp>
#include "DoublyLinkedList.hpp"

TEST_CASE("DoublyLinkedList basic operations", "[linked_list]") {
    DoublyLinkedList<int> list = {10, 20, 30};

    SECTION("Size and Initializer List") {
        REQUIRE(list.size() == 3);
    }

    SECTION("Iteration") {
        int expected[] = {10, 20, 30};
        int i = 0;
        for (int x : list) {
            REQUIRE(x == expected[i++]);
        }
    }
}
