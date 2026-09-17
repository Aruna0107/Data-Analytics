weight=float(input("enter weight in kg:"))
unit=input("enter height unit (cm/feet):")
height=float(input("enter height:"))
if unit=="cm":
    height=height/100
elif unit=="feet":
    height=height*0.3048
else:
    print("invalid unit")
bmi=weight/(height*height)
print("bmi=",bmi)
if bmi<18.5:
    print("underweight")
elif bmi<25:
    print("normal weight")
elif bmi<30:
    print("overweight")
else:
    print("obese")
