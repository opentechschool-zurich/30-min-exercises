import tkinter as tk
import random
from dataclasses import dataclass

@dataclass
class Column():
    canvas: tk.Canvas
    x: int
    y: int
    text: str

    def draw(self):
        for i, c in enumerate(self.text):
            self.canvas.create_text(
                (self.x, self.y - i * 32),
                text=c,
                fill="green",
                font='tkDefaeultFont 24'
            )

    def step(self):
        self.y += 32

def main():
    root = tk.Tk()
    root.geometry('800x600')
    root.title('Matrix')

    canvas = tk.Canvas(root, width=800, height=600, bg='black')
    canvas.pack(anchor=tk.CENTER, expand=True)


    def cancel():
        nonlocal root
        root.quit()
        root.withdraw()

    root.bind('<Escape>', lambda *args: cancel())

    matrix = [Column(canvas, 30, 0, 'hello')]

    def task():
        if random.randrange(10) == 0:
            matrix.append(Column(canvas, random.randrange(780), 0, 'hello'))

        canvas.delete('all')

        to_delete = []
        for i, column in enumerate(matrix):
            column.draw()
            if column.y < 600:
                column.step()
            else:
                to_delete.append(i)
        for i in reversed(to_delete):
            del matrix[i]

        root.after(100, task)  # reschedule event in 1 seconds

    root.after(2000, task)

    root.mainloop()

if __name__ == '__main__':
    main()
