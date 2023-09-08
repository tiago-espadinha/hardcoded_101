#include <iostream>
#include <string>
#include <vector>
#include <numeric>
#include <algorithm>
#include <sstream>

class Student {
private:
    std::string name;
    int id;
    std::vector<double> grades;

public:
    // Default constructor
    Student(std::string n, int i) : name(std::move(n)), id(i) {
        std::cout << "[LOG] Constructor: Student " << name << " (ID: " << id << ") created." << std::endl;
    }

    // Rule of Three: Destructor
    ~Student() {
        std::cout << "[LOG] Destructor: Student " << name << " (ID: " << id << ") destroyed." << std::endl;
    }

    // Rule of Three: Copy Constructor
    Student(const Student& other) : name(other.name + " (Copy)"), id(other.id + 1000), grades(other.grades) {
        std::cout << "[LOG] Copy Constructor: Created " << name << " from " << other.name << "." << std::endl;
    }

    // Rule of Three: Copy Assignment Operator
    Student& operator=(const Student& other) {
        std::cout << "[LOG] Copy Assignment: Assigning " << other.name << " to " << name << "." << std::endl;
        if (this != &other) {
            name = other.name + " (Assigned)";
            id = other.id + 2000;
            grades = other.grades;
        }
        return *this;
    }

    void addGrade(double grade) {
        grades.push_back(grade);
    }

    double average() const {
        if (grades.empty()) return 0.0;
        return std::accumulate(grades.begin(), grades.end(), 0.0) / grades.size();
    }

    double highest() const {
        if (grades.empty()) return 0.0;
        return *std::max_element(grades.begin(), grades.end());
    }

    double lowest() const {
        if (grades.empty()) return 0.0;
        return *std::min_element(grades.begin(), grades.end());
    }

    std::string toString() const {
        std::ostringstream oss;
        oss << "Student: " << name << " (ID: " << id << "), Avg: " << average();
        return oss.str();
    }
};

int main() {
    std::cout << "--- Creating Student s1 ---" << std::endl;
    Student s1("Alice", 101);
    s1.addGrade(85.5);
    s1.addGrade(92.0);
    s1.addGrade(78.0);
    std::cout << s1.toString() << std::endl;

    std::cout << "\n--- Copy Constructor (s2 = s1) ---" << std::endl;
    Student s2 = s1;
    std::cout << s2.toString() << std::endl;

    std::cout << "\n--- Copy Assignment (s3 = s1) ---" << std::endl;
    Student s3("Bob", 102);
    s3 = s1;
    std::cout << s3.toString() << std::endl;

    std::cout << "\n--- End of Main ---" << std::endl;
    return 0;
}
