import random
import shutil
import time
import sys


class MatrixScreen:
    MIN_LEN = 5
    MAX_LEN = 30

    def __init__(self, pause=0.05):
        self.__pause = pause
        self.__density = 0.03
        self.__columns = [0] * (shutil.get_terminal_size()[0] - 1)
        self.__chars = MatrixScreen.get_chars()

    def start(self):
        """Run matrix screen"""
        self.__pre_start()
        try:
            self.__run()
        except KeyboardInterrupt:
            sys.exit()

    def __run(self):
        """Run main loop that displays so-called matrix screen"""
        while True:
            print(self.__build_line())
            sys.stdout.flush()
            time.sleep(self.__pause)

    def __build_line(self):
        """Build line to display"""
        line = ''
        for i in range(len(self.__columns)):
            if self.__columns[i] == 0:
                self.__restart_column_stream(i)

            line += self.__column_char(i)

        return f'\033[32m{line}\033[00m'

    def __restart_column_stream(self, index):
        """Restart column stream depending on random number"""
        if random.random() <= self.__density:
            self.__columns[index] = MatrixScreen.column_len()

    def __column_char(self, index):
        """Get char to display for the specified column"""
        if self.__columns[index] < 1:
            return ' '

        ch = random.choice(self.__chars)
        self.__columns[index] -= 1

        return ch

    @staticmethod
    def column_len():
        """Get random length to set on column"""
        return random.randint(MatrixScreen.MIN_LEN, MatrixScreen.MAX_LEN)

    @staticmethod
    def get_chars():
        """Get chars list that can be displayed"""
        return ['0', '1']

    @classmethod
    def __pre_start(cls):
        """Actions to execute before starting"""
        print('Press Ctrl-C to quit.')
        time.sleep(1)


(MatrixScreen()).start()
