# ssh_brute_basic
A simple ssh bruteforcer written in python

      Usage: python3   ssh_brute.py  [options]   argument

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

Some good wordlists

      https://github.com/danielmiessler/SecLists/blob/master/Passwords/Common-Credentials/10-million-password-list-top-1000000.txt
      
      https://www.google.com/url?sa=t&rct=j&q=&esrc=s&source=web&cd=&cad=rja&uact=8&ved=2ahUKEwi578K0s-jrAhV8wTgGHe0-ABcQFjAAegQIAxAB&url=https%3A%2F%2Fgithub.com%2Fbrannondorsey%2Fnaive-hashcat%2Freleases%2Fdownload%2Fdata%2Frockyou.txt&usg=AOvVaw3snAERl1mU6Ccr4WFEazBd
