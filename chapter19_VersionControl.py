#add your GitHub repository
$ git clone [repository_url]

#the command GIT REMOVE -V prints the central repository your local repository is pushing and pulling from
$ git remote -v
#the URLs for pushing and pulling(fetch) will usually be the same

#to push changes from local repository to central, first you need to stage the files
$ git status

#enter the name of the file that you want to push then enter GIT STATUS to confirm
$ git add [file_name]

#to unstage a file from making changes to your central:
$ git reset [file_path]

#once you've staged the files, you are ready to move to commiting
$ git commit -m ["your_message"]

#then once you've commited, you can push
$ git push origin master

#you can update your local repository from changes in your cental repository
$ git pull origin master
