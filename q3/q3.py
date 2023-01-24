#region Part 1
def shared_rucksack_items(input_file_name):
  # Idea: iterate over each line (representing a rucksack) and seperate them into two compartments (rucksack[:len(rucksack/2)], rucksack[len(rucksack/2):])
  # Then, convert each half into a hashmap of the 26 letters (either upper or lowercase)
  # Figure out which are the common elements from each rucksack, store them in a dictionary
  # Based on the position of the characters, add their value to the total

  total_priority = 0
  total_shared_characters = []
  input_file = open(input_file_name, 'r')

  for line in input_file:
    comp_1, comp_2 = line[:int(len(line)/2)], line[int(len(line)/2):]
    comp_1_dict, shared_characters = {}, set()
    for character in comp_1:
      comp_1_dict[character] = 1 + comp_1_dict.get(character, 0) # Add 1 to the count if exists in dictionary's keys, initialize with 1 otherwise
    for character in comp_2:
      if character in comp_1_dict.keys():
        shared_characters.add(character) # Add it to the shared_characters set if both compartments share this letter
    total_shared_characters.append(shared_characters)
  
  for shared_character_set in total_shared_characters:
    for shared_character in shared_character_set:
      if shared_character.isupper(): # If it is an uppercase character
        priority = ord(shared_character) - ord('a') # Find out the value of the ASCII character
        total_priority += (52 + priority + 7) # Calculate the correct value and add it to the total, A is -32 and Z is -7, so want 52 + priority, then +7 for the offset at the end
      else:
        total_priority += ord(shared_character) - ord('a') + 1 

  return total_priority
#endregion

#region Part 2
def shared_rucksack_badge(input_file_name):

  # Similar to the problem above, going to seperate each grouping of 3 lines (representing 3 elves) and iterate over them to find the common character
  # Then, take all the shared characters and calculate the priorities

  input_file = open(input_file_name, 'r')
  input_file_lines = input_file.readlines()
  shared_characters = []
  grouping, rucksacks = 0, []

  while len(input_file_lines) > 0 or (grouping == 3 and len(input_file_lines) == 0) :
    if grouping < 3: # While there are < 3 items in this grouping, append to it
      line = input_file_lines.pop().strip()
      rucksacks.append(line)
      grouping += 1
    elif grouping == 3:
      rucksack_set = set(rucksacks[0]) # Initialize a set from the first rucksuck
      for character in rucksack_set: # Iterate over all the characters in the set, if it's in both the second and third rucksacks, add it to the shared_characters
        if character in rucksacks[1] and character in rucksacks[2]:
          shared_characters.append(character)
      grouping = 0 # Reset grouping and rucksacks to prepare for the next batch of 3
      rucksacks = []
  
  total_badge_priority = 0
  for shared_character in shared_characters:
    if shared_character.isupper(): # If it is an uppercase character
      priority = ord(shared_character) - ord('a') # Find out the value of the ASCII character
      total_badge_priority += (52 + priority + 7) # Calculate the correct value and add it to the total, A is -32 and Z is -7, so want 52 + priority, then +7 for the offset at the end
    else:
      total_badge_priority += ord(shared_character) - ord('a') + 1

  return total_badge_priority

#endregion

if __name__ == '__main__':
  total_priority = shared_rucksack_items('input.txt')
  print('Total priority is: ' + str(total_priority))

  total_badge_priority = shared_rucksack_badge('input.txt')
  print('Total badge priority is: ' + str(total_badge_priority))