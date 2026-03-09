#!/bin/bash
source git_helpers.sh

## list all global configs
git config --global --list

## setup test directory
TEST_DIR=/tmp/git_test   # test in temporary directory
mkdir -p $TEST_DIR
cd $TEST_DIR
rm -rf my_remote working_copy_1 working_copy_2

## create repos
git init --bare -b main my_remote
git clone my_remote working_copy_1
git clone my_remote working_copy_2

## add file.txt in working_copy_1
cd working_copy_1
echo "line1" >> file.txt
echo "line2" >> file.txt
cat file.txt
git add file.txt
git ls-files
git status
git commit -m "added file.txt in wc1"
git status
git log
git push

## get file.txt in working_copy_2
cd ../working_copy_2
git fetch
git merge 
# or 'git pull' for fetch + merge
git log
ls
cat file.txt

## add lines to file.txt in working_copy_2
echo "line3" >> file.txt
echo "line4" >> file.txt
echo "line5" >> file.txt
cat file.txt
git status
git add file.txt
git status
git commit -m "added to file.txt in wc2"
git status
git log
git push

## get changes in file.txt in working_copy_1
cd ../working_copy_1
git pull
git log
cat file.txt

## change line 5 in working_copy_1
change_line 5 file.txt "line5 edit wc1"
cat file.txt
git commit -am "changed line 5 in wc1"
# '-a' auto-stage modified files: add + commit
git log
git push

## change line 1 in working_copy_2
cd ../working_copy_2
change_line 1 file.txt "line1 edit wc2"
cat file.txt
git commit -am "changed line 1 in wc2"
git log
git push  # doesn't work: remote has changes
git pull  # first pull these changes
git log
cat file.txt
git push  # now we can push

# now change line 3 in working_copy_2
change_line 3 file.txt "line3 edit wc2"
cat file.txt
git commit -am "changed line 3 in wc2"
git push

## now change the same line 3 in working_copy_1, CONFLICT!!!
cd ../working_copy_1
change_line 3 file.txt "line3 edit wc1"
cat file.txt
git commit -am "changed line 3 in wc1 ALSO"
git pull
git status

## fix conflict manually
cat file.txt
replace_conflict file.txt "line3 resolve wc1 wc2"
cat file.txt
git status
git add file.txt  # signal conflict is resolved
git status
git commit -m "fixed the conflict"
git push
git log
gitk --all # graphical repo viewer
