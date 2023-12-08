#include <iostream>
#include <memory>
#include <vector>

// 1. Unique Ownership: Linked List Node
struct ListNode {
    int value;
    std::unique_ptr<ListNode> next;
    ListNode(int v) : value(v) { std::cout << "  [LOG] ListNode Created: " << value << std::endl; }
    ~ListNode() { std::cout << "  [LOG] ListNode Destroyed: " << value << std::endl; }
};

// 2. Shared/Weak Ownership: Tree Node
struct TreeNode {
    int value;
    std::vector<std::shared_ptr<TreeNode>> children;
    std::weak_ptr<TreeNode> parent; // Avoid cyclic dependency

    TreeNode(int v) : value(v) { std::cout << "  [LOG] TreeNode Created: " << value << std::endl; }
    ~TreeNode() { std::cout << "  [LOG] TreeNode Destroyed: " << value << std::endl; }
};

void testLinkedList() {
    std::cout << "--- Testing unique_ptr (Linked List) ---" << std::endl;
    auto head = std::make_unique<ListNode>(1);
    head->next = std::make_unique<ListNode>(2);
    head->next->next = std::make_unique<ListNode>(3);
    // Automatic cleanup when 'head' goes out of scope
}

void testTree() {
    std::cout << "\n--- Testing shared_ptr / weak_ptr (Tree) ---" << std::endl;
    auto root = std::make_shared<TreeNode>(100);
    auto child = std::make_shared<TreeNode>(200);

    root->children.push_back(child);
    child->parent = root;

    std::cout << "  Root use count: " << root.use_count() << std::endl;
    if (auto p = child->parent.lock()) {
        std::cout << "  Child's parent value: " << p->value << std::endl;
    }
}

int main() {
    testLinkedList();
    testTree();
    std::cout << "\n--- End of Main ---" << std::endl;
    return 0;
}
