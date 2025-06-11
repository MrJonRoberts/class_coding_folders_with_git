# CLASS CODING WITH GIT
This repository contains some scripts that are used to create a branch for each student in the class and then have a save (commit and push) script to run.
Using Git: Teaching Digital Technology.

Requirements:
•	Python installed
•	Git installed
•	A GitHub account for each member.

1.	Create a GitHub repository. 
2.	Protect the master branch (settings -> Rules -> Branch ruleset)
3. Clone the repository to your local computer.
4.	Add files and folders for each student:

  	a.Assignment Folder

  	i.	A1

  	  1.	Task Sheet
    
    b.	Notes Folder

  	  1.	ANY NOTES GO IN HERE.

c.	.gitignore
i.	Add the following to the .gitignore: 

  create_class_git.py
  
  clone_repo.py
  
  students.txt
  
  expected_hash
  
  LICENSE
  
  README.md

  .gitignore

5.	Add the save_work.py to the folder.
6.	Edit clone_repo.py with your repo URL as REPO_URL
7.	Create a students.txt with a single student ID on each line.
8.	Commit and Push to GitHub
9.	Run clone_repo.py
10.	Distribute clone_repo.py to each student and have them run it. (can provide via link to file in master branch)
a.	They should run it and enter an ID: eg xx123213
b.	This will pull the branch for their ID student
11.	They use the folders as usual.
12.	Run save_work.py to commit (with the default date) at the end of each session. (could modify to have it auto save in the background)
    a.	Minimal security checks to see if the hash is the same and won't run.

