students = {"Eric":14 , "Bob":12, "Tina":26, "Cris":15}

    # .clear()
students.clear()
print(students)

students = {"Eric":14 , "Bob":12, "Tina":26, "Cris":15}

    # len()
print(len(students))

    # .keys()
print(students.keys())

    # .values()
print(students.values())

    # .update()
students = {"Eric":14 , "Bob":12, "Tina":26, "Cris":15}
students2 = {"Eric":12 , "Bob":12, "Tim":19}
students.update(students2)
print(students)