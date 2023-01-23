# https://adventofcode.com/2022/day/1

#region Part 1
def get_most_calories(input_file_name):
  # From the input file of numbers seperated by empty lines, sum up all the numbers until an empty line (representing one elf)
  # Calculate which elf has the most amount of calories

  # 0. Initialize variables for maximum calories overall
  # 1. Iterate over every line in input
  # 2. Create a variable to keep track of the current total of calories for an given elf
  # 3. Until hitting an empty line, add the current line's number to the total
  # 4. If the current sum of calories is greater than the max, update max 
  max_calories, current_calories = 0, 0
  input_file = open(input_file_name, 'r')

  for line in input_file:
    if line == '\n':
      max_calories = max(max_calories, current_calories)
      current_calories = 0
    else:
      current_calories += int(line)
  
  input_file.close()
  return max_calories
#endregion

#region Part 2
# This implementation of a max heap was found here:
# https://www.techiedelight.com/max-heap-implementation-in-python-using-heapq/
import heapq
 
class MaxHeap:
 
    # Initialize the max heap
    def __init__(self, data=None):
        if data is None:
            self.data = []
        else:
            self.data = [-i for i in data]
            heapq.heapify(self.data)
 
    # Push item onto max heap, maintaining the heap invariant
    def push(self, item):
        heapq.heappush(self.data, -item)
 
    # Pop the largest item off the max heap, maintaining the heap invariant
    def pop(self):
        return -heapq.heappop(self.data)
 
    # Pop and return the current largest value, and add the new item
    def replace(self, item):
        return heapq.heapreplace(self.data, -item)
 
    # Return the current largest value in the max heap
    def top(self):
        return -self.data[0]

def get_sum_top_k_calories(input_file_name, k=1):
  # Similar to part 1, going to iterate over every line in the input_file denoted by input_file_name and add the numbers until an newline character
  # However this time, the outputs will be stored in a max heap
  # At the end of parsing the file, going to pop from the max heap [k] times, add all the results together for the final answer
  
  # 1. Initialize all required variables, and open the file
  current_calories = 0
  result_list = []
  input_file = open(input_file_name, 'r')

  # 2. Iterate over the file, and add the number to the running total until a newline character
  for line in input_file:
    if line == '\n':
      # Once at a newline, add it to the list of calories for that elf
      result_list.append(current_calories)
      current_calories = 0
    else:
      current_calories += int(line)
  
  # Close the file after reading
  input_file.close()

  # 3. Convert the result_list into a max heap, and pop [k] elements from the heap and add it the total, returning it at the end
  calories_max_heap = MaxHeap(result_list)
  total_calories_result = 0
  for i in range(k):
    # Add the popped number to the total
    total_calories_result += calories_max_heap.pop()

  # Return the total
  return total_calories_result
#endregion

if __name__ == '__main__':
  max_calories = get_most_calories('input.txt')
  print('The maximum calories carried by one elf is: '+ str(max_calories))
  num_elves = 3
  top_3_calories_sum = get_sum_top_k_calories('input.txt', num_elves)
  top_3_output_str = ('The maximum calories carried by the top {0} elves total is: ' + str(top_3_calories_sum)).format(num_elves)
  print(top_3_output_str)
