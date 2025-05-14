import os
import sys
import shutil
from datetime import datetime
from pathlib import Path

def rename_files(directory_path, pattern, start_number=1, preserve_extension=True, preview=True):

    try:
        # Get all files in the directory (excluding directories)
        files = [f for f in os.listdir(directory_path) if os.path.isfile(os.path.join(directory_path, f))]
        
        # Sort files alphabetically
        files.sort()
        
        # Get the current date in YYYYMMDD format
        current_date = datetime.now().strftime("%Y%m%d")
        
        # Track how many files will be renamed
        rename_count = 0
        
        # Preview table headers
        if preview:
            print("\nPREVIEW MODE - No files will be actually renamed\n")
            print(f"{'Original Filename':<40} {'New Filename':<40}")
            print("-" * 80)
        
        # Process each file
        for i, filename in enumerate(files, start=start_number):
            # Get file extension if preserving extensions
            original_ext = ""
            if preserve_extension:
                original_ext = os.path.splitext(filename)[1]
            
            # Create new filename based on pattern
            new_filename = pattern.replace("{n}", str(i))
            new_filename = new_filename.replace("{date}", current_date)
            new_filename = new_filename + original_ext
            
            # Full paths
            original_path = os.path.join(directory_path, filename)
            new_path = os.path.join(directory_path, new_filename)
            
            # In preview mode, just print what would happen
            if preview:
                print(f"{filename:<40} {new_filename:<40}")
                rename_count += 1
            else:
                # Skip if the new filename already exists
                if os.path.exists(new_path) and original_path != new_path:
                    print(f"Skipped: '{new_filename}' already exists")
                    continue
                
                # Perform the actual rename
                try:
                    os.rename(original_path, new_path)
                    rename_count += 1
                except Exception as e:
                    print(f"Error renaming '{filename}': {e}")
        
        return rename_count
    
    except Exception as e:
        print(f"Error: {e}")
        return 0

def main():
    """Main function to run the file renamer"""
    print("=" * 50)
    print("File Renaming Tool")
    print("=" * 50)
    
    # Get directory path
    if len(sys.argv) > 1:
        directory_path = sys.argv[1]
    else:
        directory_path = input("Enter the directory path: ")
    
    # Check if directory exists
    if not os.path.isdir(directory_path):
        print(f"Error: '{directory_path}' is not a valid directory")
        return
    
    # Count files in directory
    files_count = len([f for f in os.listdir(directory_path) if os.path.isfile(os.path.join(directory_path, f))])
    print(f"\nFound {files_count} files in '{directory_path}'")
    
    # Explain pattern options
    print("\nPattern options:")
    print("  {n} - Sequential number")
    print("  {date} - Current date (YYYYMMDD)")
    print("\nExamples:")
    print("  'file_{n}' -> file_1, file_2, file_3, ...")
    print("  'photo_{date}_{n}' -> photo_20240514_1, photo_20240514_2, ...")
    
    # Get renaming pattern
    pattern = input("\nEnter the renaming pattern: ")
    if not pattern:
        print("Error: Pattern cannot be empty")
        return
    
    # Get starting number
    try:
        start_number = int(input("Enter starting number (default: 1): ") or "1")
        if start_number < 0:
            raise ValueError("Starting number must be positive")
    except ValueError:
        print("Invalid number. Using default: 1")
        start_number = 1
    
    # Ask about preserving extensions
    preserve_ext = input("Preserve file extensions? (Y/n): ").lower() != "n"
    
    # Show preview first
    files_to_rename = rename_files(directory_path, pattern, start_number, preserve_ext, preview=True)
    
    if files_to_rename > 0:
        # Ask for confirmation
        confirm = input(f"\nRename {files_to_rename} files? (y/N): ").lower()
        
        if confirm == "y" or confirm == "yes":
            # Create a backup of the directory
            backup_dir = f"{directory_path}_backup_{datetime.now().strftime('%Y%m%d%H%M%S')}"
            shutil.copytree(directory_path, backup_dir)
            print(f"Backup created at: {backup_dir}")
            
            # Perform actual renaming
            renamed = rename_files(directory_path, pattern, start_number, preserve_ext, preview=False)
            print(f"\nSuccessfully renamed {renamed} files")
            print(f"Backup of original files is available at: {backup_dir}")
        else:
            print("Operation cancelled")
    else:
        print("No files to rename")

if __name__ == "__main__":
    main()