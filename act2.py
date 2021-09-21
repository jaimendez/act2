prelims = int(input("Enter Prelims grade: "))
midterm = int(input("Enter Midterm grade: "))
semis = int(input("Enter Semi Finals Grade: "))
finals = int(input("Enter Finals Grade: "))

avg = (prelims + midterm + semis + finals)/4

passing = 75

if avg >= passing:
    print("You passed!")

else:
    print("You Failed")

