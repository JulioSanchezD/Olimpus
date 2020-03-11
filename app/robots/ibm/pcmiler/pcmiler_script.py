from time import sleep
import pandas as pd
import threading


class PCMiler:

    def __init__(self, filename, directory):
        self.filename = filename
        self.directory = directory
        thread = threading.Thread(target=self.run, args=())
        thread.daemon = True
        thread.start()

    def run(self):
        df: pd.DataFrame = pd.read_excel(self.directory + self.filename)
        sleep(3)
        with open(f"{self.directory}test.txt", 'w') as out:
            out.writelines(df.head().to_string())
