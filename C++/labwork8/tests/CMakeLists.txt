add_executable(bst_test bst_test.cpp)
target_link_libraries(bst_test PRIVATE gtest_main bst)
enable_testing()
add_test(NAME bst_test COMMAND bst_test)