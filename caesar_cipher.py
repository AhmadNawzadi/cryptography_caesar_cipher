

def caesar_cipher():
    alphabet = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 
                'H', 'I', 'K', 'L', 'M', 'N', 'O', 
                'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'X', 'Y', 'Z',
                'A', 'B', 'C', 'D', 'E', 'F', 'G', 
                'H', 'I', 'K', 'L', 'M', 'N', 'O', 
                'P', 'Q', 'R', 'S', 'T', 'V', 'X', 'Y', 'Z']
    
    lowerCase_alphabet = [l.lower() for l in alphabet]
    print("Welcome to the Caesar Cipher code and decode a message!")
    user_choice = input("Would you like to code or decode a message ?\n").lower()
    if user_choice == 'code':
        user_text = input("Write your message to code!\n").lower()
        shift = int(input("Write your shift number!\n"))
        coded_text = ' '
        for l in user_text : 
            if l in lowerCase_alphabet and l != ' ':
                ind = lowerCase_alphabet.index(l)
                ind += shift
                coded_text += lowerCase_alphabet[ind]
                #print(coded_text)
        print(f"the encrypted text is {coded_text}")
    elif user_choice == 'decode':
        user_text = input("Write your message to decode!\n").lower()
        shift = int(input("Type your shift number!\n"))
        decoded_text = ' '
        for l in user_text: 
            if l in lowerCase_alphabet:
                ind = lowerCase_alphabet.index(l)
                ind -= shift
                decoded_text += lowerCase_alphabet[ind]
                #print(coded_text)
        print(f"the decrypted text is {decoded_text}")
    else:
        print("please select either 'code' or 'decode' word!")




if __name__ == "__main__":
    caesar_cipher()
