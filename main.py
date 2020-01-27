import sys
from pathlib import Path
from LanguageHelpers import isValidLanguage, genClassByLanguage

# Todo: Check for include/ and src/.
# Then for each slash in the path, create the directory if it does not exist.
# Then write the header and source files into their respective places.

if len(sys.argv) > 1:
  # for x in range(1, len(sys.argv)):
  #   print("\t", sys.argv[x])

  if sys.argv[1] == "--help":
    print("Give this command a language and a filename")
    print("Like this:", sys.argv[0], "c ClassName")
    print("Or this:", sys.argv[0], "c++ helpers/HelperClass")
  elif sys.argv[1] == "--options":
    print("Language options are c, c++, cpp, and cxx")
  else:

    if (isValidLanguage(sys.argv[1])):
      if len(sys.argv) > 2:
        # Guarantees the path does not contain any special characters or special dir paths
        genClassByLanguage(sys.argv[1], str(Path(sys.argv[2]).resolve()))
      else:
        print("You must provide a class name or class path")

    else:
      print("Invalid language given, see", sys.argv[0], "--options for language options")
    
else:
  print("Run", sys.argv[0], " --help for help, or", sys.argv[0], "--options for language options")