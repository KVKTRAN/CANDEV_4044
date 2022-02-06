import numpy as np

data_points = {0: 0,
3: 0.025813692,
5: 0.053872054,
7: 0.119191919,
9: 0.236139169,
11: 0.412794613,
13: 0.621997755,
15: 0.797306397,
17: 0.908417508,
19: 0.964534231,
21: 0.992592593,
23: 0.999775533}

def leth_fnc(speed):
  
  if (speed < 0):
    return 0
  elif (speed > 23):
    return 0.999775533
  else:
    return np.interp(speed, list(data_points.keys()), list(data_points.values()))