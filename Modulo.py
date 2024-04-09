import time

def clear():
    for x in range(50):
        print()

class Student:
    def __init__(self, name: str, student_id: int, category: str):
        self.name = name
        self.college_id = student_id
        self.category = category
        self.parking_credits = 5

    def useCredit(self):
        self.parking_credits -= 1

    def addCredit(self, answer):
        if answer.lower() == "y":
            valid = False
            while not valid:
                clear()
                print("How many credits do you want to add?")
                credit = int(input())
                if (self.parking_credits + credit) >= 5:
                    self.parking_credits += credit
                    print("Credits added successfully")
                    valid = True
                else:
                    print("Your total amount of credits has to be equal or higher than 5 if you want to add credits")
                    time.sleep(1)
            time.sleep(1)
            clear()
            return True
        elif answer.lower() == "n":
            print("Alright, just remember you need to have credits to park here")
            time.sleep(1)
            clear()
            return True
        else:
            print("Invalid Answer")
            print(" ")
            time.sleep(1)
            clear()
            return False


class Car:
    def __init__(self, owner: Student, license_plate: str):
        self.owner = owner
        self.license_plate = license_plate
        self.next = None


class Queue:
    def __init__(self, type):
        self.front = None
        self.rear = None
        self.type = type

    def addCar(self, car: Car):
        car.next = None
        if not (self.front and self.rear):
            self.front = car
            self.rear = car
        else:
            self.rear.next = car
            self.rear = car

    def parkCars(self):
        current = self.front
        if not current:
            if self.type == "priority":
                print("There are no cars in the priority queue")
            elif self.type == "regular":
                print("There are no cars in the regular queue")
            time.sleep(1)
            clear()
        while current:
            if current.owner.parking_credits > 1:
                current.owner.useCredit()
                print(current.owner.name + " welcome to the EAFLYPASS parking lot")
                print("Category: " + current.owner.category)
                print("Vehicle Registration Plate: " + current.license_plate)
                print("Remaining Credits: " + str(current.owner.parking_credits))
            elif current.owner.parking_credits == 1:
                current.owner.useCredit()
                print("************** ALERT **************")
                valid = False
                while not valid:
                    print(current.owner.name + ", you have wasted your last credit. "
                                               "Do you want to add more credits? ( Y / N )")
                    answer = input()
                    valid = current.owner.addCredit(answer)
                print(current.owner.name + " welcome to the EAFLYPASS parking lot")
                print("Category: " + current.owner.category)
                print("Vehicle Registration Plate: " + current.license_plate)
                print("Remaining Credits: " + str(current.owner.parking_credits))
            else:
                valid = False
                while not valid:
                    print(current.owner.name + ", you don't have enough credits to park here. "
                                               "Do you want to add more credits? ( Y / N )")
                    answer = input()
                    valid = current.owner.addCredit(answer)
                if current.owner.parking_credits >= 1:
                    current.owner.useCredit()
                    print(current.owner.name + " welcome to the EAFLYPASS parking lot")
                    print("Category: " + current.owner.category)
                    print("Vehicle Registration Plate: " + current.license_plate)
                    print("Remaining Credits: " + str(current.owner.parking_credits))
                else:
                    print(current.owner.name + " could not park here")
            time.sleep(1)
            clear()
            current = current.next
        self.front = None
        self.rear = None

