# basic git commands

## Configuring git

* git config # configures git as we need it
system - all users
global - repo of current user
local - current repo
git config --global user.name "User Name"
git config --global user.email "email"
git config --global core.editor "code --wait" # code -> vs code --wait -> wait for user to close file
git config --global -e #opens the editor for changing all the configured settings
git config --global diff.tool vscode # tells git that we will use vscode for git diff

*
git init
git status (-s for short) # used to check the status of the files in the repo
A - added
M - modified but not in staging area yet
R - renamed
?? - untracked
green - ready to be committed
red - files changed after

*
git add # adds the given files to staging area to commit later 
(removes the file from staging area if it is not found in dir)

## some styles to add files

file1.txt file2.txt
\*.txt #adds all files with .txt extension
. # adds all files except the ones gitignored

*
help
git command --help # for full help/docs
git command -h #just for a hint

*

git ls-files # shows the files git is tracking

*

git rm #removes files from working directory as well as staging area

*

git mv #moves files (renames files if the dir is same)

*

if a file is tracked already then gitignore might not work so we have to use
git rm --cached <file/folder> which removes it from staging area once
(-r for removing recursively i.e it it a folder)

*
git diff # used to check the change in exact lines of code we made
git diff-tool # same thing but in vsc window
(--staged for checking the files in the staging area)

## info for reading `git diff` messages

two different copies of the file
a/file.txt - old file
b/file.txt - new file (in staging area)

## legend

--- (dev/null means the file is new) removals (changes in old copy)
+++ additions (changes on new copy)
index ... (metadata - doesn't matter much to us)

## header (only part of a change is shown at once (chunk-⬇️))

@@ -c,d +m,n @@  

-indicates old file, + indicates new file
c-d lines are shown from old
m-n lines are shown from new

*

git log # view history (latest to earliest)
 q - quit
 --oneline (shows everything in one line)
 space (next page)
 --reverse (reverse the sorting order)

*

 git show (open a particular commit)
 (HEAD~1) (for comparing the commit with the head (the last commit))
 :path (shows the file data in that commit)
 we can use the random id generated and shown in

*

 git ls-tree (shows the files and directories stored in a commit)
 git ls-files (shows the files added )

*

git restore path (to restore file to last commit version)

git clean (to undo local changes)
git revert
git restore --source==HEAD~1 path ( restores files/dir to previous versions)
