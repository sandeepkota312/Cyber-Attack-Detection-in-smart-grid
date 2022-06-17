import tkinter as tk
import keras
import tensorflow as tf
import numpy as np

main_screen=tk.Tk()
main_screen.title('Cyber Attack Detection')
main_screen_canvas = tk.Canvas(main_screen, width =800, height
=800, bg="white")

main_screen_canvas.pack()

IP_variable = tk.StringVar()
srv_rate_variable= tk.StringVar()
flag_S3_variable= tk.StringVar()
flag_RSTR_variable= tk.StringVar()
dst_host_srv_serror_rate_variable= tk.StringVar()
dst_host_serror_rate_variable= tk.StringVar()
srv_serror_rate_variable= tk.StringVar()
serror_rate_variable= tk.StringVar()
dst_host_same_srv_rate_variable= tk.StringVar()
dst_host_srv_count_variable= tk.StringVar()
count_variable= tk.StringVar()
service_hostnames_variable= tk.StringVar()
result_variable= tk.StringVar()
Data_variable= tk.StringVar()


lbl = tk.Label(main_screen, text="Cyber Attack Detection in Smart Grid")
lbl.config(font=('Comic serif', 20, 'bold'),bg='white',fg='black')
main_screen_canvas.create_window(400, 20, window=lbl)

parameters_lbl = tk.Label(main_screen, text="Input Parameters")
parameters_lbl.config(font=('Comic serif', 12, 'bold'),bg='white',fg='black')
main_screen_canvas.create_window(90, 80, window=parameters_lbl)

#00
IP_lbl = tk.Label(main_screen, text="IP Address")
IP_lbl.config(font=('Comic serif', 10, 'bold'),bg='white',fg='black')
main_screen_canvas.create_window(130, 120, window=IP_lbl)

IP_entry = tk.Entry(main_screen, textvariable=IP_variable, width = 10, font=('Comic serif',15, 'bold'),bg='grey',fg='white')
main_screen_canvas.create_window(350,120, window=IP_entry)
IP_entry.insert(0, "12.702.00.2")


#01
srv_rate_lbl = tk.Label(main_screen, text="srv_rate")
srv_rate_lbl.config(font=('Comic serif', 10, 'bold'),bg='white',fg='black')
main_screen_canvas.create_window(130, 150, window=srv_rate_lbl)

srv_rate_entry = tk.Entry(main_screen, textvariable=srv_rate_variable, width = 10, font=('Comic serif',15, 'bold'),bg='grey',fg='white')
main_screen_canvas.create_window(350,150, window=srv_rate_entry)
srv_rate_entry.insert(0, "0.05")

#02
flag_S3_lbl = tk.Label(main_screen, text="flag_S3")
flag_S3_lbl.config(font=('Comic serif', 10, 'bold'),bg='white',fg='black')
main_screen_canvas.create_window(130, 180, window=flag_S3_lbl)

flag_S3_entry = tk.Entry(main_screen, textvariable=flag_S3_variable, width = 10, font=('Comic serif',15, 'bold'),bg='grey',fg='white')
main_screen_canvas.create_window(350,180, window=flag_S3_entry)
flag_S3_entry.insert(0, "0")

#03
flag_RSTR_lbl = tk.Label(main_screen, text="flag_RSTR")
flag_RSTR_lbl.config(font=('Comic serif', 10, 'bold'),bg='white',fg='black')
main_screen_canvas.create_window(130, 210, window=flag_RSTR_lbl)

flag_RSTR_entry = tk.Entry(main_screen, textvariable=flag_RSTR_variable, width = 10, font=('Comic serif',15, 'bold'),bg='grey',fg='white')
main_screen_canvas.create_window(350,210, window=flag_RSTR_entry)
flag_RSTR_entry.insert(0, "0")

#04
dst_host_srv_serror_rate_lbl = tk.Label(main_screen, text="dst_host_srv_serror_rate")
dst_host_srv_serror_rate_lbl.config(font=('Comic serif', 10, 'bold'),bg='white',fg='black')
main_screen_canvas.create_window(130, 240, window=dst_host_srv_serror_rate_lbl)

dst_host_srv_serror_rate_entry = tk.Entry(main_screen, textvariable=dst_host_srv_serror_rate_variable, width = 10, font=('Comic serif',15, 'bold'),bg='grey',fg='white')
main_screen_canvas.create_window(350,240, window=dst_host_srv_serror_rate_entry)
dst_host_srv_serror_rate_entry.insert(0, "1")


#05
dst_host_serror_rate_lbl = tk.Label(main_screen, text="dst_host_serror_rate")
dst_host_serror_rate_lbl.config(font=('Comic serif', 10, 'bold'),bg='white',fg='black')
main_screen_canvas.create_window(130, 270, window=dst_host_serror_rate_lbl)

dst_host_serror_rate_entry = tk.Entry(main_screen, textvariable=dst_host_serror_rate_variable, width = 10, font=('Comic serif',15, 'bold'),bg='grey',fg='white')
main_screen_canvas.create_window(350,270, window=dst_host_serror_rate_entry)
dst_host_serror_rate_entry.insert(0, "1")

#06
srv_serror_rate_lbl = tk.Label(main_screen, text="srv_serror_rate")
srv_serror_rate_lbl.config(font=('Comic serif', 10, 'bold'),bg='white',fg='black')
main_screen_canvas.create_window(130, 300, window=srv_serror_rate_lbl)


srv_serror_rate_entry = tk.Entry(main_screen, textvariable=srv_serror_rate_variable, width = 10, font=('Comic serif',15, 'bold'),bg='grey',fg='white')
main_screen_canvas.create_window(350,300, window=srv_serror_rate_entry)
srv_serror_rate_entry.insert(0, "1")

#07
serror_rate_lbl = tk.Label(main_screen, text="serror_rate")
serror_rate_lbl.config(font=('Comic serif', 10, 'bold'),bg='white',fg='black')
main_screen_canvas.create_window(130, 330, window=serror_rate_lbl)

serror_rate_entry = tk.Entry(main_screen, textvariable=serror_rate_variable, width = 10, font=('Comic serif',15, 'bold'),bg='grey',fg='white')
main_screen_canvas.create_window(350,330, window=serror_rate_entry)
serror_rate_entry.insert(0, "1")


#08
dst_host_same_srv_rate_lbl = tk.Label(main_screen, text="dst_host_same_srv_rate")
dst_host_same_srv_rate_lbl.config(font=('Comic serif', 10, 'bold'),bg='white',fg='black')
main_screen_canvas.create_window(130, 360, window=dst_host_same_srv_rate_lbl)

dst_host_same_srv_rate_entry = tk.Entry(main_screen, textvariable=dst_host_same_srv_rate_variable, width = 10, font=('Comic serif',15, 'bold'),bg='grey',fg='white')
main_screen_canvas.create_window(350,360, window=dst_host_same_srv_rate_entry)
dst_host_same_srv_rate_entry.insert(0, "1")

#09
dst_host_srv_count_lbl = tk.Label(main_screen, text="dst_host_srv_count Address")
dst_host_srv_count_lbl.config(font=('Comic serif', 10, 'bold'),bg='white',fg='black')
main_screen_canvas.create_window(130, 390, window=dst_host_srv_count_lbl)

dst_host_srv_count_entry = tk.Entry(main_screen, textvariable=dst_host_srv_count_variable, width = 10, font=('Comic serif',15, 'bold'),bg='grey',fg='white')
main_screen_canvas.create_window(350,390, window=dst_host_srv_count_entry)
dst_host_srv_count_entry.insert(0, "0.03")

display_content_1=tk.Label(main_screen, text="max Value= 255; min value= 0")
display_content_1.config(font=('Comic serif', 10, 'bold'),bg='white',fg='black')
main_screen_canvas.create_window(550, 390, window=display_content_1)


#10
count_lbl = tk.Label(main_screen, text="count")
count_lbl.config(font=('Comic serif', 10, 'bold'),bg='white',fg='black')
main_screen_canvas.create_window(130, 420, window=count_lbl)

count_entry = tk.Entry(main_screen, textvariable=count_variable, width = 10, font=('Comic serif',15, 'bold'),bg='grey',fg='white')
main_screen_canvas.create_window(350,420, window=count_entry)
count_entry.insert(0, "0.027451")

display_content_2=tk.Label(main_screen, text="max Value= 511; min value =1")
display_content_2.config(font=('Comic serif', 10, 'bold'),bg='white',fg='black')
main_screen_canvas.create_window(550, 420, window=display_content_2)

# 11
service_hostnames_lbl = tk.Label(main_screen, text="service_hostnames")
service_hostnames_lbl.config(font=('Comic serif', 10, 'bold'),bg='white',fg='black')
main_screen_canvas.create_window(130, 450, window=service_hostnames_lbl)

service_hostnames_entry = tk.Entry(main_screen, textvariable=service_hostnames_variable, width = 10, font=('Comic serif',15, 'bold'),bg='grey',fg='white')
main_screen_canvas.create_window(350,450, window=service_hostnames_entry)
service_hostnames_entry.insert(0, "0.509804")


Result = tk.Entry(main_screen,textvariable=result_variable, width = 20, font=('Comic serif',15, 'bold'),bg='white',fg='black')
main_screen_canvas.create_window(350,650, window=Result)

#Button - Run

rock_button=tk.Button(text='Predict Attack',command=lambda:Check(),font=('helvitica',12,'bold'),bg='blue',fg='white')
main_screen_canvas.create_window(300,500, window=rock_button)

Data_lbl = tk.Label(main_screen, text="Data")
Data_lbl.config(font=('Comic serif', 10, 'bold'),bg='white',fg='black')
main_screen_canvas.create_window(50, 550, window=Data_lbl)

Data_entry = tk.Entry(main_screen, textvariable=Data_variable, width = 50, font=('Comic serif',15, 'bold'),bg='grey',fg='white')
main_screen_canvas.create_window(400,580, window=Data_entry)
Data_entry.insert(0, "")

def Check():
  Data_variable.set(str([IP_variable.get(),float(srv_rate_variable.get()),float(flag_S3_variable.get()),float(flag_RSTR_variable.get()),float(dst_host_srv_serror_rate_variable.get()),float(dst_host_serror_rate_variable.get()),float(srv_serror_rate_variable.get()),float(serror_rate_variable.get()),float(dst_host_same_srv_rate_variable.get()),float(dst_host_srv_count_variable.get()),float(count_variable.get()),float(service_hostnames_variable.get())]))
  data=[float(srv_rate_variable.get()),float(flag_S3_variable.get()),float(flag_RSTR_variable.get()),float(dst_host_srv_serror_rate_variable.get()),float(dst_host_serror_rate_variable.get()),float(srv_serror_rate_variable.get()),float(serror_rate_variable.get()),float(dst_host_same_srv_rate_variable.get()),float(dst_host_srv_count_variable.get()),float(count_variable.get()),float(service_hostnames_variable.get())]
#   print("inputs", data)
  global valid_ips
#   print('IP data',data[0])
  valid_ips = ['12702002','191255004', '223255255']
  model_regen = keras.models.load_model('FinalModel.h5')
  if str(int(str(IP_variable.get()).replace('.',''))) in valid_ips:
    var=tf.convert_to_tensor(data[:],dtype=tf.float32)
    var=tf.reshape(var,shape=(1,11))
    Answer=[0]*5
    Answer[np.argmax(model_regen.predict(var))]=1
    if Answer[0]==1:
        result_variable.set('Safe Data')
    elif Answer[1]==1:
        result_variable.set('DOS attack Detected')
    elif Answer[2]==1: 
        result_variable.set('Probing attack Detected')
    elif Answer[3]==1:
        result_variable.set('R2L attack Detected')
    elif Answer[4]==1:
        result_variable.set('U2R attack Detected')
    else:
      result_variable.set('Valid Ip')
  else:
    result_variable.set('UnAuthorised IP Detected')
  
main_screen.mainloop()