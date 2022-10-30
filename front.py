import os
import configparser


class front
    def __int__(self):
        print("frontend")
        try:
            print(os.listdir().index('config.ini'))  # if it finds the file , then do nothing
        except:
            self.reset_config()  # if th file is not here juste create new one
    def reset_config(self):
        config = configparser.ConfigParser()
        config['DEFAULT'] = {'colors': [[255, 255, 255], [255, 0, 0], [0, 255, 0], [0, 0, 255]],
                             'backlight': '100',
                             'state': '1',
                             'mode': '1',
                             'delay': '1000'}  # default values
        with open('config.ini', 'w') as configfile:
            config.write(configfile)

