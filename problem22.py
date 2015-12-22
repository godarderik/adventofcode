import copy
import random

f = open("input22.txt")


spells = {}
spells["magic_missile"] = [53,4,0]
spells["drain"] = [73,2,2]
spells["shield"] = [113,0,0]
spells["poison"] = [173,0,0]
spells["recharge"] = [229,0,0]



class Stack:
    "A container with a last-in-first-out (LIFO) queuing policy."
    def __init__(self):
        self.list = []

    def push(self,item):
        "Push 'item' onto the stack"
        self.list.append(item)

    def pop(self):
        "Pop the most recently pushed item from the stack"
        return self.list.pop()

    def isEmpty(self):
        "Returns true if the stack is empty"
        return len(self.list) == 0


def updateSpells(gameState):
    if gameState["shield_active"] > 0:
        gameState["shield_active"] -= 1
        gameState["player_armor_bonus"] = 7
    elif gameState["shield_active"] == 0:
        gameState["player_armor_bonus"] = 0

    if gameState["poison_active"] > 0:
        gameState["poison_active"] -= 1
        gameState["monster_hp"] -= 3
    if gameState["recharge_active"] > 0:
        gameState["recharge_active"] -= 1
        gameState["player_mana"] += 101
    return gameState

def checkDeath(gameState):
    if gameState["player_hp"] <= 0:
        gameState["winner"] = "monster"
    elif gameState["monster_hp"] <= 0:
        gameState["winner"] = "player"
    return gameState
     #potential bug here


def stepPlayer(gameState, spell):
    gameState["player_hp"] -= 1
    updatedGameState = checkDeath(gameState)
    if gameState["winner"] != None:
        return gameState
    gameState = updateSpells(gameState)
    updatedGameState = checkDeath(gameState)
    if gameState["winner"] != None:
        return gameState
    if gameState["player_mana"] < 53:
        gameState["winner"] = "monster"
        return gameState

    if spell == "magic_missile" and gameState["player_mana"] >= 53:
        gameState["player_mana"] -= 53
        gameState["player_mana_spent"] += 53
        gameState["monster_hp"] -= 4
    elif spell == "drain" and gameState["player_mana"] >= 73:
        gameState["player_mana"] -= 73
        gameState["player_mana_spent"] += 73
        gameState["monster_hp"] -= 2
        gameState["player_hp"] += 2
    elif spell == "shield" and gameState["shield_active"] == 0 and gameState["player_mana"] >= 113:
        gameState["player_mana"] -= 113
        gameState["player_mana_spent"] += 113
        gameState["shield_active"] = 6
    elif spell == "poison" and gameState["poison_active"] == 0 and gameState["player_mana"] >= 173:
        gameState["player_mana"] -= 173
        gameState["player_mana_spent"] += 173
        gameState["poison_active"] = 6 
    elif spell == "recharge" and gameState["recharge_active"] == 0 and gameState["player_mana"] >= 229:
        gameState["player_mana"] -= 229
        gameState["player_mana_spent"] += 229
        gameState["recharge_active"] = 5 
    else:
        gameState["winner"] = "monster"
    
    
    updatedGameState = checkDeath(gameState)
    return updatedGameState

def stepMonster(gameState):
    gameState = updateSpells(gameState)
    updatedGameState = checkDeath(gameState)
    if gameState["winner"] != None:
        return gameState
    gameState["player_hp"] -= max(gameState["monster_damage"] - gameState["player_armor_bonus"], 1)
    updatedGameState = checkDeath(gameState)
    return updatedGameState

def generateSuccessors(gameState):
    for z in spells.keys():
        a = gameState.copy()
        b = stepPlayer(a,z)
        if b["winner"] == "player":
            yield b
        elif b["winner"] == None:
            x = stepMonster(b)
            if x["winner"] != "monster" and x["player_mana_spent"] < 2200:
                yield x
def problema():

    queue = Stack()
    gameState = {}
    gameState["player_hp"] = 50
    gameState["player_mana"] = 500
    gameState["player_mana_spent"] = 0
    gameState["player_armor_bonus"] = 0
    gameState["monster_hp"] = 71
    gameState["monster_damage"] = 10
    gameState["shield_active"] = 0
    gameState["poison_active"] = 0
    gameState["recharge_active"] = 0
    gameState["winner"] = None
    gameState["moves"] = []
    queue.push(gameState)

    minCost = 9999999
    count = 0
    while not queue.isEmpty():
        state = queue.pop()
        if state["winner"] == "player":
            minCost = min(minCost, state["player_mana_spent"])
            print state
        else:
            for x in generateSuccessors(state):
                queue.push(x)
    return minCost

print problema()

    
