import World
import threading
import time
import matplotlib.pyplot as plt

discount = 0.9
actions = World.actions
states = []
Q = {}
cpteur=0

for i in range(World.x):
    for j in range(World.y):
        states.append((i, j))

for state in states:
    temp = {}
    for action in actions:
        temp[action] = 0.1
    Q[state] = temp

for (i, j, c, w) in World.specials:
    for action in actions:
        Q[(i, j)][action] = w

print(Q)

def signal_arret(liste,thr):
	n,aux =len(liste),liste[n-1]
	
	for k in range(n,n-5,-1):
		listescores[k]

def do_action(action):
    s = World.player
    r = -World.score
    
    if action == actions[0]:
        World.try_move(0, -1)
    elif action == actions[1]:
        World.try_move(0, 1)
    elif action == actions[2]:
        World.try_move(-1, 0)
    elif action == actions[3]:
        World.try_move(1, 0)
    else:
        return
    s2 = World.player
    r += World.score
    return s, action, r, s2


def max_Q(s):
    val ,act= 0,0
    for a, q in Q[s].items():
        if val == 0 or (q > val):
            val , act = q,a
    return act, val


def inc_Q(s, a, alpha, inc):
    Q[s][a] = (1 - alpha)*Q[s][a] + alpha*inc


def run():
    global discount,cpteur
    time.sleep(1)
    alpha = 1
    t = 1
    while True:
        # Pick the right action
        s = World.player
        max_act, max_val = max_Q(s)
        (s, a, r, s2) = do_action(max_act)

        # Update Q
        max_act, max_val = max_Q(s2)
        inc_Q(s, a, alpha, r + discount * max_val)
        #print(Q)

        # Check if the game has restarted
        t += 1.0
        if World.has_restarted():
            World.restart_game()
            cpteur += 1
            time.sleep(0.001)
            t = 1.0

        # Update the learning rate
        alpha = pow(t, -0.001)

        # MODIFY THIS SLEEP IF THE GAME IS GOING TOO FAST.
        time.sleep(0.000001)


t = threading.Thread(target=run)
t.daemon = True
t.start()
World.start_game()


	
print(cpteur,World.listescores)
plt.close()
plt.plot(range(cpteur),World.listescores)
plt.show()


