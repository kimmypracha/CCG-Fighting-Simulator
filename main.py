import random
from Player import Player
from Game import CodeConquerorGame as ccg
from config import game_conf
userList = [Player(name = "A" + str(i), 
                   display_mode = game_conf.display_mode)
                  for i in range(100)]
game = ccg(userList)
silent_table = []
# simulation 
for i in range(10000):
    game.play()
    silent_table += game.compute_silent()
print("============================================")
mn = min(silent_table)
mx = max(silent_table)
avg = sum(silent_table)//len(silent_table)
print(f"Minimum Silent Time : {mn//60}m {mn%60}s")
print(f"Maximum Silent Time : {mx//60}m {mx%60}s")
print(f"Average Silent Time : {avg//60}m {avg%60}s")
print("============================================")
mn = min(game.end_time)
mx = max(game.end_time)
avg = sum(game.end_time)//len(game.end_time)
print(f"Minimum End Time : {mn//60}m {mn%60}s")
print(f"Maximum End Time : {mx//60}m {mx%60}s")
print(f"Average End Time : {avg//60}m {avg%60}s")
print("============================================")
print(f"Give up Match (No move left) : {game.nomove_cnt}")
print(f"Time up Match : {game.timeup_cnt}")





        
