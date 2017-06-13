import crypt

def testPass(cryptPass):
    salt = cryptPass[0:2]
    print('\n')
    print(salt)
    print('\n')
    dictFile = open('dictionary.txt','r')
    for word in dictFile.readlines():
        word = word.strip('\n')
        cryptWord = crypt.crypt(word,salt)

        if cryptPass == cryptWord:
            print('Found passwd:',word)
            return
        print('Passwd not found!')
        return


def main():
    passfile = open('passwords.txt','r')
    for line in passfile.readlines():
        user = line.split(':')[0]
        linuxPass = line.split(':')[1].strip('')
        print("Cracking Password For:",linuxPass)
        testPass(linuxPass)

if __name__=='__main__':
    main()
