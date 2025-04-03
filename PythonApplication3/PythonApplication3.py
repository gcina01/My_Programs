def reverse_words(input_string):
    # Your code here
    print("Original String:", "Hello World! Python is awesome.")
    x=len(input_string)
    reversed_string =""
    s=""
    for i in range (x):
        s=s+input_string[i]
        if input_string[i]==" ":
            reversed_string= s+reversed_string 
            s=""
        
    reversed_string= s+ " "+ reversed_string 
    print("Reversed Words:", reversed_string)
        
    return reversed_string
reverse_words("Hello World! Python is awesome.")

def word_frequency(input_string):
    # Your code here    
    frequency_dict ={}
    x=len(input_string)
    list_string =[]
    s=""
    p=0
    for i in range (x):
        s=s+input_string[i]
        if input_string[i]==" ":
            list_string.append(s)
            s=""
            frequency_dict[list_string[p]]=1
            p=p+1
    return frequency_dict

# Test your function
sample_text = "This is a sample text. Sample text is used for testing."
result = word_frequency(sample_text)
print("Input Text:", sample_text)
print("Word Frequency:", result)

def FizzBuzz(n):
        
    for i in range(n): 
        i=i+1
        if i%3 == 0:
           if i%5==0:
               print("FizzBuzz")
           else:
                print("Fizz")    
        elif i%5 ==0:
            print("Buzz")    
        else:
            print(i)    
                  
FizzBuzz(15)

def is_palindrome(s):
    # Your code here
    t=""
    x=len(s)
    d=""
    for i in range(x):
        if s[i]==" " or s[i]==",":
            gcina=1
        else:
            t=t+s[i]
            d=s[i]+d
    if t.upper()==d.upper():
        return True
    else:
        return False

word1 = "level"
word2 = "Hello World"
word3 = "A man, a plan, a canal, Panama"
word4 = "python"
print(f"Is '{word1}' a palindrome? {is_palindrome(word1)}")
print(f"Is '{word2}' a palindrome? {is_palindrome(word2)}")
print(f"Is '{word3}' a palindrome? {is_palindrome(word3)}")
print(f"Is '{word4}' a palindrome? {is_palindrome(word4)}")

def word_frequency(input_string):
    frequency_dict={}
    l=[]
    a=len(input_string)
    c=""
    for i in range (a):
        if input_string[i]==" ":
            l.append(c)
            c=""
        else:
            c=c+input_string[i]
    for i in range(len(l)):
        b=l[i]        
        frequency_dict[b] = frequency_dict.get(b, 0) + 1   
    return frequency_dict

sample_text = "This is a sample text. Sample text is used for testing."
print(word_frequency(sample_text))

def find_even_numbers(numbers):
    # Your code here
    even_numbers=[]
    for i in range (len(numbers)):
        if numbers[i]%2==0:
            even_numbers.append(numbers[i])
    return even_numbers

numbers_list = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
result = find_even_numbers(numbers_list)
print("Original List:", numbers_list)
print("Even Numbers:", result)

def are_anagrams(str1, str2):
    a = len(str1)
    b = len(str2)

    if a == b:
        # Convert strings to lowercase and remove spaces for comparison
        str1 = str1.lower().replace(" ", "")
        str2 = str2.lower().replace(" ", "")

        # Check if the sorted characters of both strings are the same
        return sorted(str1) == sorted(str2)
    else:
        return False
# Test your function
word1 = "listen"
word2 = "silent"
word3 = "Hello"
word4 = "Hola"
print(f"Are '{word1}' and '{word2}' anagrams? {are_anagrams(word1, word2)}")
print(f"Are '{word3}' and '{word4}' anagrams? {are_anagrams(word3, word4)}")

def count_vowels_and_consonants(input_string):
    vcount=0
    conscount=0
    str0=input_string.lower()
    for i in range (len(input_string)):
        if input_string[i]=="a"or input_string[i]=="e" or input_string[i]=="i" or input_string[i]=="o" or input_string[i]=="u":
            vcount=vcount+1
        elif input_string[i]==" ":
            space=0
        else:
            conscount=conscount+1
    result=[vcount,conscount]        
    return result

 #Test your function
text = "Hello World"
result = count_vowels_and_consonants(text)
print(f"Text: '{text}'")
print(f"Vowels: {result[0]}, Consonants: {result[1]}")

def back_titration():
    # Analyte
    Analyte = input("Enter the Analyte: ")
    Mm = input('Enter the molar mass of ' + Analyte + " : ")

    # Secondary Standard
    Secondary = input("Enter the Secondary standard: ")
    V_tsec = float(input("Enter the volume of " + Secondary + " : "))
    c_tsec = float(input("Enter the concentration of " + Secondary + " : "))
    n_tsec = c_tsec * V_tsec

    # Primary Standard
    Primary = input("Enter the Primary standard: ")
    V_primary = float(input("Enter the volume of " + Primary + " : "))
    c_primary = float(input("Enter the concentration of " + Primary + " : "))
    n_primary = c_primary * V_primary

    print("For the reaction between " + Primary + " and " + Secondary + " : ")
    CE10 = float(input("Enter the coefficient of " + Primary + " : "))
    CE12 = float(input("Enter the coefficient of " + Secondary + " : "))
    n_exc = n_primary * CE10 / CE12
    n_sec = n_tsec - n_exc

    print("For the reaction between " + Secondary + " and " + Analyte + " : ")
    CE20 = float(input("Enter the coefficient of " + Secondary + " : "))
    CE21 = float(input("Enter the coefficient of " + Analyte + " : "))
    n_ana = n_sec * CE20 / CE21
    print("The number of moles of " + Analyte + " = " + str(n_ana))

# Example usage
back_titration()
