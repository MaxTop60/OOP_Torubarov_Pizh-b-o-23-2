#include <iostream>
#include <memory>
#include <functional>
#include <initializer_list>

// Tags для диспетчеризации типов обхода
struct InOrderTag {};
struct PreOrderTag {};
struct PostOrderTag {};

// Узел дерева
template <typename T>
struct TreeNode {
    T value;
    std::unique_ptr<TreeNode<T>> left;
    std::unique_ptr<TreeNode<T>> right;
    TreeNode<T>* parent;

    TreeNode(const T& val, TreeNode<T>* p = nullptr) 
        : value(val), left(nullptr), right(nullptr), parent(p) {}
};

// Базовый класс итератора
template <typename T, typename OrderTag>
class BSTIterator {
    TreeNode<T>* current;
    
public:
    using iterator_category = std::bidirectional_iterator_tag;
    using value_type = T;
    using difference_type = std::ptrdiff_t;
    using pointer = T*;
    using reference = T&;

    BSTIterator(TreeNode<T>* node = nullptr) : current(node) {}

    // Инкремент с диспетчеризацией по тегу
    BSTIterator& operator++() {
        advance(OrderTag{});
        return *this;
    }

    BSTIterator operator++(int) {
        BSTIterator tmp = *this;
        ++(*this);
        return tmp;
    }

    reference operator*() const { return current->value; }
    pointer operator->() const { return &current->value; }

    bool operator==(const BSTIterator& other) const { return current == other.current; }
    bool operator!=(const BSTIterator& other) const { return !(*this == other); }

private:
    void advance(InOrderTag) {
        if (current->right) {
            current = current->right.get();
            while (current->left) {
                current = current->left.get();
            }
        } else {
            TreeNode<T>* p = current->parent;
            while (p && current == p->right.get()) {
                current = p;
                p = p->parent;
            }
            current = p;
        }
    }

    void advance(PreOrderTag) {
        if (current->left) {
            current = current->left.get();
        } else if (current->right) {
            current = current->right.get();
        } else {
            TreeNode<T>* p = current->parent;
            while (p && (!p->right || current == p->right.get())) {
                current = p;
                p = p->parent;
            }
            current = p ? p->right.get() : nullptr;
        }
    }

    void advance(PostOrderTag) {
        if (!current->parent) {
            current = nullptr;
        } else if (current == current->parent->left.get()) {
            if (current->parent->right) {
                current = current->parent->right.get();
                while (current->left || current->right) {
                    if (current->left) {
                        current = current->left.get();
                    } else {
                        current = current->right.get();
                    }
                }
            } else {
                current = current->parent;
            }
        } else {
            current = current->parent;
        }
    }
};

// Шаблон бинарного дерева поиска
template <typename T, 
          typename Compare = std::less<T>,
          typename Allocator = std::allocator<TreeNode<T>>>
class BinarySearchTree {
public:
    using InOrderIterator = BSTIterator<T, InOrderTag>;
    using PreOrderIterator = BSTIterator<T, PreOrderTag>;
    using PostOrderIterator = BSTIterator<T, PostOrderTag>;

    BinarySearchTree() : root(nullptr), cmp(Compare()), alloc(Allocator()) {}

    void insert(const T& value) {
        insert(root, nullptr, value);
    }

    InOrderIterator in_order_begin() {
        TreeNode<T>* node = root.get();
        while (node && node->left) {
            node = node->left.get();
        }
        return InOrderIterator(node);
    }

    InOrderIterator in_order_end() { return InOrderIterator(nullptr); }

    PreOrderIterator pre_order_begin() { return PreOrderIterator(root.get()); }
    PreOrderIterator pre_order_end() { return PreOrderIterator(nullptr); }

    PostOrderIterator post_order_begin() {
        TreeNode<T>* node = root.get();
        while (node && (node->left || node->right)) {
            if (node->left) {
                node = node->left.get();
            } else {
                node = node->right.get();
            }
        }
        return PostOrderIterator(node);
    }
    PostOrderIterator post_order_end() { return PostOrderIterator(nullptr); }

private:
    std::unique_ptr<TreeNode<T>> root;
    Compare cmp;
    Allocator alloc;

    void insert(std::unique_ptr<TreeNode<T>>& node, TreeNode<T>* parent, const T& value) {
        if (!node) {
            node = std::unique_ptr<TreeNode<T>>(alloc.allocate(1));
            alloc.construct(node.get(), value, parent);
        } else if (cmp(value, node->value)) {
            insert(node->left, node.get(), value);
        } else if (cmp(node->value, value)) {
            insert(node->right, node.get(), value);
        }
    }
};
