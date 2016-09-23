import pickle
import sys
class person:
    def __init__(self, name):
        self.name = name
        self.lOfFriends = [] 
    
    def setName(self, name):
        self.name = name
    def setFriends(self, *friendList):
        self.lOfFriends += [friendList]
    def setAge(self, age):
        self.age = age 
    # def __call__(self):
    #     return self 

    def getFriends(self):
        for friend in self.lOfFriends:
            print friend
 
# ---- making some objects
person1 = person("behzad")
person1.setFriends("asghar", "ali")
person1.setAge(1)

person2 = person("molly")
person2.setFriends("negar", "huray")
person2.setAge(10)

lOfPeople = [person1, person2]


# ---- pickling (puttin any object in a file). that seems to be the right way to
# ---- about storing info in a file (as opposed to storing data in a data base)
PIK = "pickle_stuff.dat"

with open(PIK, "wb") as f:
    for myPerson in lOfPeople:
        pickle.dump(myPerson, f)

listOfPeople = [] 
with open(PIK, "rb") as f:
    # pickle.load(f)
    while True: 
        try: 
            myPerson = pickle.load(f)# 
            listOfPeople.append(myPerson)# 
            # listOfPeople.append(copy.copy(person))# 
        except Exception as ex:
            if not (type(ex).__name__ == "EOFError"):
                print type(ex).__name__ 
                print ex.args
            break

for myPerson in listOfPeople:
    myPerson.getFriends()


