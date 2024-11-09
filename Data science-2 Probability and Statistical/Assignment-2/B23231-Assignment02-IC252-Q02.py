import numpy as np
import matplotlib.pyplot as plt

print("Stirlings method")


factorial=[]

for i in range(1,21):
    result=1
    for j in range(1,i+1):
        result=result*j
    factorial.append(result)    
factorial_array= np.array(factorial)
n=np.arange(1,21)

# Stirling's approximation formula for factorial
stirlings_approximation=np.sqrt(2 * np.pi * n) * ((n/ np.e) ** n)

result=factorial_array/stirlings_approximation

list1=list(range(1,21))

plt.plot(list1,result)
plt.xlabel("K values")
plt.ylabel("Ratio")
plt.title("Ratio of factorial by simple method to stirling")
plt.grid(True)
plt.savefig("Stirlings.png")

plt.xticks(np.arange(1, 21, 1))

plt.show()






