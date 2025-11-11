from datetime import datetime

class Logger:
    def __init__(self, log_file):
        self.log_file = log_file

    def log(self, message):
        timestamp = datetime.now().strftime("[%d-%m-%y %H:%M:%S]")
        log_entry = f"{timestamp} {message}\n"
        with open(self.log_file, "a") as f:
            f.write(log_entry)
        print(f'LOG: {message}')