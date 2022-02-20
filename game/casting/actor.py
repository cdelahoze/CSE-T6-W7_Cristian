import random
import time
from pyray import *
from raylib.colors import VIOLET, WHITE, BLUE, GREEN, RED, BLACK, YELLOW, GRAY, GOLD, PINK, PURPLE
class Actor():

    def __init__(self):
        
        self.actor_value()

    def actor_value(self):
        x = self.__x_value()
        y = self.__y_value()
        for z in range(0, 150):
            time.sleep(0.05)
            self.__drawing(x, y, z)

    def __x_value(self):
        x = []
        for i in range(61):
            a = int(random.randrange(0, 900, 30))
            x.append(a)
        return x

    def __y_value(self):
        y = []
        for i in range(61):
            a = int(random.randrange(0, 600, 20))
            y.append(a)
        return y

    def __drawing(self, x, y, z):
            
        begin_drawing()
        clear_background(BLACK)
        draw_text("o",  (x[0]),  (y[0]+z), 20, VIOLET)
        draw_text("*",  ( x[1]),  (y[1]+z), 20, YELLOW)
        draw_text("o",  ( x[2]),  (y[2]+z), 20, RED)
        draw_text("o",  ( x[3]),  (y[3]+z), 20, GREEN)
        draw_text("*",  ( x[4]),  (y[4]+z), 20, BLUE)
        draw_text("*",  ( x[5]),  (y[5]+z), 20, GRAY)
        draw_text("*",  ( x[6]),  (y[6]+z), 20, GOLD)
        draw_text("o",  ( x[7]),  (y[7]+z), 20, PINK)
        draw_text("o",  ( x[8]),  (y[8]+z), 20, VIOLET)
        draw_text("*",  ( x[9]),  (y[9]+z), 20, YELLOW)
        draw_text("*",  ( x[10]),  (y[10]+z), 20, RED)
        draw_text("o",  ( x[11]),  (y[11]+z), 20, GREEN)
        draw_text("o",  ( x[12]),  (y[12]+z), 20, BLUE)
        draw_text("*",  ( x[13]),  (y[13]+z), 20, GRAY)
        draw_text("o",  ( x[14]),  (y[14]+z), 20, PINK)
        draw_text("*",  ( x[15]),  (y[15]+z), 20, GOLD)
        draw_text("o",  ( x[16]),  (y[16]+z), 20, PINK)
        draw_text("*",  ( x[17]),  (y[17]+z), 20, GOLD)
        draw_text("o",  ( x[18]),  (y[18]+z), 20, VIOLET)
        draw_text("*",  ( x[19]),  (y[19]+z), 20, YELLOW)
        draw_text("o",  ( x[20]),  (y[20]+z), 20, PURPLE)
        draw_text("*",  ( x[21]),  (y[21]+z), 20, YELLOW)
        draw_text("o",  ( x[22]),  (y[22]+z), 20, RED)
        draw_text("o",  ( x[23]),  (y[23]+z), 20, GREEN)
        draw_text("*",  ( x[24]),  (y[24]+z), 20, BLUE)
        draw_text("*",  ( x[25]),  (y[25]+z), 20, GRAY)
        draw_text("*",  ( x[26]),  (y[26]+z), 20, GOLD)
        draw_text("o",  ( x[27]),  (y[27]+z), 20, PINK)
        draw_text("o",  ( x[28]),  (y[28]+z), 20, VIOLET)
        draw_text("*",  ( x[29]),  (y[29]+z), 20, YELLOW)
        draw_text("*",  ( x[30]),  (y[30]+z), 20, RED)
        draw_text("*",  ( x[31]),  (y[31]+z), 20, PURPLE)
        draw_text("o",  ( x[32]),  (y[32]+z), 20, RED)
        draw_text("o",  ( x[33]),  (y[33]+z), 20, GREEN)
        draw_text("*",  ( x[34]),  (y[34]+z), 20, BLUE)
        draw_text("*",  ( x[35]),  (y[35]+z), 20, GRAY)
        draw_text("*",  ( x[36]),  (y[36]+z), 20, GOLD)
        draw_text("o",  ( x[37]),  (y[37]+z), 20, PINK)
        draw_text("o",  ( x[38]),  (y[38]+z), 20, VIOLET)
        draw_text("*",  ( x[39]),  (y[39]+z), 20, YELLOW)
        draw_text("*",  ( x[40]),  (y[40]+z), 20, RED)
        draw_text("o",  ( x[41]),  (y[41]+z), 20, GREEN)
        draw_text("o",  ( x[42]),  (y[42]+z), 20, BLUE)
        draw_text("*",  ( x[43]),  (y[43]+z), 20, GRAY)
        draw_text("o",  ( x[44]),  (y[44]+z), 20, PINK)
        draw_text("*",  ( x[45]),  (y[45]+z), 20, GOLD)
        draw_text("o",  ( x[46]),  (y[46]+z), 20, PURPLE)
        draw_text("*",  ( x[47]),  (y[47]+z), 20, GOLD)
        draw_text("o",  ( x[48]),  (y[48]+z), 20, VIOLET)
        draw_text("*",  ( x[49]),  (y[49]+z), 20, PURPLE)
        draw_text("o",  ( x[50]),  (y[50]+z), 20, PURPLE)
        draw_text("*",  ( x[51]),  (y[51]+z), 20, YELLOW)
        draw_text("o",  ( x[52]),  (y[52]+z), 20, RED)
        draw_text("o",  ( x[53]),  (y[53]+z), 20, GREEN)
        draw_text("*",  ( x[54]),  (y[54]+z), 20, BLUE)
        draw_text("*",  ( x[55]),  (y[55]+z), 20, GRAY)
        draw_text("*",  ( x[56]),  (y[56]+z), 20, GOLD)
        draw_text("o",  ( x[57]),  (y[57]+z), 20, PINK)
        draw_text("o",  ( x[58]),  (y[58]+z), 20, VIOLET)
        draw_text("*",  ( x[59]),  (y[59]+z), 20, YELLOW)
        draw_text("*",  ( x[60]),  (y[60]+z), 20, RED)
        end_drawing()