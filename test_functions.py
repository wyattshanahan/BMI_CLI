from functions import * #import functions from calculator.py

def test_categotise_under(): #ensure underweight is categorised correctly
    assert categoriseBMI(18.4999) == "Underweight"

def test_categotise_normal_Lbound(): #check the lower boundary for normal weight
    assert categoriseBMI(18.5) == "Normal Weight"

def test_categotise_normal(): # check a middle value for normal weight
    assert categoriseBMI(22.0) == "Normal Weight"

def test_categotise_normal_Ubound(): # check upper boundary for normal weight
    assert categoriseBMI(24.9999) == "Normal Weight"

#def test_categotise_under():
#    assert categoriseBMI(18.49) == "Underweight"