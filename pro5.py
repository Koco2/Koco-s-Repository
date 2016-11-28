
################################################
import tkinter


class RingsApplication:
    def __init__(self, rectangles):
        self._rectangles = rectangles
        self.width = 500
        self.height = 500
        self._button_is_down = False
        self.clicked_list = []

    
        self._root_window = tkinter.Tk()

        self._canvas = tkinter.Canvas(
            master = self._root_window,
            width = self.width, height = self.height,
            background = 'green')

        self._canvas.bind('<Button-1>', self._on_button_down)

          
        self._canvas.grid(
            row = 0, column = 0, padx = 100, pady = 0,
            sticky = tkinter.N + tkinter.S + tkinter.W + tkinter.E)


        self._canvas.bind('<Configure>', self._on_canvas_resized)

        

        self._root_window.rowconfigure(0, weight = 1)
        self._root_window.columnconfigure(0, weight = 1)
        


    def run(self) -> None:
        self._root_window.mainloop()

    
    def _on_button_down(self, event: tkinter.Event) -> None:
        '''
        Event handler that is called when the primary mouse button
        is down within the canvas.
        
        '''
        canvas_width = self._canvas.winfo_width()
        canvas_height = self._canvas.winfo_height()

        
        
        
        for frac_x1, frac_y1, frac_x2, frac_y2, x, y in self._rectangles:
            if event.x > canvas_width * frac_x1 and event.y > canvas_height * frac_y1 and event.x < canvas_width * frac_x2 and event.y < canvas_height * frac_y2:
                self.clicked_list = []
                self.clicked_list.append([frac_x1, frac_y1, frac_x2, frac_y2])
                self._canvas.create_oval(
                    canvas_width * frac_x1, canvas_height * frac_y1,
                    canvas_width * frac_x2, canvas_height * frac_y2,
                    outline = 'gray', fill = 'black') 
                print(x, y)
                break
        








    def _on_canvas_resized(self, event: tkinter.Event) -> None:
        self._draw_rectangles()


    def _draw_rectangles(self) -> None:

        self._canvas.delete(tkinter.ALL)

   
        for frac_x1, frac_y1, frac_x2, frac_y2, x, y in self._rectangles:
            self._draw_rectangle(frac_x1, frac_y1, frac_x2, frac_y2)


    def _draw_rectangle(self, frac_x1, frac_y1, frac_x2, frac_y2) -> None:
        
        canvas_width = self._canvas.winfo_width()
        canvas_height = self._canvas.winfo_height()

        # Now we can do the multiplication and draw the oval.
        self._canvas.create_rectangle(
            canvas_width * frac_x1, canvas_height * frac_y1,
            canvas_width * frac_x2, canvas_height * frac_y2,
            outline = 'black')



if __name__ == '__main__':
    w = 5
    h = 5
    rectangles = []
    for x in range(h):
       for y in range(w):
           rectangle = [y/w, x/h, y/w + 1/w, x/h + 1/h, x+1, y+1]
           rectangles.append(rectangle)
           
    app = RingsApplication(rectangles)
    app.run()
