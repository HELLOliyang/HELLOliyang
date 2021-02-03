import csv
import excelDo
class csvIO():
    def write_dict(self,path,header,rows_dict):
        row = csv.DictWriter(open(path,'w'),header)
        row.writeheader()
        row.writerows(rows_dict)
        open(path,'w').close()
        return None
    def read(self,path):
        reader = csv.DictReader(open(path,'r'))
        list = []
        for i in reader:
            list.append(i)
        open(path,'r').close()
        return list
if __name__ == '__main__':
    base = csvIO()
    path = 'config.csv'
    f = base.read(path=path)[0]
    print(f)