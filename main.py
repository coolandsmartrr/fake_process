import time
from datetime import datetime
import random

loglines = """Process started.
Initializing batch process...
Loading data from source files...
Data loaded successfully.
Applying transformations to the data...
Transformations applied successfully.
Performing data validation...
Data validation completed. No errors found.
Starting batch processing...
Process completed.
Generating report...
Report generated successfully.
Finalizing batch process...
Batch process finalized.
Cleaning up temporary files...
Temporary files cleaned up successfully.
Preparing for next iteration...
Next iteration prepared.""".split('\n')

linenum = 0
fillup_lines = 50

while True:
  logline = loglines[linenum % len(loglines)]
  linenum += 1

  now = datetime.now()
  date = now.strftime("%Y-%m-%d")
  curr_time = now.strftime("%H:%M:%S")
  timestring = f"[{date} {curr_time} {logline}]"
  print(timestring)

  if (linenum > fillup_lines):
    interval = round(random.random() * 10)
    time.sleep(interval)