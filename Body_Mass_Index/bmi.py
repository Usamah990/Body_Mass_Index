import emoji

# welcome message and introduction to the Body Mass Index and how it works
print("Welcome!")
print("This is BMI Calculator Made by Usamah As Salafi.")
print(" ")
print("""Body Mass Index (BMI) is a person's weight in kilograms (or pounds) 
divided by the square of height in meters (or feet). 
A high BMI can indicate high body fatness. BMI screens for weight categories that may lead to health problems, 
but it does not diagnose the body fatness or health of an individual. """)
print(" ")

# asking for user name (optional), sex, height, and weight measured in cm & kg
name = input("What's your name? (optional) ")

gender = input("Are you a Female or Male? ")
male = "Male"
female = "Female"
while gender != male and gender != "male" and gender != female and gender != "female":
    print("=================")
    gender = input("""wrong inputs.
    re-type here: """)

height = int(input("Height(cm) : "))
height2 = height / 100
meter_height = height2 * height2

weight = int(input("Weight(kg) : "))
print(" ")

# BMI results goes here
results = weight / meter_height
print("====================================")

print(f'Alright {name}, so this is the results! '+ emoji.emojize(":smiling_face_with_hearts:"))

print("Your BMI: ", round(results, 2))
if gender == male or gender == "male":
    print("Your ideal weight is: ", (height-100) - (height-100) * 0.1)
elif gender == female or gender == "female":
    print("Your ideal weight is: ", (height - 100) - (height - 100) * 0.15)

print("====================================")
