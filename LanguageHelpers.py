from ClassGenerators import genCClass, genCppClass

def isValidLanguage(lang: str):
  return lang.lower() in ['c', "cpp", "cxx", "cpp"]

def genClassByLanguage(lang: str, classPath: str):
  if lang.lower() in ['c']:
    genCClass(classPath)
  elif lang.lower() in ["cpp", "cxx", "cpp"]:
    genCppClass(classPath)
