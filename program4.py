'''#display sundays you lived till now
a=int(input("Enter date: "))
b=int(input("Enter month: "))
c=int(input("Enter year: "))'''
# Replace 'YYYY-MM-DD' with your actual birth date in the format 'YYYY-MM-DD'
birth_date_str = '2005-11-03'

# Convert the birth date string to year, month, and day integers
birth_year, birth_month, birth_day = map(int, birth_date_str.split('-'))

# Initialize counters
sunday_count = 0
days_in_month = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]

# Function to check if a year is a leap year
def is_leap_year(year):
    return (year % 4 == 0 and year % 100 != 0) or (year % 400 == 0)

# Iterate through each year
for year in range(birth_year, 2023):  # Change 2023 to the current year
    # Iterate through each month
    for month in range(1, 13):
        # Get the number of days in the current month
        if month == 2 and is_leap_year(year):
            days_in_month[1] = 29
        else:
            days_in_month[1] = 28
        
        # Iterate through each day
        for day in range(1, days_in_month[month - 1] + 1):
            # Check if the current day is a Sunday and after the birth date
            if day == 1 and month >= birth_month and year >= birth_year:
                sunday_count += 1
    
# Print the result
print(f"You have lived through {sunday_count} Sundays.")
