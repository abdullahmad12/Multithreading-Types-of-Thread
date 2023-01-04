import threading

def input_thread():
  while True:
    try:
      # Take input from user
      input_str = input("Enter a string: ")
    except EOFError:
      # If the input thread receives an EOFError, break out of the loop
      break
    except Exception as e:
      # If any other exception is raised, print the exception and continue the loop
      print(e)
      continue
    # Set the input string as a global variable so that the other threads can access it
    global input_string
    input_string = input_str
    # Notify the other threads that the input is ready
    input_ready.set()

def reverse_thread():
  while True:
    # Wait for the input to be ready
    input_ready.wait()
    # Reverse the input string
    reversed_string = input_string[::-1]
    # Print the reversed string
    print("Reversed string:", reversed_string)
    # Clear the input_ready event
    input_ready.clear()

def capital_thread():
  while True:
    # Wait for the input to be ready
    input_ready.wait()
    # Capitalize the input string
    capitalized_string = input_string.upper()
    # Print the capitalized string
    print("Capitalized string:", capitalized_string)
    # Clear the input_ready event
    input_ready.clear()

def shift_thread():
  while True:
    # Wait for the input to be ready
    input_ready.wait()
    # Shift the characters in the input string by two
    shifted_string = ""
    for c in input_string:
      shifted_string += chr(ord(c) + 2)
    # Print the shifted string
    print("Shifted string:", shifted_string)
    # Clear the input_ready event
    input_ready.clear()

# Create a global event to signal when the input is ready
input_ready = threading.Event()

# Create the input, reverse, capital, and shift threads
input_t = threading.Thread(target=input_thread)
reverse_t = threading.Thread(target=reverse_thread)
capital_t = threading.Thread(target=capital_thread)
shift_t = threading.Thread(target=shift_thread)

# Start the threads
input_t.start()
reverse_t.start()
capital_t.start()
shift_t.start()

# Wait for the input thread to finish
input_t.join()

# Notify the other threads to exit
input_ready.set()

# Wait for the other threads to finish
reverse_t.join()
capital_t.join()
shift_t.join()
