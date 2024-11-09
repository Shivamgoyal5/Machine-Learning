import numpy as np
import pandas as pd
from matplotlib import pyplot as plt
condition=np.zeros((3,3))
testcases=100000
for x in range(testcases):
    weather=np.random.choice(["rainy","sunny","cloudy"])
    garment=np.random.choice(["tshirt","sweater","jacket"])
    if weather=="rainy":
        if garment=="tshirt":
            condition[0][0]+=1
        elif garment=="sweater":
            condition[0][1]+=1
        elif garment=="jacket":
            condition[0][2]+=1
    elif weather=="sunny":
        if garment=="tshirt":
            condition[1][0]+=1
        elif garment=="sweater":
            condition[1][1]+=1
        elif garment=="jacket":
            condition[1][2]+=1
    if weather=="cloudy":
        if garment=="tshirt":
            condition[2][0]+=1
        elif garment=="sweater":
            condition[2][1]+=1
        elif garment=="jacket":
            condition[2][2]+=1
condition=condition/testcases
df=pd.DataFrame(condition.tolist(),index=["Rainy","Sunny","Cloudy"],columns=["Tshirt","Sweater","Jacket"])
print(df)
Marginal_Garment=[condition[0][0]+condition[1][0]+condition[2][0],condition[0][1]+condition[1][1]+condition[2][1],condition[0][2]+condition[1][2]+condition[2][2]]
Marginal_Weather=[condition[0][0]+condition[0][1]+condition[0][2],condition[1][0]+condition[1][1]+condition[1][2],condition[2][0]+condition[2][1]+condition[2][2]]
plt.bar(["Tshirt","Sweater","Jacket"],Marginal_Garment)
plt.title("Marginal distribution of Garments")
plt.xlabel("Garment")
plt.ylabel("Probability")
plt.show()
plt.bar(["Rainy","Sunny","Cloudy"],Marginal_Weather)
plt.title("Marginal distribution of Weather")
plt.xlabel("Weather")
plt.ylabel("Probability")
plt.show()
condition2=condition.copy()
for x in range(3):
    for y in range(3):
        condition[x][y]=(condition2[x][y])/(condition2[x][0]+condition2[x][1]+condition2[x][2])
df=pd.DataFrame(condition.tolist(),index=["Given Rainy","Given Sunny","Given Cloudy"],columns=["Tshirt","Sweater","Jacket"])
print(df)