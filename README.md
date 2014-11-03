Dconf
========
Never Ever Redo Duh Conf

> The goal of NERDconf is to sync shell and system config files across multipull Users and Operating Systems. NERDconf uses git track files you want to be consistant on all your machienes. Each machine just runs a cron job that updates conf every five minuites. If you infact need to force confupdate, dont worrie its easy peasy! 
######STOP WAISTING TIME CONFIGURING UR SETUP, SPEND YOUR TIME HACKING INSTEAD :)

Easy Peasy - how to NERDconf
----
 - add files to NERDconf
```sh 
nerdc -a /path/to/conf.conf 
```
 - remove files from NERDconf
```sh 
nerdc -r /path/to/conf.conf
```
 - update all configs
```sh
nerdc -u
```

 - list config files tracked by NERDconf
```sh
nerdc -l
```

 - get some help
```sh
nerc -h
```


System Requirements
----
 - Python 3.3
 - git
 - Mac 10.x or Ubuntu (possibly add Arch)

Instulation
------------
```sh
git clone git@github.com:dwolfm/nerdconf
cd nerdconf/bin/
sudo setup_nerdconf.py
```

Removal
-------
```sh
cd nerdconf/bin/
sudo remove_nerdconf.py
```

Version
----
0.0 aint made it


Complaints
----
email me at [dwolfm@gmail.com]

[dwolfm@gmail.com]:dwolfm@gmail.com



