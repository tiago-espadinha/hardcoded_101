#include <iostream>
#include <fstream>
#include <string>
#include <algorithm>
#include <stdexcept>

// 1. FileWrapper class: RAII for file handles
class FileWrapper {
private:
    std::ofstream file;
    std::string filename;

public:
    FileWrapper(const std::string& fname) : filename(fname) {
        file.open(filename);
        if (!file.is_open()) {
            throw std::runtime_error("Could not open file: " + filename);
        }
        std::cout << "[LOG] FileWrapper: Opened " << filename << std::endl;
    }

    ~FileWrapper() {
        if (file.is_open()) {
            file.close();
            std::cout << "[LOG] FileWrapper: Closed " << filename << std::endl;
        }
    }

    void write(const std::string& text) {
        file << text << std::endl;
    }

    // Disable copy
    FileWrapper(const FileWrapper&) = delete;
    FileWrapper& operator=(const FileWrapper&) = delete;
};

// 2. ArrayWrapper<T>: RAII for heap array + Move semantics (Rule of Five)
template <typename T>
class ArrayWrapper {
private:
    T* data;
    size_t size;

public:
    ArrayWrapper(size_t s) : data(new T[s]), size(s) {
        std::cout << "[LOG] ArrayWrapper: Allocated " << size << " elements." << std::endl;
    }

    // 1. Destructor
    ~ArrayWrapper() {
        delete[] data;
        std::cout << "[LOG] ArrayWrapper: Destroyed." << std::endl;
    }

    // 2. Copy Constructor
    ArrayWrapper(const ArrayWrapper& other) : data(new T[other.size]), size(other.size) {
        std::copy(other.data, other.data + size, data);
        std::cout << "[LOG] ArrayWrapper: Copy Constructor called." << std::endl;
    }

    // 3. Copy Assignment
    ArrayWrapper& operator=(const ArrayWrapper& other) {
        std::cout << "[LOG] ArrayWrapper: Copy Assignment called." << std::endl;
        if (this != &other) {
            delete[] data;
            size = other.size;
            data = new T[size];
            std::copy(other.data, other.data + size, data);
        }
        return *this;
    }

    // 4. Move Constructor
    ArrayWrapper(ArrayWrapper&& other) noexcept : data(other.data), size(other.size) {
        other.data = nullptr;
        other.size = 0;
        std::cout << "[LOG] ArrayWrapper: Move Constructor called." << std::endl;
    }

    // 5. Move Assignment
    ArrayWrapper& operator=(ArrayWrapper&& other) noexcept {
        std::cout << "[LOG] ArrayWrapper: Move Assignment called." << std::endl;
        if (this != &other) {
            delete[] data;
            data = other.data;
            size = other.size;
            other.data = nullptr;
            other.size = 0;
        }
        return *this;
    }

    size_t getSize() const { return size; }
};

int main() {
    try {
        std::cout << "--- Testing FileWrapper ---" << std::endl;
        {
            FileWrapper fw("test.txt");
            fw.write("RAII is awesome!");
            // No file handle leak even if exception thrown here
        }

        std::cout << "\n--- Testing ArrayWrapper (Rule of Five) ---" << std::endl;
        ArrayWrapper<int> a1(10);
        ArrayWrapper<int> a2 = std::move(a1); // Move ctor

        ArrayWrapper<int> a3(5);
        a3 = std::move(a2); // Move assign

        std::cout << "Final size of a3: " << a3.getSize() << std::endl;
    } catch (const std::exception& e) {
        std::cerr << "Error: " << e.what() << std::endl;
    }

    std::cout << "\n--- End of Main ---" << std::endl;
    return 0;
}
