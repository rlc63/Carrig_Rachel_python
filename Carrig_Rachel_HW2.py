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
COMPLETE
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
COMPLETE
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
COMPLETE
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
COMPLETE
Question 7: Using the higher order function reduce(), write a function that takes a list of numbers and returns the largest one
"""
import functools #we are going to import the tool so that we can use reduce, as it is not inherently recognized in python

def max_in_list(numbers): #we define max_in_list for the numbers provided
    """
    we are defining a function that takes a list of numbers and returns the largest of those numbers
    Parameters: we will input a list of numbers
    Return: the largest number inputted
    """    
    return functools.reduce(max, numbers) #when given the function max_in_list, we want it to call the function reduce, in which it reduces the list of numbers inputted to only the maximum one
    
"""
COMPLETE
Question 8: Write a program that maps a list of words into a list of integers
representing the lengths of the correponding words in three ways - with a for loop, the map function, and list comprehensions
"""
#first, we will use the for-loop 
def length_of_words_forloop(words0):
    """
    we are defining the function length_of_words_forloop which will return the length of the words given using a for loop in the code
    Parameters: a list of characters
    Return: the length of each word separated by a comma in the input
    """
    intlengths0 = [] #we start out with nothing in the output
    for word0 in words0: #for each word found in the input
        intlengths0.append(len(word0)) #the lengths is the length of each word added to 0 (giving the length of each word), separately
    return intlengths0 #the result is returned, which is a list of the lengths of each word
    
#next, we will use the map function
def length_of_words_map(words1):
    """
    we are defining the function length_of_words_map which will return the length of the words given using the map function in the code
    Parameters: a list of characters
    Return: the length of each word separated by a comma in the input
    """
    return list(map(len, words1)) #for the fucntion, we map each word to its length. we then return the list of the lengths of each word
    
#finally, we will use list comprehension
def length_of_words_list(words2): 
    """
    we are defining the function length_of_words_list which will return the length of the words given using list comprehension in the code
    Parameters: a list of characters
    Return: the length of each word separated by a comma in the input
    """
    return [len(word2) for word2 in words2] #here, we return the length (using the built in len function) for each word listed in the input, words2
    
    
"""
COMPLETE
Question 9: Write a function find_longest_word()that takes a list of words and returns the length of the longest one using only higher order functions
"""
def find_longest_word(longword):
    """
    we define the function that will take the length of each word inputted and return the longest length
    Parameters: a list of characters
    Return: the length of the longest word in the inputted list
    """
    longwordlength = list(map(len, longword)) #we first define what the length of each word is by mapping each word to its length and listing out those lengths
    return functools.reduce(max, longwordlength) #we then call the lengths mapped out above, and using the reduce function pick the max of that list and return that max

"""
COMPLETE
Question 10: Using the higher order function filter(), define a function that takes a list of words and an integer and returns the list of words longer than the integer
"""
def filter_long_words(input, n):
    """
    this function takes a list of words, an integer n, and returns the length of each word that is larger than n
    Parameters: a list of words and an integer n
    Return: the words in the list that are longer than n
    """
    return list(filter(lambda i: len(i) > n, input)) #we take the length n given, and use it to filter the inputs for those that are longer than n. we then return the list of those words
    
"""
COMPLETE
Question 11:  . Use the higher order function map()to write a function that takes a specified list of English words and returns a specified list of Swedish words.
"""
def translatemap(*english): #changed the name from translate so as not to duplicate the function from question 1
    """
    we are defining a function that translates specific English words into Swedish using a map function
    Pameters: the English words in the defined dictionary
    Return: the corresponding Swedish words for each inputted English word within the defined dictionary
    """     
    dict = {"merry":"god", "christmas":"jul", "and":"och", "happy":"gott", "new":"nytt", "year":"år"} #first, we define the words that can be translated from English to Swedish
    translated = map(lambda swedish: dict[swedish], english) #we define translated, which is the map of each English word to the corresponding Swedish word
    return list(translated) #we then return the list of each of the words that has been mapped
    
"""
COMPLETE
Question 12: Implement the higher order functions map(), filter() and reduce()
"""
def mapfunc(functionmap, iterablemap):
    """
    we are defining a function that does what the built in map function does
    Parameters: a function is given first for functionmap, and then a string or list is given for iterablemap
    Return: the application of the function to the list or string inputted
    """
    ansmap = [] #we start out with an empty aswer
    for i in iterablemap: #for each element in the given iterable
        mapping = functionmap(i) #we apply the function to the iterable and have that equal mapping
        ansmap.append(mapping) #for each function applied to each element in iterable, we add the solution to the list of final answers
    return ansmap #we then print the list of final answers

def filterfunc(functionfilter, iterablefilter):
    """
    we are defining a function that does what the built in filter function does
    Parameters: a function is given first for functionfilter, and then a string or list is given for iterablefilter
    Return: the items in the string or list that match the parameters given in the function
    """
    ansfilter = [] #we start out with an empty answer
    for j in iterablefilter: #for each item in the iterablefilter input
        if functionfilter(j) == True: #if the item is true under the parameters of the function
            ansfilter.append(j) #we will add that item to the list of the answers that are outputted
    return ansfilter #we then produce all the items that fit the parameters of the function

def reducefunc(functionreduce, sequencereduce, initial=None):
    """
    we are defining a function that does what the built in reduce function does
    Parameters: a function is given for functionreduce, then a string or list for sequencereduce, and the initial value is none
    Return: the value that wins out the reduce function when compared to the other values in the inputted sequence
    """
    ansreduce = initial if initial else sequencereduce[0] #the answer is the initial value in the list given in sequencereduce
    for k in sequencereduce: #for each element in sequencereduce
        ansreduce = functionreduce(ansreduce, k) #the answer applies that element to the function and compares it to the previous answer (or 0 if there is no previous answer)
    return ansreduce #the element that best fits the function after all iterations is kept and produced
    