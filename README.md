sublime-javap
=============

Javap support for the Sublime Text 2 editor.
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

No license, no liability, use as you see fit.
