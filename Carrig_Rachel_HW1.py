# -*- coding: utf-8 -*-
"""
Created on Thu Sep  8 19:18:19 2016

@author: Rachel Carrig; rlc63
"""
#Overall Comment: Very good assignment! You covered all possible situations and commented well. But please include examples
#to show that your functions really work. I have made a few comment with "Comment:" in front, you may have a look. If any
#misunderstanding happened. Please feel free to email me.
"""
COMPLETE
Question 1: This function defines which number is the larger of two given numbers.
"""
def print_max(a, b): #the function will print the largest of two numbers
    """
    This function will print the larger of two numerical values
    Parameters: real numbers
    Return: the larger of two numbers, assuming they are different. if they are the same, it returns that number.
    """
    if a >= b:
        print(a, 'is maximum')#if a is greater than or equal to b, a is maximum
    elif a <= b:
        print(b, 'is maximum')#if b is greater than or equal to a, b is maximum
    

x = 2#here we give values for x and y corresponding to a and b
y = 3

print_max(x, y)#prints the maximum of x and y; in this case y
#Comment: You don't need to set variable x and y individually, put 2 and 3 into function directly.

"""
COMPLETE
Question 2: This function defines which of three numbers is the largest.
"""
def print_max_of_three(a, b, c): #the function will print the largest of three variables
    """
    This function will print the largest of three numerical values
    Parameters: real numbers
    Return: the largest of the three numbers, assuming they are different. if two or three of the numbers are the same and that number is the largest, it will print that one.
    """
    if a >= b and a >= c:
        print(a, 'is maximum')#if a is greater than or equal to b AND greater than or equal to c, then a is the maximum
    elif c >= a and c >= b:
        print(c, 'is maximum')#if c is greater than or equal to a AND greater than or equal to b, then c is the maximum
    elif b >= a and b >= c:
        print(b, 'is maximum')#if b is greater than or equal to a AND greater than or equal to c, then b is the maximum
    
x = 1#here we give values for x, y, and z corresponding to a, b, and c
y = 0
z = 1
print_max_of_three(x, y, z)#prints the maximum of x, y, and z


"""
COMPLETE
Question 3: This function defines the length of a given list or string.
"""
def length(sentence): #the function will print the length of a given sentence
    """
    This function provides the length of the text entered.
    Parameters: text, not including spaces
    Return: an integer containing the number of letters in the text.
    """
    x = 0 #we start out with 0 letters before anything is submitted
    for i in sentence:
        x = (x + 1) #we want to add 1 to 0 for the first letter, and keep adding 1 for each letterin the string
    print(x) #this will print the final count of all the letters in the string

  
"""
COMPLETE
Question 4: This function returns "True" for a vowel given, and "False" for anything else.
"""
vowels = 'aeiouAEIOU' #first we define all vowels, which can be both lower or upper case
def isVowel(char): #then for our function, we have one character
    """
    this function determines whether or not the character given is a vowel, as defined above
    Parameters: a single character must be entered, otherwise it will automatically give False
    Return: True if a single vowel, false otherwise
    """
    if len(char) == 1: #this limits the input to one character
        if char in vowels: #if the character inputted is in the vowels set, or is a vowel, then it will print True
            print("True")
    else: #if the character inputted is not in the vowel set, False will print
        print("False")


"""
COMPLETE
Question 5: Translate English into Robber's Language, where when a consonant is listed it is replaced by the consonant + o + the consonant again.
"""
consonants = 'bcdfghjklmnpqrstvwxyzBCDFGHJKLMNPQRSTVWXYZ' #first, we define what consonants are. The consonants can be either capital or lowercase, and all are included here. We consider y and Y a consonant for this exercise.
def translate(language): #this function will translate the language inputted into Robber's Language
    """
    this function translates a string of text entered into "robber's Language", where each consonant as defined above is rewritten as that consonant plus o and then plus that consonant again.
    Parameters: a string of text
    Return: the initial language translated into the "robber's language" as described above
    """
    newtext = "" #we will define what the new text will be based on the input
    for i in language:
        if i in consonants:
            newtext+=i+'o'+i #for any character i inputted that is a consonant (as found in consonants), it will be returned as i + o + i, or "ioi" in practice.
        else:
            newtext+=i #if the character is NOT a consonant, it will stay the same
    print(newtext) #the code will now print the language in Robber's Language
#Comment: it is good to cover all possible situations!  
    
"""
COMPLETE
Question 6: Define sum() and multiply() such that they sum and multiply, respectively, everything in a list of numbers
"""
#first, we will define the function sum() to add numbers provided in a list
def sum(numlist): 
    """
    this function adds together the numbers listed in the input
    Parameters: real numbers
    Return: the sum of the listed
    """
    x = 0 #we start out with x as 0, as we don't have any numbers to begin with
    for i in numlist: 
        x = (x + i) #for each number in the number list, we add it to the previous number (and if it's the first number, we add it to 0, the initial value of x)
    print(x) #this will print out the solution
    
#we will now define the function multiply() to multiply numbers provided in a list
def multiply(numlist):
    """
    this function will multiply together the numbers listed in the input
    Parameters: real numbers
    Return: the product of the numbers listed
    """
    x = 1 #we start out with 1, as any number multiplied by 1 is itself
    for i in numlist:
        x = (x * i) #for each number in the list, we multiply it by the previous number (and if it's the first number, we multiply it by 1, the initial value of x)
    print(x) #this will print out the solution
    
"""
COMPLETE
Question 7: Computes the reversal of a string
"""
def reverse(text): #define a function reverse to make a reverse string
    """
    Writes a given string in reverse
    Parameters: a string
    Return: the string printed backwards
    """
    i = len(text) - 1 #this gives us the last letter in the string of text
    backwardstext = '' #here we define backwardstext as empty
    while  i >= 0: 
        backwardstext = backwardstext + str(text[i]) #we then add the backwards text together, switching the position of each letter
        i = i -1 
    print(backwardstext) #this prints the final text created
    

"""
COMPLETE
Question 8: Define a function that recognizes palindromes
"""
def is_palindrome(text): #here we define a function that tests if the entered text is a palindrome        
    """
    This function recognizes palindromes.    
    Parameters: any word with alphabetical characters (no numbers, upper or lower case, and disregarding spaces)
    Return: Return True if it is a palindrome, False otherwise
    """    
    text = text.upper() #allows for text to be upper or lower case 
    text = text.replace(" ", "") #removes spaces from consideration, so if there is more than one word but they still form a palindrome, the result is true
    backwardstext = text [::-1] #we create a backwards text that takes the last character and oves it to the front, the second to last character and moves it to second, and so on    
    if not text.isalpha(): #if there are numbers in the input, or the input is empty it will automatically return false
        return False
    if backwardstext == text: #if the initial text is the same as the text created in above line
        return True #then, the statement will return true
    else: #if the initial text is not the same as the text created in the second line (line 117), then it returns false as it is not a palindrome
        return False


"""
COMPLETE
Question 9: Function that says if a value is in a list of values
"""
def is_member(lista, b): #we're defining a function where the first part of the entry is the list we have, and the second is the individual element we want to see is in the list
    """
    this function determines whether or not a given item is part of the given list
    Parameters: any list and an item listed separately
    Return: True if the item listed separately is within the given list, and false if it is not
    """    
    for x in lista: #we look at any element in lista
        for y in b: #we then look at the element in b
            if x == y: #if one of the elements are equal, meaning if b is in lista
                return True #the result is True and the function is complete
    else: 
        return False #if the program does not find any b within lista, then it will return false

"""
COMPLETE
Question 10: Define a function that takes two lists and says true if they have at least one member in common
"""
def overlapping(list1, list2): #we define the function so that when inputting, you write overlapping([___list 1 elements___], [___list2 elements___])
    """
    this function determines if two lists have any element within them that overlaps
    Parameters: two lists
    Return: True if there is overlap between the two lists; false otherwise
    """    
    for x in list1: #here, we want any variable in list1
        for y in list2: #again, we want any variable but this time in list2
            if x == y: #if any x in list1 is equal to anyx in list2
                return True #the result will be true. the return function looks for any values where it is true, and if it is, it just prints true
    else:
       return False #if there are NO true values, then false is printed
        

"""
COMPLETE
Question 11: Define a function generate_n_chars()that takes an integer n and a character c and returns a string, ncharacters long, consisting only of c's.
"""
def generate_n_chars(num, char): #here we generate the same character the number of times as the number inputted
    """
    this function generates a duplication of a character entered the number of times listed
    Parameters: num is a number and char is a character, and both must be inputted
    Return: the result is the character repeated number times
    """    
    out = "" #we start with nothing in the output
    for i in range(num): #for the number given as num
        out = out + char #the output is each character num times, as it starts at 0 and adds up until num is complete
    return(out) #this returns the final result we want

"""
COMPLETE
Question 12: function that creates a histogram from a list of numbers given
"""
def histogram(numbers): #we are creating a histogram from a set of numbers given
    """
    this function creates a histogram, where a list of numbers is translated into groups of * listed the number of times given
    Parameters: real numbers are inputted
    Return: the result is the character * the number of times for each element in the list
    """
    out = "" #we start out with nothing in the input
    for x in numbers: #for each number within the given set
        out = out +  generate_n_chars(x, '*') + " " #we use the function created in Question 11 to print the symbol '*' x number of times with a space added to separate the numbers
    return out[:-1] #returns everything but the last space, so there's no extra space at the end

"""
COMPLETE
Question 13: Create a function that produces the maximum element in a list (where length of list is not predetermined)
"""
def two_max(a, b): #the function will print the largest of two numbers
    """
    first, we need to find the maximum of two numbers
    Parameters: two real numbers
    Return: the larger of the two numbers
    """
    if a >= b:
        return a #if a is greater than or equal to b, a is maximum
    elif a <= b:
        return b #if b is greater than or equal to a, b is maximum
    

def max_in_list(maxlist): #here, we want a list of more than just a and b to take the maximum from
    """
    once we have defined the two_max, we then need to find the largest number in a list of numbers
    Parameters: a list of two or more real numbers
    Return: the largest of the numbers listed
    """
    heaviest = maxlist[0] #to do this, we create 'heaviest' where the maxlist is 0 (so nothing is in it at first)
    for x in maxlist: #for each element inputted
        heaviest = two_max(x, heaviest) #the element is measured against the heaviest one, and the heaviest one is kept.  So, for the first element, the first element is larger than zero, then the second element is compared to the first, and the larger one is kept, and so on
    return heaviest #this gives us the heaviest one after all of the numbers are compared
        
"""
COMPLETE
Question 14: Map a list of words into a list of integers representing the words' lengths
"""
def length_14(sentence): #the function will print the length of a given sentence
    """
    first, we define the length of a given word
    Parameters: a string of characters given
    Return: the length of the string
    """    
    x = 0 #we start out with 0 letters before anything is submitted
    for i in sentence:
        x = (x + 1) #we want to add 1 to 0 for the first letter, and keep adding 1 for each letterin the string
    return x #this returns the length of the sentence
    
def length_of_words(list0): #we now move to the length of the words in the list
    """
    once we have the length of strings of words, we can use them to create a list of each length of the words
    Parameters: a list of words
    Return: gives the length of each word in the list
    """
    out = [length_14(word) for word in list0] #here we set out equal to the length of each word in the list, using the previously defined function
    return out #we return out, giving us the lengths of each word
    
"""
COMPLETE
Question 15: Write a function that takes a list of words and returns the length of the longest one
"""
def find_longest_word(longword): #this function is similar to the max_in_list function, but with word lengths instead of numbers
    """
    using the previously defined functions length_of_words() and max_in_list(), we can determine which word is the longest given a list of words
    Parameters: a list of words given
    Return: the length of the largest word
    """    
    lcounts = length_of_words(longword) #we create lcounts, which is the length of each word given (so the result is a list of numbers)
    heaviest = max_in_list(lcounts) #we then take the numbers from lcounts and use the previously defined max_in_list function to see which is the largest
    return heaviest #this prints the largest of the numbers, which is the largest length of a word in the set
    #return max_in_list(length_of_words(longword)) #could use this instead of the three above lines
"""
COMPLETE
Question 16: Write a function that takes a list of words and an integer n and returns the list of words that are longer than n.
"""
def filter_long_words(longwords, n): #here we define the function
    """
    here we write a function that takes a list of words, finds their lengths, and writes out the list of words that are longer than n
    Parameters: a list of words, and an integer
    Return: the words longer than the integer given
    """
    out = [] #we start out with nothing in out
    for word in longwords: #for each word given in the input of the function, we do the following:
        if length_14(word) >= n: #this looks to see if the length of the word as previously defined is larger than the n given
             out.append(word) #if it is, then that word is added to the out list (which starts out as nothing) 
    return out #once all words have been evaluated, the function returns the out list, with all words longer than n appended to it
