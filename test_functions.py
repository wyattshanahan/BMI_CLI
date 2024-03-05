from functions import * #import functions from calculator.py

# tests for categoriseBMI
def test_categorise_9_25(): # test the "interior" point for underweight
    assert categoriseBMI(9.25) == "Underweight"

def test_categorise_18_4(): # test the boundary at 18.4
    assert categoriseBMI(18.4) == "Underweight"

def test_categorise_18_5(): # test the boundary at 18.5
    assert categoriseBMI(18.5) == "Normal Weight"

def test_categorise_21_7(): # test the interior point between bounds 18.5 and 25
    assert categoriseBMI(21.7) == "Normal Weight"

def test_categorise_24_9(): # test the boundary at 24.9
    assert categoriseBMI(24.9) == "Normal Weight"

def test_categorise_25_0(): # test the boundary at 25
    assert categoriseBMI(25.0) == "Overweight"

def test_categorise_27_45(): # test the interior point between bounds 25 and 30
    assert categoriseBMI(27.45) == "Overweight"

def test_categorise_29_9(): # test the boundary at 29.9
    assert categoriseBMI(29.9) == "Overweight"

def test_categorise_30_0(): # test the boundary at 30.0
    assert categoriseBMI(30.0) == "Obese"

def test_categorise_39_25(): # test the "interior" point for values over the boundary at 30.0
    assert categoriseBMI(39.25) == "Obese"
