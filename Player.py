import random
from config import usr_conf, game_conf
import pandas as pd 

def perf_sampling():
    data = pd.read_csv(usr_conf.perf_data)
    data = data.sample(frac=0.5)
    cols = [f"p{i}_time" for i in range(1,game_conf.n_task+1)]
    data.columns = data.columns.str.strip()
    data = data[cols]
    data.fillna(game_conf.time_limit)
    perf = []
    for i in range(1,game_conf.n_task+1):
        perf.append([(200 + 200*i, x) for x in data[f"p{i}_time"] if x < game_conf.time_limit])
    return perf

class Player:
    def __init__(self, name = "anon", display_mode = False): # data maybe ?
        self.name = name
        self.hp = usr_conf.max_hp
        self.mana = 0
        self.score = 0
        self.atk_skill = usr_conf.atk_skill
        self.def_skill = usr_conf.def_skill # use only when got attacked
        self.problem = perf_sampling()
        self.display_mode = display_mode
        self.task = [x for x in range(len(self.problem))]

    def reset(self):
        self.hp  = usr_conf.max_hp
        self.mana = 0
        self.score = 0
        self.task = [x for x in range(len(self.problem))]

    def next_action(self,t):
        action = []
        if len(self.task) > 0 :
            action.append("code")
        
        atk_choice = list(
            filter(
                lambda skill: skill[2] <= self.mana
                , self.atk_skill
            )
        )
        #print(self.mana, atk_choice)
        if len(atk_choice) > 0:
            action.append("attack")
        if len(action) == 0:
            action.append("nothing")
        choose = random.choice(action)
        #print(choose)
        if choose == "code":
            no_task = random.choice(self.task)
            score, time = random.choice(self.problem[no_task])
            return {
                "action" : "code",
                "time" : t+time,
                "execute" : lambda x : self.code(score, time, no_task)
            }
        elif choose == "attack":
            name, atk, mana = random.choice(self.atk_skill)
            return {
                "action" : "attack",
                "time" : t+2,
                "execute": lambda x : self.attack(atk, mana, x)
            }
        else:
            return {
                "action" : "wait",
                "time" : 999999, # signal number for giving up at the moment
                "execute" : None 
            }

    def attack(self, atk, mana, enemy):
        if self.mana < mana: 
            if self.display_mode:
                print(f"{self.name} have not enough mana to use the attack")
            return False
        self.mana -= mana
        if self.display_mode:
            print(f"{self.name} attack {enemy.name} with {atk} damage!")
            print(f"{self.name} used {mana} MP.")
            print(f"{self.name} have {self.mana} MP left.")
        enemy.damaged(atk)
        return True

    def damaged(self, atk):
        action = ["nothing"]
        def_choice = list(
            filter(
                lambda skill: skill[2] <= self.mana
                , self.def_skill
            )
        )
        if len(def_choice) > 0 :
            action.append("def")
        choose = random.choice(action)
        if choose == "nothing":
            if self.display_mode:
                print(f"{self.name} take a full damage!")
            self.hp = max(self.hp- atk,0)
            if usr_conf.mana_trigger :
                self.mana += usr_conf.mana_gain
        else:
            name, df, mana = random.choice(def_choice)
            self.hp = max(self.hp - max(atk-df, 0),0)
            self.mana -= mana
            if self.display_mode:
                print(f"{self.name} blocked the attack!")
                print(f"{self.name} used {mana} MP.")
                print(f"{self.name} have {self.mana} MP left.")
    
    def code(self, score, time, no_task):
        self.task = [x for x in self.task if x != no_task]
        self.mana += game_conf.mana_gain[no_task]
        if self.display_mode:
                print(f"{self.name} has gained {game_conf.mana_gain[no_task]} MP!")
                print(f"{self.name} have {self.mana} MP.")
        return True
