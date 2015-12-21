import itertools

hp =  109
damage =  8
armor_amt =  2


weapon = {}
armor = {}
ring = {}


def willWin(playerArmor, playerHP, playerDamage, monsterArmor, monsterHP, monsterDamage):
    turn = True
    while (playerHP > 0 and monsterHP > 0):
        if turn:
            monsterHP -= max(playerDamage - monsterArmor, 1)
        else:
            playerHP -= max(monsterDamage - playerArmor, 1)
        turn = not turn
    return not (monsterHP <= 0)
print willWin(5, 8, 5, 12, 7, 2)



with open('input21.txt') as f:
    for line in f:
        line = line.strip("\n").split(" ")
        if len(weapon) < 5:
            weapon[line[0]] = [int(line[1]), int(line[2]), int(line[3])]
        elif len(armor) < 5:
            armor[line[0]] = [int(line[1]), int(line[2]), int(line[3])]
        else:
            ring[line[0] + line[1]] = [int(line[2]), int(line[3]), int(line[4])]

minCost = 0

for x,o in weapon.iteritems():
    for y,p in armor.iteritems():
        for z in itertools.combinations(ring.keys(), 2):
            playerArmor = sum([ring[a][2] for a in z]) + o[2] + p[2]
            playerDamage = sum([ring[a][1] for a in z]) + o[1] + p[1]
            if (willWin(playerArmor, 100, playerDamage, armor_amt, hp, damage)):
                cost = o[0] + p[0] + sum([ring[a][0] for a in z]) 
                minCost = max(cost, minCost)
                if minCost == cost:
                    print x,y,z, cost

        for z,q in ring.iteritems():
            playerArmor = q[2] + o[2] + p[2]
            playerDamage = q[1] + o[1] + p[1]
            if (willWin(playerArmor, 100, playerDamage, armor_amt, hp, damage)):
                cost = o[0] + p[0] + q[0]
                minCost = max(cost, minCost)
        playerArmor = o[2] + p[2]
        playerDamage = o[1] + p[1]
        if (willWin(playerArmor, 100, playerDamage, armor_amt, hp, damage)):
            cost = o[0] + p[0]
            minCost = max(cost, minCost)
    playerArmor =  o[2]
    playerDamage = o[1] 
    if (willWin(playerArmor, 100, playerDamage, armor_amt, hp, damage)):
        cost = o[0]
        minCost = max(cost, minCost)
    for z,q in ring.iteritems():
        playerArmor = q[2] + o[2] 
        playerDamage = q[1] + o[1] 
        if (willWin(playerArmor, 100, playerDamage, armor_amt, hp, damage)):
            cost = o[0] +  q[0]
            minCost = max(cost, minCost)
    for z in itertools.combinations(ring.keys(), 2):
            playerArmor = sum([ring[a][2] for a in z]) + o[2] 
            playerDamage = sum([ring[a][1] for a in z]) + o[1] 
            if (willWin(playerArmor, 100, playerDamage, armor_amt, hp, damage)):
                cost = o[0] + sum([ring[a][0] for a in z]) 
                minCost = max(cost, minCost)
                if minCost == cost:
                    print x,y,z, cost


print minCost





