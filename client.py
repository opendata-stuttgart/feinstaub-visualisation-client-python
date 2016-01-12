import datetime
import requests
import pandas as pd
from io import StringIO
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt

ndays = 7
sensor_id = 63

data = pd.DataFrame()
ldate = datetime.date.today() - datetime.timedelta(1)
for x in range(ndays):
    dt = str(ldate - datetime.timedelta(x))
    url = "http://archive.madflex.de/{dt}/{dt}_ppd42ns_sensor_{sensor_id}.csv".format(dt=dt, sensor_id=sensor_id)
    print(url)
    r = requests.get(url)
    data = data.append(pd.read_csv(StringIO(r.text), delimiter=';'))

data['dt'] = data.apply(lambda row: datetime.datetime.strptime(row.timestamp[:-6], "%Y-%m-%dT%H:%M:%S.%f"), axis=1)

plt.rcParams['figure.figsize'] = (10.0, 8.0)
plt.plot(data.dt, data.P2, '.')
plt.savefig("/opt/code/plots/firsttry.png")
