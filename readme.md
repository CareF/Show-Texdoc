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

- v1.0.4: Write log file about getting package list, helping future develop
that supports other LaTeX distribution.

- v2.0.0: New format of cache for better performance. Therefore you have to 
refresh the cache to make it run in a right way. Description of packages added
in "mentioned in this document" command. Also, several bugs in multi-platform 
have been fixed. Unfortunately I was still told that there is some problem in 
support under Mac OS.

- v2.1.0: Solve the multi platform path environment setting problem.

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

## Acknowledgment
Thanks Carl-Henrik Buschmann who gave feedback and helped me on testing the 
package