from github import Github
import requests
import unittest
from bs4 import BeautifulSoup
import urllib
from lxml import etree
from lxml import html
import requests
import urllib
import re   # regex
import time



access_token="ebaf1a22abd62458e8583dc7e43773c09fc59d38"
gh = Github(access_token)

#########" test connection###########
user = gh.get_user()
repo = user.get_repo("RepoName")
for repo in gh.get_user().get_repos():
    print(repo.name)

###################################

def calculmeanstars( gh,username):
    k=0
    summeanuser=0
    for r in gh.get_user(username).get_repos():
        summeanuser=summeanuser+r.stargazers_count
        k=k+1
    if k==0 :
        return 0
    else :
        return summeanuser/k
###################################

topusers_dict = {}
for useraccount in listtopusers : 
    print("processing  " + useraccount)
    topusers_dict.update({useraccount:calculmeanstars(gh,useraccount)})
    time.sleep(2)

print(topusers_dict)
############# 


