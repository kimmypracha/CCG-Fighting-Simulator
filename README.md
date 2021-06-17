# CodeConqueror Game Simulator

## How to use 

```main.py``` :  Used as a command line interface simulator. It is more flexible and it could take less time than the notebook version. You can run the simulation by running this command.

``` 
python main.py
```

```summary.ipynb``` : The formal version of the simulator with the data visualization of the game factors such as the number of time-up match, etc. You can run the simulation by open this file on the Jupyter Notebook or run the following command.

```
jupyter notebook
```
And then open that file.


**Note : You need to restart the jupyter notebook kernel everytime you change the configuration.**

## Configuration 

1. ```usr_conf```
       
    This class is a configuration for a player in the simulation. 

    1.1 ```atk_skill``` : Contain the list of tuple (name, damage, mana). It could contain any amount of skills.

    1.2 ```def_skill``` : 
       Contain the list of tuple (name, defense power, mana ). It could contain any amount of skills.

    1.3 ```max_hp``` : 
       The maximum amount of HP that a player can have.

    1.4 ```mana_trigger```:
       If it is true, the mana will be increase when a player is attacked. Otherwise, False.

    1.5 ```mana_gain```: 
       the amount of mana gain when a player is damaged.

    1.6 ```perf_data```:
       the path for the csv file of task completion time in a contest. This data would be used to reference the performance of a programming contest participant by sampling the completion time.

2. game_conf
        this class is a configuration for the game system.
        
    2.1 ```n_task``` : the number of task 

    2.2 ```time_limit```: the time limit for a game in seconds.

    2.3 ```display_mode```: 
        If it is True, the simulation will print the action during the game (Attacking or Gainning Mana). Otherwise, it is False.

    2.4 ```mana_gain``` : This value is different to ```mana_gain``` in ```usr_conf```. It is the list of mana that players will get when they completed a task. A player will get mana respect to the order of task. (For example, if you complete 1st task, you will get mana equal to mana_gain[0].)




