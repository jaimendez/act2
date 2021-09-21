prelims = int(input("Enter Prelims grade: "))
midterm = int(input("Enter Midterm grade: "))
semis = int(input("Enter Semi Finals Grade: "))
finals = int(input("Enter Finals Grade: "))

avg = (prelims + midterm + semis + finals)/4

passing = 75

if avg >= passing :

    if avg >= 98:
        print(avg)
        print("Grade : A")
        print("You Passed")

    elif avg >= 90 and avg <99:
        print(avg)
        print("Grade : B")
        print("You Passed")

    elif avg >= 90 and avg <99:
        print(avg)
        print("Grade : B")
        print("You Passed")

    elif avg >= 80 and avg <90:
        print(avg)
        print("Grade : C")
        print("You Passed")

    elif avg >= 75 and avg <80:
        print(avg)
        print("Grade : D")
        print("You Passed")

else:

    elif avg >= 71 and avg <75:
        print(avg)
        print("Grade : D")
        print("You're a Failure")

    elif avg >= 61 and avg <71:
        print(avg)
        print("Grade : E")
        print("You're a Failure")  

    elif avg <= 60:
        print(avg)
        print("Grade : F")
        print("You're a Failure")      


    

