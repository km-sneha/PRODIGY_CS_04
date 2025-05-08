# Task 4: Basic Keylogger Program

## Overview

This project implements a **basic keylogger program** that records and logs keystrokes. The primary objective is to log the keys pressed and save them to a file. Ethical considerations and permissions are crucial while using keyloggers.

---

## 🔐 Features

* Records and logs all keystrokes including special keys (ENTER, TAB, SPACE, BACKSPACE, ESC)
* Logs are saved in a **timestamped text file** inside a `logs` folder
* Stops automatically after a set duration or when the **ESC** key is pressed
* Displays a summary of the session with the number of words typed and duration

---

## 🛠️ How It Works

* **Keystroke Logging**: Captures every key press, including special keys.
* **Log File Creation**: Generates a new log file with the current timestamp.
* **Session Duration**: Automatically stops logging after the specified time or when ESC is pressed.

> 💡 Note: Ensure that you have appropriate permissions before running the keylogger.

---

## 📦 Requirements

* Python 3.x
* Libraries:

  * `pynput`

To install the required library:

```
pip install pynput
```

---

## 🚀 How to Run

1. Run the Python script using the command:

```
python keylogger.py
```

2. The program will start recording keystrokes.
3. Press **ESC** to stop logging manually.

---

## 💡 Suggestions for Improvement

* Add encryption to the log file for secure storage.
* Implement a GUI for starting and stopping the keylogger.

---

## 👨‍💻 Developed By

**SNEHA K M**
*ProDigy Infotech Internship Project*

---

## ⚠️ Disclaimer

This keylogger is for educational purposes only. Unauthorized use of keyloggers is illegal and unethical. Always obtain proper consent before use.
