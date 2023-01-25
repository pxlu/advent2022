#region Part 1
# Helpers
from collections import deque

def get_crate_ordering(input_file_name):
  # Intuition: we want to track elements as they move from one stack to another, and the order of insertion / removal matters
  # This lends very nicely to the stack data structure, exactly as it sounds as a parallel to the stacks in the question
  # As each item is either added or removed from the stack, we track it with the corresponding stack data structure
  # At the end, just pop the top of each stack to get the ordering

  input_file = open(input_file_name, 'r')
  top_ordering = ''
  stacks = [deque() for i in range(9)] # Hardcoded because the input is given ahead of time, otherwise it would be calculated if needed

  for line in input_file:
    line = list(line)
    # 1. If the line does not start with the keyword `move`, is a number of represent the end of the crate represetation, or a newline character,
    # it has to be a representation of a crate
    # Crate ordering goes like this: Each stack is of len(3), then an empty character.
    if ''.join(line[0:4]) != 'move' and line[0] != '\n' and '1' not in line:
      for i in range(1, len(line)+1, 4):
        if line[i] != ' ':
          stacks[int((i-1)/4)].append(line[i])
    # 2. Otherwise, it is the newline character representing the beginning of the commands, reverse the stack so it's in the right order
    elif line[0] == '\n':
      for stack in stacks:
        stack.reverse()
    # 3. For each command, parse it and perform the correct action between the stacks
    elif ''.join(line[0:4]) == 'move':
      command = ''.join(line).strip().split(' ')
      # command[1] represents the quantity, command[3] represents the stack to move from, command[5] represents the stack to move to
      for i in range(int(command[1])):
        item = stacks[int(command[3])-1].pop()
        stacks[int(command[5])-1].append(item)

  for stack in stacks:
    top = stack.pop()
    top_ordering += top

  return top_ordering

#endregion

#region Part 2
from itertools import islice

def get_crate_ordering_multiple(input_file_name):
  # Similar to part 1, going to use a stack to keep track of the elements moving between stacks
  # However, need to move the entire slice of the stack at a time now, so going to import itertools and use the slice method from there
  
  input_file = open(input_file_name, 'r')
  top_ordering = ''
  stacks = [deque() for i in range(9)] # Hardcoded because the input is given ahead of time, otherwise it would be calculated if needed

  for line in input_file:
    line = list(line)
    # 1. If the line does not start with the keyword `move`, is a number of represent the end of the crate represetation, or a newline character,
    # it has to be a representation of a crate
    # Crate ordering goes like this: Each stack is of len(3), then an empty character.
    if ''.join(line[0:4]) != 'move' and line[0] != '\n' and '1' not in line:
      for i in range(1, len(line)+1, 4):
        if line[i] != ' ':
          stacks[int((i-1)/4)].append(line[i])
    # 2. Otherwise, it is the newline character representing the beginning of the commands, reverse the stack so it's in the right order
    elif line[0] == '\n':
      for stack in stacks:
        stack.reverse()
    # 3. For each command, parse it and perform the correct action between the stacks
    elif ''.join(line[0:4]) == 'move':
      command = ''.join(line).strip().split(' ')
      # command[1] represents the quantity, command[3] represents the stack to move from, command[5] represents the stack to move to
      # Going to grab all the items from the top of the stack to move from, and preserve the order
      items_to_move = list(islice(stacks[int(command[3])-1], len(stacks[int(command[3])-1]) - int(command[1]), len(stacks[int(command[3])-1])))
      for item in items_to_move:
        stacks[int(command[3])-1].pop()
        stacks[int(command[5])-1].append(item)

  for stack in stacks:
    top = stack.pop()
    top_ordering += top

  return top_ordering

#endregion

if __name__ == '__main__':
  crate_ordering = get_crate_ordering('input.txt')
  print('The final ordering on top is: ' + str(crate_ordering))

  crate_ordering_multiple = get_crate_ordering_multiple('input.txt')
  print('The final ordering on top with multiple is: ' + str(crate_ordering_multiple))