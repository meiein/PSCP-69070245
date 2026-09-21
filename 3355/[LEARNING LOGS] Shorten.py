""" [LEARNING LOGS] Shorten"""
mynum = []
text = int(input())
if text != -1:
    mynum.append(text)
    while text != -1:
        text = int(input())
        mynum.append(text)
        if text == -1:
            mynum.pop()
    result = []
    start = mynum[0]
    current = mynum[0]

    for i in range(1, len(mynum)):
        if mynum[i] == current +1 :
            current = mynum[i]
        else:
            if start == current:
                result.append(str(start))
            else:
                result.append(f"{start}-{current}")
            start = mynum[i]
            current = mynum[i]
    if start == current:
        result.append(str(start))
    else:
        result.append(f"{start}-{current}")
    print(", ".join(result))
else:
    print(" ")
