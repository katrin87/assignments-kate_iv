kat@kat:~$ sudo apt-get install git
[sudo] password for kat: 
Reading package lists... Done
Building dependency tree       
Reading state information... Done
git is already the newest version.
0 upgraded, 0 newly installed, 0 to remove and 26 not upgraded.
kat@kat:~$ git config ..global user.name "katrin87"
kat@kat:~$ git config ..global user.email "katriell@mail.ru"
kat@kat:~$ ls
assignments-kate  examples.desktop  pycharm-community-5.0.3  Templates
Desktop           Music             PycharmProjects          Videos
Documents         Pictures          python_information
Downloads         Public            README.md
kat@kat:~$ lsdir
No command 'lsdir' found, did you mean:
 Command 'lndir' from package 'xutils-dev' (main)
 Command 'lsdic' from package 'canna-utils' (universe)
lsdir: command not found
kat@kat:~$ mkdir
mkdir: missing operand
Try 'mkdir --help' for more information.
kat@kat:~$ mkdir assignments_kate_iv
kat@kat:~$ ls
assignments-kate     Downloads         Public                   README.md
assignments_kate_iv  examples.desktop  pycharm-community-5.0.3  Templates
Desktop              Music             PycharmProjects          Videos
Documents            Pictures          python_information
kat@kat:~$ cd assignments_kate_iv
kat@kat:~/assignments_kate_iv$ git init
Initialized empty Git repository in /home/kat/assignments_kate_iv/.git/
kat@kat:~/assignments_kate_iv$ git init
Reinitialized existing Git repository in /home/kat/assignments_kate_iv/.git/
kat@kat:~/assignments_kate_iv$ git remote add origin https://github.com/katrin87/assignments-kate_iv.git
kat@kat:~/assignments_kate_iv$ git push -u origin master
Username for 'https://github.com': katrin87
Password for 'https://katrin87@github.com': 
error: src refspec master does not match any.
error: failed to push some refs to 'https://github.com/katrin87/assignments-kate_iv.git'
kat@kat:~/assignments_kate_iv$ git remote add origin https://github.com/katrin87/assignments-kate_iv.git
fatal: remote origin already exists.
kat@kat:~/assignments_kate_iv$ git commit -m "First commit"
On branch master

Initial commit

nothing to commit
kat@kat:~/assignments_kate_iv$ git add .
kat@kat:~/assignments_kate_iv$ git commit -m "First commit"
On branch master

Initial commit

nothing to commit
kat@kat:~/assignments_kate_iv$ git push origin master
Username for 'https://github.com': katrin87
Password for 'https://katrin87@github.com': 
error: src refspec master does not match any.
error: failed to push some refs to 'https://github.com/katrin87/assignments-kate_iv.git'
kat@kat:~/assignments_kate_iv$ git add .
kat@kat:~/assignments_kate_iv$ git commit -m "First commit"
[master (root-commit) 9054bd5] First commit
 1 file changed, 4 insertions(+)
 create mode 100644 assignments_kate_iv.py
kat@kat:~/assignments_kate_iv$ git push origin master
Username for 'https://github.com': katrin87
Password for 'https://katrin87@github.com': 
Counting objects: 3, done.
Delta compression using up to 4 threads.
Compressing objects: 100% (2/2), done.
Writing objects: 100% (3/3), 267 bytes | 0 bytes/s, done.
Total 3 (delta 0), reused 0 (delta 0)
To https://github.com/katrin87/assignments-kate_iv.git
 * [new branch]      master -> master
kat@kat:~/assignments_kate_iv$ git push origin master
Username for 'https://github.com': katrin87
Password for 'https://katrin87@github.com': 
Everything up-to-date
kat@kat:~/assignments_kate_iv$ 
