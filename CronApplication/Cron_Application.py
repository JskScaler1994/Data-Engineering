import datetime

now = datetime.datetime.now()
with open("C:\\Scripts\Script_log.txt","a") as f:
    f.write(f"Script ran at: {now}\n")