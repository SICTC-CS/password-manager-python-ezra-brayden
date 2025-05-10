import os
import ast
import random
import string
import sys
import re 

db = 'db.txt'
loginCount = 0
pswrdLoop = False

class createProfile:
    def __init__(account, acntName,  username, password):
        account.acntName = acntName
        account.username = username
        account.password = password

#Functions to log into the main program
def login():
    global mainName, mainUser, mainPswrd, correct
    print("Login to Password Manager")
    mainName = input("Enter your first and last name: ")
    mainUser = input("Enter your username: ")
    mainPswrd = input("Enter your password: ")
    checkLogin()
    
def checkLogin():
    global mainName, mainPswrd, mainUser, correct, loginCount
    rightName = False
    rightUser = False
    rightPswrd = False
    correct= False
    with open(db, 'r') as file:
            for line in file:
                if rightName == False:
                    if mainName in line:
                        rightName= True
                if rightUser == False:
                    if mainUser in line:
                        rightUser = True
                if rightPswrd == False:
                    if mainPswrd in line:
                        rightPswrd= True
                        correct = True
    if correct == False:
        if loginCount < 2:
            loginCount +=1
            print("Try Again")
            login()
        else:
            quit()
    else:
        print("You are Logged in")
    
#Function that creates an account
def createAcnt():
    mainName = input("Enter your first and last name: ")
    mainUser = input("Enter your username: ")
    mainPswrd = input("Enter your password: ")
    mainAcnt = createProfile(mainName, mainUser, mainPswrd)
    data=[]
    data.append(mainAcnt.acntName)
    data.append(mainAcnt.username)
    data.append(mainAcnt.password)
    login()

    #db method from geeks for geeks
    with open(db, 'w+') as file:
        for i in data:
            file.write('%s\n' %i)
#got a little help from gpt here, but I changed it to fit the problem
def newUser():
    if os.path.getsize(db) == 0:
        print("Create an Account")
        createAcnt()
    else:
        login()

#User Input section

def inputUser():
    global pswrdLoop, mainPswrd
    mainName = input("Enter your first and last name: ")
    mainUser = input("Enter your username: ")
    
    print("Password requires 1 capital letter, 1 special character, 1 number, and must be at least 8 characters long.")
    mainPswrd = input("Enter your password: ")
    pswrdCheck()
    if pswrdLoop == False:
        print("Invalid Password :(")
        inputUser()
    else:
        print("Valid Password!")
    mainAcnt = createProfile(mainName, mainUser, mainPswrd)
    data=[]
    data.append(mainAcnt.acntName)
    data.append(mainAcnt.username)
    data.append(mainAcnt.password)

def pswrdCheck():
    global pswrdLoop, mainPswrd
    correctSpecs =0
    if (len(mainPswrd) >= 8):       #geeks for geeks gave me the starter code, changed the variable system and how the correct password is checked
        for i in mainPswrd:
            # counting lowercase alphabets 
            if (i.islower()):
                correctSpecs+=1            
            # counting uppercase alphabets
            if (i.isupper()):
                correctSpecs+=1            
            # counting digits
            if (i.isdigit()):
                correctSpecs+=1            
            # counting the special characters
            if(i=='@'or i=='$' or i=='_'):
                correctSpecs+=1           
    if correctSpecs >=4:
        pswrdLoop = True
    

def userInput():
    newInput = input("Would you like to input a password? (y or n): ")
    if newInput == "y":
        inputUser()
    more = input("Would you like to input another password? (y or n): ")
    if more == "y":
        more = True
    elif more == "n":
        more = False
    while more == True:
        inputUser()
        more = input("Would you like to input another password? (y or n): ")
        if more == "y":
            more = True
        elif more == "n":
            more = False
        
    
    
#password generator
#def generatePswrd():


newUser()
userInput()