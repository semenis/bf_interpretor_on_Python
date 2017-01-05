#!/usr/bin/python3
#
# Brainfuck Interpreter
# Copyright 2016 Semenis
#



a=[]
size=30000
for i in range (size):
    a.append(0)
curr=0
###################
def bracketfinder(s):
    counter=0
    for i in range(len(s)):
        if s[i]=='[':
            counter+=1
        if s[i]==']':
            counter-=1
        if counter==0:
            return i
###################
def runcode(dey):
    global curr
    
    i=0
    while i<len(dey):
        if dey[i]=='>':
            curr+=1
            if curr==size:
                curr=0
        elif dey[i]=='<':
            curr-=1
            if curr==-1:
                curr=(size-1)
        elif dey[i]=='+':
            a[curr]+=1
            if a[curr]==256:
                a[curr]=0
        elif dey[i]=='-':
            a[curr]-=1
            if a[curr]==-1:
                a[curr]=255
        elif dey[i]=='.':
            print(chr(a[curr]), end='')
        elif dey[i]==',':
            a[curr]=ord(input())
        elif dey[i]=='[':
            closebr=bracketfinder(dey[i:])
            if a[curr]==0:
                i=closebr+i
            else:
                runcode(dey[i+1:closebr+i])
                i-=1
        else:
            i+=1
            continue
        i+=1
runcode(input("Please enter the code: "))
