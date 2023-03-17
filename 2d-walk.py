import random

def start_walking(total_steps=500):
 x = 0
 y = 0
 
 positions = [x, y]
 timepoints = list(range(0, total_steps+1))
 
 for number in range(1, total_steps + 1):
  possibility = random.randint(1, 10)
  
  if possibility <= 2:
   #left (possibility 20%)
   x -= 1
  elif 4 >= possibility > 2:
   #right (possibility 20%)
   x += 1
  elif 9 >= possibility > 4:
   #up (possibility 50%)
   y += 1
  else:
   #down (possibility 10%)
   y -= 1
  
  positions.append([x/10, y/10])
  return timepoints, positions

time_points, positions = start_walking(500)

print(time_points)
print(positions)
print(positions[500])
