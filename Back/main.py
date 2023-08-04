# coding=utf-8

from app import main
from app.utils.log import Log as print
from app.utils.start import Check_Config, return_BackIPAndPort


def Run():
    Check_Config(print)
    IP, Port = return_BackIPAndPort()

    main.Start_Run(IP, Port)


if __name__ == "__main__":
    Run()
