#include <gtest/gtest.h>
#include "../include/bst.hpp"

class BSTTest : public ::testing::Test {
protected:
    void SetUp() override {
        tree.insert(5);
        tree.insert(3);
        tree.insert(7);
        tree.insert(2);
        tree.insert(4);
        tree.insert(6);
        tree.insert(8);
    }
    
    BinarySearchTree<int> tree;
};

// Тест in-order обхода
TEST_F(BSTTest, InOrderTraversal) {
    std::vector<int> expected = {2, 3, 4, 5, 6, 7, 8};
    std::vector<int> actual;
    
    for (auto it = tree.in_order_begin(); it != tree.in_order_end(); ++it) {
        actual.push_back(*it);
    }
    
    ASSERT_EQ(expected, actual);
}

// Тест pre-order обхода
TEST_F(BSTTest, PreOrderTraversal) {
    std::vector<int> expected = {5, 3, 2, 4, 7, 6, 8};
    std::vector<int> actual;
    
    for (auto it = tree.pre_order_begin(); it != tree.pre_order_end(); ++it) {
        actual.push_back(*it);
    }
    
    ASSERT_EQ(expected, actual);
}

// Тест post-order обхода 
TEST_F(BSTTest, PostOrderTraversal) {
    std::vector<int> expected = {2, 4, 3, 6, 8, 7, 5};
    std::vector<int> actual;
    
    for (auto it = tree.post_order_begin(); it != tree.post_order_end(); ++it) {
        actual.push_back(*it);
    }
    
    ASSERT_EQ(expected, actual);
}

// Тест вставки и поиска
TEST_F(BSTTest, InsertAndFind) {
    auto it = tree.in_order_begin();
    ASSERT_EQ(2, *it);
    ++++it; 
    ASSERT_EQ(4, *it);
}

int main(int argc, char **argv) {
    ::testing::InitGoogleTest(&argc, argv);
    return RUN_ALL_TESTS();
}