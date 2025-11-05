def calculate_bmi(height, weight):
    print("Height = "+ str(height))
    print("Weight = "+ str(weight))
    bmi = weight/(height*height)
    print("BMI is " + str(bmi))
    if bmi < 18.5:
        print("Skinny, bmi is "+ str(bmi))
        val =  -1
    elif bmi >25.0:
        print("fatty, bmi is "+ str(bmi))
        val = 1
    else:
        print("normal, bmi is"+ str(bmi))
        val = 0
    return val

valu = calculate_bmi(weight=67, height=1.63)
print(str(valu))