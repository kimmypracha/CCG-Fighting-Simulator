import random
from config import game_conf
class CodeConquerorGame:
    def __init__(self, userList):
        self.timeup_cnt = 0
        self.nomove_cnt = 0
        self.nodeath_cnt = 0
        self.history_table = []
        self.display_mode = game_conf.display_mode
        self.userList = userList
        self.intense_time = []
        self.end_time = []
        self.p1_hold = None
        self.p2_hold = None
        pass

    def reset(self):
        self.intense_time = []
        self.p1_hold = None
        self.p2_hold = None

    def play(self):
        self.reset() # reset logger
        players = random.sample(self.userList, 2)
        p1, p2 = players[0], players[1] # edit this later
        t = 0
        while p1.hp > 0 and p2.hp > 0 and t < game_conf.time_limit:
            nt = self.action(p1,p2, t) # dead air calculation in action method
            if nt == 999999 : # if both are giving up (have no move left)
                self.nomove_cnt += 1
                break
            t = nt 
        if t >= game_conf.time_limit:
            if game_conf.display_mode:
                print("Time Up!")
            self.timeup_cnt += 1
            if min(p1.hp,p2.hp) > 0:
                self.nodeath_cnt += 1
        elif min(p1.hp,p2.hp) > 0: #both giving up 
            self.nomove_cnt += 1
            

        #self.announce_result(p1,p2)
        if game_conf.display_mode:
            print(f"{p1.name}'s HP : ",p1.hp)
            print(f"{p2.name}'s HP : ",p2.hp)
            print(f"Time: {t//60} min {t%60} sec")
        self.end_time.append(t)
        p1.reset()
        p2.reset()
    
    def action(self, p1, p2, t):
        success = False
        p1_plan =  self.p1_hold if self.p1_hold else p1.next_action(t)
        p2_plan = self.p2_hold if self.p2_hold else p2.next_action(t)
        if p1_plan["time"] <= p2_plan["time"]:
            if p1_plan["action"] != "wait" : 
                t1 = p1_plan["time"]
                if t1 >= game_conf.time_limit : 
                    return game_conf.time_limit
                if game_conf.display_mode:
                    print(f"======== {t1//60} : {t1%60} ==========")
                success = p1_plan["execute"](p2)
            self.p1_hold = None 
            self.p2_hold = None if p2_plan["action"] == "wait" else p2_plan
            if p1_plan["action"] == "attack" and success:
                self.intense_time.append(p1_plan["time"])
            return p1_plan["time"]
        else:
            if p2_plan["action"] != "wait" :
                t2 = p2_plan["time"]
                if t2 >= game_conf.time_limit : 
                    return game_conf.time_limit
                if game_conf.display_mode:
                    print(f"======== {t2//60} : {t2%60} ==========")    
                success = p2_plan["execute"](p1)
            self.p1_hold = None if p1_plan["action"] == "wait" else p1_plan
            self.p2_hold = None
            if p2_plan["action"] == "attack" and success:
                self.intense_time.append(p2_plan["time"])
            return p2_plan["time"]
    
    def compute_silent(self):
        lst = []
        t = 0
        for time in self.intense_time:
            if time == t :
                continue
            if time-2-t <= 0:
                continue
            lst.append(time-2-t)
            t = time 
        if t < self.end_time[-1]: 
            lst.append(self.end_time[-1] - t)
        return lst