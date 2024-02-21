def processInput(rawHeight):
    rawHeight = rawHeight.split(",") #split heightRAW to an array of the ft, in
    feet = float(rawHeight[0]) # element 0 is ft, convert to float
    inch = float(rawHeight[1]) # element 1 is inches, convert to float
    totalIN = inch + (feet * 12) # convert and add feet to totalIN
    return totalIN

def imperialToMetric(weight, heightIN):
    weight = weight * 0.45 # convert pounds to kilogrammes
    heightM = heightIN * 0.025 #convert total inches into metres
    heightM = heightM * heightM # BMI requires square metres
    return weight, heightM

def outputBMI(inputBMI):
    if (inputBMI < 18.5):
        BMIcat = "Underweight"
    elif (18.5 <= inputBMI < 25.0): #using < rather than <= to ensure coverage
        BMIcat = "Normal Weight"
    elif (25.0 <= inputBMI < 30.0):
        BMIcat = "Overweight"
    elif (30.0 <= inputBMI):
        BMIcat = "Obese"
    else:
        print("Error processing your BMI, please validate your input.")
        raise ValueError

print("===============================================")
print("Welcome to the BMI Calculator")
print("\n(C)2024 Wyatt Shanahan")
print("===============================================")
weight = float(input("Enter your weight in pounds: ")) # read in weight and height
heightRAW = input("Enter your height in feet and inches using a comma to separate the two: ") #read in height as foot, inches to be split and processed
heightIN = processInput(heightRAW)
weight, heightM = imperialToMetric(weight, heightIN)
BMI = weight / heightM #BMI is weight/height
category = outputBMI(BMI)
print(f"Weight: {weight} height^2 {heightM} BMI: {BMI}")

#print(f"Weight: {weight} ft {heightFT} in{heightIN}")

# todo: add exceptions
# todo: validate input
# todo: finish output formatting
# todo: make the input and welcome formatting improved
# todo: round floats in BMI to 2 decimal (?)
# todo: validate input early on
# todo: add exit loop