def format_time(hour):
    if hour == 0:
        return "12:00 Midnight"
    elif hour == 12:
        return "12:00 Noon"
    elif hour < 12:
        return f"{hour}:00 AM"
    else:
        return f"{hour - 12}:00 PM"

# Print 24 hours of the day with suffixes
for hour in range(24):
    print(format_time(hour))
