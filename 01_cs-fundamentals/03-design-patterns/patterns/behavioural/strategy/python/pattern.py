from abc import ABC, abstractmethod
from typing import List, Any

class SortStrategy(ABC):
    @abstractmethod
    def sort(self, data: List[Any]) -> List[Any]:
        pass

class BubbleSort(SortStrategy):
    def sort(self, data: List[Any]) -> List[Any]:
        print("Sorting using Bubble Sort (stable, good for small data)")
        n = len(data)
        arr = data.copy()
        for i in range(n):
            for j in range(0, n-i-1):
                if arr[j] > arr[j+1]:
                    arr[j], arr[j+1] = arr[j+1], arr[j]
        return arr

class QuickSort(SortStrategy):
    def sort(self, data: List[Any]) -> List[Any]:
        print("Sorting using Quick Sort (fast, unstable)")
        if len(data) <= 1:
            return data
        pivot = data[len(data) // 2]
        left = [x for x in data if x < pivot]
        middle = [x for x in data if x == pivot]
        right = [x for x in data if x > pivot]
        return self.sort(left) + middle + self.sort(right)

class MergeSort(SortStrategy):
    def sort(self, data: List[Any]) -> List[Any]:
        print("Sorting using Merge Sort (stable, O(n log n))")
        if len(data) <= 1:
            return data
        
        mid = len(data) // 2
        left = self.sort(data[:mid])
        right = self.sort(data[mid:])
        
        return self._merge(left, right)
    
    def _merge(self, left, right):
        result = []
        i = j = 0
        while i < len(left) and j < len(right):
            if left[i] < right[j]:
                result.append(left[i])
                i += 1
            else:
                result.append(right[j])
                j += 1
        result.extend(left[i:])
        result.extend(right[j:])
        return result

class Sorter:
    def __init__(self, strategy: SortStrategy):
        self._strategy = strategy
        
    def set_strategy(self, strategy: SortStrategy):
        self._strategy = strategy
        
    def sort_data(self, data: List[Any]) -> List[Any]:
        return self._strategy.sort(data)

if __name__ == "__main__":
    data = [64, 34, 25, 12, 22, 11, 90]
    
    sorter = Sorter(BubbleSort())
    print(sorter.sort_data(data))
    
    sorter.set_strategy(QuickSort())
    print(sorter.sort_data(data))
