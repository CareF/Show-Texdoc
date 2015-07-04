#!/usr/bin/python
# -*- coding: utf-8 -*-
# Filename: TexPackageRecognizer.py
# Author:   Lyu Ming <CareF.Lm@gmail.com>
import re

def GetPackagenameInline(TeXLine):
    """This function use regular expression to recognize LaTeX userpackage name"""
    packages = re.findall(r'\\usepackage(?:\[[^\]]*\])?\{([^}]*)\}',TeXLine)
    if packages != None:
        packlist = []
        for packs in packages:
            packlist += packs.split(',')
        return packlist
    else:
        return None