import pandas

class CsvReader:

    def __init__(self) -> None:
        super().__init__()
        self.temperatures = []


    def read_csv(self):
        csv = pandas.read_csv('./weather_data.csv')
        temps = csv['temp']
        print(temps)


csvReader = CsvReader()
csvReader.read_csv()
