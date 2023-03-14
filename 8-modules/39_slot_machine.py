# Slot Machine 🎰
# Codédex

import random

symbols = [
  '🍒',
  '🍇',
  '🍉',
  '7️⃣'
]

def play():
  results = random.choices(symbols, k=3)
  win = results[0] == '7️⃣' and results[1] == '7️⃣' and results[2] == '7️⃣'

  for i in range(50):    
    print(f'{results[0]} | {results[1]} | {results[2]}')
    win = results[0] == '7️⃣' and results[1] == '7️⃣' and results[2] == '7️⃣'

    if win:
      print("Jackpot!!! 💰")
      break
    else:
      results = random.choices(symbols, k=3)

answer = "Y"
while answer.upper() != "N":
  play()
  answer = input("Keep playing? (Y/N) ")

print("Thanks for playing!")