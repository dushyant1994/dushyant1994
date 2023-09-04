from SmartApi.smartConnect import SmartConnect
import pandas as pd
from datetime import datetime, timedelta
import credentials
import requests
import numpy as np
import pyotp
import matplotlib.pyplot as plt
from time import time, sleep
from talib.abstract import *
import threading
import warnings
warnings.filterwarnings('ignore')
import json
import matplotlib.pyplot as plt
import random
from datetime import date, time, datetime 
from dateutil.relativedelta import relativedelta
import talib as ta

import pandas_ta as ta

##login and generating session
user_name='your user name'
password='your pin'
apikey='api key created'
token = "token on QR code"
totp=pyotp.TOTP(token).now()
obj=SmartConnect(api_key=apikey)


data = obj.generateSession(user_name, password, totp)
print(data)
refreshToken = data['data']['refreshToken']
res = obj.getProfile(refreshToken)
res=res['data']['exchanges']