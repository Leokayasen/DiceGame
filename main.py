import random
import time

def RollTheDice():
  input("Start the round? Y/N \n")
  score = 0
  diceA = random.randint(1,6)
  diceB = random.randint(1,6)
  total = diceA + diceB
  if total % 2 == 0:
    score = total + 10

  else:
    score = total - 5

# If both diceA and diceB roll the same numbers
#Extra roll will be triggered and a new roll for diceA will happen
  if diceA == diceB:
    print("Extra Roll!")
    diceA = random.randint(1,6)
  
  if score < 0:
    score = 10
  print("1st Dice: ",diceA)
  print("2nd Dice: ",diceB)
  print("Score: ",score)
  print("--------------------")
  time.sleep(1)
  return score

def Tiebreaker():
  print("Tiebreaker")
  input('P1 - Press Enter')
  P1Score = random.randint(1,6)
  print("P1 Score is", P1Score)
  input('P2 - Press Enter')
  P2Score = random.randint(1,6)
  print("P2 Score is", P2Score)
  while P1Score == P2Score:
    if P1Score < P2Score:
      P1Score = random.randint(1,6)
      print("P2 Wins")
      P2Score = random.randint(1,6)
      print("The scores are:",("P1:",P1Score,("P2:",P2Score)))
    else:
      print("P1 wins!")

#Main Program
#2 Players
P1Score = 0
P2Score = 0
for i in range(1,6):
  print("Round: ", i, " " "Player: 1")
  P1Score = P1Score + RollTheDice()

for i in range(1,2):
  print("Round: ", i, " " "Player: 2")
  P2Score = P2Score + RollTheDice()

print("Final Scores:")
print("Player 1 - ",P1Score,"Points")
print("Player 2 - ",P2Score,"Points")

if P1Score == P2Score:
  Tiebreaker()
elif P1Score > P2Score:
  print("Player 1 wins!")
else:
  print("Player 2 wins!")
