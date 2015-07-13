#!/usr/bin/python
# -*- coding: utf-8 -*-
# Filename: ShowTexdoc.py
# Author:   Lyu Ming <CareF.Lm@gmail.com>

import sublime, sublime_plugin
import os, pickle, threading

from .tex_package_recognizer import GetPackagenameInline
from .tex_package_list_gen  import GetPackageList
from .thread_progress import ThreadProgress

# The location of cached package list
# I have to use absolote path here
# or sometimes loading will fail
def plugin_loaded():
    global pacpath, cachedir
    pacpath = os.path.join(sublime.packages_path(), "ShowTexdoc")
    cachedir = os.path.join(pacpath, 'paclist.pcl')
    if not os.path.exists(pacpath):
        os.makedirs(pacpath)
        
class PromptShowTexdocCommand(sublime_plugin.WindowCommand):
    '''Recognize the packages used in the documents'''
    def run(self):
        if self.window.active_view():
            view = self.window.active_view()
            texts = view.substr(sublime.Region(0, view.size()))
            self.package_list = GetPackagenameInline(texts)
            if not self.package_list:
                sublime.status_message("No package found.")
                return
            self.window.show_quick_panel(self.package_list, self.on_done)
        pass

    def on_done(self, pacindex):
        try:
            if pacindex == -1:
                sublime.status_message("Package document search canceled.")
                return
            self.window.active_view().run_command("show_texdoc", \
                    {"packagename": self.package_list[pacindex]} )
        except ValueError:
            pass

class InputShowTexdocCommand(sublime_plugin.WindowCommand):
    '''Ask for input from users'''
    def run(self):
        if self.window.active_view():
            self.window.show_input_panel("Show Texdoc:", "", self.on_done, None, None)
        pass

    def on_done(self, packagename):
        try:
            self.window.active_view().run_command("show_texdoc", \
                    {"packagename": packagename} )
        except ValueError:
            pass

class ShowAllTexdocCommand(sublime_plugin.WindowCommand):
    '''Choose from all the packages installed'''
    def run(self):
        try:
            try:
                with open(cachedir, 'rb') as pacs:
                    self.package_list = pickle.load(pacs)
            except Exception as e:
                sublime.status_message("Load cache failed: "+e.strerror+" "+cachedir)
                return
            if self.window.active_view():
                self.window.show_quick_panel(self.package_list, self.on_done)
        except ValueError:
            pass

    def on_done(self, pacindex):
        try:
            if pacindex == -1:
                sublime.status_message("Package document search canceled.")
                return
            self.window.active_view().run_command("show_texdoc", \
                    {"packagename": self.package_list[pacindex][0]} )
        except ValueError:
            pass

freshlock = False
def refreshing():
    try:
        freshlock = True
        GetPackageList(cachedir)
        freshlock = False
    except ValueError:
        sublime.status_message("Refresh failed.")

class RefreshTexdocCommand(sublime_plugin.WindowCommand):
    '''Refresh the cached list of installed packages'''
    def run(self):
        try:
            #Get packages list is quite slow, so we need to make a multithread task
            if freshlock:
                sublime.status_message("Currently refreshing...")
                return
            thread = threading.Thread(target = refreshing)
            thread.start()
            ThreadProgress(thread, 'Package list refreshing', 'Refresh succeeded.')
        except ValueError:
            sublime.status_message("Refresh failed.")

class ShowTexdocCommand(sublime_plugin.TextCommand):
    '''Call for the package docs'''
    def run(self, edit, packagename = 'texlive'):
        os.system('texdoc '+packagename)