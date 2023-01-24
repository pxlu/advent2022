#region Part 1
def get_contained_ranges(input_file_name):
  # Iterate over the file, and for each pairing:
  # For each pair, check the starting range of one elf <= second elf
  # For that elf, check whether or not the ending range is >= ending range of the other elf
  # If so, then it is fully contained, increment the counter of fully contained

  total_contained_pairs = 0
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
def get_shared_ranges(input_file_name):
  # Similar to above, iterate over each line representing the pair
  # This time, use a set intersection to check if there is any overlap, if so, increment total_overlapping_pairs

  total_overlapping_pairs = 0
  # not_overlap = []
  input_file = open(input_file_name, 'r')

  for line in input_file:
    ranges = line.split(',') # Split the line by the divider
    elf_1_ranges, elf_2_ranges = ranges[0].strip(), ranges[1].strip()

    elf_1_starting, elf_2_starting = int(elf_1_ranges.split('-')[0]), int(elf_2_ranges.split('-')[0]) # Get the starting ranges for each elf
    elf_1_ending, elf_2_ending = int(elf_1_ranges.split('-')[1]), int(elf_2_ranges.split('-')[1]) # Get the ending ranges for each elf
    elf_1_range_set = set(range(elf_1_starting, elf_1_ending+1)) # Create a set out of the ranges of elf 1
    
    if len(elf_1_range_set.intersection(range(elf_2_starting, elf_2_ending+1))) > 0: # Check if there is any overlap between the two ranges, +1 to the ending because it's not inclusive
      total_overlapping_pairs += 1
    #else:
    #  not_overlap.append([(elf_1_starting, elf_1_ending), (elf_2_starting, elf_2_ending)])

  # import pprint
  # pprint.pprint(not_overlap)
  return total_overlapping_pairs

#endregion

if __name__ == '__main__':
  total_contained_pairs = get_contained_ranges('input.txt')
  print('Total contained pairs is: ' + str(total_contained_pairs))

  total_overlapping_pairs = get_shared_ranges('input.txt')
  print('Total overlapping pairs is: ' + str(total_overlapping_pairs))