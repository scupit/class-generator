import os
from pathlib import Path

# Like mkdir, but for entire paths
def createPath(pathString: str):
  dirNames = pathString.split(os.path.sep)
  dirPath = Path('.')

  for dirName in dirNames:
    dirPath /= dirName
    dirPath = dirPath.resolve()

    if not (dirPath.exists() and dirPath.is_dir()):
      dirPath.mkdir()

def includePath(pathString: str) -> str:
  return "include" + os.path.sep + pathString

def joinExtension(fileName: str, extension) -> str:
  return fileName + '.' + extension

def srcPath(pathString: str) -> str:
  return "src" + os.path.sep + pathString

def directoriesOnly(pathString: str) -> str:
  sepIndex = pathString.rfind(os.path.sep)
  if sepIndex == -1:
    return "."
  else:
    return pathString[0:sepIndex]

def getFileName(pathString: str) -> str:
  sepIndex = pathString.rfind(os.path.sep)
  return pathString if sepIndex == -1 else pathString[sepIndex + 1:]

def posixPath(pathString: str) -> str:
  return pathString.replace(os.path.sep, '/')