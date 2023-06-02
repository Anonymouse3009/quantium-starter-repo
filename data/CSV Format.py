import csv

source_files = ['CSVs\data0.csv', 'CSVs\data1.csv', 'CSVs\data2.csv']
destination_file = 'CSVs\Daily_sales_Data_Formatted.csv'

with open(destination_file, 'a', newline='') as destination:
    writer = csv.writer(destination)

    for file in source_files:
        with open(file, 'r') as source:
            reader = csv.reader(source)

            for row in reader:
                # If the row meets certain conditions, append it to the destination CSV
                if row[0] == 'pink morsel':
                    num1 = float(row[1])
                    num2 = float(row[2])
                    multiple = num1 * num2 
                    row.append(multiple)
                    writer.writerow(row)
        source.close()

destination.close()