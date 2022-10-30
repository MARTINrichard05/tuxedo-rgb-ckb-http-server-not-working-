import time
import keyboard
import configparser
import ast
import colorsys

# YOU HAVE TO STORE NEW CUSTOM VALUES IN ONLY ONE SECTION NAMED "IDK"

refresh_interval = 0


class main:
    def __init__(self):
        self.config = configparser.ConfigParser()
        timerfile = 0
        timerleds = 0
        self.generaltimer = 0
        self.buffer = {'current_color': 0,  # this is the selected color in the colors sections of cfg
                       'max_color': 3,  # this is the max color
                       'current_col_rgb': [255, 255, 255],  # this must be updated every time leds changes
                       'hsv': [0, 1, 0.5]}
        self.cfg_ready = {'colors': [[255, 255, 255], [255, 0, 0], [0, 255, 0], [0, 0, 255]],
                          'backlight': '100',
                          'state': '1',
                          'mode': '0',
                          'delay': '1'}
        while True:
            time.sleep(0.001)
            timerfile += 1
            timerleds += 1
            self.generaltimer += 1
            if timerleds == 30:
                timerleds = 0
                self.refreshleds()  # refresh the leds , change the val to change the fps.
            if timerfile == 2000:
                timerfile = 0
                self.readconfig()  # every 2 secs I reload the config file from the disk

    def getfromcfg(self, value):  # get a value from config file
        if len(self.config.sections()) == 0:  # if there is only a default section
            return self.config['DEFAULT'][value]
        else:
            return self.config[str(self.config.sections()[0])][value]

    def readconfig(self):
        self.config.read('config.ini')  # reloading the config file in cache
        # next step is to refresh the values in the cfg_ready dict to be faster to acess
        buffer = list(self.cfg_ready.keys())
        for i in range(len(buffer)):
            self.cfg_ready[buffer[i]] = self.getfromcfg(buffer[i])

    def refreshleds(self):
        color_list = ast.literal_eval(str(self.cfg_ready['colors']))
        if self.cfg_ready['mode'] == '0':
            keyboard.setcolor(
                keyboard.rgb_to_hex((int(color_list[0][0]), int(color_list[0][1]), int(color_list[0][2]))))
        elif self.cfg_ready['mode'] == '1':
            if self.buffer['hsv'][0] >= 1:
                self.buffer['hsv'][0] = 0
            self.buffer['current_col_rgb'] = colorsys.hsv_to_rgb(self.buffer['hsv'][0], self.buffer['hsv'][1],
                                                                 self.buffer['hsv'][2])
            self.buffer['hsv'][0] += 0.01

            self.buffer['current_col_rgb'] = [int(self.buffer['current_col_rgb'][0] * 255),
                                              int(self.buffer['current_col_rgb'][1] * 255),
                                              int(self.buffer['current_col_rgb'][2] * 255)]

            keyboard.setcolor(keyboard.rgb_to_hex((self.buffer['current_col_rgb'][0], self.buffer['current_col_rgb'][1],
                                                   self.buffer['current_col_rgb'][2])))
        elif self.cfg_ready['mode'] == '2':
            if self.generaltimer >= int(self.cfg_ready['delay']):
                self.generaltimer = 0
                if self.buffer['current_color'] < self.buffer['max_color']:
                    self.buffer['current_color'] += 1
                    keyboard.setcolor(keyboard.rgb_to_hex((int(color_list[self.buffer['current_color']][0]),
                                                           int(color_list[self.buffer['current_color']][1]),
                                                           int(color_list[self.buffer['current_color']][2]))))
                else:
                    self.buffer['current_color'] = 0
                    keyboard.setcolor(keyboard.rgb_to_hex((int(color_list[self.buffer['current_color']][0]),
                                                           int(color_list[self.buffer['current_color']][1]),
                                                           int(color_list[self.buffer['current_color']][2]))))


a = main()
