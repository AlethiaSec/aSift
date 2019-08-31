import os
from os import listdir
from os.path import isfile, join
from colorama import Fore, Back

mypath = "./"
onlyfiles = [f for f in listdir(mypath) if isfile(join(mypath, f))]

def clearterm():
    os.system("cls")


def check(file, srchstr):
    with open(file) as f:
        datafile = f.readlines()
    found = False  # This isn't really necessary
    for line in datafile:
        if srchstr.upper() in line.upper():
            # found = True # Not necessary
            return True
    return False


def highlight(key, text):
    """
    Replace case insensitive
    Raises ValueError if string not found
    """
    index_l = text.lower().index(key.lower())
    return text[:index_l] + Fore.RED + text[index_l:index_l + len(key)] + Fore.RESET + text[index_l + len(key):]


def resolve(searchterm):
    clearterm()
    found = False
    for fname in onlyfiles:
        try:
            with open(fname, encoding="utf8") as infile:
                if check(fname, searchterm.upper()):
                    for line in infile:
                        if searchterm.upper() not in line.upper():
                            pass
                        else:
                            found = True
                            print(highlight(searchterm, 'Found: ' + line + ' (' + fname + ")"))
                else:
                    pass
        except:
            pass
    if found==False:
        print("We found nothing!")
    else:
        print("Done!")
    input("\nPress enter to return!")
    main()

def main():
    clearterm()
    print("aSift - By Alethia\n")
    srchtm = input("user@aSift:/dbs/~$ ")
    resolve(srchtm)

main()