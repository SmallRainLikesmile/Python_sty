import zipfile
import threading

def extractFile(zFile, password):
    try:
        zFile.extractall(pwd=password)
        print("Found Passwd:",password)
        return password
    except:
        pass


def main():
    zFile = zipfile.ZipFile('test.zip')
    passFile = open('dictionary.txt','r')
    for line in passFile.readlines():
        password = line.strip('\n')
        '''
        t = threadind.Thread(target=extractFile, args=(zFile,password))
        t.start()
        '''
        print(password)
        guess = extractFile(zFile, password)
        if guess:
            print('Password:',password)
        else:
            print("can't find password")

if __name__=='__main__':
    main()

