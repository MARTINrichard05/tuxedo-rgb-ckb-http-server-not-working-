import os
import configparser
from multiprocessing import Process


class main :
    def __init__(self):

        try:
            os.listdir().index('config.ini') # if it finds the file , then do nothing
            print('config.ini found')
        except:
            print('no config.ini found')
            #self.reset_config()  # if th file is not here juste create new one
            #print('config.ini generated successfully')

        self.start_daemon()
    def reset_config(self):
        config = configparser.ConfigParser()
        config['DEFAULT'] = {'daemon_status': '1'}  # default values
        with open('config.ini', 'w') as configfile:
            config.write(configfile)

    def daemon(self):
        os.system('sudo python core.py')
    def start_daemon(self):
        print('Starting daemon...')
        daemon = Process(target=self.daemon)
        daemon.start()
a = main()
print("done my job")