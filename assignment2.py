import timeit

###############################? Assignment 1 ###############################

#! Task 1

def squares_list(n):
  squares = [(i * i) for i in range(1, n)]
  return squares


times = []
for n in [10, 100, 1000, 10000, 100000]:
  t = timeit.timeit(lambda: squares_list(n), number=1000)
  times.append((n, t))
  print(f'n={n}: {t} seconds')
    
# Time Complexity: O(n)
# Space Complexity: O(n)
  
#? Task 2

def reversed_sublist(list, i, j):
  sublist = list[i:(j+1)]
  reverse_list = sublist[::-1]
  return reverse_list

def time_reversed_sublist(size, i, j):
    lst = list(range(size))
    return timeit.timeit(lambda: reversed_sublist(lst, i, j), number=1000)
  
sizes = [10, 100, 1000, 10000, 1000000]
times = []

for size in sizes:
    i = size // 4
    j = 3 * size // 4
    t = time_reversed_sublist(size, i, j)
    times.append((size, t))
    print(f'size={size}, i={i}, j={j}: {t} seconds')

#	Time complexity: O(k), where k = j - i + 1
# Space complexity: O(k), where k = j - i + 1
  

#! Task 3: Implement a function to merge two sorted lists into a single sorted list. Analyze the time and space complexity of this operation.

def merged_lists(list1, list2):
    sorted_1 = sorted(list1)
    sorted_2 = sorted(list2)
    
    merged_list = []
    i, j = 0, 0
    
    while i < len(sorted_1) and j < len(sorted_2):
        if sorted_1[i] < sorted_2[j]:
            merged_list.append(sorted_1[i])
            i += 1
        else:
            merged_list.append(sorted_2[j])
            j += 1
    
    merged_list.extend(sorted_1[i:])
    merged_list.extend(sorted_2[j:])
    
    return merged_list
  
def wrapper(func, *args, **kwargs):
  def wrapped():
      return func(*args, **kwargs)
  return wrapped

sizes = [10, 100, 1000, 10000]
for size in sizes:
    l1 = list(range(size))
    l2 = list(range(size, 2*size))
    wrapped = wrapper(merged_lists, l1, l2)
    time_taken = timeit.timeit(wrapped, number=10)
    print(f"Time taken for size {size}: {time_taken:.6f} seconds")

l1 = [2, 3, 4, 5, 6]
l2 = [6, 7, 8, 9, 0]

print(merged_lists(l1, l2))

# Time Complexity:  O(nlogn + mlogm)
# Space Complexity: O(n + m)

###############################! Assignment 2 ###############################

#? Task 1: Implement a function to merge two dictionaries, preserving the values of common keys from the second dictionary. Analyze the time and space complexity of this operation.

def merge_dicts(dict1, dict2):
    merged_dict = dict1.copy()
    
    for key, value in dict2.items():
        if key in dict1:
            merged_dict[key] = value
    
    return merged_dict
  
def wrapper(func, *args, **kwargs):
    def wrapped():
        return func(*args, **kwargs)
    return wrapped

sizes = [10, 100, 1000, 10000]
for size in sizes:
    dict1 = {f'key{i}': i for i in range(size)}
    dict2 = {f'key{i}': i + size for i in range(size // 2, size + size // 2)}
    wrapped = wrapper(merge_dicts, dict1, dict2)
    time_taken = timeit.timeit(wrapped, number=10)
    print(f"Time taken for size {size}: {time_taken:.6f} seconds")
  
dict1 = {'a': 1, 'b': 2, 'c': 3}
dict2 = {'b': 4, 'c': 5, 'd': 6}

print(merge_dicts(dict1, dict2))

# Time Complexity: O(n + m)
# Space Complexity: O(n)

#! Task 2: Implement a function to find the intersection of two dictionaries, i.e., keys common to both dictionaries along with their values. Analyze the time and space complexity of this operation.

def intersect_dicts(dict1, dict2):
    intersect_dict = {}
    
    for key, value in dict1.items():
        if key in dict2:
            intersect_dict[key] = value
    
    return intersect_dict
  
def wrapper(func, *args, **kwargs):
    def wrapped():
        return func(*args, **kwargs)
    return wrapped

sizes = [10, 100, 1000, 10000]
for size in sizes:
    dict1 = {f'key{i}': i for i in range(size)}
    dict2 = {f'key{i}': i + size for i in range(size // 2, size + size // 2)}
    wrapped = wrapper(intersect_dicts, dict1, dict2)
    time_taken = timeit.timeit(wrapped, number=10)
    print(f"Time taken for size {size}: {time_taken:.6f} seconds")
  
dict1 = {'a': 1, 'b': 2, 'c': 3}
dict2 = {'b': 4, 'c': 5, 'd': 6}

print(intersect_dicts(dict1, dict2))

# # Time Complexity: O(n)
# # Space Complexity: O(n)


#? Task 3: Implement a function to count the frequency of each unique word in a list using a dictionary. Analyze the time and space complexity of this operation.

def word_frequency(words):
    freq_dict = {}
    
    for word in words:
        if word in freq_dict:
            freq_dict[word] += 1
        else:
            freq_dict[word] = 1
    
    return freq_dict
  
def wrapper(func, *args, **kwargs):
    def wrapped():
        return func(*args, **kwargs)
    return wrapped

sizes = [10, 100, 1000, 10000]
for size in sizes:
    words = ['word' + str(i % 10) for i in range(size)]
    wrapped = wrapper(word_frequency, words)
    time_taken = timeit.timeit(wrapped, number=10)
    print(f"Time taken for size {size}: {time_taken:.6f} seconds")
  
words = ['apple', 'banana', 'apple', 'pie', 'apple', 'banana', 'pie', 'apple', 'cake']

print(word_frequency(words))

# Time Complexity: O(n)
# Space Complexity: O(n)