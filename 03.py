## Calculate age in seconds

print(time())
print(times())

print("Calculate your age in seconds!")
year = input("What year were you born? (YYYY) ")
if len(str(year)) == 2:
    yearStr = str(year)
    q = str(input("You were born in 19" + yearStr + "? (y/n)"))
    if q == "n":
        year = input("What year were you born? (YYYY) ")
month = input("What month were you born? (MM) ")
day = input("What day where you born? (DD) ")
