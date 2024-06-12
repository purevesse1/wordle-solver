input_file = '../wordlists/word-bank.csv'
output_file = '../wordlists/possible_answers.txt'
past_ans_file = '../wordlists/past_answers.txt'


def extract_five_letter_words(input_file, output_file, past_ans_file):
    try:
        with open(input_file, 'r') as infile:
            words = infile.readlines()

        with open(past_ans_file, 'r') as excfile:
            past_words = excfile.readlines()

        past_words_lowercase = [word.lower() for word in past_words]

        with open(output_file, 'w') as outfile:
            for word in words:
                word = word.strip()
                if len(word) == 5 and word not in past_words_lowercase:
                    outfile.write(word + '\n')
        print(past_words_lowercase)

        print(f"Successfully extracted possible answers to {output_file}")
    except Exception as e:
        print(f"An error occurred: {e}")


extract_five_letter_words(input_file, output_file, past_ans_file)
