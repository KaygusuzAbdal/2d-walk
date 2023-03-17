import random

def start_walking(total_steps=500):
 x = 0
 y = 0
 
 positions = [x, y]
 timepoints = list(range(0, total_steps+1))
 
 for number in range(1, total_steps + 1):
 possibility = random.randint(1, 10)
 if possibility <= 2:
 #left
 x -= 1
 elif 4 >= possibility > 2:
 #right
 x += 1
 elif 9 >= possibility > 4:
 #up
 y += 1
 else:
 #down
 y -= 1
 positions.append([x/10, y/10])
 return timepoints, positions
time_points, positions = start_walking(500)
print(time_points)
print(positions)
print(positions[500])
