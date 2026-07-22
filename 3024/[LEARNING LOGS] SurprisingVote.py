"""[LEARNING LOGS] SurprisingVote"""
score = float(input())
top = float(input())
left = score - top
mininum = left - top
if mininum > top:
    mininum = top
elif mininum < 0:
    mininum = 0
if top - mininum > 2:
    print("Surprising")
else:
    print("Not surprising")
  
