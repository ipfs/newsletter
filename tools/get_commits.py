#!/usr/bin/env python2

# If you have virtualenv installed:
#
# $ python2 virtualenv.py venv
# $ venv/bin/pip install pygit2 dateparser

# To run:
# $ venv/bin/python tools/get_commits.py $HOME/ipfs_stuff/repos

# Pass this tool a folder that contains all of the IPFS repos you wish to scan
# It will output a list of authors

import pygit2
import dateparser
import glob
import argparse
import sys
import os.path
import time
from datetime import datetime,timedelta
from pprint import pprint

name_map = {
    ('Jeromy', 'jeromyj@gmail.com'): 'Jeromy Johnson',
    'juan@benet.ai': 'Juan Benet',
    'dignifiedquire@gmail.com': 'Friedel Ziegelmayer',
    }

def apply_name_map(name, email):
    "Attempt to convert a name+email into a name"

    if (name, email) in name_map:
        return name_map[(name, email)]
    if email in name_map:
        return name_map[email]
    return name



def main(repo_path, start, days):

    oneweek_ago = start - timedelta(days)
    print "Getting all commits made between %s and %s" % (start.ctime(), oneweek_ago.ctime())


    authors = set()
    repos = glob.glob(os.path.join(repo_path, "*", ".git"))
    print "Scanning for repos... Found %d repos" % len(repos)
    print "If they have a remote named `origin`, it will be fetched from..."


    for repo_path in repos:

        repo = pygit2.Repository(repo_path)
        for remote in repo.remotes:
            if remote.name == "origin":
                try:
                    transfer = remote.fetch()
                    while transfer.received_objects < transfer.total_objects:
                        time.sleep(0.1)
                        print "\r%d of %d    " % (transfer.received_objects, transfer.total_objects) ,
                    print "Fetch complete for", remote.url
                except:
                    print "Error while fetching for", repo_path, remote.url



        master_oid = repo.lookup_reference("refs/remotes/origin/master").target

        for commit in repo.walk(master_oid, pygit2.GIT_SORT_TIME):
            commit_time = datetime.fromtimestamp(commit.commit_time)
            if commit_time >= oneweek_ago:
                authors.add(apply_name_map(commit.author.name, commit.author.email))


    print "\nContributors for this period (%s to %s):" % (oneweek_ago.ctime(), start.ctime())
    for a in sorted(authors):
        print "*", a
    print ""



if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument('--end', default='')
    parser.add_argument('--days', type=int, default=7, help="Default is 7 days")
    parser.add_argument('repo_dirs', help="Path to directories container all IPFS repos")
    args = parser.parse_args()

    start = None
    if args.end:
        start = dateparser.parse(args.end)
    if start is None:
        start = datetime.now()
    main(args.repo_dirs, start, args.days)

