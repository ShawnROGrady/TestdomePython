# Created by Shawn O'Grady on 12/7/17.
# Copyright 2017 Shawn O'Grady. All rights reserved.

 #This code is a practice Python interview question from testdome.com

 #https://www.testdome.com/questions/python/palindrome/7962?visibility=1&skillId=9

 # Problem statement: Write a function that checks if a given word is a palindrome. Character case should be ignored.

 #Passes 3/3 tests
class Palindrome:

    @staticmethod
    def is_palindrome(word):
        word=word.lower() #just setting all characters to lower case for simplicity
        i=len(word)
        for letter in word:
            if letter!=word[i-1]:
                return False
            i=i-1
        return True

print(Palindrome.is_palindrome('Deleveled'))
