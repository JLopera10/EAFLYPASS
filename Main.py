import time
from Modulo import Student, Car, PriorityQueue, RegularQueue, clear

priorityqueue = PriorityQueue()
regularqueue = RegularQueue()
creationqueue = []
arrivalqueue = []

clear()
leave = False
while not leave:
    print("--------------------- EAFLYPASS Parking Lot ---------------------")
    print("1. Add student to the system")
    print("2. Add car to the queue")
    print("3. Park cars")
    print("4. Leave")
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
            i = 1
            for x in creationqueue:
                if x not in arrivalqueue:
                    print(str(i) + ". " + x.owner.name)
                    print("Category: " + x.owner.category)
                    print()
                i += 1
            index = int(input("Who is gonna join the queue?: "))
            if 0 <= index - 1 < len(creationqueue):
                if creationqueue[index - 1] not in arrivalqueue:
                    arrivalqueue.append(creationqueue[index - 1])
                    print("Car added successfully to the queue")
                else:
                    print("This car is already in the queue")
            else:
                print("Invalid index")
            time.sleep(1)
            clear()
        case "3":
            for x in arrivalqueue:
                if x.owner.category == "Priority":
                    priorityqueue.addCar(x)
                elif x.owner.category == "Regular":
                    regularqueue.addCar(x)
            priorityqueue.parkCars()
            regularqueue.parkCars()
            arrivalqueue.clear()
            print("All cars have been parked successfully, the queue is now empty")
            time.sleep(2)
            clear()
        case "4":
            print("Leaving...")
            quit()
        case _:
            print("Invalid Input")
