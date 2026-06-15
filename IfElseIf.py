print("=========Ticket Pcing Software==========")

print("Ente Your Age : ")
Age = int(input())

if(Age <= 5):
    print("Ticket : Free")
elif(Age > 5 and Age <= 18):
    print("Ticket : 900 Rs.")
elif(Age > 18 and Age <= 40):
    print("Ticket : 1200")
else:
    print("Ticket id: 500")


