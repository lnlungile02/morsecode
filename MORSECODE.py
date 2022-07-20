LETTERS_TO_MORSE = {
     " ": "/",
    "'": ".----.",
    "(": "-.--.-",
    ")": "-.--.-",
    ",": "--..--",
    "-": "-....-",
    ".": ".-.-.-",
    "/": "-..-.",
    "0": "-----",
    "1": ".----",
    "2": "..---",
    "3": "...--",
    "4": "....-",
    "5": ".....",
    "6": "-....",
    "7": "--...",
    "8": "---..",
    "9": "----.",
    ":": "---...",
    ";": "-.-.-.",
    "?": "..--..",
    "A": ".-",
    "B": "-...",
    "C": "-.-.",
    "D": "-..",
    "E": ".",
    "F": "..-.",
    "G": "--.",
    "H": "....",
    "I": "..",
    "J": ".---",
    "K": "-.-",
    "L": ".-..",
    "M": "--",
    "N": "-.",
    "O": "---",
    "P": ".--.",
    "Q": "--.-",
    "R": ".-.",
    "S": "...",
    "T": "-",
    "U": "..-",
    "V": "...-",
    "W": ".--",
    "X": "-..-",
    "Y": "-.--",
    "Z": "--..",
    "_": "..--.-",
	"@": ".--.-.",
	"!":"-.-.--",
	"&":".-...",
	"=":"-...-",
	"+":".-.-.",
	'"':".-..-.",
	"$":"...-..-",
	}


def letters_to_morsecode(sentence):
	sentence = sentence.upper()
	morsecode = ""
	for word in sentence:
		morsecode +=LETTERS_TO_MORSE[word] + " "
	assert count_spaces(sentence) == (count_slash(morsecode)),f"spaces are not equal in input {sentence} and output {morsecode}"
	assert count_characters(sentence) == count_morse_characters(morsecode),f"number of characters represented are not equal in input {sentence} and output {morsecode}"
	return morsecode
	
def morsecode_to_letters(output):
	morse_to_letters = {value: key for key, value in LETTERS_TO_MORSE.items()}
	output_list = output.split()
	original_word = " "
	for morse in output_list:
		original_word += morse_to_letters[morse]
    
   
	assert count_slash(output) == count_spaces(original_word),f"spaces are not equal in input {output} and output {original_word}"
	assert count_morse_characters(output) == count_characters(original_word),f"number of characters represented are not equal in input {output} and output {original_word}"
	return original_word.upper()

def count_spaces(string):
    count = 0
    for char in string:
        if char == " ":
            count += 1
    return count

def count_slash(string):
    count = 0
    for char in string:
        if char == '/':
            count += 1
    return count

def count_morse_characters(string):
    new_string = string.split()
    return len(new_string)

def count_characters(string):
    count = 0
    for char in string:
        count +=1
    return count

if __name__ in "__main__":
    sentence = "HI THERE"
    print(letters_to_morsecode(sentence))
    output = letters_to_morsecode(sentence)
    print(morsecode_to_letters(output))
