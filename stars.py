import os
import time
import random

# constants that control the behaviour of the stars
DELAY = 0.3
DENSITY = 0.8

os.system('cls' if os.name == 'nt' else 'clear')

# arrays to store stars and colours
stars = [u"✦", u"✧", u"*", u"☄"]
colours = ['\033[31m', '\033[32m', '\033[33m', '\033[35m', '\033[36m', '\033[37m']

# store the number of columns of the terminal
t_w = os.get_terminal_size()[0]

def make_row():
  # generate each row to print by randomly selecting stars from the array
  row = []
  for _ in range(t_w//2):
    # append random star based on a predefined density
    if(random.random() < DENSITY):
      # randomly append a star with a random colour
      row.append(random.choice(colours) + random.choice(stars))
    else:
      row.append(' ')

  print(*row, end='', flush=True)
  time.sleep(DELAY)
  print("\n")
  # reset the row
  row = []

while True:
  make_row()