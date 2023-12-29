# Function to convert time into seconds
def convert_to_seconds(time):
    h, m, s = map(int, time.split(':'))
    return h * 3600 + m * 60 + s

# Function to convert seconds into time
def convert_to_time(seconds):
    h = seconds // 3600
    m = (seconds % 3600) // 60
    s = seconds % 60
    return h, m, s

# Start and end times
start_time = input()
end_time = input()    

# Convert times into seconds
start_seconds = convert_to_seconds(start_time)
end_seconds = convert_to_seconds(end_time)

# If end time is earlier than start time, add 24 hours to end time
if end_seconds < start_seconds:
    end_seconds += 24 * 60 * 60 

# Calculate difference
diff_seconds = end_seconds - start_seconds

# Convert difference back into time
hours, minutes, seconds = convert_to_time(diff_seconds)



# Define new_hours, new_minutes, and new_seconds
new_hours = hours
new_minutes = minutes
new_seconds = seconds

# for edit result (0 -> 00 or 7 -> 07)
if hours < 10 : 
    new_hours = '0{}'.format(hours)

if minutes < 10 : 
    new_minutes = '0{}'.format(minutes)

if seconds < 10 : 
    new_seconds = '0{}'.format(seconds)

print(f"{new_hours}:{new_minutes}:{new_seconds}")