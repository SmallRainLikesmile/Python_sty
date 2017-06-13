import optparse
import nmap

def nmapScan(tgtHost, tgtPort):
    nmScan = nmap.PortScanner()
    results = nmScan.scan(tgtHost, tgtPort)
    print(results)
    state = results['scan'][tgtHost]['tcp'][int(tgtPort)]['state']
    print("[*]" + tgtHost + " tcp/" + tgtPort + " " + state)

def main():
    parser = optparse.OptionParser('uasge %prog -H <target host> -p <target port>')

    parser.add_option('-H',dest='tgtHost',type='string',help='specify target host')
    parser.add_option('-p',dest='tgtPort',type='int',help='specify target port')

    (options, args) = parser.parse_args()
    tgtHost = options.tgtHost
    tgtPort = options.tgtPort
    args.append(str(tgtPort))
    if(tgtHost == None)|(tgtPort == None):
        print("[-] You must specify a target host and port[s]!")
        exit(0)
    print(args)
    for tgport in args:
        nmapScan(tgtHost, tgport)


if __name__ == "__main__":
    main()
