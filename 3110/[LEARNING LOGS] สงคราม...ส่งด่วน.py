"""[LEARNING LOGS] สงคราม...ส่งด่วน"""

place = input().split()
w = float(input())
if place[0] == "BKK":
    if place[1] == "CNX":
        print(f"{10 + (w * 30):.2f}")
    elif place[1] == "PKT":
        print(f"{25 + (w * 50):.2f}")
    else:
        print("Error")
elif place[0] == "CNX":
    if place[1] == "UBP":
        print(f"{15 + (w * 40):.2f}")
    else:
        print("Error")
elif place[0] == "UBP":
    if place[1] == "BKK":
        print(f"{20 + (w * 40):.2f}")
    elif place[1] == "PKT":
        print(f"{40 + (w * 70):.2f}")
    else:
        print("Error")
elif place[0] == "PKT":
    if place[1] == "CNX":
        print(f"{30 + (w * 60):.2f}")
    else:
        print("Error")
else:
    print("Error")
