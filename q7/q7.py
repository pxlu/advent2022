#region Part 1
# Helpers
class Element:

  def __init__(self, parent, name=None, size=0):
    self.name = name.strip()
    self.size = size
    self.children = []
    self.parent = parent

def parse_commands(input_file_name):

  # Iterate over the input_file, and keep track of the following:
  # 1. What is the current directory?
  # 2. What is inside the current directory? (file and other directories)
  # 3. What is the size of every element in the current directory?
  # To keep track of these things, need variables to hold them
  # The overall directories structure should be a object, with the attributes [name], [children], [parent] and [size]

  # After iterating over the entire input_file, then can traverse through the directories structure and calculate the number of directories with size > 100k
  input_file = open(input_file_name, 'r')
  current_directory, root = None, None

  for line in input_file:
    line = line.split(' ')
    # If it is a command, either [cd] or [ls]
    if line[0] == '$':
      # If it is [ls], then we know until we change directories, everything is part of the current_directory
      if line[1] == 'ls':
        continue
      # If it is [cd], then we know the current_directory is about to change
      elif line[1] == 'cd':
        # If current_directory is None, then we are at the root, create it
        if current_directory is None:
          new_root = Element(None, '/', 0)
          current_directory = new_root
          root = new_root
        # If the command is [..], then it means go up a directory, to it's parent
        elif line[2] == '..':
          if current_directory.parent is not None:
            current_directory = current_directory.parent
          else:
            print('Cannot go up a level, parent is None')
        # If the command is [/], then go all the way to the root
        elif line[2] == '/':
          current_directory = root
        else:
          for child in current_directory.children:
            if child.name == line[2].strip(): # line[3] is the name of the directory
              current_directory = child
              print('new current_dir: ' + current_directory.name)
    # If it is not a command, can only be a listing of directories and files
    else:
      for child in current_directory.children:
        if child.name == line[1]:
          break
      # If it starts with [dir], it is a directory, add it to the list of children of the current_directory if it doesn't exist
      if line[0] == 'dir':
          new_dir = Element(parent=current_directory, name=line[1], size=0)
          current_directory.children.append(new_dir)
      # It is a file, add it to the children of the current_directory if it doesn't exist
      else:
        new_file = Element(parent=current_directory, name=line[1], size=line[0])
        current_directory.children.append(new_file)

  for child in root.children:
    print(child.name)
    
#endregion

#region Part 2
#endregion

if __name__ == '__main__':
  signal = parse_commands('input.txt')
  print('The length from the start-of-packet is: ' + str(signal))