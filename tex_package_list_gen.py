#!/usr/bin/env python
# -*- coding: utf-8 -*-
# Filename: tex_package_list_gen.py
# Author:   Lyu Ming <CareF.Lm@gmail.com>
import re, pickle
from os import popen

pacpattern = re.compile(r'^i ([^:]*): (.*)$', re.MULTILINE)

def GetPackageList(savedir):
    '''Save a list of installed packages 
    in format ['package name', 'discription']'''
    pacs_raw = popen('tlmgr list --only-installed').read().splitlines()
    pacs =  [list(pacpattern.search(line).groups()) for line in pacs_raw]
    with open(savedir,'wb') as output:
        pickle.dump(pacs, output, pickle.HIGHEST_PROTOCOL)

if __name__ == '__main__':
    GetPackageList('paclist.pcl')
    # pacs = GetPackageList()
    # with open('paclist.pcl','wb') as output:
    #     pickle.dump(pacs, output, pickle.HIGHEST_PROTOCOL)
    # with open('paclist.pcl', 'rb') as inputs:
    #     pacs = pickle.load(inputs)
    # print pacs