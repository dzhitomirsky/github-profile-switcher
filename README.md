# Github prfile switcher

## Intro
Sometime you may face the situation when you want to commit under different github profiles/accouts, 
e.g. at office you use company accout _google-john-doe_ and at home you want to create super-secret projects
under your persona github accout _john-doe_ and also you do it all on **MACBOOK**.

## Manual steps 
To do the actions described above you need to:
* drop _~/.git-credentials_ folder
* rewrite _~/.gitconfig_ file like
```
[user]
        email = {email}
	      name =  {user}

[credential]
        helper = store

[push]
        default = current
```
* as far as you use macbook drop _github_ note in **keychain**

All this stuff is a long stroy...so I introduce a small fency script written ib python 2.7 to do all this for you

## How to use 
* clone the repo
```bash
git clone https://github.com/dzhitomirsky/github-prfile-switcher
```
* add next env variables (potensially you will need sudo mode - so add them to _~/.bashrc_ and _visudo_)
```
HOME_USER 
HOME_EMAIL

WORK_USER 
WORK_EMAIL 
```

if you want to do it per terminal sessions:
```bash
export HOME_USER=super-user
...
```

* call the script
```python
#to setup home env
python gitprofile.py home 

#to setup work env
python gitprofile.py work


#work env is used by default
#next line will give the same result as python gitprofile.py work
python gitprofile.py
```

## Setup script to PATH to use from place
* create _~/bin_ (if it doesn't exit)
* add _bin_ folder to PATH (if it isn't so), you can also make it in _.bashrc_ to make it constant 
```bash
export PATH=$PATH:/home/el/bin
```
* copy _gitprofile.py_ to  _bin_
```bash
cd github-prfile-switcher
cp gitprofile.py ~/gitprofile
```
* make it executable
```bash
chmod +x ~/bin/gitprofile
```
* Call it in any place
```bash
gitprofile work #work profile
gitprofile home #home profile
gitprofile #work profile by default
```
