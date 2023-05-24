from projectile_motion_calculator import calculate_angle_of_launch, calculate_initial_velocity, \
calculate_initial_height, calculate_landing_distance, determine_enough_variables, determine_calculations_possible
from pytest import approx
import pytest
from math import pi


def test_calculate_angle_of_launch():
    """Test the calculate_angle_of_launch function by calling it and
    comparing the values it returns to the expected values.
    These values are compared with the values that mathematica computes.
    """

    a,b = calculate_angle_of_launch(344.73, 1000, 9.8, 500.0)
    assert a == approx(89.9039, rel=1e-3)
    assert b == approx(55.3187, rel=1e-3)

    a,b = calculate_angle_of_launch(30, 10, 9.8, 50)
    assert a == approx(40.0173, rel=1e-3)
    assert b == approx(9.05357, rel=1e-3)
    

    a,b = calculate_angle_of_launch(3, 13, 9.8, 599)
    assert a == approx(88.9389, rel=1e-3)
    assert b == approx(88.652, rel=1e-3)
    
    a,b = calculate_angle_of_launch(10, 10, 9.8, 0)
    assert a == approx(50.7392, rel=1e-3)
    assert b == approx(39.2608, rel=1e-3)
    

def test_calculate_initial_velocity():
    """Test the calculate_initial_velocity function by calling it and
    comparing the values it returns to the expected values.
    These values are compared with the values that mathematica computes.
    """

    assert calculate_initial_velocity(344.73, 34 * pi/180, 9.8, 500.0) == approx(34.0072, rel=1e-3)
    assert calculate_initial_velocity(10000, 0, 9.8, 10) == approx(7000, rel=1e-3)
    assert calculate_initial_velocity(10, 10 * pi/180, 9.8, 10) == approx(6.55364, rel=1e-3)
    assert calculate_initial_velocity(100, 10 * pi/180, 9.8, 56) == approx(26.1946, rel=1e-3)


def test_calculate_initial_height():
    """Test the calculate_initial_height function by calling it and
    comparing the values it returns to the expected values.
    These values are compared with the values that mathematica computes.
    """

    assert calculate_initial_height(100, 10 * pi/180, 9.8, 1) == approx(50505.8, rel=1e-3)
    assert calculate_initial_height(10000, 0, 9.8, 10) == approx(4.9 * 10 **6, rel=1e-3)
    assert calculate_initial_height(10, 10 * pi/180, 9.8, 10) == approx(3.28908, rel=1e-3)
    assert calculate_initial_height(100, 10 * pi/180, 9.8, 56) == approx(-1.5219, rel=1e-3)


def test_calculate_landing_distance():
    """Test the calculate_initial_height function by calling it and
    comparing the values it returns to the expected values.
    These values are compared with the values that mathematica computes.
    """

    assert calculate_landing_distance(100, 10 * pi/180, 9.8, 1) == approx(354.582, rel=1e-3)
    assert calculate_landing_distance(10000, 0, 9.8, 10) == approx(14285.7, rel=1e-3)
    assert calculate_landing_distance(10, 10 * pi/180, 9.8, 10) == approx(15.9215, rel=1e-3)
    assert calculate_landing_distance(100, 10 * pi/180, 9.8, 56) == approx(550.385, rel=1e-3)



def test_determine_enough_variables():
    """Test the determine_enough_variables function by setting all the 
    possible inputs for the dictionary into the determine_enough_variables
    function.
    """
    
    dictionary =  {"initial height": 34.56,
                    "initial velocity": "NA",
                    "angle of launch": 45,
                    "landing distance": "NA"}
    
    assert determine_enough_variables(dictionary) == False

    dictionary =  {"initial height": 34.56,
                    "initial velocity": "NA",
                    "angle of launch": "NA",
                    "landing distance": "NA"}
    
    assert determine_enough_variables(dictionary) == False

    dictionary =  {"initial height": "NA",
                    "initial velocity": "NA",
                    "angle of launch": "NA",
                    "landing distance": "NA"}
    
    assert determine_enough_variables(dictionary) == False

    dictionary =  {"initial height": 34.6,
                    "initial velocity": 36.6,
                    "angle of launch": 34.634,
                    "landing distance": "NA"}
    
    assert determine_enough_variables(dictionary) == True

    dictionary =  {"initial height": 34.6,
                    "initial velocity": 36.6,
                    "angle of launch": "NA",
                    "landing distance": "NA"}
    
    assert determine_enough_variables(dictionary) == False

    
    dictionary =  {"initial height": "NA",
                    "initial velocity": 36.6,
                    "angle of launch": "",
                    "landing distance": "NA"}
    
    assert determine_enough_variables(dictionary) == False


def test_determine_calculations_possible():
    """
    This tests determine_calculations_possible to make sure that 
    it is functioning properly.
    """

    #d=0, v=0, a=0, y=0, g=9.8
    assert determine_calculations_possible(1000, 1, 10, 56) == True
    assert determine_calculations_possible(1000, 1, 0, 56) == False
    assert determine_calculations_possible(0, 0, 0, 0) == False
    assert determine_calculations_possible(1, 1000, 10, 56) == True
    assert determine_calculations_possible(1, 1000, 10, 0) == False


# Call the main function that is part of pytest so that the
# computer will execute the test functions in this file.
pytest.main(["-v", "--tb=line", "-rN", __file__])