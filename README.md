# CFG-Degree Assignments

## Useful Information About Me

### The Basics

- My name is  **<sup><u>Curtisha It</sup></u>** however I prefer to go by **<sub><u>Tish</sub></u>**.
- I have done a few MOOCs and a Python Kickstarter with CFG
- I have also done a Python and Microsoft Azure bootcamp with Firebrand

### My Hobbies & Interests
- :books: Collecting Special Editions of books :books:
- :open_book: Reading different genre of books like; Thrillers, Graphic Novels etc. :open_book:
- Currently fixated on books where the FMC's are ~~serial killers~~
- :heartbeat: I tend to struggle with RomComs be it in book form, TV shows or Movies, but I'll devour Bridgerton in any form :two_hearts:
- I love reading Manga and Webtoons
- :tv: I love anime with a passion :lantern:
- I tend to hyper fixate on different crafts but never finish them
- :thread: I really like embroidery (*this stems from growing up with a seamstress for a mom*) :sewing_needle:


## CFG-Assignments - Assignment One
This assignment is all about learning to effectively utilise GitHub for future 
projects and assignments.


![#c5f015](https://placehold.co/15x15/c5f015/c5f015.png) **Task One: Create a repository on my local machine**

I created a new repository on my local machine called `CFG-Assignments` which will hold all the work I do as part of the program.

```commandline
# Determine the current working directory
pwd
# Create a new directory which will be the go to folder for CFG assignments
mkdir CFG-Assignments
# Change directory to move into the folder
cd CFG-Assignments
# Initialise the project as a git repository
git init
# Use git status to confirm that the repository has be successfull created
git status
```
<details><summary>Click for screenshot</summary>

![Screenshot01.png](Assignment1Screenshots%2FScreenshot01.png)

</details>


![#c5f015](https://placehold.co/15x15/c5f015/c5f015.png) **Task Two: Create a private repository on GitHub**

After creating an account on GitHub, I was then able to create a new private repository with the same name as my local repository.

<details><summary>Click for screenshot</summary>

![Screenshot03.png](Assignment1Screenshots%2FScreenshot03.png)

</details>


![#c5f015](https://placehold.co/15x15/c5f015/c5f015.png) **Task Three: Create a commit and push to my GitHub repository**

Next I want to link my local repository to my remote repository on GitHub. 
To do so, I will:
 * Create a README.md file locally
 * Add it to git to track
 * Commit it
 * Ensure I'm on the main branch
 * Add the remote repository to track
 * Push the commit to the remote repository

```commandline
# Create a new file called README.md using nano
nano README.md
# Ensure the file exists and git detects it using git status
git status
# Add README.md to git to track changes
git add README.md
# Commit the file with a suitable commit message
git commit -m "Adding READMD.md file for usage in project documentation"
# Ensure the current branch is "main" to be in line with remote main branch
git branch -M main
# Add the remote repository to git to track
git remote add origin https://github.com/Tish-I/CFG-Assignments.git
# Push the commits to the main branch on the remote repository
git push -u origin main
```
<details><summary>Click for screenshot</summary>

![Screenshot02.png](Assignment1Screenshots%2FScreenshot02.png)

</details>


![#c5f015](https://placehold.co/15x15/c5f015/c5f015.png) **Task Four: Clone the GitHub repository using PyCharm**

It's easier to work on this project in PyCharm rather than using the terminal. 
My GitHub account had to be configured in Pycharm before I could clone the project into it.

 * From the main menu, click VCS -> Get from Version Control -> GitHub.
 * Log in to GitHub and clone the repository.

<details><summary>Click for screenshot</summary>

![Screenshot04.png](Assignment1Screenshots%2FScreenshot04.png)

</details>


![#c5f015](https://placehold.co/15x15/c5f015/c5f015.png) **Task Five: Adding a .gitignore file**

The purpose of this task is add a .gitignore file. 
This file is intended is to tell git to ignore certain files/folders.
In this case it will be ignoring the folder created by PyCharm which we don't want included in the repository.

The first step is to create a new branch to work on. Then the file can be created and committed to the repository.

```commandline
# Checkout a new branch
git checkout -b gitignore
# Create a new file .gitignore
nano .gitignore
# Add it to git to track
git add .gitignore
# Commit the file with a suitable commit message
git commit -m "Adding .gitignore file to avoid tracking .idea folder"
# Push the commit to GitHub while also creating a new new remote branch called requirements
git push -uf origin gitignore
```
<details><summary>Click for screenshot</summary>

![GitIgnore1.png](Assignment1Screenshots%2FGitIgnore1.png)

</details>

Next a PR is created on GitHub with a descriptive message. 
This is to allow for code review before merging to the main branch:

<details><summary>Click for screenshot</summary>

![GitIgnore2.png](Assignment1Screenshots%2FGitIgnore2.png)

</details>

The PR was then reviewed and comments were added:

<details><summary>Click for screenshot</summary>

![GitIgnore3.png](Assignment1Screenshots%2FGitIgnore3.png)

</details>

After a successful review, the PR was merged and the local main branch could be updated to pull in the latest changes:

```commandline
# Switch back to the main branch
git checkout main
# Pull the latest changes from GitHub
git pull
# print the contents of the .gitignore file to show it exists and contains the .idea folder
cat .gitignore
```

<details><summary>Click for screenshot</summary>

![GitIgnore4.png](Assignment1Screenshots%2FGitIgnore4.png)

</details>


![#c5f015](https://placehold.co/15x15/c5f015/c5f015.png) **Task Six: Create a Python file**

This task is to demonstrate creating a Python file.

```commandline
# Create a new Python file e.g. greetings.py
nano greetings.py
# Add all files to git to track
git add .
# Identify files currently stated for commiting
git status
# Commit the changes with an appropriate commit message
git commit -m "Adding greetings.py to add welcoming functionality to the project"
```

<details><summary>Click for screenshot</summary>

![Screenshot05.png](Assignment1Screenshots%2FScreenshot05.png)
![Screenshot06.png](Assignment1Screenshots%2FScreenshot06.png)
![Screenshot07.png](Assignment1Screenshots%2FScreenshot07.png)

</details>

![#c5f015](https://placehold.co/15x15/c5f015/c5f015.png) **Task Seven: Make use of `git push`**

Now that a commit has been created locally, it can be pushed to the remote repository.

Push the latest commits to GitHub from the local repository using `git push`
```commandline
# Push new commits from local main branch to remote main branch
git push
```

The repository can then be refreshed on GitHub to view the latest changes. 
It wil now show the `greeting.py` file that has been added

<details><summary>Click for screenshot</summary>

![Screenshot08.png](Assignment1Screenshots%2FScreenshot08.png)
![Screenshot09.png](Assignment1Screenshots%2FScreenshot09.png)

</details>

Changes can also be made, committed and pushed through the PyCharm IDE. 
For example, make another change to the python file `greetings.py` to make it interactive

<details><summary>Click for screenshot</summary>

![Screenshot10.png](Assignment1Screenshots%2FScreenshot10.png)

</details>

Through PyCharm, we can add and commit the file. 
Then from the main menu select `Git -> Push` to push the commits from local main branch to remote main branch

<details><summary>Click for screenshots</summary>

![Screenshot11.png](Assignment1Screenshots%2FScreenshot11.png)
![Screenshot12.png](Assignment1Screenshots%2FScreenshot12.png)

</details>

Commits can also be inspected at this point to review the latest changes

<details><summary>Click for screenshot</summary>

![Screenshot13.png](Assignment1Screenshots%2FScreenshot13.png)

</details>

Once pushed, the new commits can be seen on GitHub

<details><summary>Click for screenshot</summary>

![Screenshot14.png](Assignment1Screenshots%2FScreenshot14.png)

</details>


![#c5f015](https://placehold.co/15x15/c5f015/c5f015.png) **Task Eight: Make use of branches**

The previous sections created and added new files without making use of branching.
Branching is recommended to use in order to avoid encountering merge conflicts.
For this task I will add a new file `farewell.py` by making use of branches

```commandline
# Check the current branch
git branch
# Create a new branch called branch1
git checkout -b branch1
# List branches to ensure on the correct branch
git branch
# Create a new file, farewell.py
nano farewell.py
# Check the file can be seen by git
git status
```
<details><summary>Click for screenshot</summary>

![Screenshot15.png](Assignment1Screenshots%2FScreenshot15.png)

</details>

This file was added and committed, which then allowed it to be pushed to a new remote branch.
Once the files are committed create and push to a new branch using `push -uf origin <BranchName>`

```commandline
# Push to a new remote upstream branch called branch1
git push -uf origin branch1
```

<details><summary>Click for screenshot</summary>

![Screenshot16.png](Assignment1Screenshots%2FScreenshot16.png)

</details>

Create a new Pull Request(PR) on GitHub to merge the new commits/branch to the main branch

<details><summary>Click for screenshot</summary>

![Screenshot17.png](Assignment1Screenshots%2FScreenshot17.png)

</details>

The PR allows the changes to be reviewed and then merged to the main branch

<details><summary>Click for screenshots</summary>

![Screenshot18.png](Assignment1Screenshots%2FScreenshot18.png)
![Screenshot19.png](Assignment1Screenshots%2FScreenshot19.png)
![Screenshot20.png](Assignment1Screenshots%2FScreenshot20.png)

</details>

Once the PR has been merged the new files exist on the main branch

<details><summary>Click for screenshot</summary>

![Screenshot21.png](Assignment1Screenshots%2FScreenshot21.png)

</details>

In the local repository switch back to the main branch
```commandline
# Switch to the main branch
git checkout main
# Confirm the switch
# git branch
```

<details><summary>Click for screenshot</summary>

![Screenshot22.png](Assignment1Screenshots%2FScreenshot22.png)

</details>

Initially the commits will be missing from the main branch. 
They can be pulled and then they will appear

```commandline
# Update the current branch with the latest commits
git pull
```
<details><summary>Click for screenshot</summary>

![Screenshot24.png](Assignment1Screenshots%2FScreenshot24.png)

</details>

Alternatively, the commits can be pulled through the PyCharm IDE. 
The blue arrow next to the main branch indicates that there are changes upstream ready to pull in.

<details><summary>Click for screenshot</summary>

![Screenshot23.png](Assignment1Screenshots%2FScreenshot23.png)

</details>


![#c5f015](https://placehold.co/15x15/c5f015/c5f015.png) **Task Nine: Adding a requirements.txt file**

The purpose of this task is add a requirements.txt file. 
This file is intended is to keep track of any python libraries required for use in a virtual environment.

The first step is to create a new branch to work on. Then the file can be created and committed to the repository.

```commandline
# Checkout a new branch
git checkout -b requirements
# Create a new file requirements.txt
nano requirements.txt
# Add it to git to track
git add requirements.txt
# Commit the file with a suitable commit message
git commit -m "Adding placeholder python requirements.txt file"
# Push the commit to GitHub while also creating a new remote branch called requirements
git push -uf origin requirements
```
<details><summary>Click for screenshot</summary>

![Requirements1.png](Assignment1Screenshots%2FRequirements1.png)

</details>

Next a PR is created on GitHub with a descriptive message. 
This is to allow for code review before merging to the main branch:

<details><summary>Click for screenshot</summary>

![Requirements2.png](Assignment1Screenshots%2FRequirements2.png)

</details>

The PR was then reviewed and comments were added:

<details><summary>Click for screenshot</summary>

![Requirements3.png](Assignment1Screenshots%2FRequirements3.png)

</details>

After a successful review, the PR was merged and the local main branch could be updated to pull in the latest changes:

```commandline
# Switch back to the main branch
git checkout main
# Pull the latest changed from GitHub
git pull
# print the contents of the requiments.txt file to show it exists
cat requirements.txt
```

<details><summary>Click for screenshot</summary>

![Requirements4.png](Assignment1Screenshots%2FRequirements4.png)

</details>