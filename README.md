# HTML Me Something

You've learned a bit of HTML and some CSS, but you have likely only used it in bits and pieces so far, adding or modifying content in exercises or pre-existing files. We're going to take another step forward here.

You'll be building your own web page from scratch, and utilizing GitHub for storing and hosting your page. GitHub's primary use is to host Git repositories, but they also have a cool feature called [GitHub Pages](https://pages.github.com/) that allows you to easily host web sites that consist of only HTML and CSS (and perhaps some front-end JavaScript). You will build your own site using GitHub Pages, and once you're finished you will  add your work back to this repository, where it will be listed alongside that of your classmates.

## Getting started

There are two parts to this exercise, one focused on HTML and another focused on CSS. HTML makes up the *structure and content* of web pages, while CSS dictates the *visual style*.

Best practices dictate that these should be kept as separate as possible. To that end, we'll build the HTML portion of our page first, and only then add a few styles with CSS. This will help us avoid adding HTML elements simply to change the style of our page.

### Fork and clone

To get started, you'll need to make a copy of this repository on your own computer. Rather than just download it, we'll use Git to manage the copying process so that your work will be managed with version control, and can easily be incorporated back into this project when you're done.

You should have already:
* installed Git on your computer
* created a GitHub account
* configured your Git install to use your GitHub account
* practiced basic Git commands such as `add`, `commit`, and `push`

If you haven't done these things, go back and do the pre-work outlined on the course page.

Now, fork this project by clicking on the Fork button at the top right of this page:

![fork button](images/fork-button.png)

Recall that this makes a *copy* of the repository and places it in your GitHub account. GitHub will redirect you to your new project page once the fork has been created. At the top right of this page, click on the "Clone or download" button and copy the URL from the text box.

![clone button](images/clone.png)

Now, in a terminal navigate to the directory where you store your code, and type

```
$ git clone [URL]
```

where `[URL]` is the URL you copied from GitHub, pasted into the terminal. This will clone your copy of the `html-me-something` repository to your computer, so that you have a copy of the repository to work on locally.

Verify that everything went according to plan by changing directories into the new project, and checking the Git status.

```
$ cd html-me-something/
$ git status
```

You should see a message like this:

```
On branch master
Your branch is up-to-date with 'origin/master'.
nothing to commit, working directory clean
```

If you don't, make sure you're in the correct directory (use `pwd`), retrace your steps through the instructions above.

A few more steps and we'll be ready to go:

* In the `submissions` directory, create a new directory with the same name as your GitHub username:
    ```
    $ cd submissions/
    $ mkdir [USERNAME]
    ```
* Jump down into this new directory, and create and open a new file, `index.html`. Add a single line with the following HTML and save: `<p>YOUR NAME</p>`
* In Terminal, from the project root folder (you'll need to run `cd ../..` to get there) run `git add .` to stage your new file. Then commit and push it to your fork. When pushing, note that you're on the `gh-pages` branch of the project, not the `master` branch (as you'll often be, and will see most often in documentation). So push using
    ```
    git push origin gh-pages
    ```
* You should be able to view your page live at http://&lt;username&gt;.github.io/html-me-something/submissions/&lt;username&gt;/. This may take a few minutes to go live, so if you don't see it right away, try again in a few minutes. This is the magic of [GitHub Pages](https://pages.github.com)

## Getting to work

Now it's time to build a page! Dive in, then come back here to follow submission instructions.

- HTML portion

- CSS portion

## Submitting your work

### Pull request

Now that you've created a lovely page, let's request that it be added to the main project repository, so course staff can add it to the class submissions directory.

### Vocareum
