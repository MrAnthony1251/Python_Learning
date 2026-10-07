# Logical Operators = evaluate multiple conditions 
# or = at least one condition must be True
# and = both conditions must be true
# not = inverts the condition (not False, not True)


# Or

temp = 20
is_raining = True

if temp > 20 or temp < 0 or is_raining:
    print("The outdoor event is cancelled")
else: 
    print("the outdoor event is still scheduled")


#and

temp = 20
is_sunny = True

if temp >= 28 and is_sunny:
    print("It is hot outside")
    print("It is Sunny")
elif temp <= 0 and is_sunny:
    print("It is cold Outside")
    print("It is Sunny")
elif 28 > temp > 0 and is_sunny:
    print("It is warm outside")
    print("It is Sunny")
elif temp <= 0 and not is_sunny:
    print("It is cold Outside")
    print("It is Sunny")
elif 28 > temp > 0 and not is_sunny:
    print("It is warm outside")
    print("It is Cloudy")
elif temp <= 0 and not is_sunny:
    print("It is cold Outside")
    print("It is Cloudy")

    
    