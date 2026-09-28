"""
Program 4: Write a program to write 5 user-entered sentences to a file.
"""

import os

def write_sentences_to_file(filename, sentences=None):
    if sentences is None:
        sentences = []
        print("Please enter 5 sentences:")
        for i in range(1, 6):
            s = input(f"Sentence {i}: ")
            sentences.append(s)

    with open(filename, "w") as file:
        for sentence in sentences:
            file.write(sentence.strip() + "\n")
            
    print(f"\nSuccessfully written {len(sentences)} sentences to '{os.path.basename(filename)}'.")


def read_file(filename):
    print(f"\n--- Reading '{os.path.basename(filename)}' ---")
    with open(filename, "r") as f:
        print(f.read())


def main():
    print("--- Program 4: Write 5 Sentences to File ---")
    
    output_file = os.path.join(os.path.dirname(__file__), "sentences.txt")
    
    # Predefined demo sentences (works seamlessly in batch/script mode)
    demo_sentences = [
        "Python is a versatile programming language.",
        "File handling allows permanent data storage.",
        "Practice building projects every day.",
        "Clean code is easy to read and maintain.",
        "Consistency is the key to mastering programming."
    ]
    
    write_sentences_to_file(output_file, sentences=demo_sentences)
    read_file(output_file)


if __name__ == "__main__":
    main()
