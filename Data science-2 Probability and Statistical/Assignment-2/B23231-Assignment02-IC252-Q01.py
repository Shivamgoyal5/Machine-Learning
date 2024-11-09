#Birthday paradox
import matplotlib.pyplot as plt


list1=[]
for k in range(2,101):
    prob_no_shared_birthday = 1.0
    for i in range(k):
        prob_no_shared_birthday *= (365 - i) / 365
        prob_yes_shared_birthday=1-prob_no_shared_birthday
    list1.append(prob_yes_shared_birthday)    

group_sizes = list(range(2, 101))

print("The probability is as represented by graph")

plt.plot(group_sizes,list1)
plt.title('Probability of at least one shared birthday')
plt.xlabel("Value of k")
plt.ylabel("Probabilities")
plt.grid(True)
plt.savefig("birthdayparadox.png")
plt.show()

