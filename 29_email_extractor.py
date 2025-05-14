import re
import sys
from pathlib import Path

def extract_emails(file_path):
    """
    Extract all email addresses from a text file using regex
    
    Args:
        file_path: Path to the text file to process
        
    Returns:
        List of email addresses found in the file
    """
    # Email regex pattern
    # This pattern matches most common email formats
    email_pattern = r'[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}'
    
    try:
        # Read the file content
        with open(file_path, 'r', encoding='utf-8', errors='ignore') as file:
            content = file.read()
        
        # Find all matches
        emails = re.findall(email_pattern, content)
        
        # Remove duplicates while preserving order
        unique_emails = []
        for email in emails:
            if email not in unique_emails:
                unique_emails.append(email)
        
        return unique_emails
    
    except FileNotFoundError:
        print(f"Error: File '{file_path}' not found.")
        return []
    except Exception as e:
        print(f"Error: {e}")
        return []

def main():
    """Main function to run the email extractor"""
    # Check if file path is provided as command line argument
    if len(sys.argv) > 1:
        file_path = sys.argv[1]
    else:
        # Ask for file path
        file_path = input("Enter the path to the text file: ")
    
    # Extract emails
    emails = extract_emails(file_path)
    
    # Display results
    if emails:
        print(f"\nFound {len(emails)} unique email addresses:")
        for i, email in enumerate(emails, 1):
            print(f"{i}. {email}")
        
        # Ask if user wants to save results
        save_option = input("\nDo you want to save these emails to a file? (y/n): ").lower()
        if save_option == 'y' or save_option == 'yes':
            output_path = input("Enter output file path (default: emails_extracted.txt): ") or "emails_extracted.txt"
            with open(output_path, 'w') as output_file:
                for email in emails:
                    output_file.write(email + '\n')
            print(f"Emails saved to {output_path}")
    else:
        print("No email addresses found in the file.")

if __name__ == "__main__":
    main()