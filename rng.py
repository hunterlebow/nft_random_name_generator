#Author: Hunter Lebow
import random
#Adjust k value to determine number of random generations.  
# An optimized k hyperparameter should not be greater than the length of the largest TXT file to avoid repeats.
k = 20
'''Open TXT Files'''
with open('adj.txt') as f:
    adj = f.read().splitlines()
    rand_adj = random.choices(adj, k = k)

with open ('all_animals.txt') as ff:
    anmls = ff.read().splitlines()
    rand_anmls = random.choices(anmls, k = k)

with open ('club.txt') as fff:
    clb = fff.read().splitlines()
    rand_clb = random.choices(clb, k = k)


'''Random NFT Name Generator'''
for (adj, anml, clb) in zip(rand_adj, rand_anmls, rand_clb):
    nft_name = f'{adj} {anml} {clb} Club'
    print(nft_name.title())

'''Close TXT Files'''
f.close()
ff.close()
fff.close()