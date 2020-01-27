import sys
from pathlib import Path
from LanguageHelpers import isValidLanguage, genClassByLanguage

if len(sys.argv) > 1:

  if sys.argv[1][0] == '-':
    if sys.argv[1] == "--help":
      print("Give this command a language and a filename. See --options or -o for language options")
      print("Like this:", sys.argv[0], "c ClassName")
      print("Or this:", sys.argv[0], "c++ helpers/HelperClass")
    elif sys.argv[1] == "--options" or sys.argv[1] == "-o":
      print("Language options are c, c++, cpp, and cxx")
    else:
      print("Invalid argument, see --help for help")
  else:
    if (isValidLanguage(sys.argv[1])):
      if len(sys.argv) > 2:
        # Guarantees the path does not contain any special characters or special dir paths
        genClassByLanguage(sys.argv[1], str(Path(sys.argv[2]).resolve()))
      else:
        print("You must provide a class name or class path")

    else:
      print("Invalid language given, see --options for language options")
    
else:
  print("Use --help for help, or --options for language options")