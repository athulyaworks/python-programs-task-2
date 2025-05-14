import string
import sys
from collections import Counter

def count_word_frequency(file_path):
   
    try:
        # Read the file
        with open(file_path, 'r', encoding='utf-8', errors='ignore') as file:
            text = file.read().lower()
        
        # Remove punctuation
        for char in string.punctuation:
            text = text.replace(char, ' ')
        
        # Split into words and count frequencies
        words = text.split()
        word_counts = Counter(words)
        
        return word_counts
    
    except FileNotFoundError:
        print(f"Error: File '{file_path}' not found.")
        return Counter()
    except Exception as e:
        print(f"Error: {e}")
        return Counter()

def main():
    """Main function to run the word frequency counter"""
    # Check if file path is provided as command line argument
    if len(sys.argv) > 1:
        file_path = sys.argv[1]
    else:
        # Ask for file path
        file_path = input("Enter the path to the text file: ")
    
    # Count word frequencies
    word_counts = count_word_frequency(file_path)
    
    if word_counts:
        # Display results
        total_words = sum(word_counts.values())
        unique_words = len(word_counts)
        
        print(f"\nFile Analysis Results:")
        print(f"Total words: {total_words}")
        print(f"Unique words: {unique_words}")
        
        # Ask user how many top words to display
        try:
            n = int(input("\nHow many top words do you want to see? (default: 10): ") or "10")
        except ValueError:
            n = 10
            print("Invalid input. Showing top 10 words.")
        
        # Display top words
        print(f"\nTop {n} most frequent words:")
        print("-" * 30)
        print("Word               | Count")
        print("-" * 30)
        
        for word, count in word_counts.most_common(n):
            print(f"{word:<20}| {count}")
        
        # Ask if user wants to save results
        save_option = input("\nDo you want to save these results to a file? (y/n): ").lower()
        if save_option == 'y' or save_option == 'yes':
            output_path = input("Enter output file path (default: word_frequency.txt): ") or "word_frequency.txt"
            
            with open(output_path, 'w') as output_file:
                output_file.write(f"File Analysis Results:\n")
                output_file.write(f"Total words: {total_words}\n")
                output_file.write(f"Unique words: {unique_words}\n\n")
                
                output_file.write("Word Frequencies (in descending order):\n")
                output_file.write("-" * 40 + "\n")
                output_file.write("Word                 | Count\n")
                output_file.write("-" * 40 + "\n")
                
                for word, count in word_counts.most_common():
                    output_file.write(f"{word:<20} | {count}\n")
            
            print(f"Results saved to {output_path}")
    
    else:
        print("No words found or invalid file.")

if __name__ == "__main__":
    main()