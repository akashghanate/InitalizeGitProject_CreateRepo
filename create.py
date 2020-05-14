import sys
import os
from dotenv import load_dotenv
from github import Github

load_dotenv()
username=os.getenv("username")
password=os.getenv("password")
path=os.getenv("path")

 
def create():
    directory= sys.argv[1]
    fullpath=os.path.join(path,directory)
    os.makedirs(fullpath)
    g = Github(username,password).get_user()
    repo = g.create_repo(directory)


if __name__=="__main__":
    create()


