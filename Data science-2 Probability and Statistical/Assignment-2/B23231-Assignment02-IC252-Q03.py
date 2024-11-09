import matplotlib.pyplot as plt


def factorial(n):
    if n ==0:
        return 1
    else:
        return n*factorial(n-1)


def card_flip_game(n):
    win = 0
    for i in range(1,n+1):
       win += ((-1)**(i+1))/factorial(i) 
    return win

n_values = list(range(2,101))
winning_probability = [card_flip_game(n) for n in n_values]
plt.plot(n_values,winning_probability)
plt.ylabel("Winning Probaility")
plt.xlabel("Value of n")
plt.savefig("q3plot.png")
plt.show()