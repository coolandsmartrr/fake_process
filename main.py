import time, random, argparse, subprocess
from datetime import datetime
from rich import print
from tqdm import tqdm
import curses


loglines = """Process started.
Initializing batch process...
Loading data from source files...
Data loaded successfully.
Applying transformations to the data...
Transformations applied successfully.
Performing data validation...
progressbar
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


def getHeight():
    stdscr = curses.initscr()
    height, _ = stdscr.getmaxyx()
    curses.endwin()
    return height

def set_consoleview():
  height = 60
  width = 80
  command = f"printf '\\e[8;{height};{width}t'"

  try:
      subprocess.call(command, shell=True)
  except Exception as e:
      print(f"An error occurred: {str(e)}")


def show_progressbar(linenum, fillup_lines):
  total_iterations = random.randint(70, 100)
  with tqdm(total=total_iterations, unit="epochs", leave=True) as pbar:
    if linenum < fillup_lines:
      pbar.update(total_iterations)
    while pbar.n < pbar.total:
      time.sleep(random.randrange(0,2))
      pbar.update(random.randint(0,5))
      # Check if progress reaches 100%
      if pbar.n >= total_iterations:
        pbar.n = total_iterations  # Set progress to total value
        pbar.refresh() 
        break


def main(fillup_lines, isConsoleView=False):
  if (isConsoleView): set_consoleview()
  
  linenum = 0
  
  while True:
    logline = loglines[linenum % len(loglines)]
    linenum += 1

    now = datetime.now()
    date = now.strftime("%Y-%m-%d")
    curr_time = now.strftime("%H:%M:%S")
    timestring = f"[{date} {curr_time} {logline}]"
    show_progressbar(linenum, fillup_lines) if (logline == "progressbar") else print(timestring)

    if (linenum > fillup_lines):
      interval = round(random.random() * 10)
      time.sleep(interval)


if __name__ == "__main__":
  parser = argparse.ArgumentParser()
  parser.add_argument("-sl", "--startlines", type=int, default=getHeight(), help="Number of lines for initial console output")
  parser.add_argument("-c", "--consoleview", action="store_true", default=False, help="Change the size of terminal window to 80x60")
  args = parser.parse_args()

  main(args.startlines, args.consoleview)