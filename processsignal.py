#!/ser/bin/env python3
#-*- coding: utf-8- -*-

import os,signal
def chldHandler(signum,stackframe):  
    while 1:  
        try:  
            result = os.waitpid(-1,os.WNOHANG)  
        except:  
            break
        print 'Reaped child process %d' % result[0]  
signal.signal(signal.SIGCHLD,chldHandler)
