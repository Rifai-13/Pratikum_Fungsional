
import getpass

# Database storage (as dictionary)
accounts = {}  # Format: {nim: password}
profiles = {}  # Format: {nim: {'name': 'John Doe', 'role': 'user', 'phone': '08512345678'}}
friends = {}   # Format: {nim: ['friend1', 'friend2', ...]}

# Function to register a new user
def register():
    nim = input("Enter your NIM: ")
    if nim in accounts:
        print("NIM already registered. Try logging in.")
        return

    password = getpass.getpass("Enter your password: ")
    accounts[nim] = password
    print("Registration successful!")
    
    # Ask user if they want to skip filling profile and friends list
    choice = input("Would you like to fill your profile now? (yes/skip): ").lower()
    if choice == "yes":
        fill_profile(nim)
        add_friends(nim)
    else:
        print("You can complete your profile and friends list later.")

# Function to login a user
def login():
    nim = input("Enter your NIM: ")
    password = getpass.getpass("Enter your password: ")
    
    if nim in accounts and accounts[nim] == password:
        print("Login successful!")
        user_menu(nim)
    else:
        print("Invalid NIP or password.")

# Function to fill or edit user profile
def fill_profile(nim):
    name = input("Enter your name: ")
    role = input("Enter your role (e.g., employee): ")
    phone = input("Enter your phone number: ")
    
    profiles[nim] = {'name': name, 'role': role, 'phone': phone}
    print("Profile updated successfully!")

# Function to display profile in a formatted way
def view_profile(nim):
    if nim in profiles:
        profile = profiles[nim]
        print("\n-- Your Profile --")
        print(f"Name      : {profile.get('name', 'Not provided')}")
        print(f"Role      : {profile.get('role', 'Not provided')}")
        print(f"Phone     : {profile.get('phone', 'Not provided')}")
    else:
        print("Profile not found. Please complete your profile.")

    if nim in friends:
        print("\n-- Your Friends List --")
        for index, friend in enumerate(friends[nim], start=1):
            print(f"{index}. {friend}")
    else:
        print("No friends added yet.")

        
# Function to add friends
def add_friends(nim):
    if nim not in friends:
        friends[nim] = []
    
    while True:
        friend = input("Enter friend's name (or type 'done' to finish): ")
        if friend.lower() == "done":
            break
        friends[nim].append(friend)
        print(f"Added {friend} to your friends list.")

# Function to edit profile or friends list
def edit_profile(nim):
    if nim not in profiles:
        print("No profile found, please create one")
    fill_profile(nim)

def edit_friends(nim):
    if nim not in friends:
        print("No friends list found, please add one")
    add_friends(nim)

# Function to delete profile or friends
def delete_profile(nim):
     if nim in profiles:
        profile = profiles[nim]
        print("\n-- Select the profile data you want to delete --")
        print(f"1. Name: {profile['name']}")
        print(f"2. Role: {profile['role']}")
        print(f"3. Phone: {profile['phone']}")
        print("4. Cancel")
        
        choice = input("Choose an option: ")
        
        if choice == '1':
            del profiles[nim]['name']
            print("Name deleted.")
        elif choice == '2':
            del profiles[nim]['role']
            print("Role deleted.")
        elif choice == '3':
            del profiles[nim]['phone']
            print("Phone deleted.")
        elif choice == '4':
            print("Cancelled.")
        else:
            print("Invalid option.")
     else:
        print("Profile not found.")

def delete_friends(nim):
    if nim in friends:
        print(f"Your current friends list: {friends[nim]}")
        friend = input("Enter the friend's name to delete: ")
        if friend in friends[nim]:
            friends[nim].remove(friend)
            print(f"{friend} removed from friends list.")
        else:
            print("Friend not found.")
    else:
        print("No friends list found.")

# User menu after login
def user_menu(nim):
    while True:
        print("\n-- User Menu --")
        print("1. View Profile")
        print("2. Edit Profile")
        print("3. Add/Edit Friends List")
        print("4. Delete Profile")
        print("5. Delete Friend")
        print("6. Logout")
        choice = input("Choose an option: ")

        if choice == '1':
            view_profile(nim)
        elif choice == '2':
            edit_profile(nim)
        elif choice == '3':
            edit_friends(nim)
        elif choice == '4':
            delete_profile(nim)
        elif choice == '5':
            delete_friends(nim)
        elif choice == '6':
            print("Logged out.")
            break
        else:
            print("Invalid option.")
# Main menu
def main():
    while True:
        print("\n-- Main Menu --")
        print("1. Register")
        print("2. Login")
        print("3. Exit")
        choice = input("Choose an option: ")

        if choice == '1':
            register()
        elif choice == '2':
            login()
        elif choice == '3':
            print("Goodbye!")
            break
        else:
            print("Invalid option.")

# Run the main program
main()
