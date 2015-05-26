#!/usr/bin/python
# -*- coding: utf-8 -*-
# Filename: ShowTexdoc.py
# Author:   Lyu Ming <CareF.Lm@gmail.com>

import sublime, sublime_plugin
import os

class PromptShowTexdocCommand(sublime_plugin.WindowCommand):
    '''Ask for input from users'''
    def run(self):
        self.window.show_input_panel("Show Texdoc:", "", self.on_done, None, None)
        pass

    def on_done(self, packagename):
        try:
            if self.window.active_view():
                self.window.active_view().run_command("show_texdoc", {"packagename": packagename} )
        except ValueError:
            pass

class ShowTexdocCommand(sublime_plugin.TextCommand):
    '''Call for the package docs'''
    def run(self, edit, packagename = 'texlive'):
        os.system('texdoc '+packagename)