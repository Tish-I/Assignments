# Useful Information About Me

My name is Curtisha It however I prefer to go by Tish.

## CFG-Assignments
### Assignment One
This assignment is all about learning to effectively utilise GitHub for future 
projects and assignments.

The first task was to create a repository on my local machine
![Screenshot01.png](Assignment1Screenshots%2FScreenshot01.png)
The steps were as follows:
I used pwd to determine my current directory
Then made a new directory using mkdir <CFG-Assignments>
cd <CFG-Assignments> took me into this newly created directory
I used git init to initialise a repository
git status then showed me that my repo was initialised, and I was in the master branch
and hadn't made any changes so there was nothing to commit.

The Second task involved making my first commit in order push my repository 
![Screenshot02.png](Assignment1Screenshots%2FScreenshot02.png)
The steps were as follows:
I used nano to make my first file which in this instance was a README.md
git status then showed I had one commit in the form of the README.md
git add <README.md> allowed me to stage my file for committing 
git commit -m allowed me to commit my file with a description 
git branch -M renamed 'master' to 'main'
git remote add origin <https...> and git push -u origin main allowed my local commits to the repository on GitHub

This shows successful push of the repository
![Screenshot03.png](Assignment1Screenshots%2FScreenshot03.png)
I was able to set the newly pushed repository as private and finally click create a new repository.

The Third task involved using PyCharm and cloning from my remote repository
![Screenshot04.png](Assignment1Screenshots%2FScreenshot04.png)
The steps were as follows:
I needed to choose VCS|Get from Version Control in the main menu, then choose GitHub.
I was then able to log in to GitHub and clone my repository.

The Fourth task was making a py file and using .gitignore
![Screenshot05.png](Assignment1Screenshots%2FScreenshot05.png)
I made a py file titled greetings.py then used git status to track the state of my files
This showed the created py as well as a .idea/
I created a new file titled .gitignore and added .idea/ into it.
I then used git add . to stage all my changes 
![Screenshot06.png](Assignment1Screenshots%2FScreenshot06.png)
I used git status once more in order to track my changes.
git commit -m allowed me to commit my files with a description
![Screenshot07.png](Assignment1Screenshots%2FScreenshot07.png)

The Fifth task shows the use of git push 
![Screenshot08.png](Assignment1Screenshots%2FScreenshot08.png)
I used git push in order to push my newly created files from my local repository to my remote repository.
The changes can be successfully viewed here;
![Screenshot09.png](Assignment1Screenshots%2FScreenshot09.png)

I wanted to make my greetings.py file interactive
![Screenshot10.png](Assignment1Screenshots%2FScreenshot10.png)
I've made my changes, and I'm now ready to commit them
![Screenshot11.png](Assignment1Screenshots%2FScreenshot11.png)
Using the main menu tab in my IDE I selected Git then Push, selected all my changes and used my commit button to add my commit message and pushed my changes.
![Screenshot12.png](Assignment1Screenshots%2FScreenshot12.png)

This shows the differences in the changes made to my greetings.py file
![Screenshot13.png](Assignment1Screenshots%2FScreenshot13.png)

This shows updated commits on my remote repository
![Screenshot14.png](Assignment1Screenshots%2FScreenshot14.png)

The sixth task shows the use of branches
![Screenshot15.png](Assignment1Screenshots%2FScreenshot15.png)
The steps were as follows:
git branch lists the branches currently created. In the case main is the only one
git checkout -b branch1 allowed me to make and name a new branch titled branch1 and immediately switch into it.
Using git branch again lists branch1 and main the <*> indicates which branch I'm currently in.
I then created a second py file titled farewell.py inside branch1
git status shows the untracked file.
![Screenshot16.png](Assignment1Screenshots%2FScreenshot16.png)
I used push -uf origin branch1 to create and update the remote branch1 with my new commits

This shows a newly created pull request on GitHub
![Screenshot17.png](Assignment1Screenshots%2FScreenshot17.png)

This shows the merging of the pull request to the main branch
![Screenshot18.png](Assignment1Screenshots%2FScreenshot18.png)
![Screenshot19.png](Assignment1Screenshots%2FScreenshot19.png)
![Screenshot20.png](Assignment1Screenshots%2FScreenshot20.png)

This shows the created branch live in the remote repository
![Screenshot21.png](Assignment1Screenshots%2FScreenshot21.png)

In order to pull edited branch1 changes to the main branch on my local repository.
I first needed to switch back to the main branch using git checkout main
![Screenshot22.png](Assignment1Screenshots%2FScreenshot22.png)

This screenshot shows changes in my remote repository could be pulled down into my main branch on my local repository
using built-in system on pycharm 
![Screenshot23.png](Assignment1Screenshots%2FScreenshot23.png)

I chose to use git pull in order to pull my changes to the main branch
![Screenshot24.png](Assignment1Screenshots%2FScreenshot24.png)

I wanted to demonstrate the built-in push system on pycharm
In order to do this I made some changes to my farewell.py file and pushed it
![Screenshot25.png](Assignment1Screenshots%2FScreenshot25.png)
![Screenshot26.png](Assignment1Screenshots%2FScreenshot26.png)
![Screenshot27.png](Assignment1Screenshots%2FScreenshot27.png)
And finally pulled my changes to update my local repository
![Screenshot28.png](Assignment1Screenshots%2FScreenshot28.png)





