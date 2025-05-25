cmake_minimum_required(VERSION 3.10)
project(BSTProject)

# Для header-only библиотеки
add_library(bst INTERFACE)
target_include_directories(bst INTERFACE 
    ${CMAKE_CURRENT_SOURCE_DIR}/include
)

# Google Test
add_subdirectory(libs/googletest)

# Тесты
add_executable(bst_test tests/bst_test.cpp)
target_link_libraries(bst_test PRIVATE gtest_main bst)

enable_testing()
add_test(NAME bst_test COMMAND bst_test)