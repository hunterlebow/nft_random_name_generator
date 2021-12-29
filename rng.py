#Author: Hunter Lebow
import random
import csv
#Adjust k value to determine number of random generations.  
# An optimized k hyperparameter should not be greater than the length of the largest TXT file to avoid repeats.
k = 20

with open('adj.txt') as f:
    adj = f.read().splitlines()
    rand_adj = random.choices(adj, k = k)

with open ('all_animals.txt') as ff:
    anmls = ff.read().splitlines()
    rand_anmls = random.choices(anmls, k = k)

with open ('club.txt') as fff:
    clb = fff.read().splitlines()
    rand_clb = random.choices(clb, k = k)

records = [f'{a} {b} {c} Club' for (a, b, c) in zip(rand_adj, rand_anmls, rand_clb)]
for i in range(len(records)):
    records[i] = records[i].title()
master = [row for row in enumerate(records)]   

with open('output.csv', 'w', encoding = 'UTF8', newline = '') as output:
    writer = csv.writer(output)
    writer.writerows(master)
    output.close()

f.close()
ff.close()
fff.close()
