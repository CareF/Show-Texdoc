# Show Texdoc
by Lyu Ming
[https://github.com/CareF]

## Introduction
This is a Sublime Text package for showing the LaTeX package documents. 

I develop and test the package under Sublime Text 3 and Windows 8 but I 
shall not use anything not supported by other platform. If anyone found 
it cannot run under Sublime Text 2 or other OS, please contact me. 

I use TexLive 2014, and know nothing about other TeX distribution. This 
package requires the following two commands about TeX:

    tlmgr list --only-installed
    texdoc <package name>

Any distribution that supports these two commands should be supported
by this package. 

## Version
- v1.0.0: The first release that realize basic function of showing docs.

- v1.0.1: Bug fix. Create path for cache file when loading the package.

## Usage
Press `Ctrl+Shift+P` to call the panel, input `show texdoc` and choose 
from the 4 items. 

* `Show TeXdoc mentioned in this document`: This will scan the document 
in the active view and list all the packages mentioned.
* `Show TeXdoc from all packages installed`: This will give all the packages
installed in the local machine (acquired by `tlmgr list` command).
* `Show TeXdoc with user input`: This will allow you to input a package name, 
which is equivalent to the shell command `texdoc`.
* `Show TeXdoc: refresh the list of installed packages`: Searching for all 
packages installed is costly, so the list of packages is actually stored in 
`Packages\ShowTexdoc\paclist.pcl` as pickle binary. And this command will 
refresh the cache.

You need to run `Show TeXdoc: refresh the list of installed packages` at least 
once to get the cache!
