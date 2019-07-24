import praw
import pdb
import re
import os

import datetime

import sqlite3 as lite
import sys

# Initialize Reddit
reddit = praw.Reddit('nixBot_v0')

# Get userlist

with open("uncontactedUsers.txt", "r") as f:
    userList = f.read()
    userList = userList.split("\n")
    userList = list(filter(None, userList))


# Send message

subject = "I can haz convo about kwitting smoking pleez"

with open("messagingLog_batch2.txt", "w") as f:

    for user in userList[1:100]:
        print(user)

        reddit.redditor(user).message("Can I interview you on quitting smoking?",
    
                                      "First off, I am not a troll. Promise :).\n\n" +
                                      "I'm a student at Georgia Tech. Tech's a stressful school. So unfortunately, I have a lot of friends that smoke/vape.\n\n" +
                                      "This summer, I'm working on a project to help smokers quit smoking. I'm trying to speak with 100 people and extract patterns from all the narratives I hear.\n\n" +
                                      "May I please talk to you about your journey through smoking cessation? I just want to hear your story about quitting. " +
                                      "I totally understand your privacy concerns and would be happy to work with any constraints you have.\n\n" +
                                      "THANKS!\n\n" +
                                      "P.S. this doesn't change the fact that I'm a total rando, but this is me www.mohammedaamir.com/about :)")

        f.write(user + "\t" + subject + "\t" + datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S") + "\n")

