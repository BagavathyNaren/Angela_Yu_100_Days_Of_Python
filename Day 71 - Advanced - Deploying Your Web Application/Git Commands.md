Create a new repository on the command line

echo "# MyLife" >> README.md
git init
git add README.md
git commit -m "first commit"
git branch -M main
git remote add origin https://github.com/BagavathyNaren/MyLife.git
git push -u origin main


--------------------------------------------------------------------------------


Push an existing repository from the command line

git remote add origin https://github.com/BagavathyNaren/MyLife.git
git branch -M main
git push -u origin main



--------------------------------------------------------------------------------

git init            => Initialize Git


git add .           => Add multiple files

git add <FileName>  => Add Specific file

git status          => Check the file in staging area

git log             => Check the commits made by person


git push origin main  => send your commits to your remote branch

Combine Add + Commit + Push

git add . && git commit -m "Your message" && git push origin main


git rm -r --cached folder_name/ => git rm -r --cached folder_name/


🧩 1️⃣ git pull — Get the latest from remote

Command:

git pull origin main


Meaning:

Downloads the latest commits from the remote branch (origin/main)

Merges them into your local branch

Essentially:
🡒 git fetch + git merge in one step

Use when: You want your branch updated with the latest remote changes.

Example:

git pull origin dev


Updates your local dev branch with remote dev.

🧩 2️⃣ git merge — Combine branches

Command:

git merge feature-branch


Meaning:

Merges another branch (e.g. feature-branch) into your current branch.

Example:
You’re on main:

git merge feature-branch


🡒 Combines changes from feature-branch into main.

Two types:

Fast-forward merge – if no new commits diverged, Git just moves the branch pointer.

3-way merge – if both branches diverged, Git creates a merge commit.

Use when: You want to integrate changes while keeping commit history intact.

🧩 3️⃣ git rebase — Reapply commits on top of another base

Command:

git rebase main


Meaning:

Takes your current branch’s commits and replays them on top of the target branch (main).

It re-writes history to make it look linear.

Example:
If feature-branch was branched from an older main,
you can do:

git checkout feature-branch
git rebase main


Now your feature branch looks like it was built on the latest main.

Use when: You want a clean, linear commit history (no merge commits).

⚠️ Warning: Avoid rebasing shared/public branches — it rewrites history.

🧩 4️⃣ git cherry-pick — Apply a specific commit from another branch

Command:

git cherry-pick <commit-hash>


Meaning:

Takes a single commit from anywhere and applies it to your current branch.

Example:
You’re on main and want one fix from feature-branch:

git cherry-pick a1b2c3d


🡒 That commit is now added to main.

Use when: You want to apply specific changes from another branch without merging the entire branch.

⚡ Summary Table

Command	Purpose	Modifies History?	           Typical Use

git pull	                        Fetch + Merge remote changes	No	Update local repo
git merge	                                    Combine branches	No	Keep all commits
git rebase	                          Replay commits on new base	Yes	Linearize history
git cherry-pick	                            Copy a single commit	No	Apply specific fixes

🧠 Quick Visual Summary

Main:       A --- B --- C --- D

Feature:          \--- E --- F

Merge →    A --- B --- C --- D --- M
                          \--- E --- F

Rebase →   A --- B --- C --- D --- E' --- F'


🧩 1️⃣ git clone — Copy a remote repository to your local machine

Command:

git clone <repository-url>


Meaning:

Makes a full local copy of a remote repository (including all history, branches, tags, etc.)

Automatically sets up the origin remote.

Example:

git clone https://github.com/username/project.git


This will:

Create a folder project/

Initialize a Git repo inside it

Download all commits from the remote

Optional (clone a specific branch):

git clone -b dev https://github.com/username/project.git

🧩 2️⃣ git pull --rebase — Update your branch cleanly

Command:

git pull --rebase origin main


Meaning:

Fetches the latest changes from the remote (like git fetch)

Instead of merging, it rebases your local commits on top of the updated remote branch.

Normal pull (git pull):

Remote: A --- B --- C
Local:        \--- D --- E
Result: Merge commit F created


Rebase pull (git pull --rebase):

Remote: A --- B --- C
Local:                  \--- D' --- E'


Your commits are “replayed” on top of the remote branch — no merge commit is created.

🧠 Why use --rebase?
git pull (merge)	git pull --rebase
Keeps full commit history (including merge commits)	Keeps linear, clean history
Adds an extra merge commit	Rewrites local commits to be on top of remote
Safer for collaboration	Cleaner for personal or feature branches

Best practice:

Use git pull for shared branches (like main or develop)

Use git pull --rebase for your personal feature branches

🧩 3️⃣ How to set rebase as default pull behavior

If you prefer rebase pulls always:

git config --global pull.rebase true


Now git pull will automatically behave like git pull --rebase.

⚡ Summary Table
Command	Purpose	Key Use Case
git clone	Copy a remote repo locally	Start working on an existing repo
git pull	Fetch + merge remote changes	Update local branch with merge commits
git pull --rebase	Fetch + rebase local commits on top of remote	Keep history linear and clean
--------------------------------------------------------------------------------