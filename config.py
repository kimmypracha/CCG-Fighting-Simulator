class usr_conf:
    atk_skill = [('normal', 500, 20), ('special', 750, 40)]
    def_skill = [('shield', 400, 30)]
    max_hp = 1000
    mana_trigger = True # mana increase when attacked
    mana_gain = 10 # mana gained from damaging
    perf_data = "data/weekly-contest-245_sec.csv"

    
class game_conf:
    n_task = 3
    time_limit = 1800 # seconds
    display_mode = False
    mana_gain = [30, 40 , 60] # mana gain from completing the task
    
    