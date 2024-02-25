def processRawHeight(rawHeight):
    rawHeight = rawHeight.split(",") #split heightRAW to an array of the ft, in
    try:
        feet = float(rawHeight[0]) # element 0 is ft, convert to float
    except ValueError: #if value error, try seeing if user forgot to include a comma and used a space
        try:
            rawHeight = rawHeight[0].split()  # try splitting on a space
            feet = float(rawHeight[0])  # element 0 is ft, convert to float
        except: #if spaces and comma failed, then throw an error and abort execution
            print("\nError parsing your height, please validate your input.")
            exit("ParseError") #exit and report a parsing error
    try:
        inch = float(rawHeight[1]) # element 1 is inches, convert to float
    except IndexError:
        print("\nError processing your height, please validate your input.") #exit and report an indexing error
        exit("IndexError")
    totalIN = inch + (feet * 12) # convert and add feet to totalIN
    return totalIN #return totalIN

def imperialToMetric(weight, heightIN):
    weight = float(weight) * 0.45 # convert pounds to kilogrammes
    heightM = float(heightIN) * 0.025 #convert total inches into metres
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
        exit("ValueError")
    return BMIcat

print("=============================================================================")
print("Welcome to the BMI Calculator")
print("\n(C)2024 Wyatt Shanahan")
print("=============================================================================")

weight = float(input("Enter your weight in pounds: ")) # read in weight and height
heightRAW = input("Enter your height in feet and inches using a comma to separate the two: ") #read in height as foot, inches to be split and processed

heightIN = processRawHeight(heightRAW) #process raw height, outputs the height in inches
weight, heightM = imperialToMetric(weight, heightIN) #converts from imperial to metric
BMI = weight / heightM #BMI is weight/height
category = categoriseBMI(BMI)


print(f"\nYour BMI is {BMI:.1f}\nYour BMI category is {category}")
waitToExit = input("\nPress Enter to exit...") # prevents program from exiting til the user says to