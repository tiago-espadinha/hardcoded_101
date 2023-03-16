from pattern import Sorter, BubbleSort, QuickSort, MergeSort

class SmartSorter:
    """A high-level sorter that chooses the strategy based on data size."""
    
    def __init__(self):
        self._sorter = Sorter(BubbleSort())
        
    def sort(self, data):
        if len(data) < 10:
            self._sorter.set_strategy(BubbleSort())
        elif len(data) < 1000:
            self._sorter.set_strategy(QuickSort())
        else:
            self._sorter.set_strategy(MergeSort())
            
        print(f"Data size: {len(data)}. ", end="")
        return self._sorter.sort_data(data)

if __name__ == "__main__":
    smart_sorter = SmartSorter()
    
    small_data = [5, 2, 9, 1]
    smart_sorter.sort(small_data)
    
    medium_data = list(range(100, 0, -1))
    smart_sorter.sort(medium_data)
