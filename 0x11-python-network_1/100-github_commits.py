#!/usr/bin/python3
""" Script that list ten commits for a repository
and an owner"""
import requests
import sys


if __name__ == '__main__':
    the_repo = sys.argv[1]
    the_owner = sys.argv[2]
    the_url = "https://api.github.com/repos/{}/{}/commits".format(
        the_repo, the_owner)

    the_req = requests.get(the_url)
    the_commits = the_req.json()
    try:
        for i in range(10):
            print("{}: {}".format(
                the_commits[i].get("sha"),
                the_commits[i].get("commit").get("author").get("name")))
    except IndexError:
        pass
