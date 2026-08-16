"""[LEARNING LOGS] สลากกินแบ่ง"""

real_char, real_num = input().split()
char, num = input().split()

if real_char == char and real_num == num:
    print("1000000")
elif real_num == num:
    print("100000")
elif real_char == char and real_num[2:4] == num[2:4]:
    print("2000")
elif real_char == char and real_num[3:4] == num[3:4]:
    print("1000")
elif real_num[2:4] == num[2:4]:
    print("200")
elif real_num[3:4] == num[3:4]:
    print("100")
elif real_char == char:
    print("20")
else:
    print("0")
