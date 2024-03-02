import argparse
from bigsansar.core.init import initsetup


class root:

    def __init__(self):
        self.parser = argparse.ArgumentParser()
        self.parser.add_argument('init', help='Create a django server and related files ')
        


        self.args = self.parser.parse_args()

    def execute(self):

        if self.args.init == 'init':
            print('configuring now')
            print('Are you sure , you are using vertualenv for install bigsansar.')
            print("if you Are using vertualenv then type 'Y' or 'y' else type any other ")
            get_input_init = input()
            if get_input_init == 'Y':
                    return initsetup()
                
            elif get_input_init == 'y':
                    return initsetup()
                
            else:
                    print('exit')
                    exit()
                    

        else:
            print('usage: bigsansar --help')
            exit()

def main():
   cli = root()
   cli.execute()
