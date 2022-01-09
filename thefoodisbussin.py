class bcolors:
    HEADER = '\033[95m'
    OKBLUE = '\033[94m'
    OKCYAN = '\033[96m'
    OKGREEN = '\033[92m'
    WARNING = '\033[93m'
    FAIL = '\033[91m'
    BOLD = '\033[1m'
    UNDERLINE = '\033[4m'
    ENDC = '\033[0m'

class Letsgo:
    def __init__(self):
        self.sheesh = bcolors.HEADER
        self.dababycar = bcolors.OKBLUE
        self.nineplustenistwentyone = bcolors.OKCYAN
        self.yeet = bcolors.OKGREEN
        self.hackertryingtotellmewhereilivemealreadyknowingwhereilive = bcolors.WARNING
        self.moneyprintergobrrrrrrrr = bcolors.FAIL
        self.pogchamp = bcolors.BOLD
        self.wnerd = bcolors.UNDERLINE
        self.dezznuts = bcolors.ENDC
        self.everysixtysecondsinafricaaminutepasses = "Hello, World!"

    def printing(self, colors, text):
        print(f"{colors}{text}{self.dezznuts}")
    
    def yeeting(self):
        self.printing(self.sheesh, self.everysixtysecondsinafricaaminutepasses)
        self.printing(self.dababycar, self.everysixtysecondsinafricaaminutepasses)
        self.printing(self.nineplustenistwentyone, self.everysixtysecondsinafricaaminutepasses)
        self.printing(self.yeet, self.everysixtysecondsinafricaaminutepasses)
        self.printing(self.hackertryingtotellmewhereilivemealreadyknowingwhereilive, self.everysixtysecondsinafricaaminutepasses)
        self.printing(self.moneyprintergobrrrrrrrr, self.everysixtysecondsinafricaaminutepasses)
        self.printing(self.pogchamp, self.everysixtysecondsinafricaaminutepasses)
        self.printing(self.wnerd, self.everysixtysecondsinafricaaminutepasses)

if __name__ == '__main__':
    Letsgo().yeeting()





































