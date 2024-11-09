import numpy as np
import matplotlib.pyplot as plt
def ProfA(x):
    return 1/(np.sqrt(2*3.14)*5)*np.exp(-0.5*((x-78)/5)**2)
def ProfB(x):
    return 1/(np.sqrt(2*3.14)*3)*np.exp(-0.5*((x-85)/3)**2)
x=np.arange(0,100,0.1)
plt.plot(x,ProfA(x),label='ProfA',color='b')
plt.plot(x,ProfB(x),label='ProfB',color='r')
plt.xlabel('Scores')
plt.ylabel('PDF')
plt.legend()
plt.grid()
plt.show()