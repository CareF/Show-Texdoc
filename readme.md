# Show Texdoc
by Lyu Ming
[https://github.com/CareF]

## Introduction
This is a Sublime Text package for showing the LaTeX package documents. 

I develop and test the package under Sublime Text 3 and Windows 8 but I 
should not use anything not supported by other platform. If anyone find 
it cannot run under Sublime Text 2 or other OS, please contact me. 

I use TexLive 2014, and know nothing about other TeX distribution. This 
package require the following two commands about TeX:

    tlmgr list --only-installed
    texdoc <package name>

Any distribution that supported These two commands should be supported
by this package. 

## Version
- v1.0.0: The first realse that realize basic function of showing docs.

- v1.0.1: Bug fix. Creat path for cache file when loading the package.

## Usage
Press `Ctrl+Shift+P` to call the panel, input `show texdoc` and choose 
from the 4 items. 

* `Show TeXdoc mentioned in this document`: This will scan the document 
in the active view and list all the package mentioned.
* `Show TeXdoc from all packages installed`: This will give all the packages
installed in the local machine (acquired by `tlmgr list` command).
* `Show TeXdoc with user input`: This will allow you to input a package name, 
which is equivalent to the shell command `texdoc`.
* `Show TeXdoc: refresh the list of installed packages`: Searching for all 
packages installed is costy, so it is actually stored in `Packages\ShowTexdoc\
paclist.pcl` as pickle binary. And this command will refresh the chache.

You need to run `Show TeXdoc: refresh the list of installed packages` at least 
once to get the chache!

-----

## License

Show Texdoc is licensed under the MIT license.

All of the source code (except for `Show Texdoc/thread_progress.py`), 
is under the license:

```
Copyright (c) 2015 Lyu Ming <CareF.Lm@gmail.com>

Permission is hereby granted, free of charge, to any person obtaining a copy
of this software and associated documentation files (the "Software"), to deal
in the Software without restriction, including without limitation the rights
to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
copies of the Software, and to permit persons to whom the Software is
furnished to do so, subject to the following conditions:

The above copyright notice and this permission notice shall be included in
all copies or substantial portions of the Software.

THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN
THE SOFTWARE.
```

`Show Texdoc/thread_progress.py` is under the license:

```
Copyright (c) 2011-2015 Will Bond <will@wbond.net>

Permission is hereby granted, free of charge, to any person obtaining a copy
of this software and associated documentation files (the "Software"), to deal
in the Software without restriction, including without limitation the rights
to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
copies of the Software, and to permit persons to whom the Software is
furnished to do so, subject to the following conditions:

The above copyright notice and this permission notice shall be included in
all copies or substantial portions of the Software.

THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN
THE SOFTWARE.
```
