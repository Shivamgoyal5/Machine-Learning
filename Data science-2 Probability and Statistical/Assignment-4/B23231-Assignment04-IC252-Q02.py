import numpy as np
from matplotlib import pyplot as plt
import statistics
import random
import math
from mpl_toolkits.mplot3d import Axes3D
# We define two RV's X(no of LED chosen)={0,1,2} and Y(no of defective bulbs chosen)={0,1,2}
test_cases=10000
trials={}
trials["00"]=0
trials["01"]=0
trials["02"]=0
trials["10"]=0
trials["11"]=0
trials["12"]=0
trials["20"]=0
trials["21"]=0
trials["22"]=0
for i in range(test_cases):
    cases=["L","L","L","I","I"]
    trial=""
    t1=random.choice(cases)
    cases.remove(t1)
    if t1=="L":
        trial+="L"
        d=random.choices(["U","D"],weights=(95,5))
        trial+=d[0]
    else:
        trial+="I"
        d=random.choices(["U","D"],weights=(90,10))
        trial+=d[0]
    t2=random.choice(cases)
    if t2=="L":
        trial+="L"
        d=random.choices(["U","D"],weights=(95,5))
        trial+=d[0]
    else:
        trial+="I"
        d=random.choices(["U","D"],weights=(90,10))
        trial+=d[0]
    x=trial.count("L")
    y=trial.count("D")
    trials[str(x)+str(y)]+=1
for i in trials:
    trials[i]=trials[i]/test_cases
print(trials)
x = [0, 0, 0, 1,1,1,2,2,2]
y = [0,1,2,0,1,2,0,1,2]
z = [trials['00'], trials['01'], trials['02'], trials['10'], trials['11'], trials['12'], trials['20'], trials['21'], trials['22']]
fig = plt.figure()
ax = fig.add_subplot(111, projection='3d')
ax.scatter(x, y, z, c='b', marker='.')
ax.set_xlabel('X ')
ax.set_ylabel('Y ')
ax.set_zlabel('PXY(x,y)')
ax.set_title('Joint probability distribution')
plt.show()
#b)
print("Marginal probability for X=0 is=",trials['00']+trials['01']+trials['02'])
print("Marginal probability for X=1 is=",trials['10']+trials['11']+trials['12'])
print("Marginal probability for X=2 is=",trials['20']+trials['21']+trials['22'])
print("Marginal probability for Y=0 is=",trials['00']+trials['10']+trials['20'])
print("Marginal probability for Y=1 is=",trials['01']+trials['11']+trials['21'])
print("Marginal probability for Y=2 is=",trials['02']+trials['12']+trials['22'])
#c)
plt.cla()
plt.clf()
plt.bar([0,1,2],[trials['00']+trials['01']+trials['02'],trials['10']+trials['11']+trials['12'],trials['20']+trials['21']+trials['22']])
plt.title("PMF of Random Variable X")
plt.xlabel("X")
plt.ylabel("PX(x)")
plt.show()
#d)
test_cases=10000
trials={}
trials["00"]=0
trials["01"]=0
trials["02"]=0
trials["10"]=0
trials["11"]=0
trials["12"]=0
for i in range(test_cases):
    cases=["L","L","L","I","I"]
    trial=""
    t1="I"
    cases.remove(t1)
    trial+="I"
    d=random.choices(["U","D"],weights=(90,10))
    trial+=d[0]
    t2=random.choice(cases)
    if t2=="L":
        trial+="L"
        d=random.choices(["U","D"],weights=(95,5))
        trial+=d[0]
    else:
        trial+="I"
        d=random.choices(["U","D"],weights=(90,10))
        trial+=d[0]
    x=trial.count("L")
    y=trial.count("D")
    trials[str(x)+str(y)]+=1
for i in trials:
    trials[i]=trials[i]/test_cases
print("Conditional probability to get 1 defective bulb or Y=1 is=",trials['01']+trials['11'])
#e)
print("No the events X and Y are not independent as clearly PX(x)*PY(y)!=PXY(x,y). They still wont be independent after replacement as the probability of getting a defective bulb changes with choosing an LED or Incandescent")
trials={}
trials["00"]=0
trials["01"]=0
trials["02"]=0
trials["10"]=0
trials["11"]=0
trials["12"]=0
trials["20"]=0
trials["21"]=0
trials["22"]=0
for i in range(test_cases):
    cases=["L","L","L","I","I"]
    trial=""
    t1=random.choice(cases)
    if t1=="L":
        trial+="L"
        d=random.choices(["U","D"],weights=(95,5))
        trial+=d[0]
    else:
        trial+="I"
        d=random.choices(["U","D"],weights=(90,10))
        trial+=d[0]
    t2=random.choice(cases)
    if t2=="L":
        trial+="L"
        d=random.choices(["U","D"],weights=(95,5))
        trial+=d[0]
    else:
        trial+="I"
        d=random.choices(["U","D"],weights=(90,10))
        trial+=d[0]
    x=trial.count("L")
    y=trial.count("D")
    trials[str(x)+str(y)]+=1
for i in trials:
    trials[i]=trials[i]/test_cases
x = [0, 0, 0, 1,1,1,2,2,2]
y = [0,1,2,0,1,2,0,1,2]
z = [trials['00'], trials['01'], trials['02'], trials['10'], trials['11'], trials['12'], trials['20'], trials['21'], trials['22']]
fig = plt.figure()
ax = fig.add_subplot(111, projection='3d')
ax.scatter(x, y, z, c='b', marker='.')
ax.set_xlabel('X ')
ax.set_ylabel('Y ')
ax.set_zlabel('PXY(x,y)')
ax.set_title('Joint probability distribution with Replacement')
plt.show()
print("Marginal probability for X=0 with replacement is=",trials['00']+trials['01']+trials['02'])
print("Marginal probability for X=1 with replacement is=",trials['10']+trials['11']+trials['12'])
print("Marginal probability for X=2 with replacement is=",trials['20']+trials['21']+trials['22'])
print("Marginal probability for Y=0 with replacement is=",trials['00']+trials['10']+trials['20'])
print("Marginal probability for Y=1 with replacement is=",trials['01']+trials['11']+trials['21'])
print("Marginal probability for Y=2 with replacement is=",trials['02']+trials['12']+trials['22'])
#g)
plt.cla()
plt.clf()
plt.bar([0,1,2],[trials['00']+trials['01']+trials['02'],trials['10']+trials['11']+trials['12'],trials['20']+trials['21']+trials['22']])
plt.title("PMF of Random Variable X with Replacement")
plt.xlabel("X")
plt.ylabel("PX(x)")
plt.show()
print("Obviously the PMF of X will change as after the first pull the second pull has its probability changed for getting a LED from 2/4 or 3/4 to 3/5 again")
