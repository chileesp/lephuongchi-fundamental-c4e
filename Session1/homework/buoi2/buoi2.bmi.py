weight = int(input ("how heavy are you? (kg)"))
height = int(input ("how tall are you? (cm)"))
heightm = height / 100
BMI = weight / (heightm * heightm)

if (BMI < 16):
    print ("Severely underweight")
elif (16 < BMI < 18.5 ):
    print ("Underweight")
elif (18.5 < BMI < 25):
    print ("Normal")
elif (25 < BMI < 30):
    print ("Overweight")
else:
    print ("Obese")
