from Controller import *
from GUI import *


def main():
    ctrl = Controller()
    gui = GUI(ctrl)
    gui.root.mainloop()


main()
