#region Part 1
def play_rps(input_file_name):
  # From the input file, each line represents a game of RPS played
  # For each line, calculate the result + number of points scored

  # 1. Initialize the variables and open the file
  total_score = 0
  input_file = open(input_file_name, 'r')

  # 2. Iterate over each line of the input file, and calculate the total score
  for line in input_file:
    # Each line in the file, calculate the score based on the inputs
    p1_play, p2_play = line.strip()[0], line.strip()[-1]
    # If p2_play == X, it's rock, and +1 points to the total
    # If p2_play == Y, it's paper, and +2 points to the total
    # If p2_play == Z, it's scissors, and +3 points to the total
    # Otherwise, its +0 for losses, +3 for ties, and +6 for wins
    if p2_play == 'X':
      if p1_play == 'A': # You are both rock
        total_score += (1 + 3)
      elif p1_play == 'B':
        total_score += 1 # You are rock and they are paper
      else:
        total_score += (1 + 6) # You are rock and they are scissors
    elif p2_play == 'Y':
      if p1_play == 'A':
        total_score += (2 + 6) # You are paper and they are rock
      elif p1_play == 'B':
        total_score += (2 + 3) # You are both paper
      else:
        total_score += 2 # You are paper and they are scissors
    elif p2_play == 'Z':
      if p1_play == 'A':
        total_score += 3 # You are scissors and they are rock
      elif p1_play == 'B':
        total_score += (3 + 6) # You are scissors and they are paper
      else:
        total_score += (3 + 3) # You are both scissors
  
  return total_score
#endregion

#region Part 2
def play_rps_rigged(input_file_name):
  # Similar to before, need to calculate the score for each round represented by a line in the input_file
  # However this time, need to use the second column to figure out what the result should be and calculate based off that

  # 1. Initialize the variables and open the file
  total_score_rigged = 0
  input_file = open(input_file_name, 'r')

  for line in input_file:
    # Each line in the file, calculate the score based on the inputs
    p1_play, expected_result = line.strip()[0], line.strip()[-1]
    if p1_play == 'A':
      if expected_result == 'X': # You need to lose, so be scissors
        total_score_rigged += 3
      elif expected_result == 'Y':
        total_score_rigged += (1 + 3) # You need to tie, so be rock
      else:
        total_score_rigged += (2 + 6) # You need to win, so be paper
    elif p1_play == 'B':
      if expected_result == 'X':
        total_score_rigged += 1 # You need to lose, so be rock
      elif expected_result == 'Y':
        total_score_rigged += (2 + 3) # You need to tie, so be paper
      else:
        total_score_rigged += (3 + 6) # You need to win, so be scissors
    elif p1_play == 'C':
      if expected_result == 'X':
        total_score_rigged += 2 # You need to lose, so be paper
      elif expected_result == 'Y':
        total_score_rigged += (3 + 3) # You need to tie, so be scissors
      else:
        total_score_rigged += (1 + 6) # You need to win, so be rock

  return total_score_rigged

#endregion

if __name__ == '__main__':
  total_score = play_rps('input.txt')
  print('Total score is: ' + str(total_score))
  total_score_rigged = play_rps_rigged('input.txt')
  print('Total rigged score is: ' + str(total_score_rigged))