# Initialize a set to store safe trap IDs
safe_traps = set()

# Read the log data from the file
with open(r'03_trap_logs.txt', 'r') as file:
    trap_logs = file.readlines()

# Define a function to check if a trap is safe
def is_safe(log):
    # Split the log into individual words
    words = log.split()

    # Define the categories of words
    safe_keywords = {'inactive', 'disabled', 'quiet', 'standby', 'idle'}
    unsafe_keywords = {'live', 'armed', 'ready', 'primed', 'active'}
    change_keywords = {'flipped', 'toggled', 'reversed', 'inverted', 'switched'}

    # Initialize the state as inactive (safe)
    state = 'inactive'

    # Process each word in the log
    for word in words:
        if word in safe_keywords:
            state = 'inactive'
        elif word in unsafe_keywords:
            state = 'active'
        elif word in change_keywords:
            state = 'active' if state == 'inactive' else 'inactive'

    # A trap is safe if it ends in the 'inactive' state
    return state == 'inactive'

# Iterate through trap logs and identify safe traps
for line in trap_logs:
    trap_id, log = line.strip().split(': ')
    if is_safe(log):
        safe_traps.add(int(trap_id))

# Print the IDs of safe traps
print("Safe trap IDs:")
for trap_id in safe_traps:
    print(trap_id)

# Calculate the sum of safe trap IDs
result = sum(safe_traps)

# Print the result
print("The sum of safe trap IDs is:", result)
