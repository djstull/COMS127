L = [1,2,3,4,5,6,7,8,9,10]

for i in L:
    print(i)

a=0
for i in L:
    a = a + i
print(a)
        
for i in L:
    print("Death to the stormcloaks!")

cocopuffs = ["I'm", "Coo", "Coo", "for", "Coco", "Puffs!"]

for puffs in cocopuffs:
    print(puffs)

name = "Leeroy Jenkins"
for c in name:
    print(c)

word = "Here comes dat boi"

count = 0
for e in word:
    if e == "e":
        count += 1
    print(word, "has", count, "e's")