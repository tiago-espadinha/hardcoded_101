#include <catch2/catch_test_macros.hpp>
#include "HashMap.hpp"

TEST_CASE("HashMap basic operations", "[hash_map]") {
    HashMap<std::string, int> map;

    SECTION("Inserting and retrieving values") {
        map.insert("Alice", 25);
        map.insert("Bob", 30);
        REQUIRE(map.get("Alice") == 25);
        REQUIRE(map.get("Bob") == 30);
        REQUIRE(map.get("Charlie") == std::nullopt);
    }

    SECTION("Subscript operator") {
        map["Charlie"] = 35;
        REQUIRE(map["Charlie"] == 35);
        REQUIRE(map.size() == 1);
    }
}
