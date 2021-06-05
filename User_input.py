emotions = []
a = input("enter your name please? ")
b = input("where are you from country only? ")
c = input("enter your age ")
cc = int(c)
emotions.insert(0,a)
emotions.insert(1,b)
emotions.insert(2,cc)
print(emotions)
if emotions[2] > 100:
    print("invalid input hit refresh")
elif emotions[2] > 50:
    print("more assistance needed based on age ")
else:
    print("you should be okay")
d = input("what is your friends height? ")
e = input("what is your friends weight? ")
f = input("what is your friends name? ")
data = {}
data["height"] = d
data["weight"] = e
data["name"] = f
data["your name"] = a
data["Country"] = b
data["age"] = cc
print(data)
























