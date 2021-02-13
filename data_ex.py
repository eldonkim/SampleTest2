#!/usr/bin/python

import sys
import re

if __name__ == '__main__' :

    xList = []
    labels = []
    names = []
    firstLine = True
    
    for line in sys.stdin :
        if firstLine :
            names = line.strip().split(";")
            firstLine = False
        else :
            row = line.strip().split(";")
            labels.append(float(row[-1]))

            row.pop()
            floatRow = [ float(num) for num in row ]
            xList.append(floatRow)


    print len(xList)
    print len(xList[0])
    print xList[0]

