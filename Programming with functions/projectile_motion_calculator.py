"""
Projectile motion calculator
This program's purpose is to aid in the graphing of projectile motion in 2D.
It prompts user input for variables, determines if the calculation is possible,
and then graphs it using Euler's method. 
The calculations are primarily based off of basic kinematic equations, 
which include:

equation for position:
s(f) = s(i) +v(i)t + (1/2)a(s)t^2

equation for final velocity:
v(f(s)) = v(i(s)) + a(s)t

equation for velocity without time dependency:
v(f(s))^2 = v(i(s))^2 + 2(a)(delta_s)

where s,v,a,t are: 
s- position
v- velocity (initial and final respectively)
a- acceleration
t- time

The other calculations in this code, primarily for solving for a possible missing variable
(initial height, angle of launch, initial velocity, or landing distance)
are complex rearrangements of the range equation, 
which is:

R = vcos(theta)/g  * (vsin(theta) + Sqrt(v^2 * sin(theta)^2 + 2gy))

where theta, v, g, R, y are:
v- initial velocity
theta- angle of launch 
y- initial height
R- landing distance (range)
g- acceleration due to gravity 

enjoy :)
Seth Ricks 
CSE 111
"""

from math import cos, sin, sqrt, tan, pi
import numpy as py
import matplotlib.pyplot as plot


def main():

    print('\nWelcome to 2D projectile motion calculator. Please input the known variables below.\
          \nIf a variable is not known, please input "NA"\n')

    #height and other inital conditions
    accel_gravity = 9.8
    starting_time = 0
    #small time step used in Euler's method
    dt = 0.01

    #dictionary used to keep track of input variables
    initial_conditions_dict =  {"initial height": "",
                                "initial velocity": "",
                                "angle of launch": "",
                                "landing distance": ""}

    #ask the user to input known variables  
    prompt_initial_height(initial_conditions_dict)
    prompt_initial_velocity(initial_conditions_dict)
    prompt_angle_of_launch(initial_conditions_dict)
    prompt_landing_distance(initial_conditions_dict)
            
    #If there are enough variables, proceed with calculations        
    if determine_enough_variables(initial_conditions_dict):

        #If initial height is not known
        if initial_conditions_dict["initial height"] == "NA":

            initial_velocity = initial_conditions_dict["initial velocity"]
            angle_of_launch = initial_conditions_dict["angle of launch"]
            landing_distance = initial_conditions_dict["landing distance"]

            #determine if the user's input is feasable
            if determine_calculations_possible(landing_distance, initial_velocity, angle_of_launch):

                initial_height = calculate_initial_height(landing_distance, angle_of_launch, accel_gravity, initial_velocity)
                position, velocity, acceleration = create_graphing_arrays(initial_height, initial_velocity, angle_of_launch, accel_gravity)
                configure_projectile_graph(position, initial_height, velocity, acceleration, dt, starting_time)
                
                #These must be printed before showing the plot, otherwise they will not be seen until the graph is deleted
                print(f"Max height: {(velocity[1] ** 2) / (2 * -acceleration[1]) + position[1]:.2f} m")
                print(f"Initial height: {initial_height:.2f} m")
                print(f"Initial velocity: {initial_velocity:.2f} m/s")
                print(f"Angle of launch: {py.degrees(angle_of_launch):.2f} degrees")
                print(f"Landing distance: {landing_distance:.2f} m")

                #Display the graph that was configured by configure_projectile_graph
                plot.show()

            else:
                print("Sorry, this projectile motions is not possible. Please try again.")

        #If initial velocity is not known
        elif initial_conditions_dict["initial velocity"] == "NA":

            initial_height = initial_conditions_dict["initial height"]
            angle_of_launch = initial_conditions_dict["angle of launch"]
            landing_distance = initial_conditions_dict["landing distance"]

            initial_velocity = calculate_initial_velocity(landing_distance, angle_of_launch, accel_gravity, initial_height)
            position, velocity, acceleration = create_graphing_arrays(initial_height, initial_velocity, angle_of_launch, accel_gravity)
            configure_projectile_graph(position, initial_height, velocity, acceleration, dt, starting_time)

            #These must be printed before showing the plot, otherwise they will not be seen until the graph is deleted
            print(f"Max height: {(velocity[1] ** 2) / (2 * -acceleration[1]) + position[1]:.2f} m")
            print(f"Initial height: {initial_height:.2f} m")
            print(f"Initial velocity: {initial_velocity:.2f} m/s")
            print(f"Angle of launch: {py.degrees(angle_of_launch):.2f} degrees")
            print(f"Landing distance: {landing_distance:.2f} m")

            #Display the graph that was configured by configure_projectile_graph
            plot.show()

        #If angle of launch is not known
        elif initial_conditions_dict["angle of launch"] == "NA":

            initial_height = initial_conditions_dict["initial height"]
            initial_velocity = initial_conditions_dict["initial velocity"]
            landing_distance = initial_conditions_dict["landing distance"]

            #determine if the user's input is feasable. "0" is used to determine which variable is unkown
            if determine_calculations_possible(landing_distance, initial_velocity, 0, initial_height):
                angle_of_launch1, angle_of_launch2 = calculate_angle_of_launch(landing_distance, initial_velocity, accel_gravity, initial_height)
                position, velocity, acceleration = create_graphing_arrays(initial_height, initial_velocity, angle_of_launch1, accel_gravity)
                configure_projectile_graph(position, initial_height, velocity, acceleration, dt, starting_time)

                #These must be printed before showing the plot, otherwise they will not be seen until the graph is deleted
                print(f"Max height: {(velocity[1] ** 2) / (2 * -acceleration[1]) + position[1]:.2f} m")
                print(f"Initial height: {initial_height:.2f} m")
                print(f"Initial velocity: {initial_velocity:.2f} m/s")
                print(f"Angle of launch: {angle_of_launch1:.2f} or {angle_of_launch2:.2f} degrees")
                print(f"({angle_of_launch1:.2f} degrees was used in the graph.)")
                print(f"Landing distance: {landing_distance:.2f} m")

                #Display the graph that was configured by configure_projectile_graph
                plot.show()

            else:
                print("Sorry, this projectile motions is not possible. Please try again.")

        #If landing distance is not known   
        elif initial_conditions_dict["landing distance"] == "NA":

            initial_height = initial_conditions_dict["initial height"]
            initial_velocity = initial_conditions_dict["initial velocity"]
            angle_of_launch = initial_conditions_dict["angle of launch"]

            landing_distance = calculate_landing_distance(initial_velocity, angle_of_launch, accel_gravity, initial_height)
            position, velocity, acceleration = create_graphing_arrays(initial_height, initial_velocity, angle_of_launch, accel_gravity)
            configure_projectile_graph(position, initial_height, velocity, acceleration, dt, starting_time)
            
            #These must be printed before showing the plot, otherwise they will not be seen until the graph is deleted
            print(f"Max height: {(velocity[1] ** 2) / (2 * -acceleration[1]) + position[1]:.2f} m")
            print(f"Initial height: {initial_height:.2f} m")
            print(f"Initial velocity: {initial_velocity:.2f} m/s")
            print(f"Angle of launch: {py.degrees(angle_of_launch):.2f} degrees")
            print(f"Landing distance: {landing_distance:.2f} m")

            #Display the graph that was configured by configure_projectile_graph
            plot.show()
        
        #If all the variables are known
        else: 
            
            initial_height = initial_conditions_dict["initial height"]
            initial_velocity = initial_conditions_dict["initial velocity"]
            angle_of_launch = initial_conditions_dict["angle of launch"]

            position, velocity, acceleration = create_graphing_arrays(initial_height, initial_velocity, angle_of_launch, accel_gravity)
            configure_projectile_graph(position, initial_height, velocity, acceleration, dt, starting_time)

            #These must be printed before showing the plot, otherwise they will not be seen until the graph is deleted
            print(f"Max height: {(velocity[1] ** 2) / (2 * -acceleration[1]) + position[1]:.2f} m")
            print(f"Initial height: {initial_height:.2f} m")
            print(f"Initial velocity: {initial_velocity:.2f} m/s")
            print(f"Angle of launch: {py.degrees(angle_of_launch):.2f} degrees")
            if calculate_landing_distance(initial_velocity, angle_of_launch, accel_gravity, initial_height) != initial_conditions_dict["landing distance"]:
                print(f"The landing distance that you entered was faulty.")
            print(f"Landing distance: {position[0]:.2f} m")
            
            #Display the graph that was configured by configure_projectile_graph
            plot.show()
    
    else:
        print("Sorry, the caluclations are not possible with the given amount of variables. Please try again.")
        print()           


def prompt_initial_height(dictionary):
    """
    This function stores the user input for initial height in the initial_conditions_dictionary.
    It does not allow user input that is not a number greater than  or equal to zero.

    Parameters: the initial conditions dictionary
        
    Return: returns nothings, but stores the inputed value in the intial_conditions_dictionary
    """

    print()
    error = True
    while error == True:
        error = False
        try:
            initial_height = input("What is the initial height (in meters)? ")
            if initial_height == "-0" or initial_height == "+0":
                raise ValueError
            
            if initial_height.upper() != "NA":
                initial_height = float(initial_height)
                if initial_height < 0:
                    print("Sorry, please enter a positive height.")
                    error = True
                else:
                    dictionary["initial height"] = initial_height

            else:
                print("You inputed NA")
                dictionary["initial height"] = initial_height.upper()

        except ValueError:
            print("Sorry, the value that you entered is not valid. Please enter a number or NA. ")
            error = True
        

def prompt_initial_velocity(dictionary):
    """
    This function stores the user input for initial velocity in the initial_conditions_dictionary.
    It does not allow user input that is not a number greater than zero.

    Parameters: the initial conditions dictionary
        
    Return: returns nothings, but stores the inputed value in the intial_conditions_dictionary
    """
    
    print()
    error = True
    while error == True:
        error = False
        try:
            initial_velocity = input("What is the initial velocity (in meters/second)? ")
            if initial_velocity == "-0" or initial_velocity == "+0":
                raise ValueError
            if initial_velocity.upper() != "NA":
                initial_velocity = float(initial_velocity)
                if initial_velocity <= 0:
                    print("Sorry, please enter a positive velocity.")
                    error = True
                else:
                    dictionary["initial velocity"] = initial_velocity

            else:
                print("You inputed NA")
                dictionary["initial velocity"] = initial_velocity.upper()
        except ValueError:
            print("Sorry, the value that you entered is not valid. Please enter a number or NA. ")
            error = True



def prompt_angle_of_launch(dictionary):
    """
    This function stores the user input for angle of launch in the initial_conditions_dictionary.
    It does not allow user input that is not a number greater than zero and less than 90.

    Parameters: the initial conditions dictionary
        
    Return: returns nothings, but stores the inputed value in the intial_conditions_dictionary
    """

    print()
    error = True
    while error == True:
        error = False
        try:
            angle_of_launch = input("What is the angle of launch (in degrees)? ")
            if angle_of_launch == "-0" or angle_of_launch == "+0":
                raise ValueError
            
            if angle_of_launch.upper() != "NA":
                angle_of_launch = float(angle_of_launch)
                if (angle_of_launch < 0) or (angle_of_launch > 90):
                    print("Sorry, please enter an angle between 0 and 90 degrees.")
                    error = True
                else:
                    dictionary["angle of launch"] = angle_of_launch * (pi /180)
            else:
                print("You inputed NA")
                dictionary["angle of launch"] = angle_of_launch.upper()

        except ValueError:
            print("Sorry, the value that you entered is not valid. Please enter a number or NA. ")
            error = True
    


def prompt_landing_distance(dictionary):
    """
    This function stores the user input for landing distance in the initial_conditions_dictionary.
    It does not allow user input that is not a number greater than zero.

    Parameters: the initial conditions dictionary
        
    Return: returns nothings, but stores the inputed value in the intial_conditions_dictionary
    """
    
    print()
    error = True
    while error == True:
        error = False
        try:
            landing_distance = input("What is the landing distance (in meters)? ")
            if landing_distance == "-0" or landing_distance == "+0":
                raise ValueError
            
            if landing_distance.upper() != "NA":
                landing_distance = float(landing_distance)
                if landing_distance <= 0:
                    print("Sorry, please enter a positive landing distance.")
                    error = True
                else: 
                    dictionary["landing distance"] = landing_distance

            else:
                print("You inputed NA")
                dictionary["landing distance"] = landing_distance.upper()

        except ValueError:
            print("Sorry, the value that you entered is not valid. Please enter a number or NA. ")
            error = True



def create_graphing_arrays(initial_height, initial_velocity, angle_of_launch, accel_gravity):
    """
    This function creates the arrays that are needed to graph the function later using Euler's method.

    Parameters:
    initial_height- the initial height of the projectile
    initial_velocity- the initial velocity of the projectile
    angle_of_launch- the angle of launch of the projectile
    accel_gravity- the acceleration due to gravity

    Return: returns the needed arrays for position, velocity, and acceleration
    """
    
    #x,y
    position = py.array([0, initial_height]) 

    #initial velocities in the x and y directions
    velocity = py.array([initial_velocity * cos(angle_of_launch), initial_velocity * sin(angle_of_launch)])

    #ax, ay
    acceleration = py.array([0, -accel_gravity])

    return position, velocity, acceleration



def calculate_angle_of_launch(d, v, g, y):
    """
    This function calculates the angle of launch of the projectile, given four parameters.
    The parameters are used with one letter in order to make the calculation easier to read.

    Parameters:
        d- horizonal landing distance of the projectile (in meters)
        v- initial velocity of the projectile (in m/s)
        g- acceleration due to gravity (in m/s^2)
        y- initial height of the projectile before launch (in meters)

    Return: the two possible angles of launch for the projectile in the first quadrant, in degrees 
    """

    angle_of_launch1 = py.arccos(sqrt((d ** 2 * (v ** 4 + g * v ** 2 * y) - sqrt(d ** 4 * v ** 4 * (-d ** 2 * g ** 2 + v ** 4 + 2 * g * v ** 2 * y))) / (v ** 4 * (d ** 2 + y ** 2))) / sqrt(2)) * (180 / pi)
    angle_of_launch2 = py.arccos(sqrt((d ** 2 * (v ** 4 + g * v ** 2 * y) + sqrt(d ** 4 * v ** 4 * (-d ** 2 * g ** 2 + v ** 4 + 2 * g * v ** 2 * y))) / (v ** 4 * (d ** 2 + y ** 2))) / sqrt(2)) * (180 / pi)

    return angle_of_launch1, angle_of_launch2



def calculate_initial_velocity(d, a, g, y):
    """
    This function calculates the initial velocity of the projectile, given four parameters.
    The parameters are used with one letter in order to make the calculation easier to read.

    Parameters:
        d- horizonal landing distance of the projectile (in meters)
        a- angle of launch of the projectile (inputed in radians for ease of sqrt calculation)
        g- acceleration due to gravity (in meters/second^2)
        y- initial height of the projectile before launch (in meters)

    Return: the initial velocity for the projectile
    """

    initial_velocity = (d * sqrt(g) * sqrt(1 / cos(a))) / (sqrt(2 * y * cos(a) + 2 * d * sin(a)))

    return initial_velocity



def calculate_initial_height(d, a, g, v):
    """
    This function calculates the initial velocity of the projectile, given four parameters.
    The parameters are used with one letter in order to make the calculation easier to read.

    Parameters:
        d- horizonal landing distance of the projectile (in meters)
        a- angle of launch of the projectile (inputed in radians)
        g- acceleration due to gravity (in meters/second^2)
        v- initial velocity of the projectile before launch (in m/s)

    Return: the initial height for the projectile
    """

    initial_height = (0.5) * d * (d * g * (1 / cos(a)) ** 2 / (v ** 2) - 2 * tan(a))
    
    return initial_height


def calculate_landing_distance(v, a, g, y):
    """
    This function calculates the landing distance of the projectile, given four parameters.
    The parameters are used with one letter in order to make the calculation easier to read.

    Parameters:
        v- initial velocity of the projectile before launch (in m/s)
        a- angle of launch of the projectile (inputed in radians for ease of sqrt calculation)
        g- acceleration due to gravity (in meters/second^2)
        y- initial height of the projectile before launch (in meters)

    Return: the landing distance for the projectile
    """

    landing_distance = (v * cos(a) * (v * sin(a) + sqrt(2 * g * y + v **2 * (sin(a) ** 2)))) / g

    return landing_distance



def determine_enough_variables(dictionary, count=0):
    """
    This function determines if there are enough known variables to calculate projectile motion.

    Parameters: the initial conditions dictionary
        
    Return: a boolean variable
    True- the calculation is possible
    False- the calculation is not possible
    """
     
    for value in dictionary.values():
        if value == "NA":
            count += 1
    
    if count > 1:
        possible = False
    else:
        possible = True

    return possible

def determine_calculations_possible(d, v, a=0, y=0, g=9.8):
    """
    This function determines if the calculations are feasible. The only equations that need to be tested are the 
    the ones for angles of launch, and for initial height. All the others will return real values.

    Parameters: single letters for ease of calculations
    d- horizontal distance traveled
    v- initial velocity
    a- angle of launch, set to zero if it is not known
    y- initial height, set to zero if it is not known
    g- acceleration due to gravity
        
    Return: 
    """
    
    possible = True
    if a ==0:
        try:

            #equations for angles of launch
            py.arccos(sqrt((d ** 2 * (v ** 4 + g * v ** 2 * y) - sqrt(d ** 4 * v ** 4 * (-d ** 2 * g ** 2 + v ** 4 + 2 * g * v ** 2 * y))) / (v ** 4 * (d ** 2 + y ** 2))) / sqrt(2)) * (180 / pi)
            py.arccos(sqrt((d ** 2 * (v ** 4 + g * v ** 2 * y) + sqrt(d ** 4 * v ** 4 * (-d ** 2 * g ** 2 + v ** 4 + 2 * g * v ** 2 * y))) / (v ** 4 * (d ** 2 + y ** 2))) / sqrt(2)) * (180 / pi)

        except ValueError:
            possible = False
        except ZeroDivisionError:
            possible = False

    elif y == 0:

        #equation for initial height
        initial_height = (0.5) * d * (d * g * (1 / cos(a)) ** 2 / (v ** 2) - 2 * tan(a))
        if initial_height < 0:
            possible = False

    return possible
        
def configure_projectile_graph(position, initial_height, velocity, acceleration, dt, starting_time=0):
    """
    This function configures the graph of the projectile so it is ready to graph, using matplotlib

    Parameters:
        position- an array of x and y positions configured as [x,y]
        initial_height- the initial height of the projectile
        velocity- an array of the velocities in the x and y directions configured as [x,y]
        acceleration- an array of the accelerations in the x and y directions, configured as [x,y]
        dt- small time step used to plot the projectile at different points in time
        starting_time- time at which the projectile was launch, which logically should almost always be 0

    Return: returns nothing, but configures the plot so that it is ready to graph upon command
    """

    plot.figure()
    plot.xlabel("x (meters)")
    plot.ylabel("y (meters)")
    plot.title("Motion of Projectile (with no air resistance)")
    
    #plot x and y for increasing intervals of t
    while position[1] >= initial_height or position[1] >= 0:
        velocity += acceleration * dt
        position += velocity * dt
        starting_time += dt
        plot.plot(position[0], position[1],'r.')

    print()
    #time of flight must be printed inside this function in order for it to be seen
    print(f"Time of flight: {starting_time:.2f} seconds")

if __name__ == "__main__":
    main()