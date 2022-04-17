import tkinter as tk
import webbrowser


class Link(tk.Label):
    
    def __init__(self, master=None, link=None, fg='grey', font=('Arial', 10), *args, **kwargs):
        super().__init__(master, *args, **kwargs)
        self.master = master
        self.default_color = fg # keeping track of the default color 
        self.color = 'blue'   # the color of the link after hovering over it 
        self.default_font = font    # keeping track of the default font
        self.link = link 

        """ setting the fonts as assigned by the user or by the init function  """
        self['fg'] = fg
        self['font'] = font 

        """ Assigning the events to private functions of the class """

        self.bind('<Enter>', self._mouse_on)    # hovering over 
        self.bind('<Leave>', self._mouse_out)   # away from the link
        self.bind('<Button-1>', self._callback) # clicking the link

    def _mouse_on(self, *args):
        """ 
            if mouse on the link then we must give it the blue color and an 
            underline font to look like a normal link
        """
        self['fg'] = self.color
        self['font'] = self.default_font + ('underline', )

    def _mouse_out(self, *args):
        """ 
            if mouse goes away from our link we must reassign 
            the default color and font we kept track of   
        """
        self['fg'] = self.default_color
        self['font'] = self.default_font

    def _callback(self, *args):
        webbrowser.open_new(self.link)  
