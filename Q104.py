from datetime import datetime

# Write a script that gets the current date and time and formats it as YYYY-
# MM-DD HH:MM:SS.
# Get the current date and time
now = datetime.now()

# Format the date and time as YYYY-MM-DD HH:MM:SS
formatted_now = now.strftime("%Y-%m-%d %H:%M:%S")

# Print the formatted date and time
print(formatted_now)