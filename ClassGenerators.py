from PathHelpers import createPath, directoriesOnly, includePath, srcPath, getFileName

def getGuardName(fileName: str, extension: str):
  return fileName.upper() + '_' + extension.upper()

# Add #endif after this manually
def headerGuard(file, fileName: str, extension: str):
  guardName = getGuardName(fileName, extension)

  file.write("#ifndef " + guardName)
  file.write("\n#define " + guardName)

def include(file, classPath: str, extension: str):
  file.write("#include \"" + classPath + '.' + extension + '"')

def endif(file):
  file.write("\n#endif")

def genCClass(classPath: str):
  includeClassPath = includePath(classPath)
  sourcesClassPath = srcPath(classPath)
  fileName = getFileName(classPath)

  createPath(directoriesOnly(includeClassPath))
  createPath(directoriesOnly(sourcesClassPath))

  with open(includeClassPath + ".h", 'w') as includeFile:
    headerGuard(includeFile, fileName, "H")
    includeFile.write("\n")
    endif(includeFile)

  with open(sourcesClassPath + ".c", 'w') as srcFile:
    include(srcFile, classPath, "H")
    srcFile.write("\n")

def genCppClass(classPath: str):
  includeClassPath = includePath(classPath)
  sourcesClassPath = srcPath(classPath)
  fileName = getFileName(classPath)

  createPath(directoriesOnly(includeClassPath))
  createPath(directoriesOnly(sourcesClassPath))

  with open(includeClassPath + ".hpp", 'w') as includeFile:
    headerGuard(includeFile, fileName, "HPP")
    includeFile.write("\nclass " + fileName + " {")
    includeFile.write("\n\tprivate:\n\t\n\tpublic:")
    includeFile.write("\n\n}\n")
    endif(includeFile)

  with open(sourcesClassPath + ".cpp", 'w') as srcFile:
    include(srcFile, classPath, "HPP")
    srcFile.write("\n")