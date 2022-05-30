import re

def password(v):
   

    if v == "\n" or v == " ":
        return "Password cannot be a newline or space!"
   

    if 9 <= len(v) <= 20:
   

        if re.search(r'(.)\1\1', v):
            return "Weak Password: Same character repeats three or more times in a row"
   

        if re.search(r'(..)(.*?)\1', v):
            return "Weak password: Same string pattern repetition"
   
        else:
            return "Strong Password!"
   
    else:
        return "Password length must be 9-20 characters!"
  

def main():
   
    print(password("Qggf!@ghf3"))
    print(password("passwordpass"))
    print(password("aaabnil1gu"))
    print(password("Aasd!feasn"))
    print(password("772*hd897"))
    print(password(" "))
   
if __name__ == '__main__':
    main()