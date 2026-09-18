from typing import List


def sort_words(words: List[str]) -> List[str]:
    arr = words.copy()
    arr.sort(key=lambda word: len(word), reverse=True)
    return arr

def sort_numbers(numbers: List[int]) -> List[int]:
    arr = numbers.copy()
    arr.sort(key=lambda num: abs(num))
    return arr

print(sort_words(["cherry", "apple", "blueberry", "banana", "watermelon", "zucchini", "kiwi", "pear"]))

print(sort_numbers([1, -5, -3, 2, 4, 11, -19, 9, -2, 5, -6, 7, -4, 2, 6]))
