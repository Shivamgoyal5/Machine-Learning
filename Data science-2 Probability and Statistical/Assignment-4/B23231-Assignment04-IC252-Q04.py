#PART a
import seaborn
import random
from matplotlib import pyplot as plt
import numpy as np
import pandas as pd
from scipy.stats import norm
import statistics as st
x= np.arange(0,3,0.04)
y1=norm.pdf(x,1,0.5)
y2=norm.pdf(x,1.5,0.75)
plt.plot(x,y1,label="AM")
plt.plot(x,y2,label="FM")
plt.show()


#PART b
#As both events are independent the condition dosen't change anything
y1=np.random.normal(1.5,0.75,100)
success=0
for i in y1:
    if i<1:
        success+=1
print("Prob that repair time taken for FM will be less than 1 hour given AM takes 2 hours is=",success/100)


#PART c
y1=np.random.normal(1.5,0.75,100)
y2=np.random.normal(1,0.5,100)
y=y1+y2
print("Sum of 100 AM's and FM's is=",sum(y))


#PART d
plt.hist(y,bins="auto")
plt.show()
print("Mean of T's is=",st.mean(y))
print("Standard deviation of T's is=",st.stdev(y))
