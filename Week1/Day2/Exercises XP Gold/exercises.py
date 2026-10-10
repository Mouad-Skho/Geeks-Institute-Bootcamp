month = int(input("What is the month? "))
if month in range(1,13):
    if month in range(3,5):
        print("Spring")
    elif month in range(6,8):
        print("Summer")

    elif month in range(9,11):
        print("Autumn")

    elif month in [12,1,2]:
        print("Winter")

else:
    print("type a valid month bettwen 1 to 12")
