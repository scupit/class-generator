# Class Generator
This is a simple naive python script for generating C++ and C base header and source files.

## How Does it work?
The script takes two arguments:
* Language (c, cpp, c++, cxx)
* File Name

These are then used to generate a header and inplementation file by language.
The file name can be either a single word or path

**Ex:** `python main.py c FileName` creates
* include/FileName.h
* src/FileName.c

**Ex:** `python main.py cpp path/to/file/ClassName` creates
* include/path/to/file/ClassName.hpp
* src/path/to/file/ClassName.cpp

Any directories leading up to the file that do not exist will be generated.
Note that *file extensions are not used*.

## What is generated?

### For C Files
A header guard in the format *FILENAME_H* in the header file, and a source file which
includes the header file.

### For C++ Files
A header guard in the format *FILENAME_HPP* in the header file. A class is also generated
using the file name (matching capitalization). The class contains a default constructor and
non-virtual destructor. The source file includes the header file and provides empty
implementations for the constructor and desctructor.
