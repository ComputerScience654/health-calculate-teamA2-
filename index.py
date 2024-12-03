#นายวรวุฒิ ยาชัยยะ 465415241013,นายปรเมศวร์ สุขรอด 465415241005 CSS46541N

print("----- Health Calculator -----")

gender = input("Enter your gender (M/F): ")

weight = float(input("Enter your weight (in kg): "))

height = float(input("Enter your height (in cm): "))

age = int(input("Enter your age(year): "))

if gender == "M" or gender == "m":
    def calorie(weight, height, age):
        return (10 * weight) + (6.25 * height) - (5 * age) + 5
    calorie2 = calorie(weight, height, age)
    print(f"Your daily calorie intake is: {calorie2}")
    print(f"protein : {weight}g")
    print(f"carbs : {weight*5}g")
    print("fat : %.2fg"%(calorie2*0.3*0.129598))
    print("water should drink : %.2fL"%(weight*0.033))
    print("water should not drink over : %.2fL"%(weight*0.044)) #line 1-22 by worawut