import os
import time
import random
import sys
import shutil

# Global variable for logging commands
command_log = []

def lag_simulation():
    print("Wait...")
    for _ in range(10):
        time.sleep(random.uniform(0.1, 0.5))  # Simulate random processing time
        print(".", end='', flush=True)
    print("\nComplete!")

def generate_random_ip():
    return ''.join(random.choice('0123456789') for _ in range(10))

def get_random_location():
    locations = [
        "New York, USA",
        "Tokyo, Japan",
        "Paris, France",
        "Sydney, Australia",
        "Rio de Janeiro, Brazil",
        "Cape Town, South Africa",
        "Mumbai, India",
        "Moscow, Russia",
        "Toronto, Canada",
        "Dubai, UAE",
        "Buenos Aires, Argentina",
        "Seoul, South Korea",
    ]
    return random.choice(locations)

def authenticate():
    allowed_users = {"user": "password123"}  # Hardcoded username and password for demonstration
    max_attempts = 3

    for _ in range(max_attempts):
        username = input("Enter your username: ")
        password = input("Enter your password: ")

        if username in allowed_users and allowed_users[username] == password:
            print("Authentication successful!")
            return True

        print("Invalid username or password. Please try again.")

    print("Max attempts reached. Exiting.")
    sys.exit()

def display_commands():
    banner = """
    ██╗░░██╗██╗░░██╗░░░░░░░██╗░░░░░░░██╗░█████╗░██████╗░███████╗
    ██║░░██║╚██╗██╔╝░░░░░░░██║░░██╗░░██║██╔══██╗██╔══██╗██╔════╝
    ███████║░╚███╔╝░█████╗░╚██╗████╗██╔╝███████║██████╔╝█████╗░░
    ██╔══██║░██╔██╗░╚════╝░░████╔═████║░██╔══██║██╔══██╗██╔══╝░░
    ██║░░██║██╔╝╚██╗░░░░░░░░╚██╔╝░╚██╔╝░██║░░██║██║░░██║███████╗
    ╚═╝░░╚═╝╚═╝░░╚═╝░░░░░░░░░╚═╝░░░╚═╝░░╚═╝░░╚═╝╚═╝░░╚═╝╚══════╝
    """
    print(banner)
    print("Welcome to the Software")
    print("------------------------")

def display_help():
    print("Available commands:")
    print("connect discord = Connecting to Discord client")
    print("ip = Generate a random IP address")
    print("find ip [1-100] = Find a specified amount of random IPs")
    print("lag [10-digit-code] = Simulate a loading process")
    print("shut = Close the software")
    print("help = Display this help message")
    print("chat = Enter the chat room")
    print("exit = Exit the chat room")
    print("location = Get a random location in the world")
    print("time = Display the current time")
    print("log = Display the command log")
    print("save log = Save the command log to a file")
    print("delete log = Delete the command log file")
    print("all save = Save configuration and code to a .cfg file and create subfolders")
    print("exe = Generate standalone executable")

def chat_room():
    print("Welcome to the Chat Room! Type 'exit' to go back.")
    while True:
        user_input = input("You: ")
        if user_input.lower() == 'exit':
            break
        else:
            print("Bot is typing...")
            time.sleep(random.uniform(1, 3))  # Simulate bot response delay
            bot_response = generate_random_chat()
            print(f"Bot: {bot_response}")
            # Log the chat command
            command_log.append(f"You: {user_input}\nBot: {bot_response}\n")

def generate_random_chat():
    possible_responses = [
        "Hello!",
        "How are you?",
        "What's your favorite color?",
        "Nice weather today, isn't it?",
        "I like programming!",
        "Tell me a joke!",
        "Random response!",
        "How's your day going?",
        "What's your favorite food?",
        # ... (remaining responses)
    ]
    return random.choice(possible_responses)

def get_current_time():
    return time.strftime("%H:%M:%S")

def log_command(command):
    command_log.append(command)

def save_log_to_file():
    folder_path = "HX-Ware"
    if not os.path.exists(folder_path):
        os.makedirs(folder_path)

    file_path = os.path.join(folder_path, "command_log.txt")
    with open(file_path, "w") as file:
        for command in command_log:
            file.write(command)
            file.write("\n")
    print(f"Command log saved to '{file_path}'")

def delete_log_file():
    file_path = os.path.join("HX-Ware", "command_log.txt")
    try:
        os.remove(file_path)
        print(f"Command log file '{file_path}' deleted.")
    except FileNotFoundError:
        print(f"Command log file '{file_path}' not found.")

def save_configuration_and_code():
    folder_path = "HX-Ware"
    if not os.path.exists(folder_path):
        os.makedirs(folder_path)

    # Save configuration to .cfg file
    cfg_file_path = os.path.join(folder_path, "config.cfg")
    with open(cfg_file_path, "w") as cfg_file:
        cfg_file.write("Software Configuration\n")
        cfg_file.write("-----------------------\n")
        cfg_file.write("Date: " + time.strftime("%Y-%m-%d %H:%M:%S") + "\n")
        cfg_file.write("User: [Your Username]\n")
        # Add more configuration details as needed

    print(f"Configuration saved to '{cfg_file_path}'")

    # Save raw code to Raw folder
    raw_code_folder = os.path.join(folder_path, "Raw")
    if not os.path.exists(raw_code_folder):
        os.makedirs(raw_code_folder)

    raw_code_file_path = os.path.join(raw_code_folder, "raw_code.txt")
    with open(raw_code_file_path, "w") as raw_code_file:
        with open(__file__, "r") as current_file:
            raw_code_file.write(current_file.read())

    print(f"Raw code saved to '{raw_code_file_path}'")

    # Save code to PY folder as .py file
    py_code_folder = os.path.join(folder_path, "PY")
    if not os.path.exists(py_code_folder):
        os.makedirs(py_code_folder)

    py_code_file_path = os.path.join(py_code_folder, "hx_ware.py")
    shutil.copy(__file__, py_code_file_path)

    print(f"Code saved to '{py_code_file_path}'")

def generate_exe():
    # Run PyInstaller to create the standalone executable
    os.system("pyinstaller --onefile " + __file__)

    # Move the generated executable to the HX-Ware folder
    exe_file_path = os.path.join("dist", "hx_ware.exe")
    hx_ware_folder = os.path.join(os.getcwd(), "HX-Ware")
    shutil.move(exe_file_path, hx_ware_folder)

    print(f"Executable file generated and moved to '{hx_ware_folder}'")

# Display initial information
display_commands()

# Authenticate the user
authenticate()

while True:
    user_input = input("Enter a command: ")
    
    # Log all commands
    log_command(user_input)

    if user_input.lower() == "connect discord":
        # Connect to Discord logic
        print("Connecting to Discord client... Successfully connected!")
    elif user_input.upper() == "IP":
        random_ip = generate_random_ip()
        print(f"Random IP: {random_ip}")
    elif user_input.lower().startswith("find ip"):
        try:
            amount = int(user_input.split()[-1])
            ips = [generate_random_ip() for _ in range(amount)]
            print(f"Generated {amount} random IPs:")
            for ip in ips:
                print(ip)
        except ValueError:
            print("Invalid input. Please provide a valid number after 'find ip'.")
    elif user_input.lower().startswith("lag"):
        lag_code = user_input.split()[-1]
        if len(lag_code) == 10 and lag_code.isdigit():
            lag_simulation()
        else:
            print("Invalid code. Please provide a 10-digit code after 'lag'.")
    elif user_input.lower() == "shut":
        print("Closing the software. Goodbye!")
        save_log_to_file()  # Save log before exiting
        sys.exit()
    elif user_input.lower() == "help":
        display_help()
    elif user_input.lower() == "chat":
        chat_room()
    elif user_input.lower() == "location":
        print(f"Random Location: {get_random_location()}")
    elif user_input.lower() == "time":
        print(f"Current Time: {get_current_time()}")
    elif user_input.lower() == "log":
        print("Command Log:")
        for command in command_log:
            print(command)
    elif user_input.lower() == "save log":
        save_log_to_file()
    elif user_input.lower() == "delete log":
        delete_log_file()
    elif user_input.lower() == "all save":
        save_configuration_and_code()
    elif user_input.lower() == "exe":
        generate_exe()
    else:
        print("Command not recognized.")
