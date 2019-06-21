# Created by Shawn O'Grady on 12/7/17.
# Copyright 2017 Shawn O'Grady. All rights reserved.

 #This code is a practice Python interview question from testdome.com

 #https://www.testdome.com/questions/python/file-owners/11846

 # Problem statement: Implement a group_by_owners function that:
    # i)Accepts a dictionary containing the file owner name for each file name.
    # ii) Returns a dictionary containing a list of file names for each owner name, in any order.

#Passes 3/3 tests

def FileOwners(files):
 return { owner:[kas for kas in files if files[kas]==owner] for owner in set([files[own_test] for own_test in files]) }


files = {
    'Input.txt': 'Randy',
    'Code.py': 'Stan',
    'Output.txt': 'Randy'
}
print(FileOwners.group_by_owners(files))
