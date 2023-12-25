import time
from datetime import datetime
from urllib.request import urlopen
import json
import requests
from path_url import Path_URL

path_file = Path_URL
path_url = path_file.path_local+"api/Rest_api/get_data_setting"
url_data_logger = path_file.path_server+"api/Data_logger/logger"
url_upload_local =  path_file.path_local+"api/Data_logger/logger"

machine_code = ""
while True:
    try:
        read_machine_code = open("/home/pi/machine_code/machine_code.txt", "r")
        machine_code = read_machine_code.read().rstrip('\n')
        if machine_code != '':
            response = urlopen(path_url)
            data_json = json.loads(response.read())
            plc_out_read = open('/home/pi/hottub_ma/txt_file/status_plc.txt','r')
            split_file_plc_out = plc_out_read.read().split(",")
            plc_q0 = split_file_plc_out[0].replace("[","")
            plc_q1 = split_file_plc_out[1]
            plc_q2 = split_file_plc_out[2]
            plc_q3 = split_file_plc_out[3].replace("]","")
            
            # plc in
            plc_in_read = open('/home/pi/hottub_ma/txt_file/status_plc_in.txt','r')
            split_file_plc_in = plc_in_read.read().split(",")
            plc_i0 = split_file_plc_in[0].replace("[","")
            plc_i1 = split_file_plc_in[1]
            plc_i2 = split_file_plc_in[2]
            plc_i3 = split_file_plc_in[3]
            plc_i4 = split_file_plc_in[4]
            plc_i5 = split_file_plc_in[5]
            plc_i6 = split_file_plc_in[6]
            plc_i7 = split_file_plc_in[7].replace("]","")
            # relay
            relay_read = open('/home/pi/hottub_ma/txt_file/status_relay_8.txt','r')
            split_file_relay = relay_read.read().split(",")
            relay_ch0 = split_file_relay[0].replace("[","")
            relay_ch1 = split_file_relay[1]
            relay_ch2 = split_file_relay[2]
            relay_ch3 = split_file_relay[3]
            relay_ch4 = split_file_relay[4]
            relay_ch5 = split_file_relay[5]
            relay_ch6 = split_file_relay[6]
            relay_ch7 = split_file_relay[7].replace("]","")
            # ph
            read_ph = open('/home/pi/hottub_ma/txt_file/ph.txt','r')
            ph_data = read_ph.read()
            # orp
            read_orp = open('/home/pi/hottub_ma/txt_file/orp.txt','r')
            orp_data = read_orp.read()
            # temp
            read_temp = open('/home/pi/hottub_ma/txt_file/temperature.txt','r')
            temp_data = read_temp.read()
            #pressure
            read_pressure = open('/home/pi/hottub_ma/txt_file/pressure.txt','r')
            pressure_data = read_pressure.read()

            if int(data_json[0]['online_status']) == 1:
                print("อัพโหลดไฟล์ แบบ online")
                # plc out 
                resp = requests.post(url_data_logger, data={'ph':ph_data,
                                                            'orp':orp_data,
                                                            'temp':temp_data,
                                                            'pressure':pressure_data,
                                                            'plc_q0':plc_q0,
                                                            'plc_q1':plc_q1,
                                                            'plc_q2':plc_q2,
                                                            'plc_q3':plc_q3,
                                                            'plc_i0':plc_i0,
                                                            'plc_i1':plc_i1,
                                                            'plc_i2':plc_i2,
                                                            'plc_i3':plc_i3,
                                                            'plc_i4':plc_i4,
                                                            'plc_i5':plc_i5,
                                                            'plc_i6':plc_i6,
                                                            'plc_i7':plc_i7,
                                                            'relay_ch0':relay_ch0,
                                                            'relay_ch1':relay_ch1,
                                                            'relay_ch2':relay_ch2,
                                                            'relay_ch3':relay_ch3,
                                                            'relay_ch4':relay_ch4,
                                                            'relay_ch5':relay_ch5,
                                                            'relay_ch6':relay_ch6,
                                                            'relay_ch7':relay_ch7,
                                                            'machine_code':machine_code
                                                    })
                resp = requests.post(url_upload_local, data={'ph':ph_data,
                                                            'orp':orp_data,
                                                            'temp':temp_data,
                                                            'pressure':pressure_data,
                                                            'plc_q0':plc_q0,
                                                            'plc_q1':plc_q1,
                                                            'plc_q2':plc_q2,
                                                            'plc_q3':plc_q3,
                                                            'plc_i0':plc_i0,
                                                            'plc_i1':plc_i1,
                                                            'plc_i2':plc_i2,
                                                            'plc_i3':plc_i3,
                                                            'plc_i4':plc_i4,
                                                            'plc_i5':plc_i5,
                                                            'plc_i6':plc_i6,
                                                            'plc_i7':plc_i7,
                                                            'relay_ch0':relay_ch0,
                                                            'relay_ch1':relay_ch1,
                                                            'relay_ch2':relay_ch2,
                                                            'relay_ch3':relay_ch3,
                                                            'relay_ch4':relay_ch4,
                                                            'relay_ch5':relay_ch5,
                                                            'relay_ch6':relay_ch6,
                                                            'relay_ch7':relay_ch7,
                                                            'machine_code':machine_code
                                                    })

                
                time.sleep(1200)
            else:
                print("Logger Offline")
                resp = requests.post(url_upload_local, data={'ph':ph_data,
                                                            'orp':orp_data,
                                                            'temp':temp_data,
                                                            'pressure':pressure_data,
                                                            'plc_q0':plc_q0,
                                                            'plc_q1':plc_q1,
                                                            'plc_q2':plc_q2,
                                                            'plc_q3':plc_q3,
                                                            'plc_i0':plc_i0,
                                                            'plc_i1':plc_i1,
                                                            'plc_i2':plc_i2,
                                                            'plc_i3':plc_i3,
                                                            'plc_i4':plc_i4,
                                                            'plc_i5':plc_i5,
                                                            'plc_i6':plc_i6,
                                                            'plc_i7':plc_i7,
                                                            'relay_ch0':relay_ch0,
                                                            'relay_ch1':relay_ch1,
                                                            'relay_ch2':relay_ch2,
                                                            'relay_ch3':relay_ch3,
                                                            'relay_ch4':relay_ch4,
                                                            'relay_ch5':relay_ch5,
                                                            'relay_ch6':relay_ch6,
                                                            'relay_ch7':relay_ch7,
                                                            'machine_code':machine_code
                                                    })

                time.sleep(1200)
        else:
            time.sleep(3)
    except:
        pass
   

   
