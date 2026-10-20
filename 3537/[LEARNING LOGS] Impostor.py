"""[LEARNING LOGS] Impostor"""
import json

member = {}
dead = {}

while True:
    okdata = input()
    if okdata == "Start":
        break
    data = json.loads(okdata)
    member.update(data)

outmember = {}

while True:
    voted = input()
    if voted == "End":
        break

    if voted in member:
        role = member.pop(voted)
        dead[voted] = role
        outmember[voted] = role

totalimpostor = 0

for i in member.values():
    if i == "Impostor":
        totalimpostor += 1

print(totalimpostor, "Impostor Remains")
print("***Alive***")
for name in sorted(member.keys()):
    print(f"{name} : {member[name]}")
print("***Dead***")
for name in sorted(dead.keys()):
    print(f"{name} : {dead[name]}")
