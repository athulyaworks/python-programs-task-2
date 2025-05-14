import smtplib
import csv
import datetime
import time
import os
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
from pathlib import Path

class BirthdayEmailSender:
    def __init__(self, email_address, password, csv_file_path):
        """
        Initialize the BirthdayEmailSender with email credentials and contacts file
        
        Args:
            email_address: Your email address to send from
            password: Your email password or app password
            csv_file_path: Path to CSV file with birthday contacts
        """
        self.email_address = email_address
        self.password = password
        self.csv_file_path = csv_file_path
        
        # Ensure CSV file exists or create it
        if not os.path.exists(csv_file_path):
            with open(csv_file_path, 'w', newline='') as file:
                writer = csv.writer(file)
                writer.writerow(['name', 'email', 'birthday', 'last_sent'])
            print(f"Created new contacts file at {csv_file_path}")

    def check_birthdays(self):
        """Check for birthdays today and send emails accordingly"""
        today = datetime.datetime.now().strftime('%m-%d')
        today_year = datetime.datetime.now().strftime('%Y')
        
        print(f"Checking for birthdays on {today}...")
        
        birthdays_today = []
        
        # Read the CSV file
        with open(self.csv_file_path, 'r') as file:
            reader = csv.DictReader(file)
            rows = list(reader)  # Convert to list for modification
            
            for i, row in enumerate(rows):
                name = row['name']
                email = row['email']
                birthday = row['birthday']  # Expected format: MM-DD
                last_sent = row['last_sent']
                
                # Check if today is their birthday and we haven't sent an email this year
                if birthday == today and last_sent != today_year:
                    print(f"Today is {name}'s birthday!")
                    self.send_birthday_email(name, email)
                    
                    # Update the 'last_sent' field to the current year
                    rows[i]['last_sent'] = today_year
                    birthdays_today.append(name)
        
        # Update the CSV file with the new 'last_sent' values
        if birthdays_today:
            with open(self.csv_file_path, 'w', newline='') as file:
                writer = csv.DictWriter(file, fieldnames=['name', 'email', 'birthday', 'last_sent'])
                writer.writeheader()
                writer.writerows(rows)
            
            print(f"Sent birthday emails to: {', '.join(birthdays_today)}")
        else:
            print("No birthdays today!")

    def send_birthday_email(self, name, email):
        
        # Create message
        msg = MIMEMultipart()
        msg['From'] = self.email_address
        msg['To'] = email
        msg['Subject'] = f"Happy Birthday, {name}! 🎂"
        
        # Email body
        body = f"""Dear {name},

Happy Birthday! 🎉

Wishing you a fantastic day filled with joy and celebration!

Best wishes,
{self.email_address.split('@')[0]}
"""
        msg.attach(MIMEText(body, 'plain'))
        
        try:
            # Connect to the SMTP server (for Gmail)
            server = smtplib.SMTP('smtp.gmail.com', 587)
            server.starttls()
            server.login(self.email_address, self.password)
            
            # Send email
            server.send_message(msg)
            server.quit()
            print(f"Birthday email sent to {name} at {email}")
        except Exception as e:
            print(f"Failed to send email to {name}: {e}")

    def add_birthday(self, name, email, birthday):
        
        with open(self.csv_file_path, 'a', newline='') as file:
            writer = csv.writer(file)
            writer.writerow([name, email, birthday, ''])
        print(f"Added {name}'s birthday ({birthday}) to the contact list")
    
    def list_all_birthdays(self):
        """Print all birthdays in the CSV file"""
        with open(self.csv_file_path, 'r') as file:
            reader = csv.DictReader(file)
            print("\nBirthday List:")
            print("-" * 50)
            for row in reader:
                print(f"{row['name']}: {row['email']} (Birthday: {row['birthday']})")
            print("-" * 50)

def main():
    """Main function to run the birthday email sender"""
    # Configuration
    EMAIL = input("Enter your email address: ")
    PASSWORD = input("Enter your email password or app-specific password: ")
    
    # Use a sensible default path for the CSV file
    default_path = os.path.join(Path.home(), "birthday_contacts.csv")
    csv_path = input(f"Enter path for contacts CSV file (default: {default_path}): ") or default_path
    
    # Create the birthday email sender
    sender = BirthdayEmailSender(EMAIL, PASSWORD, csv_path)
    
    while True:
        print("\n===== Birthday Email Sender =====")
        print("1. Check for birthdays today and send emails")
        print("2. Add a new birthday")
        print("3. List all birthdays")
        print("4. Exit")
        
        choice = input("\nEnter your choice (1-4): ")
        
        if choice == '1':
            sender.check_birthdays()
        
        elif choice == '2':
            name = input("Enter person's name: ")
            email = input("Enter person's email: ")
            birthday = input("Enter birthday (MM-DD format, e.g., 01-15): ")
            sender.add_birthday(name, email, birthday)
        
        elif choice == '3':
            sender.list_all_birthdays()
        
        elif choice == '4':
            print("Exiting program. Goodbye!")
            break
        
        else:
            print("Invalid choice. Please try again.")

if __name__ == "__main__":
    main()