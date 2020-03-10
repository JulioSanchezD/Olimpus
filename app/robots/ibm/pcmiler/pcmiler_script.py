from time import sleep
import pandas as pd
import threading


class PCMiler:

    def __init__(self, filename: str, directory: str):
        self.filename: str = filename
        self.directory: str = directory
        thread = threading.Thread(target=self.run, args=())
        thread.daemon = True
        thread.start()

    def run(self):
        df: pd.DataFrame = pd.read_excel(self.directory + self.filename)
        sleep(3)
        with open(f"{self.directory}test.txt", 'w') as out:
            out.writelines(df.head().to_string())
