#!/usr/bin/python
# -*- coding: utf-8

import praw
import pdb
import re
import os

import sqlite3 as lite
import sys

# Initialize database

con = lite.connect('users.db')

with

with con:
    cur = con.cursor()
    #cur.execute("CREATE TABLE Users(Name TEXT)")

    for user

# Initialize reddit

reddit = praw.Reddit('nixBot_v0')
subreddit = reddit.subreddit('stopsmoking')

for submission in subreddit.hot(limit=10):
    print(submission.author)
