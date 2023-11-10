#pragma once
#include <vector>
#include <optional>
#include <functional>
#include <string>
#include <stdexcept>

template <typename K, typename V>
class HashMap {
private:
    struct Entry {
        K key;
        V value;
        bool occupied = false;
        bool deleted = false;
    };

    std::vector<Entry> table;
    size_t count = 0;
    static constexpr float LOAD_FACTOR_THRESHOLD = 0.7f;

    size_t hash(const K& key) const {
        return std::hash<K>{}(key) % table.size();
    }

    void rehash() {
        auto oldTable = std::move(table);
        table.assign(oldTable.size() * 2, Entry{});
        count = 0;
        for (auto& entry : oldTable) {
            if (entry.occupied && !entry.deleted) {
                insert(entry.key, entry.value);
            }
        }
    }

public:
    HashMap(size_t initialSize = 16) : table(initialSize) {}

    void insert(const K& key, const V& value) {
        if ((float)count / table.size() > LOAD_FACTOR_THRESHOLD) {
            rehash();
        }

        size_t h = hash(key);
        size_t i = 0;
        while (table[(h + i * i) % table.size()].occupied && !table[(h + i * i) % table.size()].deleted) {
            if (table[(h + i * i) % table.size()].key == key) {
                table[(h + i * i) % table.size()].value = value;
                return;
            }
            i++;
        }

        size_t idx = (h + i * i) % table.size();
        table[idx] = {key, value, true, false};
        count++;
    }

    V& operator[](const K& key) {
        size_t h = hash(key);
        size_t i = 0;
        while (table[(h + i * i) % table.size()].occupied) {
            size_t idx = (h + i * i) % table.size();
            if (!table[idx].deleted && table[idx].key == key) {
                return table[idx].value;
            }
            i++;
        }
        insert(key, V{});
        return operator[](key);
    }

    std::optional<V> get(const K& key) const {
        size_t h = hash(key);
        size_t i = 0;
        while (table[(h + i * i) % table.size()].occupied) {
            size_t idx = (h + i * i) % table.size();
            if (!table[idx].deleted && table[idx].key == key) {
                return table[idx].value;
            }
            i++;
        }
        return std::nullopt;
    }

    size_t size() const { return count; }
};
