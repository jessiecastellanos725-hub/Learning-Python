import csv, json

number_request = 0
unique_ips = 0
top5ips = []
ip_dict = {}
with open('Alerts_test.csv', 'r') as f:
    reader = csv.reader(f)
    
    next(reader)


    for row_num, row in enumerate(reader, start=2):
        try:
            json_string = row[4]
            log_data = json.loads(json_string)

            ip_address = log_data.get('ip', 'No IP field')
            #print(f"Row {row_num}: IP = {ip_address}")
            number_request += 1
            if ip_address not in ip_dict:
                ip_dict[ip_address] = 1
            else:
                ip_dict[ip_address] += 1


        
        except json.JSONDecodeError as e:
            print(f"Row {row_num}: JSON Error - {e}")
        except Exception as e:
            print(f"Row {row_num}: Error - {e}")
N = 10
result = dict(sorted(ip_dict.items(), key = lambda x: x[1], reverse = True)[:N])

print(f'Total Requests: {number_request}')
print(f'Unique IPs: {len(ip_dict)}')
print('Top 10 IPs:')
for res in result:
        print(res + " : " + str(ip_dict[res]))
