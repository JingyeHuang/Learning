
# coding: utf-8

# In[6]:


import urllib.request
import json
import requests
from tkinter import *
import time

url_login = 'http://192.168.50.1/cgi-bin/MANGA/api.cgi'
data = {'func':'login','username':'admin','password':'admin'}
ap_power = 1

r = requests.post(url_login, data = data)
co = r.cookies.get_dict()
#print(co['bauth'])
print(r.cookies)
#web = requests.get('http://192.168.50.1/cgi-bin/MANGA/index.cgi?mode=config&option=main',cookies=r.cookies)


cpu_upload = requests.get('http://192.168.50.1/cgi-bin/MANGA/data.cgi?period=4&option=cpuload',cookies=r.cookies)

time = requests.get('http://192.168.50.1/cgi-bin/MANGA/data.cgi?option=uptime',cookies=r.cookies)


#Clientlist feature
clientlist = requests.get('http://192.168.50.1/cgi-bin/MANGA/data.cgi?option=client_info',cookies=r.cookies).text
length = len(clientlist)
clients = []
a=0
b=0
while a!= 11:
    a = clientlist.find('name id=',b) + 12
    b = clientlist.find('<',a)
    if a != 11:
        clients.append(clientlist[a:b])
        
client_num = len(clients)
showlist = ''
for i in range(client_num):
    if i%5 == 0:
        showlist = showlist + '\n'
    showlist = showlist + clients[i] +'\000'

def changestatus():
    # Change AP power module
    global ap_power
    def power():
        global ap_power
        if ap_power == 1:
            ap_level = 'max'
        elif ap_power == 2:
            ap_level = 'high'
        elif ap_power == 3:
            ap_level = 'medium'
        elif ap_power == 4:
            ap_level ='low'
        ap_data = {
            'mode': 'submit',
            'option': 'apconfig',
            'hidx': '6',
            'ap_number_of_antenna': '1',
            'radio_profile_order': '1',
            'ssid_list_1': '',
            'ssid_list_2': '',
            'ssid_list_3': '',
            'ap_country': '344',
            'ap_external_antenna': '',
            'ap_directional_antenna': '',
            'sche_profile': '0',
            'ap_radio_1': 'ng',
            'ap_ch_width_1': '0',
            'ap_serial_ch_1': '1 2 3 4 5 6 7 8 9 10 11 12 13',
            'ap_ch_1': '0',
            'ap_txlevel_1': ap_level,
            'client_limit': '0',
            'rssi_threshold': '0',
            'beacon_rate': '1000',
            'beacon_interval': '100',
            'dtim': '1',
            'rts_threshold': '0',
            'frag_threshold': '0',
            'distance': '4050',
            'custom_slottime': 'yes',
            'slottime': '9',
            'ack_timeout': '48',
            'ampdu_limit': '50000',
                }

        requests.post('http://192.168.50.1/cgi-bin/MANGA/index.cgi?mode=config&option=apconfig', data = ap_data, cookies=r.cookies)
        requests.get('http://192.168.50.1/cgi-bin/MANGA/index.cgi?mode=submit&option=activate&hidx=0',cookies = r.cookies)

    def refreshpower(event):
        global ap_power
        ap_power = AP.get()
    router = Toplevel()
    router.title('Router - 1')
    Button(router, text = 'Reboot').grid(row=0,column=0,sticky=W,padx=5, pady=5)
    Button(router, text = 'Change Power', command=power).grid(row=1,column=0,sticky=W,padx=5, pady=5)
    AP = Scale(router, from_=1, to=4,orient=HORIZONTAL,command = refreshpower)
    AP.grid(row=1,column=1,padx=5, pady=5)
    Button(router, text = 'Set IP').grid(row=2,column=0,sticky=W,padx=5, pady=5)
    Entry(router).grid(row=2,column=1,padx=5, pady=5)
    Button(router, text = 'Change Channel').grid(row=3,column=0,sticky=W,padx=5, pady=5)
    Scale(router, from_=1, to=12,orient=HORIZONTAL).grid(row=3,column=1,padx=5, pady=5)
    Label(router, text = 'Client list: Total client -->').grid(row=4,column=0,padx=5, pady=5)
    Label(router, text = str(client_num)).grid(row=4,column=1,padx=5,pady=5)
    Label(router, text = showlist).grid(row=5,column=0,columnspan=10,padx=5, pady=5)
    

root = Tk()

photo = PhotoImage(file = 'floorplan.png')
theLabel = Label(root, image = photo)
theLabel.grid(row=0,column=0,columnspan=20)

Button(root, text = 'Router 1', command = changestatus).grid(row=1,column=0,rowspan=2)
cpulabel = Label(root,text='cpu load: '+cpu_upload.text[29:33])
cpulabel.grid(row=1,column=1,sticky=W)
onlinelabel = Label(root,text='Router online: '+time.text[20:46])
onlinelabel.grid(row=2,column=1,sticky=W)
Button(root, text = 'Router 2', command = changestatus).grid(row=1,column=2,rowspan=2)
Button(root, text = 'Router 3', command = changestatus).grid(row=1,column=3,rowspan=2)
Button(root, text = 'Router 4', command = changestatus).grid(row=1,column=4,rowspan=2)

def ch():
    cpu_upload = requests.get('http://192.168.50.1/cgi-bin/MANGA/data.cgi?period=4&option=cpuload',cookies=r.cookies)

    time = requests.get('http://192.168.50.1/cgi-bin/MANGA/data.cgi?option=uptime',cookies=r.cookies)
    
    cpulabel.config(text='cpu load: '+cpu_upload.text[29:33])
    onlinelabel.config(text='Router online: '+time.text[20:46])
    cpulabel.grid(row=1,column=1,sticky=W)
    onlinelabel.grid(row=2,column=1,sticky=W)
    root.after(5000,ch)

root.after(5000,ch)

root.mainloop()

# headers = {
# 'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8',
# 'Accept-Encoding': 'gzip, deflate',
# 'Accept-Language': 'zh-TW,zh;q=0.9,en-US;q=0.8,en;q=0.7',
# 'Connection': 'keep-alive',
# 'Cookie': 'bauth=' + co['bauth'],
# 'Host': '192.168.50.1',
# 'Referer': 'http://192.168.50.1/',
# 'Upgrade-Insecure-Requests': '1',
# 'User-Agent':' Mozilla/5.0 (Windows NT 6.3; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/65.0.3325.181 Safari/537.36',
# }

# req = urllib.request.Request('http://192.168.50.1/cgi-bin/MANGA/index.cgi?mode=config&option=main',headers = headers)
# response = urllib.request.urlopen(req)
# html = response.read().decode('utf-8')
# print(html)

