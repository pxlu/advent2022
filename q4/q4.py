#region Part 1
def get_contained_ranges(input_file_name):
  # Iterate over the file, and for each pairing:
  # Get the minimum between the starting ranges, either elf_1 or elf_2
  # For that elf, check whether or not the ending range is >= ending range of the other elf
  # If so, then it is fully contained, increment the counter of fully contained

  total_contained_pairs = 0
  not_paired = []
  input_file = open(input_file_name, 'r')

  for line in input_file:
    ranges = line.split(',') # Split the line by the divider
    elf_1_ranges, elf_2_ranges = ranges[0].strip(), ranges[1].strip()

    elf_1_starting, elf_2_starting = int(elf_1_ranges.split('-')[0]), int(elf_2_ranges.split('-')[0]) # Get the starting ranges for each elf
    elf_1_ending, elf_2_ending = int(elf_1_ranges.split('-')[1]), int(elf_2_ranges.split('-')[1]) # Get the ending ranges for each elf
    if elf_1_starting <= elf_2_starting and elf_1_ending >= elf_2_ending: # If elf 1 fully contain's elf 2's ranges
      total_contained_pairs += 1
    elif elf_2_starting <= elf_1_starting and elf_2_ending >= elf_1_ending: # If elf 2 fully contain's elf 1's ranges
      total_contained_pairs += 1
  
  return total_contained_pairs
#endregion

#region Part 2
def get_shared_ranges():
  pass
#endregion

if __name__ == '__main__':
  total_contained_pairs = get_contained_ranges('input.txt')
  print('Total contained pairs is: ' + str(total_contained_pairs))