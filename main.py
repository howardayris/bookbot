def main():
    with open("books/frankenstein.txt") as f:
        file_contents = f.read()
    
    character_counts = {}
    lowered_string = file_contents.lower()
    
    for char in lowered_string:
        if char in character_counts:
            character_counts[char] += 1
        else:
            character_counts[char] = 1

    alphabet_counts = {}
    for char in character_counts:
        if char.isalpha():
            alphabet_counts[char] = character_counts[char]
           

    # Convert dictionary to list of dictionaries
    char_list = []
    for char in alphabet_counts:
        char_dict = {"character": char, "num": alphabet_counts[char]}
        char_list.append(char_dict)
    
    # Sort the list by number of occurrences (highest to lowest)
    def sort_on(dict):
        return dict["num"]
    
    char_list.sort(reverse=True, key=sort_on)
    

    print("--- Begin report of books/frankenstein.txt ---")
    
    # Get word count (splitting the text by spaces)
    words = file_contents.split()
    print(f"{len(words)} words found in the document\n")
    
    # Print each character count in a formatted way
    for char_dict in char_list:
        char = char_dict["character"]
        count = char_dict["num"]
        print(f"The '{char}' character was found {count} times")
    
    print("--- End report ---")
    
main()