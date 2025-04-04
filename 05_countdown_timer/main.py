import time
def countdown(t):
    while t:
        mins, secs = divmod(t,60)
        timer = '\t\t{:02d}:{:02d}'.format(mins,secs)
        print(timer, end="\r")
        time.sleep(1)
        t -= 1
    print("\t\tTime's Up!")

print("\n\n\t\tCountdown Timer")
print("\t\t==============\n")

t = int(input("\t\tEnter time in seconds:"))
countdown(t)