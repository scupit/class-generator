from PathHelpers import createPath, directoriesOnly, includePath, srcPath, getFileName, posixPath, joinExtension

# Add #endif after this manually
def headerGuard(file, fileName: str, extension: str):
  guardName = fileName.upper() + '_' + extension.upper()

  file.write("#ifndef " + guardName)
  file.write("\n#define " + guardName)

def include(file, classPath: str, extension: str):
  file.write("#include \"" + posixPath(classPath) + '.' + extension.lower() + '"')

def endif(file):
  file.write("\n#endif")

def successConfirmation(classPath, headerExtension, sourceExtension):
  print("Header and source generated successfully!")
  print("Header at", joinExtension(includePath(classPath), headerExtension))
  print("Source at", joinExtension(srcPath(classPath), sourceExtension))

def genCClass(classPath: str):
  includeClassPath = includePath(classPath)
  sourcesClassPath = srcPath(classPath)
  fileName = getFileName(classPath)

  createPath(directoriesOnly(includeClassPath))
  createPath(directoriesOnly(sourcesClassPath))

  with open(includeClassPath + ".h", 'w') as includeFile:
    headerGuard(includeFile, fileName, 'h')
    includeFile.write("\n\n\n")
    endif(includeFile)

  with open(sourcesClassPath + ".c", 'w') as srcFile:
    include(srcFile, classPath, 'h')
    srcFile.write("\n")

  successConfirmation(classPath, 'h', 'c')

def genCppClass(classPath: str):
  includeClassPath = includePath(classPath)
  sourcesClassPath = srcPath(classPath)
  fileName = getFileName(classPath)

  createPath(directoriesOnly(includeClassPath))
  createPath(directoriesOnly(sourcesClassPath))

  with open(includeClassPath + ".hpp", 'w') as includeFile:
    headerGuard(includeFile, fileName, "hpp")
    includeFile.write("\n\nclass " + fileName + " {")
    includeFile.write("\n\tprivate:\n\n\tpublic:")
    includeFile.write("\n\t\t" + fileName + "();")
    includeFile.write("\n\t\t~" + fileName + "();")
    includeFile.write("\n};\n")
    endif(includeFile)

  with open(sourcesClassPath + ".cpp", 'w') as srcFile:
    include(srcFile, classPath, "hpp")
    srcFile.write("\n\n" + fileName + "::" + fileName + "()\n{\n\n}")
    srcFile.write("\n\n" + fileName + "::~" + fileName + "() {\n\n}")
    srcFile.write("\n")

  successConfirmation(classPath, 'hpp', 'cpp')