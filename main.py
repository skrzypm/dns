# This is a sample Python script.

# Press Shift+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.

import shutil
import os
import socket
from datetime import datetime

hostname = socket.gethostname()
now = datetime.now()


files = ['db.mnc006.mcc260.gprs','db.mnc006.mcc260.gprs-p4-view','db.mnc006.mcc260.3gppnetwork.org','db.mnc006.mcc260.3gppnetwork.org-p4-view']

for i in files:
    orginal = r'C:\GIT_Core\dns\working'+"\\"+ i +".txt"
    backup = r'C:\GIT_Core\dns\backup'+ "\\" +i +".bac"
    # shutil.copyfile(orginal,backup)
    print(orginal)
    print(backup)
    log = open('C:\GIT_Core\dns\log\logfile.txt', 'a+')
    log.write(hostname+' '+str(now)+'\n')
    log.write((i+'\n'))
    with open(orginal, 'r') as file1:
        with open(backup, 'r') as file2:
            same = set(file1).difference(file2)
            diff = set(file2).difference(file1)



    same.discard('\n')
    diff.discard("\n")
    if ( same == set()):
        pass
    else:
        for x in sorted(same):
            log.write(str(x)+'\n')
            for y in sorted((diff)):
                log.write((str(y)+'\n'))

    # with open('C:\GIT_Core\dns\log\logfile.txt', 'w') as file_out:
    #     for line in same:
    #         file_out.write(line)

# log = open('C:\GIT_Core\dns\log\logfile.txt','w')

