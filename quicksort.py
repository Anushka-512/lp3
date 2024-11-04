import random

class QuickSort:
    def __init__(self) -> None:
        pass

    def partition(self, arr, low, high):
        pivot = arr[low]
        i = low + 1
        j = high

        while True:
            while i <= high and arr[i] <= pivot:
                i += 1

            while j > low and arr[j] > pivot:
                j -= 1

            if i >= j:
                break

            arr[i], arr[j] = arr[j], arr[i]

        arr[low], arr[j] = arr[j], arr[low]
        return j

    def deterministic_quick_sort(self, arr, low, high):
        if low < high:
            p = self.partition(arr, low, high)
            self.deterministic_quick_sort(arr, low, p)
            self.deterministic_quick_sort(arr, p + 1, high)

    def random_quick_sort(self, arr, low, high):
        if low < high:
            r = random.randint(low, high)
            arr[low], arr[r] = arr[r], arr[low]
            p = self.partition(arr, low, high)
            self.random_quick_sort(arr, low, p)
            self.random_quick_sort(arr, p + 1, high)

# Test cases
test_cases = [
    [29, 4, 11, 33, -1, 0, 55, 24],
    [100, 54, 2, 18, -8, 34, 76, 1],
    [10, 5, 3, 7, 2, 8, -2, 11]
]

# Create an instance of QuickSort
qs = QuickSort()

for i, test_case in enumerate(test_cases, start=1):
    # Copy the test case for deterministic and randomized sorting
    deterministic_list = test_case.copy()
    randomized_list = test_case.copy()

    # Sort with deterministic Quick Sort
    print(f"\nTest Case {i} - Deterministic Quick Sort:")
    qs.deterministic_quick_sort(deterministic_list, 0, len(deterministic_list) - 1)
    print(deterministic_list)

    # Sort with randomized Quick Sort
    print(f"Test Case {i} - Randomized Quick Sort:")
    qs.random_quick_sort(randomized_list, 0, len(randomized_list) - 1)
    print(randomized_list)
