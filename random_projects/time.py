import time

# Generate a list of 1 billion strings (for demonstration, we'll use a smaller number)
num_strings = 10**9
strings = ["string"] * num_strings

# Measure the time taken to iterate over the list
start_time = time.time()
for s in strings:
    pass  # No operation, just iteration
end_time = time.time()

elapsed_time = end_time - start_time
print(f"Time taken to iterate over {num_strings} strings: {elapsed_time} seconds")
