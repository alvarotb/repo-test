# --start
import sys

def klingon():  #add
    print('nuqneH')  #add

def default():
    print('o que voce quer?')

def main():
    if sys.argv[1] == 'klingon':
       klingon()
    elif sys.argv[1] == 'volcano':	#modified
       volcano()
    else:
       default()

if __name__ == '__main__':
    main()
# --end
