#include <iostream>
#include <vector>
#include <string>
#include <algorithm>
#include <numeric>

struct Student {
    int id;
    std::string name;
    double gpa;
};

int main() {
    std::vector<Student> students = {
        {1, "Alice", 3.8},
        {2, "Bob", 3.2},
        {3, "Charlie", 3.8},
        {4, "Dave", 2.1},
        {5, "Eve", 1.5}
    };

    std::cout << "--- STL Algorithms in One-Liners (with Lambdas) ---" << std::endl;

    // 1. Sort by GPA (desc), then alphabetically
    std::sort(students.begin(), students.end(), [](const auto& a, const auto& b) {
        return a.gpa != b.gpa ? a.gpa > b.gpa : a.name < b.name;
    });

    // 2. Find by ID
    [[maybe_unused]] auto it = std::find_if(students.begin(), students.end(), [](const auto& s) { return s.id == 3; });

    // 3. Extract names
    std::vector<std::string> names;
    std::transform(students.begin(), students.end(), std::back_inserter(names), [](const auto& s) { return s.name; });

    // 4. Compute average GPA
    double avgGpa = std::accumulate(students.begin(), students.end(), 0.0, [](double sum, const auto& s) { return sum + s.gpa; }) / students.size();

    // 5. Partition (passing vs failing)
    [[maybe_unused]] auto partitionPoint = std::partition(students.begin(), students.end(), [](const auto& s) { return s.gpa >= 2.0; });

    // 6. Count honors (GPA > 3.5)
    long honorsCount = std::count_if(students.begin(), students.end(), [](const auto& s) { return s.gpa > 3.5; });

    std::cout << "Average GPA: " << avgGpa << std::endl;
    std::cout << "Honors Students: " << honorsCount << std::endl;
    std::cout << "Top Student: " << students.front().name << std::endl;

    return 0;
}
