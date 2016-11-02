import sys
import csv
import re
import json

# Some Python 3 compatibility shims
if sys.version_info.major < 3:
    STRING_TYPES = (str, unicode)
else:
    STRING_TYPES = str
    xrange = range

arreglo = []
f = open(sys.argv[1])
while True:
    text = f.readline()
    if (text == ''):
        break
    if text.strip():
        arreglo.append(text.split())


# with open(sys.argv[1]) as tsv:
#     for line in csv.reader(tsv, dialect="excel-tab"):
#         print line

def parser(arreglo):
    tiposF = ['int', 'bool', 'void', 'string', 'char', 'double']
    tiposV = ['int', 'bool', 'string', 'char', 'double']
    commentFlag = False
    contConst = 0
    contComentarioS = 0
    contComentarioM = 0
    contConstTotal = 0
    contFunc = 0
    contFuncTotal = 0
    contVar = 0
    contTotalVar = 0
    contInclude = 0
    contIncludeTotal = 0
    contFN = 0
    contFNTotal = 0
    constantPattern = re.compile("(i|d|c|b|f|s)(Arr|Mat)?([A-Z]+)\;$")
    #functionPattern = re.compile("(i|d|c|b|f|s|v)(Arr|Mat)?([A-Z][a-z]*([A-Z][a-z]+)*\(?)$")
    functionPattern = re.compile("((i|d|c|b|f|s|v)(Arr|Mat)?([A-Z][a-z]*([A-Z][a-z]+)*\(?))|(main\(?\)?)$")
    varPattern = re.compile("(i|d|c|b|f|s)(((Arr|Mat)[A-Z][a-z]+([A-Z][a-z]+)*)|(([A-Z][a-z]+([A-Z][a-z]+)*)))\;?")
    commentSPattern = re.compile("\/\/(.)*")
    commentMPattern = re.compile("\/\*(.)*")
    includePattern = re.compile("<([a-z](.[a-z])+)*>")
    fileNamePattern = re.compile("(?![a-zA-z0-9]_)([A-Z][a-z]+([A-Z][a-z]+)*.cpp)")

    for linea in arreglo:
        if commentSPattern.match(linea[0]):
            contComentarioS += 1

        elif commentMPattern.match(linea[0]):
            contComentarioM += 1

        elif linea[0] == "#include":
            if includePattern.match(linea[1]):
                contInclude += 1
                contIncludeTotal += 1
            else:
                contIncludeTotal += 1

        elif linea[0] == 'const':
            if linea[1] in tiposV:
                if constantPattern.match(linea[2]):
                    contConst += 1
                    contConstTotal += 1
                else:
                    contConstTotal += 1

        elif any("(" in s for s in linea):
            if linea[0] in tiposF:
                if not any("=" in s for s in linea):
                    if functionPattern.match(linea[1]):
                        contFuncTotal += 1
                        contFunc += 1
                    else:
                        contFuncTotal += 1

            if any("=" in s for s in linea):
                if linea[0] in tiposV:
                    if varPattern.match(linea[1]):
                        contVar += 1
                        contTotalVar += 1
                    else:
                        contTotalVar += 1

        elif linea[0] in tiposV:
            if varPattern.match(linea[1]):
                contVar += 1
                contTotalVar += 1
            else:
                contTotalVar += 1

    if fileNamePattern.match(sys.argv[1]):
        contFN += 1
        contFNTotal += 1
    else:
        sys.argv[1]


    return json.dumps({'includesC': contInclude, 
        'includesT' : contIncludeTotal, 
        'commentsC' : contComentarioM+contComentarioS, 
        'commentsT' : contComentarioM+contComentarioS,
        'constC' : contConst,
        'constT' : contConstTotal,
        'funcC' : contFunc,
        'funcT' : contFuncTotal,
        'varC' : contVar,
        'varT' : contTotalVar,
        'filename': contFN
        }, sort_keys=True, indent=4, separators=(',',':'))

print parser(arreglo)