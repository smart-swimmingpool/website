#!/usr/bin/env python
# -*- coding: utf-8 -*-

# This python script will clone all repos defined in "multiversion.yml".
# It checks out all version tags (starting with "v") and grab all files matching
# the given file pattern. The files are prefixed with the version and added
# to the docs directory.
#
# A version switcher html code is generated and prepended to all copied files.
#
# License: Public domain
# Author: David Graeff <david.graeff@web.de>

import yaml
import io
import os
import re
import fnmatch
import shutil
import difflib
import coloredlogs, logging
from pathlib import Path
from git import Repo,Git

def readyaml():
    with open("multiversion.yml", 'r') as stream:
        try:
            content = yaml.load(stream)
            return content
        except yaml.YAMLError as exc:
            print(exc)
            exit(-1)

# Split a markdown content by its 2nd level headings and return the array
def split_by_headings(data):
    sections = []
    index = 0
    while True:
        index = data.find("\n## ", index)
        if index == -1:
            break
        nextindex = data.find("\n## ", index+1)
        if nextindex == -1:
            sections.append(data[index:])
            break
        else:
            sections.append(data[index:nextindex])
        index = nextindex
    return sections

# Create a destination filename, given the repo name ("core","ota" etc),
# and the tag name ("master","v2.0").
def dest_filepath(reponame, refname):
    reponame = reponame.replace(" ","-").lower()
    return os.path.join(reponame, refname)

# Copy files to "docs/". Filter sections of file first. Add generated header to file.
def write_file(reponame, targetdir, srcdir, filename, data, tagname, date, absurl):
    logging.info("--> write_file (")
    logging.info("  reponame: "+reponame)
    logging.info("  targetdir: "+targetdir)
    logging.info("  srcdir: "+srcdir)
    logging.info("  filename: "+filename.name)
    logging.info(")")

    sections = split_by_headings(data)
    if len(sections)<=0:
        logging.info("No sections to keep in "+filename.name)
        logging.info("<-- write_file")
        return

    header = "---\n"
    header += "source: "+absurl+"\n"
    header += "file: "+filename.name+"\n"
    header += "lastmod: "+date.strftime("%d. %B %Y")+"\n"
    header += "---\n"

    # New file content and filename
    filecontent = data #header + "\n".join(sections)
    #filepath = os.path.join(targetdir,dest_filepath(reponame, tagname)+".md")
    filepath = os.path.join(targetdir,dest_filepath(reponame, filename.name))
    filename = Path(filepath)
    filename.parent.mkdir(parents=True, exist_ok=True)
    logging.info("write filename: "+filename.name)
    with open(filename, "w+", encoding="utf8") as text_file:
        text_file.write(filecontent)
    logging.info("<-- write_file")

# Clone a repository url (or update repo), checkout all tags.
# Call copy_files for each checked out working directory
def checkout_repo(targetdir, reponame, repourl, filepattern, checkoutdir, update_repos):
    logging.info("--> checkout_repo repourl="+repourl)
    localpath = os.path.join(checkoutdir,reponame)
    if os.path.exists(localpath):
        repo = Repo(localpath)
        if update_repos:
            print("Updating "+reponame)
            repo.remotes.origin.fetch()
    else:
        print("Clone "+reponame+" to "+localpath)
        repo = Repo.clone_from(repourl, localpath)

    # Add "master"
    refs = []
    refs.append(repo.heads.master)

    # Get all preface sections from the latest master version
    repo.head.reference = repo.heads.master
    repo.head.reset(index=True, working_tree=True)

    g = Git(localpath)
    # read all files of a repo and create target files out of them
    for ref in refs:
        repo.head.reference = ref
        repo.head.reset(index=True, working_tree=True)
        logging.info("localpath="+localpath+", filepattern="+filepattern)
        #for filename in fnmatch.filter(os.listdir(localpath), filepattern):
        for filepath in Path(localpath).rglob(filepattern):
            #filepath = os.path.join(localpath,filename)
            logging.info("  filepath.name: " + filepath.name)
            with open(filepath, 'r', encoding="utf8") as myfile:
                logging.info("  myfile: " + myfile.name)
                localdata = myfile.read()
                # Check if the file has relevant sections
                sections = split_by_headings(localdata)
                if len(sections)<=0:
                    continue
                tagname = ref.name
                date = ref.commit.committed_datetime
                absurl = repourl.replace(".git","")+"/tree/"+ref.name
                write_file(reponame, targetdir, localpath, filepath, localdata, tagname, date, absurl)
    logging.info("<-- checkout_repo")


def recreate_dir(file_path, clean):
    logging.info("--> recreate_dir")
    directory = os.path.abspath(file_path)
    if clean and os.path.exists(directory):
        shutil.rmtree(directory)
    if not os.path.exists(directory):
        os.makedirs(directory)
    logging.info("<-- recreate_dir directory="+directory)
    return directory

# Main program
coloredlogs.install()
logging.basicConfig(level=logging.INFO)
logging.info("Starting grabrepos ...")
controlfile = readyaml()
checkoutdir = recreate_dir("temp", "clean" in controlfile and controlfile["clean"])
targetdir = os.path.abspath("content/en/docs")
update_repos = "updaterepos" in controlfile and controlfile["updaterepos"]
#if os.path.exists(targetdir):
#    shutil.rmtree(targetdir)
#    os.makedirs(targetdir)
for entry in controlfile['specifications']:
    if not 'disabled' in entry or not entry['disabled']:
        checkout_repo(targetdir, entry['name'], entry['repo'], entry['filepattern'],checkoutdir, update_repos)
logging.info("Finshed.")
