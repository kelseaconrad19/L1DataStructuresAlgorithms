def insertion_sort(arr):
  for i in range(1, len(arr)):
    #! => O(n)
    key = arr[i]
    j = i - 1
    
    while j >= 0 and key < arr[j]:
      #! <= O(n)
      arr[j + 1] = arr[j]
      j -= 1
    arr[j + 1] = key
    
  return arr

my_arr = [12, 11, 13, 5, 6] 
print(insertion_sort(my_arr)) #? [5, 6, 11, 12, 13] => O(n^2) operation


#? Time Complexity

#! O(n^2) - worst case scenario
for i in range(10):
  for j in range(10):
    print(f"i: {i}, j: {j}")
    #! O(n^2) operation because it has to iterate through the entire second list (j) for each element in the first list (i)


#* O(n) - best case scenario - linear time complexity
for i in range(10):
  print(i)
  #* O(n) operation because it has to iterate through the entire list
my_dict = {'key': 'value'}

if 'key' in my_dict:
  print(my_dict['key'])
  #* O(1) operation because it doesn't have to iterate through the entire dictionary

#TODO Nested Loops - O(n^2) operation USUALLY!!! - depends on the scenario - can be O(n^3), O(n^4), etc. 