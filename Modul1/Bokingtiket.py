import getpass

# Constants
DESTINATIONS = [
    ("Jakarta", "Surabaya", 120),
    ("Jakarta", "Bali", 150),
    ("Surabaya", "Medan", 200),
    ("Medan", "Jakarta", 180),
    ("Bali", "Surabaya", 170)
]

def register(accounts, profiles, booking_for_others):
    nik = input("Masukkan NIK: ")
    if nik in accounts:
        print("NIK sudah terdaftar. Coba masuk lagi")
        return accounts, profiles, booking_for_others

    name = input("Masukan Nama: ")
    password = getpass.getpass("Masukkan password: ")
    accounts[nik] = {'name': name, 'password': password}
    print("Registration successful!")

    choice = input("apakah anda ingin melengkapi profil? (yes/skip): ").lower()
    if choice == "yes":
        profiles, booking_for_others = fill_profile(nik, profiles, booking_for_others)
    return accounts, profiles, booking_for_others

def fill_profile(nik, profiles, booking_for_others):
    name = input("Masukkan Nama: ")
    role = input("Enter your role (e.g., employee): ")
    phone = input("Masukkan phone number: ")

    profiles[nik] = {'name': name, 'role': role, 'phone': phone}
    print("Profile updated successfully!")

    booking_for_others = add_booking_for_others(nik, booking_for_others)
    return profiles, booking_for_others

def add_booking_for_others(nik, booking_for_others):
    if nik not in booking_for_others:
        booking_for_others[nik] = []

    people = []
    while True:
        person = input("Masukkan Nama orang yang akan dibook tiket (or type 'done' to finish): ")
        if person.lower() == "done":
            break
        people.append(person)

    booking_for_others[nik].extend(people)
    print(f"Added {people} to your booking list.")
    return booking_for_others

def delete_profile(nik, profiles, booking_for_others):
    if nik not in profiles:
        print("Profil tidak ditemukan.")
        return profiles, booking_for_others

    print("\n-- Pilih data yang ingin dihapus --")
    options = [
        ('1', 'name', profiles[nik].get('name')),
        ('2', 'role', profiles[nik].get('role')),
        ('3', 'phone', profiles[nik].get('phone'))
    ]

    valid_options = {opt[0] for opt in options if opt[2] is not None}

    for opt in options:
        if opt[2] is not None:
            print(f"{opt[0]}. {opt[1].capitalize()}: {opt[2]}")
    print("4. Cancel")

    choice = input("Choose an option: ")

    if choice in valid_options:
        updated_profile = {k: v for k, v in profiles[nik].items() if k != options[int(choice)-1][1]}
        profiles[nik] = updated_profile
        print(f"{options[int(choice)-1][1].capitalize()} deleted.")
    elif choice == '4':
        print("Dibatalkan.")
    else:
        print("Invalid option.")

    return profiles, booking_for_others

def delete_booking_for_others(nik, booking_for_others):
    if nik not in booking_for_others or not booking_for_others[nik]:
        print("No one is on your booking list.")
        return booking_for_others

    print("\n-- Daftar orang yang akan dibook Tiket --")
    for index, person in enumerate(booking_for_others[nik], start=1):
        print(f"{index}. {person}")

    choice = input("Masukkan nomor orang yang ingin dihapus (or type 'cancel' to exit): ")

    if choice.lower() == 'cancel':
        return booking_for_others

    try:
        person_index = int(choice) - 1
        if 0 <= person_index < len(booking_for_others[nik]):
            removed_person = booking_for_others[nik].pop(person_index)
            print(f"{removed_person} Berhasil dihapus dari riwayat pemesanan.")
        else:
            print("Invalid person number.")
    except ValueError:
        print("Invalid input, please enter a number.")

    return booking_for_others

def book_flight(nik, bookings, destinations):
    print("\n-- Penerbangan Tersedia --")
    for index, (origin, destination, price) in enumerate(destinations, start=1):
        print(f"{index}. {origin} to {destination} - ${price}")

    choice = input("Masukkan nomor penerbangan (or type 'cancel' to exit): ")

    if choice.lower() == 'cancel':
        return bookings

    try:
        flight_index = int(choice) - 1
        if 0 <= flight_index < len(destinations):
            origin, destination, price = destinations[flight_index]
            bookings[nik] = bookings.get(nik, []) + [f"{origin} to {destination} - ${price}"]
            print(f"You have booked: {origin} to {destination} for ${price}")
        else:
            print("Invalid flight number.")
    except ValueError:
        print("Invalid input, please enter a number.")

    return bookings

def view_profile(nik, profiles, booking_for_others):
    if nik in profiles:
        profile = profiles[nik]
        print("\n-- Your Profile --")
        print(f"Name: {profile.get('name', 'Not provided')}")
        print(f"Role: {profile.get('role', 'Not provided')}")
        print(f"Phone: {profile.get('phone', 'Not provided')}")
    else:
        print("Profil tidak ditemukan. Silahkan lengkapi profil.")

    if nik in booking_for_others:
        print("\n-- Daftar orang yang akan dibook Tiket --")
        for index, person in enumerate(booking_for_others[nik], start=1):
            print(f"{index}. {person}")
    else:
        print(f"Belum ada orang yang ditambahkan.")

def view_bookings(nik, bookings):
    if nik in bookings and bookings[nik]:
        print("\n-- Riwayat Pemesanan --")
        for index, booking in enumerate(bookings[nik], start=1):
            print(f"{index}. {booking}")
    else:
        print("No booking history found.")

def delete_booked_flight(nik, bookings):
    if nik in bookings and bookings[nik]:
        print("\n-- Riwayat Pemesanan --")
        for index, booking in enumerate(bookings[nik], start=1):
            print(f"{index}. {booking}")

        choice = input("Masukkan nomor penerbangan yang ingin dihapus (or type 'cancel' to exit): ")

        if choice.lower() == 'cancel':
            return bookings

        try:
            flight_index = int(choice) - 1
            if 0 <= flight_index < len(bookings[nik]):
                removed_booking = bookings[nik].pop(flight_index)
                print(f"{removed_booking} Berhasil dihapus dari riwayat pemesanan.")
            else:
                print("Invalid flight number.")
        except ValueError:
            print("Invalid input, please enter a number.")

        return bookings
    else:
        print("No booking history found.")
        return bookings


def user_menu(nik, accounts, profiles, booking_for_others, bookings, destinations):
    while True:
        print("\n-- User Menu --")
        print("1. View Profile")
        print("2. Edit Profile")
        print("3. Add Orang yang akan dibook tiket")
        print("4. Book Flight")
        print("5. Delete Profile")
        print("6. Delete Orang dari booking list")
        print("7. View Booking History")
        print("8. Delete Booked Flight")
        print("9. Logout")
        choice = input("Pilih opsi: ")

        if choice == '1':
            view_profile(nik, profiles, booking_for_others)
        elif choice == '2':
            profiles, booking_for_others = fill_profile(nik, profiles, booking_for_others)
        elif choice == '3':
            booking_for_others = add_booking_for_others(nik, booking_for_others)
        elif choice == '4':
            bookings = book_flight(nik, bookings, destinations)
        elif choice == '5':
            profiles, booking_for_others = delete_profile(nik, profiles, booking_for_others)
            print("Profile deleted, logging out.")
            break
        elif choice == '6':
            booking_for_others = delete_booking_for_others(nik, booking_for_others)
        elif choice == '7':
            view_bookings(nik, bookings)
        elif choice == '8':
            bookings = delete_booked_flight(nik, bookings)
        elif choice == '9':
            print("Logged out.")
            break
        else:
            print("Invalid option.")

    return accounts, profiles, booking_for_others, bookings
def main():
    accounts = {}
    profiles = {}
    booking_for_others = {}
    bookings = {}

    while True:
        print("\n-- Main Menu --")
        print("1. Register")
        print("2. Login")
        print("3. Exit")
        choice = input("Choose an option: ")

        if choice == '1':
            accounts, profiles, booking_for_others = register(accounts, profiles, booking_for_others)
        elif choice == '2':
            nik = input("Masukkan NIK: ")
            if nik in accounts:
                password = getpass.getpass("Masukkan password: ")
                if accounts[nik]['password'] == password:
                    accounts, profiles, booking_for_others, bookings = user_menu(
                        nik, accounts, profiles, booking_for_others, bookings, DESTINATIONS
                    )
                else:
                    print("Password salah.")
            else:
                print("NIK tidak terdaftar.")
        elif choice == '3':
            print("Goodbay.")
            break
        else:
            print("Invalid option.")

main()
