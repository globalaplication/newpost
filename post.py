#!/usr/bin/env python
# -*- coding: utf-8 -*-
import urllib
import os
class post(object):
    def __init__ (self):
        url = "http://forum.pardus.org.tr/latest"
        self.file = urllib.urlopen(url)
        self.posts = ""
        if os.path.exists("./latest") is True:
            with open("./latest") as read:
                r = read.read()
            self.source = r
        else:
            self.source = ""

    def run(self, id=0):
        
        for test in self.file:
            
            if test.find("<span itemprop='name'>") is not -1:
                
                id = id + 1
                
                latest =self.chrreplace(self.gettag(test))
                self.posts = self.posts + latest + "\n"
                
                if self.source.find(latest) is -1:
                    self.temp(latest)
                    
                if id < self.getindex(latest): 
                    print ("yenipost", latest)
        
        self.update()

    def gettag(self, line):
        start = line.find(">") + 1
        end = line.find("<", start)
        return line[start:end]
    def chrreplace(self, string):
        dict = {"&#39;":"'"}
        for rep in dict:
            string = string.replace(rep, dict[rep])
        return string
    def temp(self, latest):
         with open("./latest", "a") as post:
            post.write(latest+"\n")
    def getindex(self, post):
        file = open("./latest")
        for enum, i in enumerate(file, 1):
            if i.strip("\n") == post:
                return int(enum)
    def update(self):
        with open("./latest", "w") as w :
            w.write(self.posts)
        print("ok!")
            
get = post()
get.run()
