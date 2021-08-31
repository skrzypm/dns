# This is a sample Python script.

# Press Shift+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.

import shutil
import getpass
import socket
from datetime import datetime

# hostname = socket.gethostname()
username = getpass.getuser()
now = datetime.now()
date = (str(now).replace(" ","_")).replace(":","")[:17]
# data1 = str(date)[:17]

files = ['db.mnc006.mcc260.gprs','db.mnc006.mcc260.gprs-p4-view','db.mnc006.mcc260.3gppnetwork.org','db.mnc006.mcc260.3gppnetwork.org-p4-view']

log = open('C:\GIT_Core\dns\log\logfile_'+(date)+'.log', 'w')
log.write(username+' '+str(now)+'\n')


for i in files:
    orginal = r'C:\GIT_Core\dns\working' + "\\" + i + ".txt"
    backup = r'C:\GIT_Core\dns\backup' + "\\" + i + ".bac"
    log.write(30*"#"+" " + i + 30*"#"+" "+'\n')
    with open(orginal, 'r') as file1:
        file1 = file1.readlines()
        file1 = set(file1[8:])
        with open(backup, 'r') as file2:
            file2 = file2.readlines()
            file2 = set(file2[8:])
            same = set(file1).difference(set(file2))
            diffr = set(file2).difference(set(file1))

    same.discard('\n')
    diffr.discard("\n")

    if ( same != set()):
        log.write(30 * "*" + "Zostaly dodane nowe wpisy" + 30 * "*" + "\n")
        for x in sorted(same):
            log.write(str(x)+'\n')
    else:
        log.write(30 * " " + "Brak modyfikacji" + 30 * " " + "\n")

    if ( diffr != set()):
        log.write(30 * "*" + "Zostaly usuniete wpisy" + 30 * "*" + "\n")
        for y in sorted((diffr)):
            log.write((str(y)+'\n'))

    shutil.copyfile(orginal, backup)

log.write((3*"\n"))



