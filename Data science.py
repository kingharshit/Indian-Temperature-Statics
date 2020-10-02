import numpy as np
import pandas as pd
import tkinter as tk
from tkinter import *
from matplotlib import pyplot as plt
from matplotlib.backends.backend_tkagg import (FigureCanvasTkAgg,NavigationToolbar2Tk)
from matplotlib.backend_bases import key_press_handler
from matplotlib.figure import Figure



root = tk.Tk()
root.geometry('700x700')
root.title('INDIA TEMPERATURE STATASTICS')
data_max = pd.read_csv('C:\\Users\\shreyansh\\Desktop\\Data Science Project\\MAX_TEMP.csv')
data_min = pd.read_csv('C:\\Users\\shreyansh\\Desktop\\Data Science Project\\MIN_TEMP.csv')






def year_max(g):
    r = tk.Tk()
    r.wm_title('ANNUAL MAXIMUM TEMPERATURE')
    
    
    
    a = []
    b = []
    a = data_max['YEAR']
    b = data_max['ANNUAL']
    c = pd.DataFrame(b,columns = ['ANNUAL'])
    c['YEAR'] = a
    c.set_index('YEAR',inplace = True)
    
    
    fig = Figure(figsize = (5,4), dpi = 100)
    fig.add_subplot(111).plot(a,b, linewidth = 2.0)
    canvas = FigureCanvasTkAgg(fig,master = r)
    canvas.draw()
    canvas.get_tk_widget().pack(side = tk.TOP, fill = tk.BOTH, expand = 1)
    
    toolbar = NavigationToolbar2Tk(canvas,r)
    toolbar.update()
    canvas.get_tk_widget().pack(side = tk.TOP, fill = tk.BOTH, expand = 1)
    
    def on_key(event):
        print("you pressed {}".format(event.key))
        key_press_handler(event,canvas,toolbar)
    canvas.mpl_connect("key_press_event",on_key)
    
    def quit():
        r.quit()
        r.destroy()
    button1 = tk.Button(master = r,text = 'QUIT ?', command = quit)
    button1.pack(side = tk.BOTTOM)
    r.mainloop()
#--------------------------------------------------------------------------------
    
def year_min(g1):
    r = tk.Tk()
    r.wm_title('ANNUAL MINIMUM TEMPERATURE ')
    
    
    
    a = []
    b = []
    a = data_min['YEAR']
    b = data_min['ANNUAL']
    c = pd.DataFrame(b,columns = ['ANNUAL'])
    c['YEAR'] = a
    c.set_index('YEAR',inplace = True)
    
    
    fig = Figure(figsize = (5,4), dpi = 100)
    fig.add_subplot(111).plot(a,b, linewidth = 2.0)
    canvas = FigureCanvasTkAgg(fig,master = r)
    canvas.draw()
    canvas.get_tk_widget().pack(side = tk.TOP, fill = tk.BOTH, expand = 1)
    
    toolbar = NavigationToolbar2Tk(canvas,r)
    toolbar.update()
    canvas.get_tk_widget().pack(side = tk.TOP, fill = tk.BOTH, expand = 1)
    
    def on_key(event):
        print("you pressed {}".format(event.key))
        key_press_handler(event,canvas,toolbar)
    canvas.mpl_connect("key_press_event",on_key)
    
    def quit():
        r.quit()
        r.destroy()
    button1 = tk.Button(master = r,text = 'QUIT ?', command = quit)
    button1.pack(side = tk.BOTTOM)
    r.mainloop()    
    
#---------------------------------------------------------------------------------    
    
def jan_min(g16):
    r = tk.Tk()
    r.wm_title('JANUARY MINIMUM TEMPERATURE ')
    
    
    
    a = []
    b = []
    a = data_min['YEAR']
    b = data_min['JAN']
    c = pd.DataFrame(b,columns = ['JANUARY'])
    c['YEAR'] = a
    c.set_index('YEAR',inplace = True)
    
    
    fig = Figure(figsize = (5,4), dpi = 100)
    fig.add_subplot(111).plot(a,b, linewidth = 2.0)
    canvas = FigureCanvasTkAgg(fig,master = r)
    canvas.draw()
    canvas.get_tk_widget().pack(side = tk.TOP, fill = tk.BOTH, expand = 1)
    
    toolbar = NavigationToolbar2Tk(canvas,r)
    toolbar.update()
    canvas.get_tk_widget().pack(side = tk.TOP, fill = tk.BOTH, expand = 1)
    
    def on_key(event):
        print("you pressed {}".format(event.key))
        key_press_handler(event,canvas,toolbar)
    canvas.mpl_connect("key_press_event",on_key)
    
    def quit():
        r.quit()
        r.destroy()
    button1 = tk.Button(master = r,text = 'QUIT ?', command = quit)
    button1.pack(side = tk.BOTTOM)
    r.mainloop()    

#---------------
def jan_max(g15):
    r = tk.Tk()
    r.wm_title('JANUARY MAXIMUM TEMPERATURE ')
    
    
    
    a = []
    b = []
    a = data_max['YEAR']
    b = data_max['JAN']
    c = pd.DataFrame(b,columns = ['JANUARY'])
    c['YEAR'] = a
    c.set_index('YEAR',inplace = True)
    
    
    fig = Figure(figsize = (5,4), dpi = 100)
    fig.add_subplot(111).plot(a,b, linewidth = 2.0)
    canvas = FigureCanvasTkAgg(fig,master = r)
    canvas.draw()
    canvas.get_tk_widget().pack(side = tk.TOP, fill = tk.BOTH, expand = 1)
    
    toolbar = NavigationToolbar2Tk(canvas,r)
    toolbar.update()
    canvas.get_tk_widget().pack(side = tk.TOP, fill = tk.BOTH, expand = 1)
    
    def on_key(event):
        print("you pressed {}".format(event.key))
        key_press_handler(event,canvas,toolbar)
    canvas.mpl_connect("key_press_event",on_key)
    
    def quit():
        r.quit()
        r.destroy()
    button1 = tk.Button(master = r,text = 'QUIT ?', command = quit)
    button1.pack(side = tk.BOTTOM)
    r.mainloop()    

#--------------

def feb_min(g17):
    r = tk.Tk()
    r.wm_title('FEBURARY MINIMUM TEMPERATURE ')
    
    
    
    a = []
    b = []
    a = data_min['YEAR']
    b = data_min['FEB']
    c = pd.DataFrame(b,columns = ['FEBURARY'])
    c['YEAR'] = a
    c.set_index('YEAR',inplace = True)
    
    
    fig = Figure(figsize = (5,4), dpi = 100)
    fig.add_subplot(111).plot(a,b, linewidth = 2.0)
    canvas = FigureCanvasTkAgg(fig,master = r)
    canvas.draw()
    canvas.get_tk_widget().pack(side = tk.TOP, fill = tk.BOTH, expand = 1)
    
    toolbar = NavigationToolbar2Tk(canvas,r)
    toolbar.update()
    canvas.get_tk_widget().pack(side = tk.TOP, fill = tk.BOTH, expand = 1)
    
    def on_key(event):
        print("you pressed {}".format(event.key))
        key_press_handler(event,canvas,toolbar)
    canvas.mpl_connect("key_press_event",on_key)
    
    def quit():
        r.quit()
        r.destroy()
    button1 = tk.Button(master = r,text = 'QUIT ?', command = quit)
    button1.pack(side = tk.BOTTOM)
    r.mainloop()    
    
#------------------------

def feb_max(g16):
    r = tk.Tk()
    r.wm_title('FEBURARY MAXIMUM TEMPERATURE ')
    
    
    
    a = []
    b = []
    a = data_max['YEAR']
    b = data_max['FEB']
    c = pd.DataFrame(b,columns = ['FEBURARY'])
    c['YEAR'] = a
    c.set_index('YEAR',inplace = True)
    
    
    fig = Figure(figsize = (5,4), dpi = 100)
    fig.add_subplot(111).plot(a,b, linewidth = 2.0)
    canvas = FigureCanvasTkAgg(fig,master = r)
    canvas.draw()
    canvas.get_tk_widget().pack(side = tk.TOP, fill = tk.BOTH, expand = 1)
    
    toolbar = NavigationToolbar2Tk(canvas,r)
    toolbar.update()
    canvas.get_tk_widget().pack(side = tk.TOP, fill = tk.BOTH, expand = 1)
    
    def on_key(event):
        print("you pressed {}".format(event.key))
        key_press_handler(event,canvas,toolbar)
    canvas.mpl_connect("key_press_event",on_key)
    
    def quit():
        r.quit()
        r.destroy()
    button1 = tk.Button(master = r,text = 'QUIT ?', command = quit)
    button1.pack(side = tk.BOTTOM)
    r.mainloop()    
    
#----------------------------------
    
def march_min(g18):
    r = tk.Tk()
    r.wm_title('MARCH MINIMUM TEMPERATURE ')
    
    
    
    a = []
    b = []
    a = data_min['YEAR']
    b = data_min['MAR']
    c = pd.DataFrame(b,columns = ['MARCH'])
    c['YEAR'] = a
    c.set_index('YEAR',inplace = True)
    
    
    fig = Figure(figsize = (5,4), dpi = 100)
    fig.add_subplot(111).plot(a,b, linewidth = 2.0)
    canvas = FigureCanvasTkAgg(fig,master = r)
    canvas.draw()
    canvas.get_tk_widget().pack(side = tk.TOP, fill = tk.BOTH, expand = 1)
    
    toolbar = NavigationToolbar2Tk(canvas,r)
    toolbar.update()
    canvas.get_tk_widget().pack(side = tk.TOP, fill = tk.BOTH, expand = 1)
    
    def on_key(event):
        print("you pressed {}".format(event.key))
        key_press_handler(event,canvas,toolbar)
    canvas.mpl_connect("key_press_event",on_key)
    
    def quit():
        r.quit()
        r.destroy()
    button1 = tk.Button(master = r,text = 'QUIT ?', command = quit)
    button1.pack(side = tk.BOTTOM)
    r.mainloop()    

#--------------------------
    
def march_max(g17):
    r = tk.Tk()
    r.wm_title('MARCH MAXIMUM TEMPERATURE ')
    
    
    
    a = []
    b = []
    a = data_max['YEAR']
    b = data_max['MAR']
    c = pd.DataFrame(b,columns = ['MARCH'])
    c['YEAR'] = a
    c.set_index('YEAR',inplace = True)
    
    
    fig = Figure(figsize = (5,4), dpi = 100)
    fig.add_subplot(111).plot(a,b, linewidth = 2.0)
    canvas = FigureCanvasTkAgg(fig,master = r)
    canvas.draw()
    canvas.get_tk_widget().pack(side = tk.TOP, fill = tk.BOTH, expand = 1)
    
    toolbar = NavigationToolbar2Tk(canvas,r)
    toolbar.update()
    canvas.get_tk_widget().pack(side = tk.TOP, fill = tk.BOTH, expand = 1)
    
    def on_key(event):
        print("you pressed {}".format(event.key))
        key_press_handler(event,canvas,toolbar)
    canvas.mpl_connect("key_press_event",on_key)
    
    def quit():
        r.quit()
        r.destroy()
    button1 = tk.Button(master = r,text = 'QUIT ?', command = quit)
    button1.pack(side = tk.BOTTOM)
    r.mainloop()    

    
#--------------------------

def april_min(g19):
    r = tk.Tk()
    r.wm_title('APRIL MINIMUM TEMPERATURE ')
    
    
    
    a = []
    b = []
    a = data_min['YEAR']
    b = data_min['APR']
    c = pd.DataFrame(b,columns = ['JANUARY'])
    c['YEAR'] = a
    c.set_index('YEAR',inplace = True)
    
    
    fig = Figure(figsize = (5,4), dpi = 100)
    fig.add_subplot(111).plot(a,b, linewidth = 2.0)
    canvas = FigureCanvasTkAgg(fig,master = r)
    canvas.draw()
    canvas.get_tk_widget().pack(side = tk.TOP, fill = tk.BOTH, expand = 1)
    
    toolbar = NavigationToolbar2Tk(canvas,r)
    toolbar.update()
    canvas.get_tk_widget().pack(side = tk.TOP, fill = tk.BOTH, expand = 1)
    
    def on_key(event):
        print("you pressed {}".format(event.key))
        key_press_handler(event,canvas,toolbar)
    canvas.mpl_connect("key_press_event",on_key)
    
    def quit():
        r.quit()
        r.destroy()
    button1 = tk.Button(master = r,text = 'QUIT ?', command = quit)
    button1.pack(side = tk.BOTTOM)
    r.mainloop()    
    
    
def april_max(g18):
    r = tk.Tk()
    r.wm_title('APRIL MAXIMUM TEMPERATURE ')
    
    
    
    a = []
    b = []
    a = data_max['YEAR']
    b = data_max['APR']
    c = pd.DataFrame(b,columns = ['APRIL'])
    c['YEAR'] = a
    c.set_index('YEAR',inplace = True)
    
    
    fig = Figure(figsize = (5,4), dpi = 100)
    fig.add_subplot(111).plot(a,b, linewidth = 2.0)
    canvas = FigureCanvasTkAgg(fig,master = r)
    canvas.draw()
    canvas.get_tk_widget().pack(side = tk.TOP, fill = tk.BOTH, expand = 1)
    
    toolbar = NavigationToolbar2Tk(canvas,r)
    toolbar.update()
    canvas.get_tk_widget().pack(side = tk.TOP, fill = tk.BOTH, expand = 1)
    
    def on_key(event):
        print("you pressed {}".format(event.key))
        key_press_handler(event,canvas,toolbar)
    canvas.mpl_connect("key_press_event",on_key)
    
    def quit():
        r.quit()
        r.destroy()
    button1 = tk.Button(master = r,text = 'QUIT ?', command = quit)
    button1.pack(side = tk.BOTTOM)
    r.mainloop()    
    
#--------------------------------------------

def may_min(g17):
    r = tk.Tk()
    r.wm_title('MAY MINIMUM TEMPERATURE ')
    
    
    
    a = []
    b = []
    a = data_min['YEAR']
    b = data_min['MAY']
    c = pd.DataFrame(b,columns = ['MAY'])
    c['YEAR'] = a
    c.set_index('YEAR',inplace = True)
    
    
    fig = Figure(figsize = (5,4), dpi = 100)
    fig.add_subplot(111).plot(a,b, linewidth = 2.0)
    canvas = FigureCanvasTkAgg(fig,master = r)
    canvas.draw()
    canvas.get_tk_widget().pack(side = tk.TOP, fill = tk.BOTH, expand = 1)
    
    toolbar = NavigationToolbar2Tk(canvas,r)
    toolbar.update()
    canvas.get_tk_widget().pack(side = tk.TOP, fill = tk.BOTH, expand = 1)
    
    def on_key(event):
        print("you pressed {}".format(event.key))
        key_press_handler(event,canvas,toolbar)
    canvas.mpl_connect("key_press_event",on_key)
    
    def quit():
        r.quit()
        r.destroy()
    button1 = tk.Button(master = r,text = 'QUIT ?', command = quit)
    button1.pack(side = tk.BOTTOM)
    r.mainloop()    

def may_max(g16):
    r = tk.Tk()
    r.wm_title('MAY MAXIMUM TEMPERATURE ')
    
    
    
    a = []
    b = []
    a = data_max['YEAR']
    b = data_max['MAY']
    c = pd.DataFrame(b,columns = ['MAY'])
    c['YEAR'] = a
    c.set_index('YEAR',inplace = True)
    
    
    fig = Figure(figsize = (5,4), dpi = 100)
    fig.add_subplot(111).plot(a,b, linewidth = 2.0)
    canvas = FigureCanvasTkAgg(fig,master = r)
    canvas.draw()
    canvas.get_tk_widget().pack(side = tk.TOP, fill = tk.BOTH, expand = 1)
    
    toolbar = NavigationToolbar2Tk(canvas,r)
    toolbar.update()
    canvas.get_tk_widget().pack(side = tk.TOP, fill = tk.BOTH, expand = 1)
    
    def on_key(event):
        print("you pressed {}".format(event.key))
        key_press_handler(event,canvas,toolbar)
    canvas.mpl_connect("key_press_event",on_key)
    
    def quit():
        r.quit()
        r.destroy()
    button1 = tk.Button(master = r,text = 'QUIT ?', command = quit)
    button1.pack(side = tk.BOTTOM)
    r.mainloop()    
    
    
#---------------------------------------------------

def june_min(g17):
    r = tk.Tk()
    r.wm_title('JUNE MINIMUM TEMPERATURE ')
    
    
    
    a = []
    b = []
    a = data_min['YEAR']
    b = data_min['JUN']
    c = pd.DataFrame(b,columns = ['JUNE'])
    c['YEAR'] = a
    c.set_index('YEAR',inplace = True)
    
    
    fig = Figure(figsize = (5,4), dpi = 100)
    fig.add_subplot(111).plot(a,b, linewidth = 2.0)
    canvas = FigureCanvasTkAgg(fig,master = r)
    canvas.draw()
    canvas.get_tk_widget().pack(side = tk.TOP, fill = tk.BOTH, expand = 1)
    
    toolbar = NavigationToolbar2Tk(canvas,r)
    toolbar.update()
    canvas.get_tk_widget().pack(side = tk.TOP, fill = tk.BOTH, expand = 1)
    
    def on_key(event):
        print("you pressed {}".format(event.key))
        key_press_handler(event,canvas,toolbar)
    canvas.mpl_connect("key_press_event",on_key)
    
    def quit():
        r.quit()
        r.destroy()
    button1 = tk.Button(master = r,text = 'QUIT ?', command = quit)
    button1.pack(side = tk.BOTTOM)
    r.mainloop()    


def jan_max(g16):
    r = tk.Tk()
    r.wm_title('JUNE MAXIMUM TEMPERATURE ')
    
    
    
    a = []
    b = []
    a = data_max['YEAR']
    b = data_max['JUN']
    c = pd.DataFrame(b,columns = ['JUNE'])
    c['YEAR'] = a
    c.set_index('YEAR',inplace = True)
    
    
    fig = Figure(figsize = (5,4), dpi = 100)
    fig.add_subplot(111).plot(a,b, linewidth = 2.0)
    canvas = FigureCanvasTkAgg(fig,master = r)
    canvas.draw()
    canvas.get_tk_widget().pack(side = tk.TOP, fill = tk.BOTH, expand = 1)
    
    toolbar = NavigationToolbar2Tk(canvas,r)
    toolbar.update()
    canvas.get_tk_widget().pack(side = tk.TOP, fill = tk.BOTH, expand = 1)
    
    def on_key(event):
        print("you pressed {}".format(event.key))
        key_press_handler(event,canvas,toolbar)
    canvas.mpl_connect("key_press_event",on_key)
    
    def quit():
        r.quit()
        r.destroy()
    button1 = tk.Button(master = r,text = 'QUIT ?', command = quit)
    button1.pack(side = tk.BOTTOM)
    r.mainloop()


#-----------------------------------

def july_min(g17):
    r = tk.Tk()
    r.wm_title('JULY MINIMUM TEMPERATURE ')
    
    
    
    a = []
    b = []
    a = data_min['YEAR']
    b = data_min['JUL']
    c = pd.DataFrame(b,columns = ['JULY'])
    c['YEAR'] = a
    c.set_index('YEAR',inplace = True)
    
    
    fig = Figure(figsize = (5,4), dpi = 100)
    fig.add_subplot(111).plot(a,b, linewidth = 2.0)
    canvas = FigureCanvasTkAgg(fig,master = r)
    canvas.draw()
    canvas.get_tk_widget().pack(side = tk.TOP, fill = tk.BOTH, expand = 1)
    
    toolbar = NavigationToolbar2Tk(canvas,r)
    toolbar.update()
    canvas.get_tk_widget().pack(side = tk.TOP, fill = tk.BOTH, expand = 1)
    
    def on_key(event):
        print("you pressed {}".format(event.key))
        key_press_handler(event,canvas,toolbar)
    canvas.mpl_connect("key_press_event",on_key)
    
    def quit():
        r.quit()
        r.destroy()
    button1 = tk.Button(master = r,text = 'QUIT ?', command = quit)
    button1.pack(side = tk.BOTTOM)
    r.mainloop()    



def july_max(g16):
    r = tk.Tk()
    r.wm_title('JULY MAXIMUM TEMPERATURE ')
    
    
    
    a = []
    b = []
    a = data_max['YEAR']
    b = data_max['JUL']
    c = pd.DataFrame(b,columns = ['JULY'])
    c['YEAR'] = a
    c.set_index('YEAR',inplace = True)
    
    
    fig = Figure(figsize = (5,4), dpi = 100)
    fig.add_subplot(111).plot(a,b, linewidth = 2.0)
    canvas = FigureCanvasTkAgg(fig,master = r)
    canvas.draw()
    canvas.get_tk_widget().pack(side = tk.TOP, fill = tk.BOTH, expand = 1)
    
    toolbar = NavigationToolbar2Tk(canvas,r)
    toolbar.update()
    canvas.get_tk_widget().pack(side = tk.TOP, fill = tk.BOTH, expand = 1)
    
    def on_key(event):
        print("you pressed {}".format(event.key))
        key_press_handler(event,canvas,toolbar)
    canvas.mpl_connect("key_press_event",on_key)
    
    def quit():
        r.quit()
        r.destroy()
    button1 = tk.Button(master = r,text = 'QUIT ?', command = quit)
    button1.pack(side = tk.BOTTOM)
    r.mainloop()    
    
#--------------------------
    
def august_min(g17):
    r = tk.Tk()
    r.wm_title('AUGUST MINIMUM TEMPERATURE ')
    
    
    
    a = []
    b = []
    a = data_min['YEAR']
    b = data_min['AUG']
    c = pd.DataFrame(b,columns = ['AUGUST'])
    c['YEAR'] = a
    c.set_index('YEAR',inplace = True)
    
    
    fig = Figure(figsize = (5,4), dpi = 100)
    fig.add_subplot(111).plot(a,b, linewidth = 2.0)
    canvas = FigureCanvasTkAgg(fig,master = r)
    canvas.draw()
    canvas.get_tk_widget().pack(side = tk.TOP, fill = tk.BOTH, expand = 1)
    
    toolbar = NavigationToolbar2Tk(canvas,r)
    toolbar.update()
    canvas.get_tk_widget().pack(side = tk.TOP, fill = tk.BOTH, expand = 1)
    
    def on_key(event):
        print("you pressed {}".format(event.key))
        key_press_handler(event,canvas,toolbar)
    canvas.mpl_connect("key_press_event",on_key)
    
    def quit():
        r.quit()
        r.destroy()
    button1 = tk.Button(master = r,text = 'QUIT ?', command = quit)
    button1.pack(side = tk.BOTTOM)
    r.mainloop()    


def august_max(g16):
    r = tk.Tk()
    r.wm_title('AUGUST MAXIMUM TEMPERATURE ')
    
    
    
    a = []
    b = []
    a = data_max['YEAR']
    b = data_max['AUG']
    c = pd.DataFrame(b,columns = ['AUGUST'])
    c['YEAR'] = a
    c.set_index('YEAR',inplace = True)
    
    
    fig = Figure(figsize = (5,4), dpi = 100)
    fig.add_subplot(111).plot(a,b, linewidth = 2.0)
    canvas = FigureCanvasTkAgg(fig,master = r)
    canvas.draw()
    canvas.get_tk_widget().pack(side = tk.TOP, fill = tk.BOTH, expand = 1)
    
    toolbar = NavigationToolbar2Tk(canvas,r)
    toolbar.update()
    canvas.get_tk_widget().pack(side = tk.TOP, fill = tk.BOTH, expand = 1)
    
    def on_key(event):
        print("you pressed {}".format(event.key))
        key_press_handler(event,canvas,toolbar)
    canvas.mpl_connect("key_press_event",on_key)
    
    def quit():
        r.quit()
        r.destroy()
    button1 = tk.Button(master = r,text = 'QUIT ?', command = quit)
    button1.pack(side = tk.BOTTOM)
    r.mainloop()    

    
#-----------------------

def september_min(g17):
    r = tk.Tk()
    r.wm_title('SEPTEMBER MINIMUM TEMPERATURE ')
    
    
    
    a = []
    b = []
    a = data_min['YEAR']
    b = data_min['SEP']
    c = pd.DataFrame(b,columns = ['SEPTEMBER'])
    c['YEAR'] = a
    c.set_index('YEAR',inplace = True)
    
    
    fig = Figure(figsize = (5,4), dpi = 100)
    fig.add_subplot(111).plot(a,b, linewidth = 2.0)
    canvas = FigureCanvasTkAgg(fig,master = r)
    canvas.draw()
    canvas.get_tk_widget().pack(side = tk.TOP, fill = tk.BOTH, expand = 1)
    
    toolbar = NavigationToolbar2Tk(canvas,r)
    toolbar.update()
    canvas.get_tk_widget().pack(side = tk.TOP, fill = tk.BOTH, expand = 1)
    
    def on_key(event):
        print("you pressed {}".format(event.key))
        key_press_handler(event,canvas,toolbar)
    canvas.mpl_connect("key_press_event",on_key)
    
    def quit():
        r.quit()
        r.destroy()
    button1 = tk.Button(master = r,text = 'QUIT ?', command = quit)
    button1.pack(side = tk.BOTTOM)
    r.mainloop()    



def september_max(g16):
    r = tk.Tk()
    r.wm_title('SEPTEMBER MAXIMUM TEMPERATURE ')
    
    
    
    a = []
    b = []
    a = data_max['YEAR']
    b = data_max['SEP']
    c = pd.DataFrame(b,columns = ['SEPTEMBER'])
    c['YEAR'] = a
    c.set_index('YEAR',inplace = True)
    
    
    fig = Figure(figsize = (5,4), dpi = 100)
    fig.add_subplot(111).plot(a,b, linewidth = 2.0)
    canvas = FigureCanvasTkAgg(fig,master = r)
    canvas.draw()
    canvas.get_tk_widget().pack(side = tk.TOP, fill = tk.BOTH, expand = 1)
    
    toolbar = NavigationToolbar2Tk(canvas,r)
    toolbar.update()
    canvas.get_tk_widget().pack(side = tk.TOP, fill = tk.BOTH, expand = 1)
    
    def on_key(event):
        print("you pressed {}".format(event.key))
        key_press_handler(event,canvas,toolbar)
    canvas.mpl_connect("key_press_event",on_key)
    
    def quit():
        r.quit()
        r.destroy()
    button1 = tk.Button(master = r,text = 'QUIT ?', command = quit)
    button1.pack(side = tk.BOTTOM)
    r.mainloop()    
    
    
#-------------------------------------------------


def october_min(g17):
    r = tk.Tk()
    r.wm_title('OCTOBER MINIMUM TEMPERATURE ')
    
    
    
    a = []
    b = []
    a = data_min['YEAR']
    b = data_min['OCT']
    c = pd.DataFrame(b,columns = ['OCTOBER'])
    c['YEAR'] = a
    c.set_index('YEAR',inplace = True)
    
    
    fig = Figure(figsize = (5,4), dpi = 100)
    fig.add_subplot(111).plot(a,b, linewidth = 2.0)
    canvas = FigureCanvasTkAgg(fig,master = r)
    canvas.draw()
    canvas.get_tk_widget().pack(side = tk.TOP, fill = tk.BOTH, expand = 1)
    
    toolbar = NavigationToolbar2Tk(canvas,r)
    toolbar.update()
    canvas.get_tk_widget().pack(side = tk.TOP, fill = tk.BOTH, expand = 1)
    
    def on_key(event):
        print("you pressed {}".format(event.key))
        key_press_handler(event,canvas,toolbar)
    canvas.mpl_connect("key_press_event",on_key)
    
    def quit():
        r.quit()
        r.destroy()
    button1 = tk.Button(master = r,text = 'QUIT ?', command = quit)
    button1.pack(side = tk.BOTTOM)
    r.mainloop()    



def october_max(g16):
    r = tk.Tk()
    r.wm_title('OCTOBER MAXIMUM TEMPERATURE ')
    
    
    
    a = []
    b = []
    a = data_max['YEAR']
    b = data_max['OCT']
    c = pd.DataFrame(b,columns = ['OCTOBER'])
    c['YEAR'] = a
    c.set_index('YEAR',inplace = True)
    
    
    fig = Figure(figsize = (5,4), dpi = 100)
    fig.add_subplot(111).plot(a,b, linewidth = 2.0)
    canvas = FigureCanvasTkAgg(fig,master = r)
    canvas.draw()
    canvas.get_tk_widget().pack(side = tk.TOP, fill = tk.BOTH, expand = 1)
    
    toolbar = NavigationToolbar2Tk(canvas,r)
    toolbar.update()
    canvas.get_tk_widget().pack(side = tk.TOP, fill = tk.BOTH, expand = 1)
    
    def on_key(event):
        print("you pressed {}".format(event.key))
        key_press_handler(event,canvas,toolbar)
    canvas.mpl_connect("key_press_event",on_key)
    
    def quit():
        r.quit()
        r.destroy()
    button1 = tk.Button(master = r,text = 'QUIT ?', command = quit)
    button1.pack(side = tk.BOTTOM)
    r.mainloop()    
    
    
#------------------------------------------

def november_min(g17):
    r = tk.Tk()
    r.wm_title('NOVEMBER MINIMUM TEMPERATURE ')
    
    
    
    a = []
    b = []
    a = data_min['YEAR']
    b = data_min['NOV']
    c = pd.DataFrame(b,columns = ['NOVEMBER'])
    c['YEAR'] = a
    c.set_index('YEAR',inplace = True)
    
    
    fig = Figure(figsize = (5,4), dpi = 100)
    fig.add_subplot(111).plot(a,b, linewidth = 2.0)
    canvas = FigureCanvasTkAgg(fig,master = r)
    canvas.draw()
    canvas.get_tk_widget().pack(side = tk.TOP, fill = tk.BOTH, expand = 1)
    
    toolbar = NavigationToolbar2Tk(canvas,r)
    toolbar.update()
    canvas.get_tk_widget().pack(side = tk.TOP, fill = tk.BOTH, expand = 1)
    
    def on_key(event):
        print("you pressed {}".format(event.key))
        key_press_handler(event,canvas,toolbar)
    canvas.mpl_connect("key_press_event",on_key)
    
    def quit():
        r.quit()
        r.destroy()
    button1 = tk.Button(master = r,text = 'QUIT ?', command = quit)
    button1.pack(side = tk.BOTTOM)
    r.mainloop()    


def november_max(g16):
    r = tk.Tk()
    r.wm_title('NOVEMBER MAXIMUM TEMPERATURE ')
    
    
    
    a = []
    b = []
    a = data_max['YEAR']
    b = data_max['NOV']
    c = pd.DataFrame(b,columns = ['NOVEMBER'])
    c['YEAR'] = a
    c.set_index('YEAR',inplace = True)
    
    
    fig = Figure(figsize = (5,4), dpi = 100)
    fig.add_subplot(111).plot(a,b, linewidth = 2.0)
    canvas = FigureCanvasTkAgg(fig,master = r)
    canvas.draw()
    canvas.get_tk_widget().pack(side = tk.TOP, fill = tk.BOTH, expand = 1)
    
    toolbar = NavigationToolbar2Tk(canvas,r)
    toolbar.update()
    canvas.get_tk_widget().pack(side = tk.TOP, fill = tk.BOTH, expand = 1)
    
    def on_key(event):
        print("you pressed {}".format(event.key))
        key_press_handler(event,canvas,toolbar)
    canvas.mpl_connect("key_press_event",on_key)
    
    def quit():
        r.quit()
        r.destroy()
    button1 = tk.Button(master = r,text = 'QUIT ?', command = quit)
    button1.pack(side = tk.BOTTOM)
    r.mainloop()    


#--------------------------------

def december_min(g17):
    r = tk.Tk()
    r.wm_title('DECEMBER MINIMUM TEMPERATURE ')
    
    
    
    a = []
    b = []
    a = data_min['YEAR']
    b = data_min['DEC']
    c = pd.DataFrame(b,columns = ['DECEMBER'])
    c['YEAR'] = a
    c.set_index('YEAR',inplace = True)
    
    
    fig = Figure(figsize = (5,4), dpi = 100)
    fig.add_subplot(111).plot(a,b, linewidth = 2.0)
    canvas = FigureCanvasTkAgg(fig,master = r)
    canvas.draw()
    canvas.get_tk_widget().pack(side = tk.TOP, fill = tk.BOTH, expand = 1)
    
    toolbar = NavigationToolbar2Tk(canvas,r)
    toolbar.update()
    canvas.get_tk_widget().pack(side = tk.TOP, fill = tk.BOTH, expand = 1)
    
    def on_key(event):
        print("you pressed {}".format(event.key))
        key_press_handler(event,canvas,toolbar)
    canvas.mpl_connect("key_press_event",on_key)
    
    def quit():
        r.quit()
        r.destroy()
    button1 = tk.Button(master = r,text = 'QUIT ?', command = quit)
    button1.pack(side = tk.BOTTOM)
    r.mainloop()    


def december_max(g16):
    r = tk.Tk()
    r.wm_title('DECEMBER MAXIMUM TEMPERATURE ')
    
    
    
    a = []
    b = []
    a = data_max['YEAR']
    b = data_max['DEC']
    c = pd.DataFrame(b,columns = ['DECEMBER'])
    c['YEAR'] = a
    c.set_index('YEAR',inplace = True)
    
    
    fig = Figure(figsize = (5,4), dpi = 100)
    fig.add_subplot(111).plot(a,b, linewidth = 2.0)
    canvas = FigureCanvasTkAgg(fig,master = r)
    canvas.draw()
    canvas.get_tk_widget().pack(side = tk.TOP, fill = tk.BOTH, expand = 1)
    
    toolbar = NavigationToolbar2Tk(canvas,r)
    toolbar.update()
    canvas.get_tk_widget().pack(side = tk.TOP, fill = tk.BOTH, expand = 1)
    
    def on_key(event):
        print("you pressed {}".format(event.key))
        key_press_handler(event,canvas,toolbar)
    canvas.mpl_connect("key_press_event",on_key)
    
    def quit():
        r.quit()
        r.destroy()
    button1 = tk.Button(master = r,text = 'QUIT ?', command = quit)
    button1.pack(side = tk.BOTTOM)
    r.mainloop()    
    
#------------------------------    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
#-----------------------------------------------------------------------------------
def f(b11):
    r1 = tk.Tk()
    r1.geometry('700x700')
    r1.title('MINIUM TEMPERATUE OR MAXIMUM TEMPERATURE')
    
    
    
    g2 = Button(r1,width=1000 ,height=6)
    g2.pack()
    
    g = Button(r1 , text = 'YEARLY MAXIMUM TEMPERATURE' ,width=100 ,height=3, bg='red',  bd=10, activebackground='green',  highlightcolor='purple', command= lambda:year_max(g))
    g.pack()
    
    
    g2 = Button(r1,width=1000 ,height=6)
    g2.pack()
    
    
    g1 = Button(r1 , text = 'YEARLY MINIMUM TEMPERATURE' ,width=100,height=3, bg='yellow',  bd=10, activebackground='green',  highlightcolor='purple', command=lambda:year_min(g1))
    g1.pack()
    
    
    g2 = Button(r1,width=1000 ,height=6)
    g2.pack()
    
    def quit():
        r1.quit()
        r1.destroy()
    button2 = Button(master = r1,text = 'QUIT ?',width=50,height=3, command = quit)
    button2.pack()
    r1.mainloop()
#---------------------------



    
def f1(b22):
    
    r2 = tk.Tk()
    r2.geometry('700x700')
    r2.title('MONTH WITH MINIUM TEMPERATUE OR MAXIMUM TEMPERATURE')
    
    
    
    g2 = Button(r2,width=1000 ,height=1)
    g2.pack()
    
    
    g3 = Button(r2 , text = 'JANUARY' ,width=1000,height=1, bg='yellow',  bd=10, activebackground='green',  highlightcolor='purple', command=lambda:f2(g3))
    g3.pack()
    
    #g2 = Button(r2,width=1000 ,height=1)
    #g2.pack()
    
    
    g4 = Button(r2 , text = 'FEBURARY' ,width=1000,height=1, bg='red',  bd=10, activebackground='green',  highlightcolor='purple', command=lambda:f3(g4))
    g4.pack()   
    
    
    #g2 = Button(r2,width=1000 ,height=1,bg='black')
    #g2.pack()
    
    
    g5 = Button(r2 , text = 'MARCH' ,width=1000,height=1, bg='yellow',  bd=10, activebackground='green',  highlightcolor='purple', command=lambda:f4(g5))
    g5.pack()    
    
    
    #g2 = Button(r2,width=1000 ,height=1)
    #g2.pack()
    
    
    g6 = Button(r2 , text = 'APRIL' ,width=1000,height=1, bg='red',  bd=10, activebackground='green',  highlightcolor='purple', command=lambda:f5(g6))
    g6.pack()    
    
    
    #g2 = Button(r2,width=1000 ,height=1,bg='black')
    #g2.pack()
    
    
    g7 = Button(r2 , text = 'MAY' ,width=1000,height=1, bg='yellow',  bd=10, activebackground='green',  highlightcolor='purple', command=lambda:f6(g7))
    g7.pack()    
    
    
    
    
    #g2 = Button(r2,width=1000 ,height=1)
    #g2.pack()
    
    
    g8 = Button(r2 , text = 'JUNE' ,width=1000,height=1, bg='red',  bd=10, activebackground='green',  highlightcolor='purple', command=lambda:f7(g8))
    g8.pack()    
    
    
    #g2 = Button(r2,width=1000 ,height=1,bg='black')
    #g2.pack()
    
    
    g9 = Button(r2 , text = 'JULY' ,width=1000,height=1, bg='yellow',  bd=10, activebackground='green',  highlightcolor='purple', command=lambda:f8(g9))
    g9.pack()    
    
    
    #g2 = Button(r2,width=1000 ,height=1)
    #g2.pack()
    
    
    g10 = Button(r2 , text = 'AUGUST' ,width=1000,height=1, bg='red',  bd=10, activebackground='green',  highlightcolor='purple', command=lambda:f9(g10))
    g10.pack()    
    
    
    #g2 = Button(r2,width=1000 ,height=1,bg='black')
    #g2.pack()
    
    
    g11 = Button(r2 , text = 'SEPTEMBER' ,width=1000,height=1, bg='yellow',  bd=10, activebackground='green',  highlightcolor='purple', command=lambda:f10(g11))
    g11.pack()    



    #g2 = Button(r2,width=1000 ,height=1)
    #g2.pack()
    
    
    g12 = Button(r2 , text = 'OCTOBER' ,width=1000,height=1, bg='red',  bd=10, activebackground='green',  highlightcolor='purple', command=lambda:f11(g12))
    g12.pack()




    #g2 = Button(r2,width=1000 ,height=1,bg='black')
    #g2.pack()
    
    
    g13 = Button(r2 , text = 'NOVEMBER' ,width=1000,height=1, bg='yellow',  bd=10, activebackground='green',  highlightcolor='purple', command=lambda:f12(g13))
    g13.pack()



    #g2 = Button(r2,width=1000 ,height=1)
    #g2.pack()
    
    
    g14 = Button(r2 , text = 'DECEMBER' ,width=1000,height=1, bg='red',  bd=10, activebackground='green',  highlightcolor='purple', command=lambda:f13(g14))
    g14.pack()
    
    g2 = Button(r2,width=1000 ,height=1)
    g2.pack()
    
    
    def quit():
        r2.quit()
        r2.destroy()
    button3 = Button(master = r2,text = 'QUIT ?',width=50,height=3, command = quit)
    button3.pack()
    
    
    
    r2.mainloop()



#-----------------------------------------------------------------------------------


def f2(g3):
    r3 = tk.Tk()
    r3.geometry('700x700')
    r3.title('MINIUM TEMPERATUE OR MAXIMUM TEMPERATURE')
    
    
    
    g2 = Button(r3,width=1000 ,height=6)
    g2.pack()
    
    g15 = Button(r3 , text = 'JANUARY MAXIMUM TEMPERATURE (1990 - 2017)' ,width=100 ,height=3, bg='red',  bd=10, activebackground='green',  highlightcolor='purple', command= lambda:year_max(g15))
    g15.pack()
    
    
    g2 = Button(r3,width=1000 ,height=6)
    g2.pack()
    
    
    g16 = Button(r3 , text = 'JANUARY MINIMUM TEMPERATURE (1990 - 2017)' ,width=100,height=3, bg='yellow',  bd=10, activebackground='green',  highlightcolor='purple', command=lambda:jan_min(g16))
    g16.pack()
    
    
    g2 = Button(r3,width=1000 ,height=6)
    g2.pack()
    
    def quit():
        r3.quit()
        r3.destroy()
    button2 = Button(master = r3,text = 'QUIT ?',width=50,height=3, command = quit)
    button2.pack()
    r3.mainloop()
#---------------------
def f3(g4):
    r4 = tk.Tk()
    r4.geometry('700x700')
    r4.title('MINIUM TEMPERATUE OR MAXIMUM TEMPERATURE')
    
    
    
    g2 = Button(r4,width=1000 ,height=6)
    g2.pack()
    
    g16 = Button(r4 , text = 'FEBURARY MAXIMUM TEMPERATURE (1990 - 2017)' ,width=100 ,height=3, bg='red',  bd=10, activebackground='green',  highlightcolor='purple', command= lambda:feb_max(g16))
    g16.pack()
    
    
    g2 = Button(r4,width=1000 ,height=6)
    g2.pack()
    
    
    g17 = Button(r4 , text = 'FEBURARY MINIMUM TEMPERATURE (1990 - 2017)' ,width=100,height=3, bg='yellow',  bd=10, activebackground='green',  highlightcolor='purple', command=lambda:feb_min(g17))
    g17.pack()
    
    
    g2 = Button(r4,width=1000 ,height=6)
    g2.pack()
    
    def quit():
        r4.quit()
        r4.destroy()
    button2 = Button(master = r4,text = 'QUIT ?',width=50,height=3, command = quit)
    button2.pack()
    r4.mainloop()
#------------------------

def f4(g5):
    r5 = tk.Tk()
    r5.geometry('700x700')
    r5.title('MINIUM TEMPERATUE OR MAXIMUM TEMPERATURE')
    
    
    
    g2 = Button(r5,width=1000 ,height=6)
    g2.pack()
    
    g17 = Button(r5 , text = 'MARCH MAXIMUM TEMPERATURE (1990 - 2017)' ,width=100 ,height=3, bg='red',  bd=10, activebackground='green',  highlightcolor='purple', command= lambda:march_max(g17))
    g17.pack()
    
    
    g2 = Button(r5,width=1000 ,height=6)
    g2.pack()
    
    
    g18 = Button(r5 , text = 'MARCH MINIMUM TEMPERATURE (1990 - 2017)' ,width=100,height=3, bg='yellow',  bd=10, activebackground='green',  highlightcolor='purple', command=lambda:march_min(g18))
    g18.pack()
    
    
    g2 = Button(r5,width=1000 ,height=6)
    g2.pack()
    
    def quit():
        r5.quit()
        r5.destroy()
    button2 = Button(master = r5,text = 'QUIT ?',width=50,height=3, command = quit)
    button2.pack()
    r5.mainloop()   
#-----------------------------------
    
def f5(g6):
    r5 = tk.Tk()
    r5.geometry('700x700')
    r5.title('MINIUM TEMPERATUE OR MAXIMUM TEMPERATURE')
    
    
    
    g2 = Button(r5,width=1000 ,height=6)
    g2.pack()
    
    g18 = Button(r5 , text = 'APRIL MAXIMUM TEMPERATURE (1990 - 2017)' ,width=100 ,height=3, bg='red',  bd=10, activebackground='green',  highlightcolor='purple', command= lambda:april_max(g18))
    g18.pack()
    
    
    g2 = Button(r5,width=1000 ,height=6)
    g2.pack()
    
    
    g19 = Button(r5 , text = 'APRIL MINIMUM TEMPERATURE (1990 - 2017)' ,width=100,height=3, bg='yellow',  bd=10, activebackground='green',  highlightcolor='purple', command=lambda:april_min(g19))
    g19.pack()
    
    
    g2 = Button(r5,width=1000 ,height=6)
    g2.pack()
    
    def quit():
        r5.quit()
        r5.destroy()
    button2 = Button(master = r5,text = 'QUIT ?',width=50,height=3, command = quit)
    button2.pack()
    r5.mainloop()
    
#--------------------------------


def f6(g7):
    r4 = tk.Tk()
    r4.geometry('700x700')
    r4.title('MINIUM TEMPERATUE OR MAXIMUM TEMPERATURE')
    
    
    
    g2 = Button(r4,width=1000 ,height=6)
    g2.pack()
    
    g16 = Button(r4 , text = 'MAY MAXIMUM TEMPERATURE (1990 - 2017)' ,width=100 ,height=3, bg='red',  bd=10, activebackground='green',  highlightcolor='purple', command= lambda:may_max(g16))
    g16.pack()
    
    
    g2 = Button(r4,width=1000 ,height=6)
    g2.pack()
    
    
    g17 = Button(r4 , text = 'MAY MINIMUM TEMPERATURE (1990 - 2017)' ,width=100,height=3, bg='yellow',  bd=10, activebackground='green',  highlightcolor='purple', command=lambda:may_min(g17))
    g17.pack()
    
    
    g2 = Button(r4,width=1000 ,height=6)
    g2.pack()
    
    def quit():
        r4.quit()
        r4.destroy()
    button2 = Button(master = r4,text = 'QUIT ?',width=50,height=3, command = quit)
    button2.pack()
    r4.mainloop()    
    
#---------------------
    
    
def f7(g8):
    r4 = tk.Tk()
    r4.geometry('700x700')
    r4.title('MINIUM TEMPERATUE OR MAXIMUM TEMPERATURE')
    
    
    
    g2 = Button(r4,width=1000 ,height=6)
    g2.pack()
    
    g16 = Button(r4 , text = 'JUNE MAXIMUM TEMPERATURE (1990 - 2017)' ,width=100 ,height=3, bg='red',  bd=10, activebackground='green',  highlightcolor='purple', command= lambda:june_max(g16))
    g16.pack()
    
    
    g2 = Button(r4,width=1000 ,height=6)
    g2.pack()
    
    
    g17 = Button(r4 , text = 'JUNE MINIMUM TEMPERATURE (1990 - 2017)' ,width=100,height=3, bg='yellow',  bd=10, activebackground='green',  highlightcolor='purple', command=lambda:june_min(g17))
    g17.pack()
    
    
    g2 = Button(r4,width=1000 ,height=6)
    g2.pack()
    
    def quit():
        r4.quit()
        r4.destroy()
    button2 = Button(master = r4,text = 'QUIT ?',width=50,height=3, command = quit)
    button2.pack()
    r4.mainloop()
    
    
#------------------------------


def f8(g9):
    r4 = tk.Tk()
    r4.geometry('700x700')
    r4.title('MINIUM TEMPERATUE OR MAXIMUM TEMPERATURE')
    
    
    
    g2 = Button(r4,width=1000 ,height=6)
    g2.pack()
    
    g16 = Button(r4 , text = 'JULY MAXIMUM TEMPERATURE (1990 - 2017)' ,width=100 ,height=3, bg='red',  bd=10, activebackground='green',  highlightcolor='purple', command= lambda:july_max(g16))
    g16.pack()
    
    
    g2 = Button(r4,width=1000 ,height=6)
    g2.pack()
    
    
    g17 = Button(r4 , text = 'JULY MINIMUM TEMPERATURE (1990 - 2017)' ,width=100,height=3, bg='yellow',  bd=10, activebackground='green',  highlightcolor='purple', command=lambda:july_min(g17))
    g17.pack()
    
    
    g2 = Button(r4,width=1000 ,height=6)
    g2.pack()
    
    def quit():
        r4.quit()
        r4.destroy()
    button2 = Button(master = r4,text = 'QUIT ?',width=50,height=3, command = quit)
    button2.pack()
    r4.mainloop()    
    
    
    
#------------------------------------



def f9(g10):
    r4 = tk.Tk()
    r4.geometry('700x700')
    r4.title('MINIUM TEMPERATUE OR MAXIMUM TEMPERATURE')
    
    
    
    g2 = Button(r4,width=1000 ,height=6)
    g2.pack()
    
    g16 = Button(r4 , text = 'AUGUST MAXIMUM TEMPERATURE (1990 - 2017)' ,width=100 ,height=3, bg='red',  bd=10, activebackground='green',  highlightcolor='purple', command= lambda:august_max(g16))
    g16.pack()
    
    
    g2 = Button(r4,width=1000 ,height=6)
    g2.pack()
    
    
    g17 = Button(r4 , text = 'AUGUST MINIMUM TEMPERATURE (1990 - 2017)' ,width=100,height=3, bg='yellow',  bd=10, activebackground='green',  highlightcolor='purple', command=lambda:august_min(g17))
    g17.pack()
    
    
    g2 = Button(r4,width=1000 ,height=6)
    g2.pack()
    
    def quit():
        r4.quit()
        r4.destroy()
    button2 = Button(master = r4,text = 'QUIT ?',width=50,height=3, command = quit)
    button2.pack()
    r4.mainloop()    
    

#-------------------
def f10(g11):
    r4 = tk.Tk()
    r4.geometry('700x700')
    r4.title('MINIUM TEMPERATUE OR MAXIMUM TEMPERATURE')
    
    
    
    g2 = Button(r4,width=1000 ,height=6)
    g2.pack()
    
    g16 = Button(r4 , text = 'SEPTEMBER MAXIMUM TEMPERATURE (1990 - 2017)' ,width=100 ,height=3, bg='red',  bd=10, activebackground='green',  highlightcolor='purple', command= lambda:september_max(g16))
    g16.pack()
    
    
    g2 = Button(r4,width=1000 ,height=6)
    g2.pack()
    
    
    g17 = Button(r4 , text = 'SEPTEMBER MINIMUM TEMPERATURE (1990 - 2017)' ,width=100,height=3, bg='yellow',  bd=10, activebackground='green',  highlightcolor='purple', command=lambda:september_min(g17))
    g17.pack()
    
    
    g2 = Button(r4,width=1000 ,height=6)
    g2.pack()
    
    def quit():
        r4.quit()
        r4.destroy()
    button2 = Button(master = r4,text = 'QUIT ?',width=50,height=3, command = quit)
    button2.pack()
    r4.mainloop()


#--------------------------------------
def f11(g12):
    r4 = tk.Tk()
    r4.geometry('700x700')
    r4.title('MINIUM TEMPERATUE OR MAXIMUM TEMPERATURE')
    
    
    
    g2 = Button(r4,width=1000 ,height=6)
    g2.pack()
    
    g16 = Button(r4 , text = 'OCTOBER MAXIMUM TEMPERATURE (1990 - 2017)' ,width=100 ,height=3, bg='red',  bd=10, activebackground='green',  highlightcolor='purple', command= lambda:october_max(g16))
    g16.pack()
    
    
    g2 = Button(r4,width=1000 ,height=6)
    g2.pack()
    
    
    g17 = Button(r4 , text = 'OCTOBER MINIMUM TEMPERATURE (1990 - 2017)' ,width=100,height=3, bg='yellow',  bd=10, activebackground='green',  highlightcolor='purple', command=lambda:october_min(g17))
    g17.pack()
    
    
    g2 = Button(r4,width=1000 ,height=6)
    g2.pack()
    
    def quit():
        r4.quit()
        r4.destroy()
    button2 = Button(master = r4,text = 'QUIT ?',width=50,height=3, command = quit)
    button2.pack()
    r4.mainloop()


#----------------------------------------------------
def f12(g13):
    r4 = tk.Tk()
    r4.geometry('700x700')
    r4.title('MINIUM TEMPERATUE OR MAXIMUM TEMPERATURE')
    
    
    
    g2 = Button(r4,width=1000 ,height=6)
    g2.pack()
    
    g16 = Button(r4 , text = 'NOVEMBER MAXIMUM TEMPERATURE (1990 - 2017)' ,width=100 ,height=3, bg='red',  bd=10, activebackground='green',  highlightcolor='purple', command= lambda:november_max(g16))
    g16.pack()
    
    
    g2 = Button(r4,width=1000 ,height=6)
    g2.pack()
    
    
    g17 = Button(r4 , text = 'NOVEMBER MINIMUM TEMPERATURE (1990 - 2017)' ,width=100,height=3, bg='yellow',  bd=10, activebackground='green',  highlightcolor='purple', command=lambda:november_min(g17))
    g17.pack()
    
    
    g2 = Button(r4,width=1000 ,height=6)
    g2.pack()
    
    def quit():
        r4.quit()
        r4.destroy()
    button2 = Button(master = r4,text = 'QUIT ?',width=50,height=3, command = quit)
    button2.pack()
    r4.mainloop()


#-----------------------------------
    
def f13(g14):
    r4 = tk.Tk()
    r4.geometry('700x700')
    r4.title('MINIUM TEMPERATUE OR MAXIMUM TEMPERATURE')
    
    
    
    g2 = Button(r4,width=1000 ,height=6)
    g2.pack()
    
    g16 = Button(r4 , text = 'DECEMBER MAXIMUM TEMPERATURE (1990 - 2017)' ,width=100 ,height=3, bg='red',  bd=10, activebackground='green',  highlightcolor='purple', command= lambda:december_max(g16))
    g16.pack()
    
    
    g2 = Button(r4,width=1000 ,height=6)
    g2.pack()
    
    
    g17 = Button(r4 , text = 'DECEMBER MINIMUM TEMPERATURE (1990 - 2017)' ,width=100,height=3, bg='yellow',  bd=10, activebackground='green',  highlightcolor='purple', command=lambda:december_min(g17))
    g17.pack()
    
    
    g2 = Button(r4,width=1000 ,height=6)
    g2.pack()
    
    def quit():
        r4.quit()
        r4.destroy()
    button2 = Button(master = r4,text = 'QUIT ?',width=50,height=3, command = quit)
    button2.pack()
    r4.mainloop()


#-------------------------------------------------------------------------------------


























    
    
    
    
    
    
    
    
    
    
#---------------------------



























    
g2 = Button(root,width=1000 ,height=6)
g2.pack()
    
b11 = Button(root, text=' YEARLY MINIMUM OR MAXIMUM TEMPERATURE', width=100,height=3, bg='red',  bd=10, activebackground='green',  highlightcolor='purple', command= lambda:f(b11)) 
b11.pack()


g2 = Button(root,width=1000 ,height=6)
g2.pack()

b22 = Button(root, text='MONTHLY MINIMUM OR MAXIMUM TEMPERATURE', width=100,height=3, bg='yellow',  bd=10, activebackground='green',  highlightcolor='purple', command= lambda:f1(b22)) 
b22.pack()

g2 = Button(root,width=1000 ,height=6)
g2.pack()

def quit():
        root.quit()
        root.destroy()
button2 = Button(master = root,text = 'QUIT ?',width=50,height=3, command = quit)
button2.pack()

    
    
   
    
    
    
    

    












root.mainloop()
