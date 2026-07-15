"""[LEARNING LOGS] Season"""

month = int(input())
day = int(input())

def main():
    """Condition of seasons"""
    if month == 3 and day >= 21:
        print("spring")
    elif month == 6 and day >= 21:
        print("summer")
    elif month == 9 and day >= 21:
        print("fall")
    elif month == 12 and day >= 21:
        print("winter")

    elif 1 <= month <= 3 :
        print("winter")
    elif 4 <= month <= 6 :
        print("spring")
    elif 7 <= month <= 9 :
        print("summer")
    elif month >= 10:
        print("fall")
main()
