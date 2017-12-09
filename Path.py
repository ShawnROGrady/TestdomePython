# Created by Shawn O'Grady on 12/9/17.
# Copyright 2017 Shawn O'Grady. All rights reserved.

 #This code is a practice Python interview question from testdome.com

 #https://www.testdome.com/questions/python/path/12282?visibility=1&skillId=9

 # Problem statement: Write a function that provides change directory (cd) function for an abstract file system.
    #Notes:
        #i) Root path is '/'
        #ii) Path separator is '/'
        #iii) Parent directory is addressable as '..'
        #iv) Directory names consist only of English alphabet letters (A-Z and a-z)
        #v) The function should support both relative and absolute paths
        #vi) The function will not be passed any invalid paths
        #vii) Do not use built-in path-related functions.
class Path:
    def __init__(self, path):
        self.current_path = path

    def cd(self, new_path):
        pass

path = Path('/a/b/c/d')
path.cd('../x')
print(path.current_path)
