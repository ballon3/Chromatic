def writeJSON(path, fileName, data):
    fileExt = './' + path + '/' + fileName + '.json'
    with open(fileExt, 'w') as fp:
        json.dump(data, fp)


def writePy(path, fileName, data):
    fileExt = './' + path + '/' + fileName + '.json'