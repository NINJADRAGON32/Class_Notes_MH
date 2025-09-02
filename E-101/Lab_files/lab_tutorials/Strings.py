

age_years = int(input("Enter your age: "))
age_min = age_years*365*24*60
age_sec = age_min*60
print("your age in minutes is: ",age_min)
print("your age in seconds is: ",age_sec)
total_HB = age_min * 67
print(f"your heart has beat a total of {total_HB} times")
