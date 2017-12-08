# Created by Shawn O'Grady on 12/7/17.
# Copyright 2017 Shawn O'Grady. All rights reserved.

 #This code is a practice Java interview question from testdome.com

 #https://www.testdome.com/questions/python/file-owners/11846

 # Problem statement: Implement a group_by_owners function that:
    # i)Accepts a dictionary containing the file owner name for each file name.
    # ii) Returns a dictionary containing a list of file names for each owner name, in any order.

#Passes 3/3 tests

class FileOwners:

    @staticmethod

    def group_by_owners(files):
        owners=set()
        ownerDict={}

        for k, v in files.items():
            #fill set w/ names of owners
            owners.add(v)
        for o in owners:
            ownerDict[o]=[]
            for k, v in files.items():
                #fill out new dictionary w/ list of file names
                if v==o:
                    ownerDict[o].append(k)
        return ownerDict;



files = {
    'Input.txt': 'Randy',
    'Code.py': 'Stan',
    'Output.txt': 'Randy'
}
print(FileOwners.group_by_owners(files))
