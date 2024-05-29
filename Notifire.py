import time
import psutil
from win10toast import ToastNotifier

def is_whatsapp_running():
    for process in psutil.process_iter(['name']):
        if process.info['name'] == 'WhatsApp.exe':
            return True
    return False

def send_notification(toaster):
    toaster.show_toast("WhatsApp Detector", "WhatsApp is now open!", duration=10, threaded=True)

def main():
    whatsapp_open = False
    toaster = ToastNotifier()  # Create the ToastNotifier object once
    while True:
        try:
            if is_whatsapp_running():
                if not whatsapp_open:
                    send_notification(toaster)
                    whatsapp_open = True
            else:
                whatsapp_open = False  # Reset the flag when WhatsApp is not running
            time.sleep(5)
        except Exception as e:
            print(f"An error occurred: {e}")
            time.sleep(5)

if __name__ == "__main__":
    main()
