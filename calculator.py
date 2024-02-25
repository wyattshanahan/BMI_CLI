from functions import * #import functions used for running the overall program

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