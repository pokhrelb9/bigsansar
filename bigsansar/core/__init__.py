import argparse
from bigsansar.core.ubuntu import deploy
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

            
        
        elif self.args.init == 'setup_server':
                print('configuring now')
                print('Bigsansar is available open-source under the MIT license. We recommend using the latest version of Python 3. Bigsansar is Fully based on django and linux ubuntu. You can use bigsansar for install packaged.')
                print('sure, Are you using Ubuntu lixu OS system')
                print("if your OS system is ubuntu then type 'Y' or 'y' else type any other ")
                get_input = input()
                if get_input == 'Y':
                    return deploy()
                
                elif get_input == 'y':
                    return deploy()
                
                else:
                    print('exit')
                    exit()

        else:
            print('usage: bigsansar --help')
            exit()

def main():
   cli = root()
   cli.execute()
