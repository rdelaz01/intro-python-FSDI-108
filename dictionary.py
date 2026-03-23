#dictionaries store data in KEY:VALUE pairs
#Written with curly brackets {}

students = {
    "name" : "John",
    "age" : 31,
    "major" : "Computer Science"

}
print(students)

#accessing values in a dictionary
print(students["name"]) #pulling specific value using the key
print(students.get("major")) #pulling specific value using the get method

#adding items to a dictionary
students["graduation_year"] = 2024 #adding a new key:value pair to the dictionary
print(students)

#changing values in a dictionary
students["age"] = 32 #changing the value of an existing key
print(students)

#removing items from a dictionary
students.pop("major") #removing a key:value pair using the pop method
print(students)

#check if an item exists in a dictionary
if "name" in students:
    print("key 'name' exists in the dictionary")

#nested Dictionaries
students = {
    "student1" : {"name" : "John", "age" : 31, "major" : "Computer Science"},
    "student2" : {"name" : "Jane", "age" : 29, "major" : "Mathematics"} 
}

print(students["student2"]["age"])

"""
MINI CHALLENGE: Student report card
You need to store and analyyze a students grades
1. Create a dictionary called "report_card" with keys:
    - "NAME"
    -SUBJECTS"
    -"GRADES"
#Example : {"NAME": "John", "SUBJECTS": ["Math", "Science"], "GRADES": [85, 90]}
2. Print the students name and subject.
3. Calculate the average of the 3 grades (HINT : use the sum() and len() functions) and print the average grade.
4. Add a new key called "average" with the calculated result. 
5. If the average is is 90 or above print "Exellent" 
    if between 70 and 89 -> print "Good Jon" 
    otherwise - print "Needs Improvement"
6. Remove the "subjects" key and print the updated dictionary 
"""

report_card = {
    "NAME": "John",
    "subjects": "math",
    "grades": [85, 90, 78]

}
print(f"Student Name: {report_card['NAME']}")
average_grade = sum(report_card["grades"]) / len(report_card["grades"])
print(f"Average Grade: {average_grade}")
report_card["average"] = average_grade
if average_grade >= 90:
    print("Excellent")
elif 70 <= average_grade < 90:
    print("Good Job")
else:    print("Needs Improvement")
report_card.pop("subjects")
print(report_card)


"""
ASSIGNMENT 2

"""

racer= {
    "name": "Lewis Hamilton",
    "age": 38,
    "team": "Mercedes",
    "championships": 7
}
print(racer)

#accessing values in a dictionary
print(racer["name"])
print(racer.get("team"))

#adding new keys to a dictionary
racer["nationality"] = "British"
print(racer)

#updating values in a dictionary
racer["age"] = 39
print(racer)

#removing items from a dictionary
racer.pop("championships")
print(racer)

#print dictionary and its length
print(len(racer))


