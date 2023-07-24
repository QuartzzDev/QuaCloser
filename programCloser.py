# Quartzz Dev

import os
import subprocess
import ctypes

progs = ["notepad.exe", "chrome.exe"]  # İstediğiniz programları buraya ekleyebilirsiniz

def check_and_close_programs():
    process_list = os.popen('tasklist').read().strip().split('\n')
    
    for prog in progs:
        for process in process_list:
            if prog in process.lower():
                subprocess.Popen(f"taskkill /F /IM {prog}")
                MessageBox = ctypes.windll.user32.MessageBoxW
                MessageBox(None, f"{prog} programı kapatıldı!", "Uyarı!", 0x40)
                break

while True:
    check_and_close_programs()
