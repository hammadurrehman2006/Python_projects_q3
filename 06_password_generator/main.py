import random
print("\n\t\t-=Welcome to Password Generator=-")
print("\t\t=================================\n")

n = int(input("Enter the Number of Passwords you want to generate:"))
l = int(input("Enter the length of Passwords:"))

def generate_password(l,n):
    password = "ABCDEFGHIJKLMNOPQRSTUVWXYZ" + "ABCDEFGHIJKLMNOPQRSTUVWXYZ".lower() + "1234567890" + "!@#$%&_-"
    for i in range(n):
        for j in range(l):
            