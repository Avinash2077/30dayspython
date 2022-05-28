#Day 2: 30 days of python programming
first_name="Venkata"
last_name ="Avinash"
full_name="Venkata Avinash Mudragada"
country = "India"
city = "Ongole"
age = 21
year = 2000
is_married = "not married"
is_true = True
is_light_on = 'no'

#Check the data type of all your variables using type() built-in function
print(type(first_name))
print(type(last_name))
print(type(full_name))
print(type(country))
print(type(city))
print(type(age))
print(type(year))
print(type(is_married))
print(type(is_true))
print(type(is_light_on))

#Using the len() built-in function, find the length of your first name
print(len(first_name))

#Compare the length of your first name and your last name
print(len(first_name))
print(len(last_name))
print(len(first_name),"vs",len(last_name))

#Declare 5 as num_one and 4 as num_two

num_one ,num_two=5,4
total=num_one+num_two
diff=num_one-num_two
product =num_one*num_two
division = num_one/num_two
remainder = num_one%num_two
exp = pow(num_one, num_two)
floor_division = num_one//num_two
print("Total of two numbers is:",total)
print("difference of two numbers is:",diff)
print("product of two numbers is:",product)
print("division of two numbers is:",division)
print("remainder of two numbers is:",remainder)
print("exp of two numbers is:",exp)
print("floor division of two numbers is:",floor_division)\


#Calculate the area of a circle and assign the value to a variable name of area_of_circle

radius =int(input("enter the radius:"))

area_of_circle=3.145*radius*radius
circum_of_circle = 2*3.145*radius
print("Area of the circle is:",area_of_circle)
print("Circumference of the circle is:",circum_of_circle)
