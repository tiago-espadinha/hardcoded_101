cmake_minimum_required(VERSION 3.10)
project(cpp-mastery)

set(CMAKE_CXX_STANDARD 17)
set(CMAKE_CXX_STANDARD_REQUIRED ON)
set(CMAKE_CXX_FLAGS "${CMAKE_CXX_FLAGS} -Wall -Wextra -Werror")

add_subdirectory(oop)
add_subdirectory(modern)
add_subdirectory(cpp_hash_map)
add_subdirectory(cpp_linked_list)
