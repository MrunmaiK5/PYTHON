#######################################################################################
#   Function name   :   IsVowel
#   Description     :   Checks whether given character is a vowel or not
#   Input           :   String
#   Output          :   Boolean
#   Author          :   Mrunmai Jitendra Khadpe
#   Date            :   17/01/26
#######################################################################################

def IsVowel(character):
    if (character == 'a') or (character == 'e') or (character == 'i') or (character == 'o') or (character == 'u'):
        return True
    else:
        return False


def main():
    Ret = IsVowel('a')
    
    if Ret == True:
        print("Vowel")
    else:
        print("Not a vowel")

if __name__ == "__main__":
    main()