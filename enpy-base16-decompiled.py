import base64, sys, os, time
B = '\x1b[34m'
R = '\x1b[31m'
G = '\x1b[32m'
W = '\x1b[0m'
Y = '\x1b[33;5m'

def banner():
    os.system('clear')
    print R + '                        _                  _  __'
    print R + ' ___ _ _  _ __ _  _ ___| |__  __ _ ___ ___/ |/ /'
    print R + "/ -_) ' \\| '_ \\ || |___| '_ \\/ _` (_-</ -_) / _ \\ "
    print W + '\\___|_||_| .__/\\_, |   |_.__/\\__,_/__/\\___|_\\___/'
    print W + '         |_|   |__/'
    print Y + '0{' + 45 * '=' + '}0'
    print Y + '|' + B + ' Coded by: ' + W + 'xNot_Found' + Y + '                          |'
    print Y + '|' + B + ' Contact : ' + W + '+62823-8637-2115' + Y + '                    |'
    print Y + '|' + B + ' Email   : ' + W + 'febryafriansyah@programmer.net' + Y + '      |'
    print Y + '|' + B + ' Website : ' + W + 'http://hatakecnk.noads.biz' + Y + '          |'
    print Y + '|' + B + ' Github  : ' + W + 'https://github.com/hatakecnk' + Y + '        |'
    print Y + '0{' + 45 * '=' + '}0\n'


try:
    banner()
    file = raw_input('\x1b[0m[\x1b[31m Input Your File /path/file.py \x1b[0m]> \x1b[36m')
except IndexError:
    print R + '[' + W + '!' + R + '] ' + W + 'there is an error\n'
    sys.exit()
except KeyboardInterrupt:
    print R + '[' + W + '!' + R + '] ' + W + 'ctrl+c detected'
    print R + '[' + W + '!' + R + '] ' + W + 'trying to exit'
    time.sleep(3)
    sys.exit()
except EOFError:
    print R + '\n[' + W + '!' + R + '] ' + W + 'ctrl+d detected'
    print R + '[' + W + '!' + R + '] ' + W + 'trying to exit'
    time.sleep(3)
    sys.exit()
else:
    try:
        fileopen = open(file).read()
    except IOError:
        banner()
        print R + '[' + W + '!' + R + '] ' + W + 'file not exist\n'
        sys.exit()

    try:
        a = base64.b16encode(fileopen)
    except TypeError:
        banner()
        print R + '[' + W + '!' + R + '] ' + W + 'file already compiled\n'
        sys.exit()

b = "#Encrypted By xNot_Found\n#Github : https://github.com/hatakecnk/\nDo not edit the script to avoid erros\nimport base64\nexec(base64.b16decode('" + a + "'))"
c = file.replace('.py', '_enc.py')
d = open(c, 'w')
d.write(b)
d.close()
banner()
print B + '[' + W + '+' + B + '] ' + G + 'file saved : ' + W + c
