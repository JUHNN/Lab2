def calculate_bmi(height, weight):
    print("Height = "+ str(height))
    print("Weight = "+ str(weight))
    bmi = weight/(height*height)
    print("BMI is " + str(bmi))
    if bmi < 18.5:
        print("Skinny, bmi is "+ str(bmi))
    elif bmi >25.0:
        print("fatty, bmi is "+ str(bmi))
    else:
        print("normal, bmi is"+ str(bmi))

calculate_bmi(weight=67, height=1.63)