
import game_logic
import tkinter

DEFAULT_FONT = ('Helvetica', 20)



class RingsApplication:
    def __init__(self, rectangles, obj):
        self._rectangles = rectangles
        self.width = 500
        self.height = 500
        self._button_is_down = False

    
        self._root_window = tkinter.Tk()

        label = tkinter.Label(
            master = self._root_window, text = obj.label,
            font = DEFAULT_FONT)

        label.grid(
            row = 0, column = 0, columnspan = 2, padx = 10, pady = 10,)


        self._button1 = tkinter.Button(
            master = self._root_window, text = 'Button 1', font = DEFAULT_FONT)

        self._button1.grid(
            row = 0, column = 0, padx = 10, pady = 10,
            sticky = tkinter.W)


        self._button2 = tkinter.Button(
            master = self._root_window, text = 'Button 2', font = DEFAULT_FONT)

        self._button2.grid(
            row = 0, column = 1, padx = 10, pady = 10,
            sticky = tkinter.E)

        self._canvas = tkinter.Canvas(
            master = self._root_window,
            width = self.width, height = self.height,
            background = 'green')

        self._canvas.bind('<Button-1>', self._on_button_down)

          
        self._canvas.grid(
            row = 1, column = 0, columnspan = 2, padx = 10, pady = 10,
            sticky = tkinter.N + tkinter.S + tkinter.E + tkinter.W)


        self._canvas.bind('<Configure>', self._on_canvas_resized)

        

        self._root_window.rowconfigure(0, weight = 1)
        self._root_window.rowconfigure(1, weight = 1)
        self._root_window.columnconfigure(0, weight = 1)
        self._root_window.columnconfigure(1, weight = 1)
        
        


    def run(self) -> None:
        self._root_window.mainloop()

    
    def _on_button_down(self, event: tkinter.Event) -> None:
        '''
        Event handler that is called when the primary mouse button
        is down within the canvas.
        
        '''
        canvas_width = self._canvas.winfo_width()
        canvas_height = self._canvas.winfo_height()

        
        
        
        for key in self._rectangles:
            if event.x > canvas_width * self._rectangles[key][0] and event.y > canvas_height * self._rectangles[key][1] and event.x < canvas_width * self._rectangles[key][2] and event.y < canvas_height * self._rectangles[key][3]:
                self._canvas.create_oval(
                    canvas_width * self._rectangles[key][0], canvas_height * self._rectangles[key][1],
                    canvas_width * self._rectangles[key][2], canvas_height * self._rectangles[key][3],
                    outline = 'gray', fill = 'black') 
                print(key)
                break

    def _on_canvas_resized(self, event: tkinter.Event) -> None:
        self._draw_rectangles()
        #add more later

    def _draw_rectangles(self) -> None:

        self._canvas.delete(tkinter.ALL)

   
        for key in self._rectangles:
            self._draw_rectangle(
                self._rectangles[key][0], self._rectangles[key][1],
                self._rectangles[key][2], self._rectangles[key][3])


    def _draw_rectangle(self, frac_x1, frac_y1, frac_x2, frac_y2) -> None:
        
        canvas_width = self._canvas.winfo_width()
        canvas_height = self._canvas.winfo_height()

        # Now we can do the multiplication and draw the oval.
        self._canvas.create_rectangle(
            canvas_width * frac_x1, canvas_height * frac_y1,
            canvas_width * frac_x2, canvas_height * frac_y2,
            outline = 'black')


    def print_board(self, game_board):
        for key in rectangles:
            row = int(key[0])
            col = int(key[2])
            if game_board[row][col] == 'B':
                self._canvas.create_oval(
                    canvas_width * self._rectangles[key][0], canvas_height * self._rectangles[key][1],
                    canvas_width * self._rectangles[key][2], canvas_height * self._rectangles[key][3],
                    outline = 'gray', fill = 'black')
            elif game_board[row][col] == 'W':
                self._canvas.create_oval(
                    canvas_width * self._rectangles[key][0], canvas_height * self._rectangles[key][1],
                    canvas_width * self._rectangles[key][2], canvas_height * self._rectangles[key][3],
                    outline = 'gray', fill = 'white')


    

def get_rectangles(row,col):
    rectangles = {}
    for x in range(row):
       for y in range(col):
           rectangle = [y/col, x/row, y/col + 1/col, x/row + 1/row, x+1, y+1]
           key = str(x) + ' '+ str(y)
           rectangles[key] = rectangle
    return rectangles




if __name__ == '__main__':
    print('FULL')
    obj = game_logic.state()
    obj.row = int(input())
    obj.col = int(input())
    obj.new_game_board()
    rectangles = get_rectangles(obj.ROW, obj.COL)
    obj.start_board()
    obj.get_turn()
    obj.get_rule()
    obj.count_tile()
    app = RingsApplication(rectangles, obj)
    app.run()
    #print_board(obj.game_board)
    #print('TURN: '+obj.turn)
    while True:
        obj.move()
        obj.count_tile()
        print_board(obj.game_board)
        if obj.game_over():
            break
        print('TURN: '+ obj.turn)
    obj.check_winner()
    print('WINNER: '+obj.winner)
#test only: 24,12,14,11,14,13,34,42,21,44,41,31,43






