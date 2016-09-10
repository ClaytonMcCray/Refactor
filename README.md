This is a (mainly) variable refactoring script that I wrote
because I like using vim, but have no idea how to natively refactor
variable names. If you use linux or OSX, it is useful to add this 
file to your .bashrc alias list (which is in the home folder on Linux,
I have no idea how it works on OSX).

`alias refactor='path/to/script/./refactor.py`

This line is your .bashrc will allow you to invoke the refactor script
like this:

`refactor filename old_phrase new_phrase`

The program will create a file called backup.txt in addition to making the
refactor changes. backup.txt is an exact replica of the original file.
The program is written for python 3, and is (untested, but ought to be)
cross platform (written on Debian Linux).

