# Universal Gravity Calculator (15pts)
# In physics, the force of gravity between two objects can be calculated using the equation:
# F = G * (m1 * m2) / r**2
# F is the force of gravity in Newtons
# G is the universal gravity constant (6.67e-11)
# m1 is the mass of first object in kg
# m2 is the mass of the second object in kg
# r is the center to center distance between the objects in meters


# Make a calculator that does all of the following 
# (3pts) takes the inputs for mass 1, mass 2.and distance between the two objects (m1, m2, and r) 
# (4pts) contains exceptions for any potential errors (value and dividebyzero).
# (3pts) keeps asking for inputs until they are valid (see while loop from notes)
# (4pts) calculate the force of gravity in Newtons and print the result to the user in scientific notation to two decimals.


def ugc():
    valid_input = False
    g = 6.67e-11
    while valid_input is False:
        try:
            m1 = float(input("Mass 1 (kg)?\n"))
            m2 = float(input("Mass 2 (kg)?\n"))
            r = float(input("Radius (m)?\n"))
            f = g * (m1 * m2) / r ** 2
            valid_input = True
        except ZeroDivisionError:
            print("Error. The radius may not be zero because one may not divide by zero.")
            print()
        except ValueError:
            print("Error. One must input numbers.")
            print()
    answer = (g * m1 * m2) / r ** 2
    answer = "{:.2e}".format(answer)
    print("The force of gravity in these circumstances is", answer, "newtons.")


ugc()






