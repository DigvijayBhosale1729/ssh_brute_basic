# ssh_brute_basic
A simple ssh bruteforcer written in python

Usage:  python3   ssh_brute.py  [options]   argument

Options:

      -h, --help  show this help message and exit

      -u USER     Specify User name

      -H HOST     Specify host name

     -p PASSWD   Specify dictionary file

      -t          Specify if you want to thread the process. Makes it faster but slightly more haphazard
  
Requirements

Python3

pexpect module

Install pexpect by using 

  sudo pip install pexpect

If pip isn't installed install it along with python-setuptools
