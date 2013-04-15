from .ConsoleCommandParser import handleCkStyleCmdArgs, handleFixStyleCmdArgs, handleCompressCmdArgs

def ckstyle():
    handleCkStyleCmdArgs()

def fixstyle():
    handleFixStyleCmdArgs()

def compress():
    handleCompressCmdArgs()

def main():
    ckstyle()

if __name__ == '__main__':
    main()
