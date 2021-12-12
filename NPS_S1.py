import pandas as pd
import matplotlib.pyplot as plt
from matplotlib.dates import DateFormatter, MinuteLocator, date2num
import datetime
import os 

cpath = os.path.dirname(__file__)
file = "//Data//831C_11471-20211117 144645-21111702.LD0-usb.xlsx" # location of xlsx file
NPS1raw = pd.read_excel(cpath+file,sheet_name="Time History",index_col="Date") # reading excel file into pandas for sheet 'Time History' with index as 'Date column
NPS1ThirdCols = NPS1raw.loc[:, NPS1raw.columns.str.startswith('1/3')].columns # list of 3rd octave columns
NPS1thirds = NPS1raw.loc[:, NPS1ThirdCols] # data with only third-octave columns
NPS1thirds = NPS1thirds.fillna(0) # filling NaN data with zeros

start = "2021-11-17 16:50:00" # Set start time / date required
start_dt = datetime.datetime.strptime(start, '%Y-%m-%d %H:%M:%S') # convert start time from text to datetime format
end_dt = start_dt+pd.Timedelta(hours=1) # add one hour to start time for end time
NPS1thirdsplot = NPS1thirds[start_dt:end_dt] # filtering 

# formatting matplotlib to create spectrogram 
fig, ax = plt.subplots(figsize=(8,5))
plt.title("1 HOUR PERIOD STARTING "+start, loc='right', fontsize=8) # Title
Cols = [col.replace("1/3 LZeq ","")+"Hz" for col in NPS1ThirdCols] # Formatting columns
startfloat, endfloat = date2num(start_dt), date2num(end_dt) # Converts datetime because imshow only accepts float values
ax.imshow(NPS1thirdsplot.T, aspect="auto", origin='lower', extent=[startfloat,endfloat,0,len(Cols)], interpolation=None) # plot spectrogram
tickloc = [x + 0.5 for x in range(0, len(Cols))] # moving y tick location to center of pixel line
ax.yaxis.set(ticks=tickloc) # setting tick locaiton
ax.set_yticklabels(Cols, fontsize=6) # setting y tick labels
ax.set_xlabel('Time') # x label
ax.set_ylabel('1/3 Octave band center frequency') # y label
myFmt = DateFormatter('%H:%M') # formatter for x axis datetime (##:##)
minutes = MinuteLocator(interval = 5) # 
ax.xaxis.set_major_locator(minutes)
ax.xaxis.set_major_formatter(myFmt)
fig.autofmt_xdate()
plt.show()