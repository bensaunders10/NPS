import matplotlib.pyplot as plt
from matplotlib.dates import DateFormatter, HourLocator

def plothist(data, column, night):
    fig, ax1 = plt.subplots(1, 1, figsize=(8,4))
    ax1.clear()
    bins = range(15,70)
    if night:
        t = 'Night Time'
        st, et = '23:00', '07:00'
    else:
        t = 'Day Time'
        st, et = '07:00', '23:00'
    ltall = data.between_time(st, et)
    ax1.hist(ltall[column],bins=bins,density=1,alpha=0.7)

def plotline(data, column, night): #must have datetime as index
    fig, ax1 = plt.subplots(1, 1, figsize=(8,4))
    if night:
        st, et = '23:00', '07:00'
    else:
        st, et = '07:00', '23:00'
    ltall = data.between_time(st, et)
    ax1.scatter(ltall.index,ltall[column],c='black')
    myFmt = DateFormatter('%d.%m | %H:%M')
    hours = HourLocator(interval = 6)
    ax1.xaxis.set_major_locator(hours)
    ax1.xaxis.set_major_formatter(myFmt)
    fig.autofmt_xdate()
    ax1.set_ylim(15,80)