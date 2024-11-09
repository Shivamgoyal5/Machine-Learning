import pandas as pd
import matplotlib.pyplot as plt
import numpy as np

text = ''
with open("C:\\Users\\shiva\\OneDrive\\Desktop\\B23231-Assignment05-IC252\\fileA-TimeMachine.txt", 'r', encoding='utf-8') as file:
    text += file.read().strip()

text = text.replace('\n', ' ')
words = text.split()

# Part A
word_freq = {}
for word in words:
    word_freq[word] = word_freq.get(word, 0) + 1

df = pd.DataFrame(word_freq.items(), columns=['Word', 'Frequency'])
df = df.sort_values(by='Frequency', ascending=False).reset_index(drop=True)
df['Probability'] = df['Frequency'] / df['Frequency'].sum()

freq_bins = np.linspace(0, 1, 10)
plt.hist(df['Probability'], bins=freq_bins, density=True)
plt.xlabel('Probability')
plt.ylabel('Number of Words')
plt.title('Probability Distribution of Word Frequency')
plt.show()

# Part B

letters_only = ''.join([c.lower() for c in text if c.isalpha()])
pairs = [letters_only[i:i+2] for i in range(len(letters_only) - 1)]
pair_freq = {}

for pair in pairs:
    pair_freq[pair] = pair_freq.get(pair, 0) + 1

df = pd.DataFrame(pair_freq.items(), columns=['Pair', 'Frequency'])
df = df.sort_values(by='Frequency', ascending=False).reset_index(drop=True)
df['Probability'] = df['Frequency'] / df['Frequency'].sum()

print("Igonring punctuation and white space:")
print(df.head(10))

# Part C
letters_and_space = ''.join([c.lower() for c in text if c.isalpha() or c.isspace()])
pairs = [letters_and_space[i:i+2] for i in range(len(letters_and_space) - 1)]
pair_freq = {}

for pair in pairs:
    pair_freq[pair] = pair_freq.get(pair, 0) + 1

df = pd.DataFrame(pair_freq.items(), columns=['Pair', 'Frequency'])
df = df.sort_values(by='Frequency', ascending=False).reset_index(drop=True)
df['Probability'] = df['Frequency'] / df['Frequency'].sum()

print("Including white space:")
print(df.head(10))