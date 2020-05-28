import random

boys = []
visited = []
with open("bois.txt","r") as file:
    for row in file:
    	boys.append(row)
              
boy = random.choice(boys)
if boy not in visited:
    visited.append(boy)
    print(boy)