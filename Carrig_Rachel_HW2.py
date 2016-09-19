# -*- coding: utf-8 -*-
"""
Created on Thu Sep 15 18:49:06 2016

@author: ibrlouise
"""

"""
COMPLETE
Question 1: Creating a dictionary of a few words to translate Christmas cards from English to Swedish
"""
#first, we list the dictionary and all relevant english and swedish words
dictionary = {
    "merry":"god",
    "christmas":"jul",
    "and":"och",
    "happy":"gott",
    "new":"nytt",
    "year":"år"
}

def translate(word):
    """
    here we define the function translate in order to translate the dictionary placed above
    Parameters: english words in the dictionary
    Return: the swedish words in the dictionary
    """
    swedish = "" #we start out with nothing for swedish
    for x in word.split(" "): #for the elements in word, we split them by the space markers so that each word is taken individually
        if str(dictionary.get(x)) != "None": #here we ask the program to get each x found in the dictionary in the string. if it's not none, the condition is true
            swedish = swedish + str(dictionary.get(x)) + " " #here we define the swedish output, where we return swedish as defined as nothing, then the new word gotten from the dictionary, plus a space after it to separate the swedish words
        else: #if swedish words are not inputted:
            swedish = " cannot translate - words not included in dictionary " #this text shows up if the words are not the swedish ones defined in the dictionary
    return swedish[:-1] #this returns the swedish translation minus the extra space added at the end of the swedish to separate the words
    

"""
COMPLETE
Question 2: create a function that takes a string and builds a frequency listing of the characters contained in it
"""
def char_freq(text):
    """
    we are going to define this function that will take a string of letters and create a frequency listing of the letters inputted
    Parameters: letters inputted
    Return: the number corresponding to the amount of each letter inputted
    """
    text = text.upper() #allows for text to be upper or lower case and be counted as the same letter
    text = text.replace(" ", "") #removes spaces from consideration
    if not text.isalpha(): #if there are numbers in the input, or the input is empty it will automatically return false
        return False #this will simply return false if non-letters are inputted
    frequency = {} #we define frequency here as an empty set
    for x in text: #for each letter in the text
        if x in frequency:
            frequency[x] = frequency.get(x) + 1 #here, using the get function, each time a character is read, the number 1 is added. so the first time it is 1, the second 2, etc.
        else:
            frequency[x] = 1 #we always want the frequency of each number to be at least 1
    return frequency #this tells the function to return each frequency

"""
COMPLETE
Question 3: implement an encoder/decoder of ROT-13 (cryptography)
"""
key = {'a':'n', 'b':'o', 'c':'p', 'd':'q', 'e':'r', 'f':'s', 'g':'t', 'h':'u',  
'i':'v', 'j':'w', 'k':'x', 'l':'y', 'm':'z', 'n':'a', 'o':'b', 'p':'c',
'q':'d', 'r':'e', 's':'f', 't':'g', 'u':'h', 'v':'i', 'w':'j', 'x':'k', 
'y':'l', 'z':'m', 'A':'N', 'B':'O', 'C':'P', 'D':'Q', 'E':'R', 'F':'S', 
'G':'T', 'H':'U', 'I':'V', 'J':'W', 'K':'X', 'L':'Y', 'M':'Z', 'N':'A', 
'O':'B', 'P':'C', 'Q':'D', 'R':'E', 'S':'F', 'T':'G', 'U':'H', 'V':'I', 
'W':'J', 'X':'K', 'Y':'L', 'Z':'M'} #this is the key used to translate the code

def decoder(code):  
    """
    we are defining our decoder to translate the text from the coded langauage into regular english
    Parameters: the characters in the key are translated; other characters are left alone
    Return: the code decoded into plain English
    """
    words = [words for words in code.split()] #we define words, which is what we will translate, and we split the code by each character so it's translated individually
    results = [] #the results at first are an empty string
    for x in words: #for each individual character in words
        results.append("".join([key[char] if char in key.keys() else char for char in x])) #we join together the characters so they are printed together to form words and not individual characters. this works for the characters included in the key as well as those that are not
    return " ".join(results) #the function prints the results joined together with a space between each word
 #if you print out the code, it returns "Caesar cipher? I much prefer Caesar salad!"
    
"""
Question 4: Define a "spelling correction" function that takes a string and sees to it that 1) two or more occurrences of the space character is compressed into one, and 2) inserts an extra space after a period if the period is directly followed by a letter
"""
def correct(mistakes):
    """
    we are defining a correcting function to fix spacing issues in a sentence- specifically to remove the extra space when two are present and to add a space after a period if the period is followed directly by a letter
    Parameters: the function will only affect the spaces as described above
    Return: the corrected sentence, with only one space as applicable and spaces after periods as appicable
    """
    import re #we will use a regular expression to fix the mistakes
    correctmistakes = re.sub('\ +',' ',mistakes) #first, we remove the extra spaces from the input as described in the instructions by using substitution
    correctmistakes = re.sub('\.','. ',mistakes) #then, we add a space after a period without one using substitution
    print(correctmistakes) #we then print the corrected sentence, which combines both of our definitions for the correctmistakes into one completely correct sentence

"""
Question 5: Define a function changing an infinitive verb to its third person singular form (replacing y with ies, adding es to verbs ending in  o, ch, s, sh, x, or z, and adding s to other verbs)
"""
def make_3sg_form(verb):
    """
    this function changes an infinitive verb inputted and makes it the third person singular form
    Paramets: input needs to be an infinitive verb
    Return: the third person singular form of the inputted verb
    """
    if verb.endswith('y'): #if the verb ends in y
        newverb = verb[:-1] + 'ies' #the output deletes the y, and replaces it with 'ies'
    elif verb.endswith(('o','ch','s','sh','x','z')): #if the verb ends in o, ch, s, sh, x, or z
        newverb = verb + 'es' #the output simply adds 'es' to the end of the word
    else: #for all other inputted verbs
        newverb = verb + 's' #add s to the end
    print(newverb) #print the new verb created using the above rules

"""
Question 6: Define a function that changes an infinitive verb to the present participle. For words ending in e, drop the e and add ing (with exceptions), for words ending in ie, change to y and add ing, for words that are consonant-vowel-consonant, double second consonant and add ing, and for all other words add ing
"""
def make_ing_form(ingverb):
    """
    we are defining a function that changes infinite verbs into their present participle state, as appropriate in the rules of English
    Parameters: input needs to be an infinitive verb
    Return: the present participle of the inputted verb
    """
    c = 'bcdfghjklmnpqrstvwxyzBCDFGHJKLMNPQRSTVWXYZ'
    v = 'aeiouAEIOU' #first, we define what the vowels and consonants are, which will be used later
    newingverb = '' #we start out with newingverb not being anything
    if ingverb == 'be': #be is a special case, so we define it individually to add 'ing' to it
        newingverb = ingverb + 'ing'
    elif ingverb.endswith('ee'): #the next special case is verbs with two es.  Those verbs do not drop an e as a word with one e would, so we just add ing to it
        newingverb = ingverb + 'ing'
    elif ingverb.endswith('ie'): #the next special case is verbs ending in ie. for them, we drop the ie (being the last two characters in the word) and add a y + ing
        newingverb = ingverb[:-2] + 'ying'
    elif ingverb.endswith('e'): #for words ending in one e that do not fit the earlier designations, we drop the e (the last characters) and add the ing.
        newingverb = ingverb[:-1] + 'ing'
    elif ingverb.endswith(ingverb): #here, we are defining words where the last three letters are a consonant, a vowel, or a consonant
        one   = ingverb[-3:-2] #this defines the third to last letter
        two   = ingverb[-2:-1] #this defines the second to last letter
        three = ingverb[-1:0] #this defines the last letter
        if one in c and two in v and three in c: #if the third to last eltter is a consonant, the second to last letter is a vowel, and the last letter is a consonant, we add a second last letter and then add ing
            newingverb = ingverb + ingverb[-1:] + 'ing'
        else:
            newingverb = ingverb + 'ing' #for all words that don't fit any of the above designations, we simply add 'ing' to the end of the verb
    print(newingverb) #we print the result that is the new verb conjugated for whichever of the above situations the verb fits

"""
COME BACK TO THIS 
Question 7: Using the higher order function reduce(), write a function
max_in_list()that takes a list of numbers and returns the largest
one. Then ask yourself: why define and call a new function, when I
can just as well call the reduce() function directly?
"""


"""
NEED HELP
Question 8: Write a program that maps a list of words into a list of integers
representing the lengths of the correponding words. Write it in
three different ways: 1) using a for-loop, 2) using the higher order
function map(), and 3) using list comprehensions.
"""
#first, we will use the for-loop 
def length_of_words_forloop(words0):
    intlengths0 = [] #we start out with nothing in the output
    for word0 in words0: #for each word found in the input
        intlengths0.append(len(word0)) #the lengths is the length of each word added to 0 (giving the length of each word), separately
    return intlengths0 #the result is returned, which is a list of the lengths of each word
    
#next, we will use the map function>???????
def length_of_words_map(words1):

    return map(len, words1)
    
#finally, we will use list comprehensions
def length_of_words_list(words2): 
    return [len(word2) for word2 in words2] #here, we return the length (using the built in len function) for each word listed in the input, words2
    
    
"""
Question 9: Write a function find_longest_word()that takes a list of words
and returns the length of the longest one. Use only higher order
functions.
"""
def find_longest_word(longword):
    ##need to use the result from question 7 for this question

"""
Question 10: Using the higher order function filter(), define a function filter_long_words()that takes a list of words and an integer nand returns the list of words that are longer than n
"""
def filter_long_words(filterwords):
    filter(len, n)
    return n