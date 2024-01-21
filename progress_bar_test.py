import asyncio
from tkinter import *
from tkinter import ttk


class App():
    async def exec(self):
        self.window = Window(asyncio.get_event_loop())
        await self.window.show()


class Window(Tk):
    def __init__(self, loop: asyncio.BaseEventLoop):
        self.loop = loop
        self.root = Tk()
        self.close_window_error_handler = True
        self.root.protocol('WM_DELETE_WINDOW', self.update_close_window_error_handler)
        self.root.title('Progress Bar')
        self.root.geometry('250x150')

        self.progress_bar = ttk.Progressbar(orient='horizontal', length=200, value=0)
        self.progress_bar.pack(fill=X, padx=6, pady=6)

        self.start_button = ttk.Button(text='Start', command=lambda: self.loop.create_task(self.pb_start()))
        self.start_button.pack(anchor=SW, side=LEFT, padx=6, pady=6)

        self.stop_button = ttk.Button(text='Stop', command=lambda: self.loop.create_task(self.pb_stop()))
        self.stop_button.pack(anchor=SE, side=RIGHT, padx=6, pady=6)

        self.cancel_flag = False


    async def show(self):
        while self.close_window_error_handler:
            self.root.update()
            await asyncio.sleep(.1)


    async def pb_start(self):
        self.cancel_flag = False
        while not self.cancel_flag:
            self.progress_bar.step(2)
            await asyncio.sleep(0.5)


    async def pb_stop(self):
        self.cancel_flag = True
        self.progress_bar.stop()


    def update_close_window_error_handler(self):
        self.close_window_error_handler = False


asyncio.run(App().exec())
