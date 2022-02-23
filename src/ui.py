import tkinter as tk
from PIL.ImageTk import PhotoImage
from PIL import Image
import os


class AGamersScriptUI(tk.Frame):
    """A super awesome GUI for AGamersScript!"""
    def __init__(self) -> None:
        self.root = tk.Tk()
        super().__init__(self.root)
        self.pack()
        
        self.app_width = 750
        self.app_height = 400

        self.animation_path = os.path.abspath(os.path.join(os.path.dirname(__file__), 'images\\working-gif.gif'))

        # needed for running in dev
        if 'src\\images\\working-gif.gif' in self.animation_path:
            self.animation_path = self.animation_path.replace('src\\', '')

        self.root.title("A Gamer's Script")
        self.root.geometry(self._get_geometry())

        app_icon = os.path.abspath(os.path.join(os.path.dirname(__file__), 'images\\app.ico'))

        # needed for running in dev
        if 'src\\images\\app.ico' in app_icon:
            app_icon = app_icon.replace('src\\', '')

        self.root.iconbitmap(app_icon)
        self.init_interface()

    def _get_geometry(self) -> str:
        """Creates the geometry for the window.
        This also calculates an offset to center the window.

        Example geometry: 750x400+300+300

        Returns:
            str: geometry string
        """
        screen_width = self.winfo_screenwidth()
        screen_height = self.winfo_screenheight()

        # offsets for centering the window
        width_offset = int((screen_width / 2) - (self.app_width / 2))
        height_offset = int((screen_height / 2) - (self.app_height / 2) * 1.3) # multiplied by 1.3 to start window slightly higher than middle

        return f'{self.app_width}x{self.app_height}+{width_offset}+{height_offset}'

    def _get_animation_frames(self, filepath: str) -> list[PhotoImage]:
        animation = Image.open(filepath)
        frames: list[PhotoImage] = []
        try:
            while True:
                frame = animation.copy()
                frames.append(PhotoImage(frame))
                animation.seek(len(frames)) # skip to next frame
        except EOFError:
            pass
        return frames

    def _animate_update(self, idx: int, label: tk.Label, frames: list[PhotoImage], speed: int) -> None:
        frame = frames[idx]
        idx += 1
        if idx == len(frames):
            idx = 0
        label.configure(image=frame)
        self.root.after(speed, self._animate_update, idx, label, frames, speed)

    def init_interface(self) -> None:
        self.root['background'] = '#ffffff'
        self.setup_gear_animation()
        self.setup_bottom_download_text()

    def setup_gear_animation(self) -> None:
        animation_speed = 37
        animation_frames = self._get_animation_frames(self.animation_path)

        wrench = tk.Label(self.root, borderwidth=0, anchor=tk.CENTER)
        wrench.pack()
        wrench.place(x=self.app_width / 2, y=self.app_height / 2, anchor='center')

        self.root.after(0, self._animate_update, 0, wrench, animation_frames, animation_speed)

    def setup_bottom_download_text(self) -> None:
        text = "Hang tight, we're getting your installers"
        download_text = tk.Label(self.root, text=text)
        download_text.pack()
        download_text.place(x=self.app_width / 2, y=self.app_height * 0.9, anchor=tk.CENTER)
        download_text['background'] = '#ffffff'
        download_text['foreground'] = '#8f6ea3'
        download_text['font'] = ('Segoe UI', 16, 'bold')
