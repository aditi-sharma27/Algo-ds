import pandas as pd


class DbUploader(object):
    def __init__(self, host, token, zip_list):
        self.host = host
        self.token = token
        self.zip_list = zip_list


class XLSXParser(object):
    def __init__(self, filename):
        self.file_name = filename

    def file_reader(self):
        df = pd.read_excel(self.file_name)
        print(df.columns)
        df = df.rename(columns=lambda x: x.strip())
        return list(df['zip']), list(df['prov_group'])


A = XLSXParser("test2.xlsx")
a = A.file_reader()
print(a)
