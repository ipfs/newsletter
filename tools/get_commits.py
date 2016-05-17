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
import urllib2
import json

name_map = {
    ('Jeromy', 'jeromyj@gmail.com'): 'Jeromy Johnson',
    'juan@benet.ai': 'Juan Benet',
    'dignifiedquire@gmail.com': 'Friedel Ziegelmayer',
    'kubuxu@gmail.com': 'Jakub Sztandera',
    }

def apply_name_map(name, email):
    "Attempt to convert a name+email into a name"

    if (name, email) in name_map:
        return name_map[(name, email)]
    if email in name_map:
        return name_map[email]
    return name

author_repo_map = {}

def main(repo_path, start, end):
    if not start < end:
        raise ValueError("`start` must be before `end`", start, end)
    print "Getting all commits made between %s and %s" % (start.isoformat(), end.isoformat())


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
            if commit_time >= start and commit_time <= end:
                n = apply_name_map(commit.author.name, commit.author.email)
                authors.add(n)
                author_repo_map[n] = (repo_path.split(os.sep)[-2], commit.oid)


    print "\nContributors for this period (%s to %s):" % (start.isoformat(), end.isoformat())
    for a in sorted(authors):
        try:
            f = urllib2.urlopen("https://api.github.com/repos/ipfs/%s/commits/%s" % author_repo_map[a])
            js = json.load(f)
            # example:
            # @eminence (Andrew Chin)
            # [@githubname](githuburl) (author_name)
            print "* [@%s](%s) (%s)" % (js['author']['login'], js['author']['html_url'], js['commit']['author']['name'])
        except:
            print "*", a, "https://github.com/ipfs/%s/commit/%s" % author_repo_map[a]
    print ""



if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument('--start')
    parser.add_argument('--end')
    parser.add_argument('repo_dirs', help="Path to directories container all IPFS repos")
    args = parser.parse_args()

    start = None
    end = None
    if args.start:
        start = dateparser.parse(args.start)
    if args.end:
        end = dateparser.parse(args.end)
    main(args.repo_dirs, start, end)

