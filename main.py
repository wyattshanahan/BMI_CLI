def processRawHeight(rawHeight):
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

def categoriseBMI(inputBMI):
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
    return BMIcat

print("===============================================")
print("Welcome to the BMI Calculator")
print("\n(C)2024 Wyatt Shanahan")
print("===============================================")
weight = float(input("Enter your weight in pounds: ")) # read in weight and height
heightRAW = input("Enter your height in feet and inches using a comma to separate the two: ") #read in height as foot, inches to be split and processed
heightIN = processRawHeight(heightRAW) #process raw height, outputs the height in inches
weight, heightM = imperialToMetric(weight, heightIN) #converts from imperial to metric
BMI = weight / heightM #BMI is weight/height
category = categoriseBMI(BMI)
print(f"\nYour BMI is {BMI:.1f}\nYour BMI category is {category}")
waitToExit = input("\nPress Enter to exit...") # prevents program from exiting til the user says to

#print(f"Weight: {weight} ft {heightFT} in{heightIN}")

# todo: add exceptions
# todo: validate input
# todo: finish output formatting
# todo: make the input and welcome formatting improved
# todo: validate input early on