#pragma once
#include <iostream>
#include <initializer_list>
#include <iterator>

template <typename T>
class DoublyLinkedList {
private:
    struct Node {
        T value;
        Node* prev;
        Node* next;
        Node(T v) : value(std::move(v)), prev(nullptr), next(nullptr) {}
    };

    Node* head;
    Node* tail;
    size_t count;

public:
    class Iterator {
    private:
        Node* current;
    public:
        using iterator_category = std::bidirectional_iterator_tag;
        using value_type = T;
        using difference_type = std::ptrdiff_t;
        using pointer = T*;
        using reference = T&;

        Iterator(Node* n) : current(n) {}
        reference operator*() const { return current->value; }
        Iterator& operator++() { current = current->next; return *this; }
        Iterator operator++(int) { Iterator temp = *this; ++(*this); return temp; }
        Iterator& operator--() { current = current->prev; return *this; }
        Iterator operator--(int) { Iterator temp = *this; --(*this); return temp; }
        bool operator==(const Iterator& other) const { return current == other.current; }
        bool operator!=(const Iterator& other) const { return current != other.current; }
    };

    DoublyLinkedList() : head(nullptr), tail(nullptr), count(0) {}

    DoublyLinkedList(std::initializer_list<T> list) : DoublyLinkedList() {
        for (const auto& item : list) {
            push_back(item);
        }
    }

    ~DoublyLinkedList() {
        Node* current = head;
        while (current) {
            Node* next = current->next;
            delete current;
            current = next;
        }
    }

    void push_back(T value) {
        Node* newNode = new Node(std::move(value));
        if (!tail) {
            head = tail = newNode;
        } else {
            tail->next = newNode;
            newNode->prev = tail;
            tail = newNode;
        }
        count++;
    }

    Iterator begin() { return Iterator(head); }
    Iterator end() { return Iterator(nullptr); }
    size_t size() const { return count; }
};
