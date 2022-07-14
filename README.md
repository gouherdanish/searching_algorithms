# Searching

## Introduction:
    Searching is a very important algorithm where the objective is to find if a given target element is present inside a given array.
    If it is present, then it returns the index position of the element in the array.
    If it is not present, then it returns None

# Searching Algorithms
    1) Linear Search (Sequential/Simple Search)
        - Start from the index 0 and continue till arr.length
        - Compare one by one with the target
        - If it matches, return the index
        - O(n)
    
    2) Binary Search (Sublinear Search)
        - Assumes the array is sorted
        - Find mid point of arr
        - Compare arr[mid] with target
            - if matched, return mid
            - if arr[mid] > target, search in first half
            - else search in second half
        - O(log n)

# Outputs
`python3 search.py --range 10 --target 3 --search linear`
runtime = 1.7e-05
position = 3

`python3 search.py --range 10 --target 3 --search binary`
runtime = 9e-06
position = 3

`python3 search.py --range 1000 --target 300 --search linear`
runtime = 2.2e-05
position = 300

`python3 search.py --range 1000 --target 300 --search binary`
runtime = 1e-05
position = 300

`python3 search.py --range 100000 --target 900 --search linear`
runtime = 5.1e-05
position = 900

`python3 search.py --range 100000 --target 900 --search binary`
runtime = 2.2e-05
position = 900