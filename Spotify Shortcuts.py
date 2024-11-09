import keyboard
import pyautogui

def play_pause():
    pyautogui.press('playpause')
    print("Müzik çal/duraklat işlemi yapıldı.")

def stop_track():
    pyautogui.press('stop')
    print("Müzik durduruldu.")

def next_track():
    pyautogui.press('nexttrack')
    print("Sonraki şarkıya geçildi.")

def previous_track():
    pyautogui.press('prevtrack')
    print("Önceki şarkıya geçildi.")

def volume_up():
    pyautogui.press('volumeup')
    print("Ses artırıldı.")

def volume_down():
    pyautogui.press('volumedown')
    print("Ses azaltıldı.")

def mute_volume():
    pyautogui.press('volumemute')
    print("Ses kapatıldı/açıldı.")

# Kısayol Atamaları
keyboard.add_hotkey('ctrl+w', play_pause) # Şarkıyı oynat
keyboard.add_hotkey('ctrl+q', stop_track) # Şarkıyı durdur
keyboard.add_hotkey('ctrl+right', next_track) # Sonraki şarkı
keyboard.add_hotkey('ctrl+left', previous_track) # Önceki şarkı
keyboard.add_hotkey('ctrl+up', volume_up) # Ses arttırma
keyboard.add_hotkey('ctrl+down', volume_down) # Ses azaltma
keyboard.add_hotkey('ctrl+m', mute_volume) # Sesi kapatma

print("Spotify medya kontrol programı çalışıyor.")
keyboard.wait()