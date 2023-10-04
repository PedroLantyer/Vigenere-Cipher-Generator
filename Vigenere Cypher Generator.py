import os

def clear_screen():
    if os.name == "nt":
        os.system("cls")
    else:
        os.system("clear")

def verify_input(str1,operation):
    if operation != "EXIT":
        if not(str1.isalpha()):
            clear_screen()
            print("I'm sorry I couldn't understand, please insert a valid %s (you can only use letters)\n" % (operation))
            return False
        else:
            return True
    else:
        try:
            str1.strip()
            if not(str1.isalpha()):
                raise Exception()
            if str1[0:3].upper() != "YES" and str1[0:2].upper() != "NO":
                raise Exception()
        except:
            clear_screen()
            print("I'm sorry I couldn't understand, please try again:")
            return False
        else:
            return True
    
def adjust_key(text,key):
    og_len = len(key)
    while len(key) < len(text):
        for i in range(og_len):
            key += key[i]
    else:
        return key
    
def verify_keysize(t_len,k_len):
    if k_len > t_len:
        clear_screen()
        print("Please insert a key that is as long or shorter than the text\nthe size of the current text is %d" % (t_len))
        return False
    else:
        return True

def get_text():
    done = False
    while done != True:
        text = str(input("Insert text to be encrypted (can only include letters):\n")).strip().upper()
        done = verify_input(text,"text")
    clear_screen()
    done = False
    while done != True:
        key = str(input("Insert key (can only include letters):\n")).strip().upper()
        check = verify_keysize(len(text.strip()),len(key.strip()))
        if check == True:
            done = verify_input(key,"key")
    clear_screen()
    key = adjust_key(text,key)
    return text,key

def encode(text,key):
    result = ""
    for i in range(len(text)):
        x = (ord(text[i]))
        y = (ord(key[i])-65)
        num = (x+y)
        if num > 90:
            num -= 26
        result += str(chr(num))
    return result

def continue_prompt():
    done = False
    while done != True:
        s = input("\nIf you wanna continue, type \'YES\', if you wanna exit, type \'NO\'\n(please note that only the first value will be accepted)\n")
        done = verify_input(s,"EXIT")
    else:
        if s[0:3].upper() == "YES":
            return not(True)
        elif s[0:2].upper() == "NO":
            clear_screen()
            print("Thank you, have a nice day :)")
            return not(False)

if __name__ == "__main__":
    done = False
    while done != True:
        clear_screen()
        text,key = get_text()
        result = encode(text,key)
        print("Original Text: %s\nKey: %s\nEncoded Text:%s" % (text,key,result))
        done = continue_prompt()