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
# Passes 4/4 tests

class Path:
    def __init__(self, path):
        self.current_path = path

    def cd(self, new_path):
        i=0;
        new_pathList=new_path.split('/')
        pathLength=len(new_pathList)
        pathList=self.current_path.split('/')
        #print(new_PathList)
        if new_pathList[0]=='':
            #direct pathname
            del pathList[:]
            pathList.append('/'+new_pathList[1])
            i=i+2
        while(i<pathLength):
            j=len(pathList)-1
            if new_pathList[i]=='..':
                #parent directory
                pathList.pop(j)
            else:
                pathList.append(new_pathList[i])
            i=i+1
        self.current_path="/".join(pathList)

        pass

path = Path('/a/b/c/d')
path.cd('/x/y/../z')
print(path.current_path) # '/x/z'
