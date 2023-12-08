add_executable(unit_tests
    test_hash_map.cpp
    test_linked_list.cpp
)

target_link_libraries(unit_tests PRIVATE Catch2::Catch2WithMain)
target_include_directories(unit_tests PRIVATE 
    ${CMAKE_SOURCE_DIR}/cpp_hash_map
    ${CMAKE_SOURCE_DIR}/cpp_linked_list
)

add_test(NAME unit_tests COMMAND unit_tests)
