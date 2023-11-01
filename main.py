import mysql.connector

# Establish a connection to the MySQL database
db = mysql.connector.connect(
    host="localhost",
    user="root",
    password="your_password",
    database="donaciones"
)
cursor = db.cursor()

def register_donation():
    donation_type = input("Enter type of donation (cash/clothes/food/etc.): ")
    if donation_type.lower() == "cash":
        amount = float(input("Enter donation amount: "))
        # Validate amount logic here
        # Save donation information to the database
        cursor.execute("INSERT INTO donations (type, amount) VALUES (%s, %s)", (donation_type, amount))
        db.commit()
        print("Donation registered successfully!")
    else:
        quality = input("Enter quality of donation (good, etc.): ")
        quantity = int(input("Enter quantity: "))
        # Validate quality and quantity logic here
        # Record detailed donation information and donor information to the database
        cursor.execute("INSERT INTO donations (type, quality, quantity) VALUES (%s, %s, %s)", (donation_type, quality, quantity))
        db.commit()
        print("Donation registered successfully!")

def register_beneficiary():
    # Record beneficiary information to the database
    name = input("Enter beneficiary name: ")
    contact = input("Enter contact number: ")
    reason = input("Enter reason for need: ")
    urgency = input("Is it urgent? (yes/no): ")
    # Record beneficiary information to the database
    cursor.execute("INSERT INTO beneficiaries (name, contact, reason, urgency) VALUES (%s, %s, %s, %s)", (name, contact, reason, urgency))
    db.commit()
    print("Beneficiary registered successfully!")

def register_volunteer():
    # Record volunteer information to the database
    name = input("Enter volunteer name: ")
    contact = input("Enter contact number: ")
    reason = input("Enter reason for volunteering (if available): ")
    # Record volunteer information to the database
    cursor.execute("INSERT INTO volunteers (name, contact, reason) VALUES (%s, %s, %s)", (name, contact, reason))
    db.commit()
    print("Volunteer registered successfully!")

def assign_donations():
    # Logic to assign donations to beneficiaries and save the data in the database
    pass

while True:
    print("1. Register Donation")
    print("2. Register Beneficiary")
    print("3. Register Volunteer")
    print("4. Assign Donations to Beneficiaries")
    print("5. Exit")
    choice = input("Enter your choice: ")

    if choice == "1":
        register_donation()
    elif choice == "2":
        register_beneficiary()
    elif choice == "3":
        register_volunteer()
    elif choice == "4":
        assign_donations()
    elif choice == "5":
        break
    else:
        print("Invalid choice. Please try again.")

# Close the database connection
db.close()

