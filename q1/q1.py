# https://adventofcode.com/2022/day/1

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

  return max_calories

if __name__ == '__main__':
  max_calories = get_most_calories('input.txt')
  print(max_calories)