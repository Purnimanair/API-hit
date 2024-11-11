import requests
 import csv
 def read_csv(file_path):
     ids=[]
     with open(file_path,mode='r') as file:
         csv_read=csv.reader(file)
         next(csv_read)
         for row in csv_read:
             ids.append(row[0])
     return ids
 def hitty(api_url,id_value):
     try:
         full_url=f"{api_url}?report_job={id_value}"
         print(f"requesting url:{full_url}")
         response=requests.get(full_url)
         response.raise_for_status()
         data=response.json()
         #print(f"full api response for ID {id_value}:{data}")
         latest_statuses=data.get('results')[0].get('latest_status')
         ids_in_job=data['results'][0].get('ids')
         return latest_statuses,ids_in_job
         #if 'job' in data:
         #   latest_status=data['job'].get('latest_status')
         #    ids_in_job=data['job'].get('ids')
         #    return latest_status,ids_in_job
         #else:
         #    return "no response"
     except requests.exceptions.RequestException as e:
         print(f"failed to fetch data for ID")
     return None
 def main():
     csv_path='/home/purnimanair/Downloads/rgf_scheduled_jobs.csv'
     api_url=''
     ids=read_csv(csv_path)
     for id_value in ids:
         latest_statuses=hitty(api_url,id_value)
         if latest_statuses:
             print(f"ID:{id_value},latest status:{latest_statuses}")
         else:
             print("no status found")
 if _name=="main_":
     main()
