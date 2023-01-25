#region Part 1 & Part 2
def get_signal_marker(input_file_name, signal_length):
  # Intuition: use a sliding window of size [signal_length] to check whether or not the signal has been received
  # Iterate through the input, and create left and right pointers to denote the window
  # For each window, convert the characters into a set, then check if len(set) == signal_length
  # If so, return the left pointer + signal_length

  input_file = open(input_file_name, 'r')
  left, right = 0, signal_length

  for buffer in input_file: # There is only one line this time
    while right < len(buffer):
      signal_set = set(list(buffer[left:right]))
      if len(signal_set) == signal_length:
        return left + signal_length
      left += 1
      right += 1

#endregion

if __name__ == '__main__':
  signal = get_signal_marker('input.txt', 4)
  print('The length from the start-of-packet is: ' + str(signal))

  msg_signal = get_signal_marker('input.txt', 14)
  print('The length from the start-of-m,essage is: ' + str(msg_signal))