#!venv/Scripts/python

from modules.controller import Controller

def main():

    controller = Controller()
    controller.resizeImages()

if __name__ == "__main__":
    main()