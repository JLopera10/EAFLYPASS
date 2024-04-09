import time
import random
from Modulo import Student, Car, Queue, clear

priorityqueue = Queue("priority")
regularqueue = Queue("regular")
creationqueue = []

# DEFAULT STUDENTS
student1 = Student("Juan", 1022144846, "Priority")
car1 = Car(student1, "XYZ-215")
student2 = Student("Luis", 3535983705, "Priority")
car2 = Car(student2, "JUM-543")
student3 = Student("Camilo", 6042112631, "Priority")
car3 = Car(student3, "KLO-326")
student4 = Student("Cesar", 8032174243, "Regular")
car4 = Car(student4, "WLU-580")
student5 = Student("Isabella", 9022645811, "Regular")
car5 = Car(student5, "JQM-345")
student6 = Student("Alejandra", 2327194646, "Regular")
car6 = Car(student6, "QLP-328")
student7 = Student("Sebastian", 9221193542, "Regular")
car7 = Car(student7, "WMU-362")
creationqueue.append(car1)
creationqueue.append(car2)
creationqueue.append(car3)
creationqueue.append(car4)
creationqueue.append(car5)
creationqueue.append(car6)
creationqueue.append(car7)


def randomizeArrival(random_numbers):
    total = random.randint(0, len(creationqueue) - 1)
    for i in range(total):
        found = True
        while found:
            num = random.randint(0, len(creationqueue) - 1)
            if num not in random_numbers:
                found = False
                random_numbers.append(num)


clear()
leave = False
while not leave:
    print("--------------------- EAFLYPASS Parking Lot ---------------------")
    print("1. Add student to the system")
    print("2. Park cars")
    print("3. Leave")
    decision = input()
    clear()
    match decision:
        case "1":
            invalid = False
            name = input("Name: ")
            student_id = int(input("Student ID: "))
            honor = input("Is the student enrolled with honors? ( Y / N ): ")
            plate = input("What is the Vehicle Registration Plate of the student's car?: ")
            eco = input("Is the student's car an ecologic car? ( Y / N): ")
            if honor.lower() == "y" or eco.lower() == "y":
                category = "Priority"
            elif honor.lower() == "n" and eco.lower() == "n":
                category = "Regular"
            else:
                print("You must answer either Y or N to the questions that ask you to do so")
                invalid = True
            if not invalid:
                student = Student(name, student_id, category)
                car = Car(student, plate)
                creationqueue.append(car)
                print("Student Added Correctly")
            time.sleep(1)
            clear()
        case "2":
            random_numbers = []
            randomizeArrival(random_numbers)
            for x in random_numbers:
                if creationqueue[x].owner.category == "Priority":
                    priorityqueue.addCar(creationqueue[x])
                elif creationqueue[x].owner.category == "Regular":
                    regularqueue.addCar(creationqueue[x])
            priorityqueue.parkCars()
            regularqueue.parkCars()
        case "3":
            print("Leaving...")
            quit()
        case _:
            print("Invalid Input")
