#include <iostream>
#include <vector>
#include <string>
#include <chrono>
#include <cstring>

class MyString {
private:
    static constexpr size_t SSO_CAPACITY = 15;
    char* data;
    size_t size;
    char sso_buffer[SSO_CAPACITY + 1];

    bool is_sso() const { return data == sso_buffer; }

public:
    MyString(const char* s) {
        size = std::strlen(s);
        if (size <= SSO_CAPACITY) {
            std::memcpy(sso_buffer, s, size + 1);
            data = sso_buffer;
        } else {
            data = new char[size + 1];
            std::memcpy(data, s, size + 1);
        }
    }

    ~MyString() {
        if (!is_sso()) delete[] data;
    }

    // Copy constructor (O(n))
    MyString(const MyString& other) : size(other.size) {
        if (size <= SSO_CAPACITY) {
            std::memcpy(sso_buffer, other.sso_buffer, size + 1);
            data = sso_buffer;
        } else {
            data = new char[size + 1];
            std::memcpy(data, other.data, size + 1);
        }
        // std::cout << "Copy called" << std::endl;
    }

    // Move constructor (O(1) if not SSO)
    MyString(MyString&& other) noexcept : size(other.size) {
        if (other.is_sso()) {
            std::memcpy(sso_buffer, other.sso_buffer, size + 1);
            data = sso_buffer;
        } else {
            data = other.data;
            other.data = nullptr;
        }
        other.size = 0;
        // std::cout << "Move called" << std::endl;
    }
};

void benchmark() {
    const int N = 100000;
    const char* long_str = "This is a very long string to ensure it exceeds the SSO capacity of 15 characters.";

    {
        std::vector<MyString> v;
        v.reserve(N);
        auto start = std::chrono::high_resolution_clock::now();
        for (int i = 0; i < N; ++i) {
            MyString s(long_str);
            v.push_back(s); // Uses Copy
        }
        auto end = std::chrono::high_resolution_clock::now();
        std::cout << "Copy Benchmark: " << std::chrono::duration_cast<std::chrono::milliseconds>(end - start).count() << "ms" << std::endl;
    }

    {
        std::vector<MyString> v;
        v.reserve(N);
        auto start = std::chrono::high_resolution_clock::now();
        for (int i = 0; i < N; ++i) {
            MyString s(long_str);
            v.push_back(std::move(s)); // Uses Move
        }
        auto end = std::chrono::high_resolution_clock::now();
        std::cout << "Move Benchmark: " << std::chrono::duration_cast<std::chrono::milliseconds>(end - start).count() << "ms" << std::endl;
    }
}

int main() {
    benchmark();
    return 0;
}
