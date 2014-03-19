sublime-javap
=============

Javap support for the Sublime Text 2 editor (for Sublime Text 3, see the `st3` branch).
Presents JVM classfiles in a readable format - ideal for viewing your bytecode.


Prerequisites
=============

JDK installed - `javap` must be available from the command line.


Installation
============

Through the package control plugin - run the `Install package` command and search for `Javap`.

OR, go to your Sublime Packages folder and clone this repository there:

    cd ~/Library/Application Support/Sublime Text 2/
    git clone git://github.com/axel22/sublime-javap.git sublime-javap

Usage
=====

Just open a class file in Sublime (tip: by default class files are ignored by Sublime - open 
`Preferences -> Settings Default`, and search for `"file_exclude_patterns"` to remove `.class` 
files from the exclusion list).
The classfile binary will be automatically parsed and the buffer contents will be replaced
with`javap` output. And that's it!

Or, if you already have a file open, which you know is a class file but does not
have a `.class` extension, just run the `Javap decompilation` command.

To set up a keybinding for this, add the following line to your keybindings:

    { "keys": ["ctrl+c", "ctrl+j", "ctrl+p"], "command": "javap" },

Additionally, whenever you open a `jar` file, instead of displaying the binary, this plugin will automatically
display the contents of the `jar`.


License
=======

Copyright (c) 2014, Aleksandar Prokopec
All rights reserved.

Redistribution and use in source and binary forms, with or without modification, are permitted provided that the following conditions are met:

1. Redistributions of source code must retain the above copyright notice, this list of conditions and the following disclaimer.

2. Redistributions in binary form must reproduce the above copyright notice, this list of conditions and the following disclaimer in the documentation and/or other materials provided with the distribution.

3. Neither the name of the copyright holder nor the names of its contributors may be used to endorse or promote products derived from this software without specific prior written permission.

THIS SOFTWARE IS PROVIDED BY THE COPYRIGHT HOLDERS AND CONTRIBUTORS "AS IS" AND ANY EXPRESS OR IMPLIED WARRANTIES, INCLUDING, BUT NOT LIMITED TO, THE IMPLIED WARRANTIES OF MERCHANTABILITY AND FITNESS FOR A PARTICULAR PURPOSE ARE DISCLAIMED. IN NO EVENT SHALL THE COPYRIGHT HOLDER OR CONTRIBUTORS BE LIABLE FOR ANY DIRECT, INDIRECT, INCIDENTAL, SPECIAL, EXEMPLARY, OR CONSEQUENTIAL DAMAGES (INCLUDING, BUT NOT LIMITED TO, PROCUREMENT OF SUBSTITUTE GOODS OR SERVICES; LOSS OF USE, DATA, OR PROFITS; OR BUSINESS INTERRUPTION) HOWEVER CAUSED AND ON ANY THEORY OF LIABILITY, WHETHER IN CONTRACT, STRICT LIABILITY, OR TORT (INCLUDING NEGLIGENCE OR OTHERWISE) ARISING IN ANY WAY OUT OF THE USE OF THIS SOFTWARE, EVEN IF ADVISED OF THE POSSIBILITY OF SUCH DAMAGE.
