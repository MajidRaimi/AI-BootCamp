# (Git / GitHub ) Cheat Sheet

### Using git or github for the first time ? 
### You only need to do this once
```bash
git config --global user.name "Put Your Username Here"
git config --global user.email "Put Your Email Here"
```
you will also have a login procedure to your github account
<hr>

## Five steps needed to add your project to <a href="https://github.com/">Github</a>


### 1. Go to the root of the project and initialize (.git) in your project :
```bash
git init
```

### 2. Add all the files to the staging area :
```bash
git add .
```
you can add file by file "file.py" for example or you can add all the files using the dot " . " . 

### 3. Commit the changes :
```bash
git commit -m "Put Your Commit Message Here"
```

### 4. Create a new repository on Github and connect it to your project :
```bash
git remote add origin {repository_link}
```

### 5. Push the changes to Github :
```bash
git push origin master
```

<hr>

## How to clone a project ? 
### Go to the root of the project and clone the project :
```bash
git clone {repository_link}
```

<hr>

## How to update your project ?
### Go to the root of the project :
```bash
git pull origin master
```



