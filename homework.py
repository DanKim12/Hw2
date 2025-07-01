def file_to_dictionary(file_path):
    my_dict = {}
    with open(file_path) as file:
        for line in file:
            words = line.split()
            for word in words:
                if word in my_dict:
                    my_dict[word] += 1
                else:
                    my_dict[word] = 1
    return my_dict


def count_word_in_file(file_name, num_of_words):
    word_dictionary = file_to_dictionary(file_name)
    sorted_items = sorted(word_dictionary.items(), key=lambda item: item[1], reverse=True)

    # Print top `num_of_words` most frequent words
    for word, count in sorted_items[:num_of_words]:
        print(f"{word}: {count}")





def main():
    #constants
    num_of_words = 2 # number of most frequent words to print

    #variables
    file_path = input("Enter the file path: ")
    file_path = "C:/Users/ASUS/PycharmProjects/PythonProject55/test.txt" # Just for testing, remove this line when you run the program
    count_word_in_file(file_path, num_of_words)


main()