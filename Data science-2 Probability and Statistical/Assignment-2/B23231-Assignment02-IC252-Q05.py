import random
import numpy as np
import matplotlib.pyplot as plt

print("Monty Hall problem")
print(" ")
print("You are provided with 3 doors.")
print("Behind one of 3 there is prize and in other nothing")
print("You are having door named 1,2,3.")
 

# door=int(input("Enter the door number you like: "))
# if(door!=1 or door!=2 or door!=3):
#     print("Enter valid entry: ")
#     door=int(input("Enter the door number you like: "))

switch_wins=0
stick_wins=0

for i in range(10000):
    choices=[0,0,0]
    reward_gate=random.randint(1,3)
    choices[reward_gate-1]=1

    door_opened=random.randint(1,3)
    
    #Firtsly say it remained fixed
    if(choices[door_opened-1] == 1 and choices[reward_gate - 1] == 1):
        stick_wins=stick_wins+1
    else:
        switch_wins=switch_wins+1

print("The host opened one door from other two left door and it contains no price every time") 
stick_probability = stick_wins / 10000
switch_probability = switch_wins / 10000
    

labels = ["Stick to initial Choice", "Switching the Doors"]
scenario = [stick_probability, switch_probability]

plt.bar(labels, scenario, color=["blue", "red"])
plt.title("Monty Hall Problem")
plt.ylabel("Probability of winning respectively")
plt.yticks(np.arange(0, 1.1, 0.1))
plt.savefig("monty_hall_graph.png")
plt.show()