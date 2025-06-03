import subprocess
import tkinter as tk
from tkinter import scrolledtext


def run_loot(level):
    """Run lootz edit.py once and return its output."""
    proc = subprocess.Popen(
        ['python', 'lootz edit.py'],
        stdin=subprocess.PIPE,
        stdout=subprocess.PIPE,
        stderr=subprocess.STDOUT,
        text=True,
    )
    proc.stdin.write(f"{level}\n")
    proc.stdin.flush()

    lines = []
    while True:
        line = proc.stdout.readline()
        if not line:
            break
        lines.append(line)
        if 'Hit enter for another set of loot.' in line:
            proc.kill()
            break
    proc.communicate()

    output = ''.join(lines)
    prompt = 'Encounter level? (1-30) '
    if output.startswith(prompt):
        output = output[len(prompt):]
    return output


class LootzApp(tk.Tk):
    def __init__(self):
        super().__init__()
        self.title('Lootz GUI')
        tk.Label(self, text='Encounter Level (1-30):').pack(pady=5)
        self.level_entry = tk.Entry(self)
        self.level_entry.pack(pady=5)
        tk.Button(self, text='Generate Loot', command=self.generate).pack(pady=5)
        self.output = scrolledtext.ScrolledText(self, width=80, height=30)
        self.output.pack(pady=5)

    def generate(self):
        level = self.level_entry.get().strip()
        if not level:
            return
        result = run_loot(level)
        self.output.delete('1.0', tk.END)
        self.output.insert(tk.END, result)


if __name__ == '__main__':
    app = LootzApp()
    app.mainloop()
