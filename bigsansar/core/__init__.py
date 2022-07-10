import argparse
from bigsansar.core.init import initsetup


class root:

    def __init__(self):
        self.parser = argparse.ArgumentParser()
        self.parser.add_argument('init', help='Create a django server and related files ')

        self.args = self.parser.parse_args()

    def execute(self):

        if self.args.init == 'init':
            return initsetup()

        else:
            print('usage: bigsansar --help')
            exit()

def main():
   cli = root()
   cli.execute()
