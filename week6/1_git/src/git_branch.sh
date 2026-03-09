#!/bin/bash
source git_example.sh

cd $TEST_DIR/working_copy_1

# create 'mybranch' to work in to avoid changing 'main' branch
git checkout -b mybranch
# push branch to remote, set upstream
git remote -v
git push -u origin mybranch
git branch -a
gitk --all


# make some changes in 'mybranch'
echo "line6" >> file.txt
git commit -am "added line6 in mybranch"
git push  # 'main' doesn't see 'mybranch' changes yet

echo "line7" >> file.txt
git commit -am "added line7 in mybranch"
git push  # 'main' doesn't see 'mybranch' changes yet

echo "line8" >> file.txt
git commit -am "added line8 in mybranch"
git push  # 'main' doesn't see 'mybranch' changes yet

cat file.txt
gitk --all


# switch back to 'main' and make changes there
git checkout main
change_line 2 file.txt "line2 edit wc1"
cat file.txt
git commit -am "changed line2 in main"
git push
gitk --all


# merge 'mybranch' into 'main'
git merge mybranch
cat file.txt
git push  # now 'main' sees 'mybranch' changes
gitk --all


# done with 'mybranch', remove it
git branch -d mybranch
# remove 'mybranch' from remote
git push origin --delete mybranch
git branch -a
gitk --all
