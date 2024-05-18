# CFG-Degree Assignments

## Useful Information About Me

### The Basics

- My name is **Curtisha It** however I prefer to go by **Tish**.
- I have done a few MOOCs and a Python Kickstarter with CFG
- I did a Python and Microsoft Azure bootcamp with Firebrand

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

![#c5f015](https://placehold.co/15x15/c5f015/c5f015.png) **Task one: Create a repository on my local machine**
<details><summary>Click for screenshot</summary>

![Screenshot01.png](Assignment1Screenshots%2FScreenshot01.png)

</details>

The steps were as follows:
+ Determine current directory using: `pwd`
+ Create a new project directory using `mkdir <ProjectName>`
+ Moving into the directory using`cd <ProjectName>`
+ Initialise the project as a git repo using: `git init`
+ Verify the repo is initialised using `git status`

![#c5f015](https://placehold.co/15x15/c5f015/c5f015.png) **Task two: Create a repository on GitHub**
<details><summary>Click for screenshot</summary>

![Screenshot03.png](Assignment1Screenshots%2FScreenshot03.png)

</details>

I was able to create a new private repository on GitHub

![#c5f015](https://placehold.co/15x15/c5f015/c5f015.png) **Task three: Create a commit and push to my GitHub repository**
<details><summary>Click for screenshot</summary>

![Screenshot02.png](Assignment1Screenshots%2FScreenshot02.png)

</details>

The steps were as follows:
+ Create a README.md file using `nano README.md`
+ Identify the new READMD.md file is currently unstaged using `git status`
+ Stage the file for committing using `git add README.md` 
+ Create a commit with commit message using `git commit -m "Commit message"` 
+ Rename current branch to "main" using `git branch -M main`
+ Add the GitHub Repository and track it using `git remote add origin <https...>` 
+ Push the commit to the GitHub main branch using `git push -u origin main`


![#c5f015](https://placehold.co/15x15/c5f015/c5f015.png) **Task four: Clone the GitHub repository using PyCharm**
<details><summary>Click for screenshot</summary>

![Screenshot04.png](Assignment1Screenshots%2FScreenshot04.png)

</details>

The steps were as follows:
+ From the main menu, click VCS -> Get from Version Control -> GitHub.
+ Log in to GitHub and clone the repository.

![#c5f015](https://placehold.co/15x15/c5f015/c5f015.png) **Task five: Create a python file and use `.gitignore`**
<details><summary>Click for screenshot</summary>

![Screenshot05.png](Assignment1Screenshots%2FScreenshot05.png)

</details>

The steps were as follows:
+ Create a new python file e.g. greetings.py
+ View current state of the git repo using `git status`
+ Identify the newly created python file along with a `.idea` folder
+ Create a new file called `.gitignore`
+ Add `.idea` to the `.gitignore` file to tell git to ignore the folder and avoid tracking it
+ Add all new files and changes using `git add .` 
<details><summary>Click for screenshot</summary>

![Screenshot06.png](Assignment1Screenshots%2FScreenshot06.png)

</details>

+ Identify changed staged for committing using: `git status`
+ Commit the changes using `git commit -m "Commit message"`
<details><summary>Click for screenshot</summary>

![Screenshot07.png](Assignment1Screenshots%2FScreenshot07.png)

</details>

![#c5f015](https://placehold.co/15x15/c5f015/c5f015.png) **Task six: Make use of `git push`**

The steps were as follows:

<details><summary>Click for screenshot</summary>

![Screenshot08.png](Assignment1Screenshots%2FScreenshot08.png)

</details>

Push the latest commits to GitHub from the local repository using `git push`

<details><summary>Click for screenshot</summary>

![Screenshot09.png](Assignment1Screenshots%2FScreenshot09.png)

</details>

Refresh the GitHub page to see newly added files from the commits

The changes can be successfully viewed here:

<details><summary>Click for screenshot</summary>

![Screenshot10.png](Assignment1Screenshots%2FScreenshot10.png)

</details>

Make another change to the python file `greetings.py` to make it interactive

<details><summary>Click for screenshots</summary>

![Screenshot11.png](Assignment1Screenshots%2FScreenshot11.png)
![Screenshot12.png](Assignment1Screenshots%2FScreenshot12.png)

</details>

+ Add and commit the change via pycharm rather than through the terminal
+ From the main menu select Git -> Push


<details><summary>Click for screenshot</summary>

![Screenshot13.png](Assignment1Screenshots%2FScreenshot13.png)

</details>

This shows the differences in the changes made to my greetings.py file

<details><summary>Click for screenshot</summary>

![Screenshot14.png](Assignment1Screenshots%2FScreenshot14.png)

</details>

This shows updated commits on my remote repository

![#c5f015](https://placehold.co/15x15/c5f015/c5f015.png) **Task seven: Make use of branches**
<details><summary>Click for screenshot</summary>

![Screenshot15.png](Assignment1Screenshots%2FScreenshot15.png)

</details>

The steps were as follows:
+ List the branches that currently exist using `git branch`
+ In the case main is the only branch that exists
+ Create and switch to a new branch called `branch1` using `git checkout -b <branch1>`
+ List the existing branches again using `git branch`
+ The "*" indicates which the repository is currently on 
+ Create a new python file in the `branch1` branch. E.g. `farewell.py`
+ Show the untracked file using `git status`
<details><summary>Click for screenshot</summary>

![Screenshot16.png](Assignment1Screenshots%2FScreenshot16.png)

</details>

Once the files are committed create and push to a new branch using `push -uf origin <BranchName>`

<details><summary>Click for screenshot</summary>

![Screenshot17.png](Assignment1Screenshots%2FScreenshot17.png)

</details>

Create a new Pull Request on GitHub to merge the new commits/branch to the main branch

<details><summary>Click for screenshots</summary>

![Screenshot18.png](Assignment1Screenshots%2FScreenshot18.png)
![Screenshot19.png](Assignment1Screenshots%2FScreenshot19.png)
![Screenshot20.png](Assignment1Screenshots%2FScreenshot20.png)

</details>

The Pull Request allows the changes to be reviewed and then merged to the main branch

<details><summary>Click for screenshot</summary>

![Screenshot21.png](Assignment1Screenshots%2FScreenshot21.png)

</details>

Once the Pull Request has been merged the new files exist on the main branch

<details><summary>Click for screenshot</summary>

![Screenshot22.png](Assignment1Screenshots%2FScreenshot22.png)

</details>

In the local repository switch to the main branch using `git checkout main`

<details><summary>Click for screenshot</summary>

![Screenshot23.png](Assignment1Screenshots%2FScreenshot23.png)

</details>

+ Initially the new file is missing from the main branch
+ The blue arrow indicates that there are changes upstream ready to pull in.
+ These changes can be pulled into the main branch using the Pycharm interface

<details><summary>Click for screenshot</summary>

![Screenshot24.png](Assignment1Screenshots%2FScreenshot24.png)

</details>

+ Alternatively the changes can be pulled in via the terminal
+ After pulling the changes, the new files now exist on the local main branch

![#c5f015](https://placehold.co/15x15/c5f015/c5f015.png) **Bonus: Using Pycharm to push/pull**

In order to do this I made some changes to my farewell.py file and pushed it
<details><summary>Click for screenshots</summary>

![Screenshot25.png](Assignment1Screenshots%2FScreenshot25.png)
![Screenshot26.png](Assignment1Screenshots%2FScreenshot26.png)
![Screenshot27.png](Assignment1Screenshots%2FScreenshot27.png)

</details>

And finally pulled my changes to update my local repository
<details><summary>Click for screenshot</summary>

![Screenshot28.png](Assignment1Screenshots%2FScreenshot28.png)

</details>




