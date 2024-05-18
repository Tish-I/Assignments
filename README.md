# CFG-Degree Assignments

## Useful Information About Me

**The Basics**

- My name is Curtisha It however I prefer to go by Tish.
- I have done a few MOOCs and a Python Kickstarter with CFG
- I did a Python and Microsoft Azure bootcamp with Firebrand

**My Hobbies & Interests**
- :books: Collecting Special Editions of books :books:
- :open_book: Reading different genre of books like; Thrillers, Graphic Novels etc. :open_book:
- Currently fixated on books where the FMC's are ~~serial killers~~
- :heartbeat: I tend to struggle with RomComs be it in book form, TV shows or Movies but I'll devour Bridgerton in any form :two_hearts:
- I love reading Manga and Webtoons
- :tv: I love anime with a passion :lantern:
- I tend to hyper fixate on different crafts but never finish them
- :thread: I really like embroidery (*this stems from growing up with a seamstress for a mom*) :sewing_needle:


## CFG-Assignments
### Assignment One
This assignment is all about learning to effectively utilise GitHub for future 
projects and assignments.

![#c5f015](https://placehold.co/15x15/c5f015/c5f015.png) **The first task was to create a repository on my local machine**
<details><summary>Click for screenshot</summary>

![Screenshot01.png](Assignment1Screenshots%2FScreenshot01.png)

</details>

The steps were as follows:
I used `pwd` to determine my current directory.
Then made a new directory using `mkdir <CFG-Assignments>`.
`cd <CFG-Assignments>` took me into this newly created directory.
I used `git init` to initialise a repository
`git status` then showed me that my repo was initialised, and I was in the master branch
and hadn't made any changes so there was nothing to commit.


![#c5f015](https://placehold.co/15x15/c5f015/c5f015.png) **The Second task involved making my first commit in order to push my repository**
<details><summary>Click for screenshot</summary>

![Screenshot02.png](Assignment1Screenshots%2FScreenshot02.png)

</details>

The steps were as follows:
I used `nano` to make my first file which in this instance was a README.md
`git status` then showed I had one commit in the form of the README.md
`git add <README.md>` allowed me to stage my file for committing 
`git commit -m` allowed me to commit my file with a description 
`git branch -M` renamed 'master' to 'main'
`git remote add origin <https...>` and `git push -u origin main` allowed my local commits to the repository on GitHub

This shows successful push of the repository
<details><summary>Click for screenshot</summary>

![Screenshot03.png](Assignment1Screenshots%2FScreenshot03.png)

</details>
I was able to set the newly pushed repository as private and finally click create a new repository.

![#c5f015](https://placehold.co/15x15/c5f015/c5f015.png) **The Third task involved using PyCharm and cloning from my remote repository**
<details><summary>Click for screenshot</summary>

![Screenshot04.png](Assignment1Screenshots%2FScreenshot04.png)

</details>

The steps were as follows:
I needed to choose VCS|Get from Version Control in the main menu, then choose GitHub.
I was then able to log in to GitHub and clone my repository.

![#c5f015](https://placehold.co/15x15/c5f015/c5f015.png) **The Fourth task was making a py file and using `.gitignore`**
<details><summary>Click for screenshot</summary>

![Screenshot05.png](Assignment1Screenshots%2FScreenshot05.png)

</details>

I made a py file titled greetings.py then used `git status` to track the state of my files
This showed the created py as well as a .idea/
I created a new file titled `.gitignore` and added .idea/ into it.
I then used `git add .` to stage all my changes 
<details><summary>Click for screenshot</summary>

![Screenshot06.png](Assignment1Screenshots%2FScreenshot06.png)

</details>

I used `git status` once more in order to track my changes.
`git commit -m` allowed me to commit my files with a description
<details><summary>Click for screenshot</summary>

![Screenshot07.png](Assignment1Screenshots%2FScreenshot07.png)

</details>

![#c5f015](https://placehold.co/15x15/c5f015/c5f015.png) **The Fifth task shows the use of `git push`**
<details><summary>Click for screenshot</summary>

![Screenshot08.png](Assignment1Screenshots%2FScreenshot08.png)

</details>
I used `git push` in order to push my newly created files from my local repository to my remote repository.
The changes can be successfully viewed here;
<details><summary>Click for screenshot</summary>

![Screenshot09.png](Assignment1Screenshots%2FScreenshot09.png)

</details>

I wanted to make my greetings.py file interactive
<details><summary>Click for screenshot</summary>

![Screenshot10.png](Assignment1Screenshots%2FScreenshot10.png)

</details>

I've made my changes, and I'm now ready to commit them
<details><summary>Click for screenshot</summary>

![Screenshot11.png](Assignment1Screenshots%2FScreenshot11.png)

</details>
Using the main menu tab in my IDE I selected Git then Push, selected all my changes and used my commit button to add my commit message and pushed my changes.
<details><summary>Click for screenshot</summary>

![Screenshot12.png](Assignment1Screenshots%2FScreenshot12.png)

</details>

This shows the differences in the changes made to my greetings.py file
<details><summary>Click for screenshot</summary>

![Screenshot13.png](Assignment1Screenshots%2FScreenshot13.png)

</details>

This shows updated commits on my remote repository
<details><summary>Click for screenshot</summary>

![Screenshot14.png](Assignment1Screenshots%2FScreenshot14.png)

</details>

![#c5f015](https://placehold.co/15x15/c5f015/c5f015.png) **The sixth task shows the use of branches**
<details><summary>Click for screenshot</summary>

![Screenshot15.png](Assignment1Screenshots%2FScreenshot15.png)

</details>

The steps were as follows:
`git branch` lists the branches currently created. In the case main is the only one
`git checkout -b <branch1>` allowed me to make and name a new branch titled branch1 and immediately switch into it.
Using `git branch` again lists branch1 and main the <*> indicates which branch I'm currently in.
I then created a second py file titled farewell.py inside branch1
`git status` shows the untracked file.
<details><summary>Click for screenshot</summary>

![Screenshot16.png](Assignment1Screenshots%2FScreenshot16.png)

</details>

I used `push -uf origin <branch1>` to create and update the remote branch1 with my new commits

This shows a newly created pull request on GitHub
<details><summary>Click for screenshot</summary>

![Screenshot17.png](Assignment1Screenshots%2FScreenshot17.png)

</details>

This shows the merging of the pull request to the main branch
<details><summary>Click for screenshot</summary>

![Screenshot18.png](Assignment1Screenshots%2FScreenshot18.png)
![Screenshot19.png](Assignment1Screenshots%2FScreenshot19.png)
![Screenshot20.png](Assignment1Screenshots%2FScreenshot20.png)

</details>

This shows the created branch live in the remote repository
<details><summary>Click for screenshot</summary>

![Screenshot21.png](Assignment1Screenshots%2FScreenshot21.png)

</details>

In order to pull the edited branch1 changes to the main branch on my local repository.
I first needed to switch back to the main branch using `git checkout main`
<details><summary>Click for screenshot</summary>

![Screenshot22.png](Assignment1Screenshots%2FScreenshot22.png)

</details>

This screenshot shows changes in my remote repository could be pulled down into my main branch on my local repository
using built-in system on pycharm 
<details><summary>Click for screenshot</summary>

![Screenshot23.png](Assignment1Screenshots%2FScreenshot23.png)

</details>

I chose to use git pull in order to pull my changes to the main branch
<details><summary>Click for screenshot</summary>

![Screenshot24.png](Assignment1Screenshots%2FScreenshot24.png)

</details>

I wanted to demonstrate the built-in push system on pycharm
In order to do this I made some changes to my farewell.py file and pushed it
<details><summary>Click for screenshot</summary>

![Screenshot25.png](Assignment1Screenshots%2FScreenshot25.png)
![Screenshot26.png](Assignment1Screenshots%2FScreenshot26.png)
![Screenshot27.png](Assignment1Screenshots%2FScreenshot27.png)

</details>

And finally pulled my changes to update my local repository
<details><summary>Click for screenshot</summary>

![Screenshot28.png](Assignment1Screenshots%2FScreenshot28.png)

</details>




