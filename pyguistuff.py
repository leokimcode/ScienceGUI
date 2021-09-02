#todo: Receive senor data and show

import PySimpleGUI as sg #for GUI
import pandas as pd #for Excel
            
i1 = 0
i2 = 0
i3 = 0
i4 = 0
i5 = 0
i6 = 0
i7 = 0
i8 = 0
i9 = 0
i10 = 0

#defining resetAll function
def reset1():
    values['_slider1_'] = 0
    window.Element('_slider1_').Update(values['_slider1_'])
    window.Element('_pwm1_').Update(values['_slider1_'])

def reset2():
    values['_slider2_'] = 0
    window.Element('_slider2_').Update(values['_slider2_'])
    window.Element('_pwm2_').Update(values['_slider2_'])

def reset3():
    values['_slider3_'] = 0
    window.Element('_slider3_').Update(values['_slider3_'])
    window.Element('_pwm3_').Update(values['_slider3_'])

def reset4():
    values['_slider4_'] = 0
    window.Element('_slider4_').Update(values['_slider4_'])
    window.Element('_pwm4_').Update(values['_slider4_'])

def reset5():
    values['_slider5_'] = 0
    window.Element('_slider5_').Update(values['_slider5_'])
    window.Element('_pwm5_').Update(values['_slider5_'])

def reset6():
    values['_slider6_'] = 0
    window.Element('_slider6_').Update(values['_slider6_'])
    window.Element('_pwm6_').Update(values['_slider6_'])

def reset7():
    values['_slider7_'] = 0
    window.Element('_slider7_').Update(values['_slider7_'])
    window.Element('_pwm7_').Update(values['_slider7_'])

def reset8():
    values['_slider8_'] = 0
    window.Element('_slider8_').Update(values['_slider8_'])
    window.Element('_pwm8_').Update(values['_slider8_'])

def resetAll():
    reset1()
    reset2()
    reset3()
    reset4()
    reset5()
    reset6()
    reset7()
    reset8()

def pwmInt():
    pwm1 = int(values['_slider1_'])
    pwm2 = int(values['_slider2_'])
    pwm3 = int(values['_slider3_'])
    pwm4 = int(values['_slider4_'])
    pwm5 = int(values['_slider5_'])
    pwm7 = int(values['_slider7_'])
    pwm8 = int(values['_slider8_'])

def pwmUpdate():
    window.Element('_pwm1_').Update(int(values['_slider1_']))
    window.Element('_pwm2_').Update(int(values['_slider2_']))
    window.Element('_pwm3_').Update(int(values['_slider3_']))
    window.Element('_pwm4_').Update(int(values['_slider4_']))
    window.Element('_pwm5_').Update(int(values['_slider5_']))
    window.Element('_pwm6_').Update(int(values['_slider6_']))
    window.Element('_pwm7_').Update(int(values['_slider7_']))
    window.Element('_pwm8_').Update(int(values['_slider8_']))

def manualIn():
    window.Element('_pwm1_').Update(values['_motor1in_'])
    window.Element('_pwm2_').Update(values['_motor2in_'])
    window.Element('_pwm3_').Update(values['_motor3in_'])
    window.Element('_pwm4_').Update(values['_motor4in_'])
    window.Element('_pwm5_').Update(values['_motor5in_'])
    window.Element('_pwm6_').Update(values['_motor6in_'])
    window.Element('_pwm7_').Update(values['_motor7in_'])
    window.Element('_pwm8_').Update(values['_motor8in_'])

    window.Element('_slider1_').Update(values['_motor1in_'])
    window.Element('_slider2_').Update(values['_motor2in_'])
    window.Element('_slider3_').Update(values['_motor3in_'])
    window.Element('_slider4_').Update(values['_motor4in_'])
    window.Element('_slider5_').Update(values['_motor5in_'])
    window.Element('_slider6_').Update(values['_motor6in_'])
    window.Element('_slider7_').Update(values['_motor7in_'])
    window.Element('_slider8_').Update(values['_motor8in_'])

def sliderToIn():
    window.Element('_motor1in_').Update(int(values['_slider1_']))
    window.Element('_motor2in_').Update(int(values['_slider2_']))
    window.Element('_motor3in_').Update(int(values['_slider3_']))
    window.Element('_motor4in_').Update(int(values['_slider4_']))
    window.Element('_motor5in_').Update(int(values['_slider5_']))
    window.Element('_motor6in_').Update(int(values['_slider6_']))
    window.Element('_motor7in_').Update(int(values['_slider7_']))
    window.Element('_motor8in_').Update(int(values['_slider8_']))

df = pd.DataFrame({'Temperature:', 'Humidity'})

#defining the columns

#set reset buttons
setreset = [[sg.Button("Set", size=(5,1))], [sg.Button("Reset", size=(5,1))], [sg.Button("Manual", size=(5,1))]]

#Motor columns, slider, input boxes
col1 = [[sg.Text("Motor 1", size = (12,1), justification = 'left')], [sg.Slider(range = (0, 100), key = "_slider1_", orientation = 'v', size = (5, 20), 
default_value = 0, enable_events = True, disable_number_display = True), sg.Text('0', justification = 'center', key = '_pwm1_')], [sg.Input('0', size = (3,1), key = '_motor1in_')]]

col2 = [[sg.Text("Motor 2", size = (12,1), justification = 'left')], [sg.Slider(range = (0, 100), key = "_slider2_", orientation = 'v', size = (5, 20), 
default_value = 0, enable_events = True, disable_number_display = True), sg.Text('0', justification = 'center', key = '_pwm2_')], [sg.Input('0', size = (3,1), key = '_motor2in_')]]

col3 = [[sg.Text("Motor 3", size = (12,1), justification = 'left')], [sg.Slider(range = (0, 100), key = "_slider3_", orientation = 'v', size = (5, 20), 
default_value = 0, enable_events = True, disable_number_display = True), sg.Text('0', justification = 'center', key= '_pwm3_')], [sg.Input('0', size = (3,1), key = '_motor3in_')]]

col4 = [[sg.Text("Motor 4", size = (12,1), justification = 'left')], [sg.Slider(range = (0, 100), key = "_slider4_", orientation = 'v', size = (5, 20), 
default_value = 0, enable_events = True, disable_number_display = True), sg.Text('0', justification= 'center', key= '_pwm4_')], [sg.Input('0', size = (3,1), key = '_motor4in_')]]

col5 = [[sg.Text("Motor 5", size = (12,1), justification = 'left')], [sg.Slider(range = (0, 100), key = "_slider5_", orientation = 'v', size = (5, 20), 
default_value = 0, enable_events = True, disable_number_display = True), sg.Text('0', justification= 'center', key= '_pwm5_')], [sg.Input('0', size = (3,1), key = '_motor5in_')]]

col6 = [[sg.Text("Motor 6", size = (12,1), justification = 'left')], [sg.Slider(range = (0, 100), key = "_slider6_", orientation = 'v', size = (5, 20), 
default_value = 0, enable_events = True, disable_number_display = True), sg.Text('0', justification= 'center', key= '_pwm6_')], [sg.Input('0', size = (3,1), key = '_motor6in_')]]

col7 = [[sg.Text("Motor 7", size = (12,1), justification = 'left')], [sg.Slider(range = (0, 100), key = "_slider7_", orientation = 'v', size = (5, 20), 
default_value = 0, enable_events = True, disable_number_display = True), sg.Text('0', justification= 'center', key= '_pwm7_')], [sg.Input('0', size = (3,1), key = '_motor7in_')]]

col8 = [[sg.Text("Motor 8", size = (12,1), justification = 'left')], [sg.Slider(range = (0, 100), key = "_slider8_", orientation = 'v', size = (5, 20), 
default_value = 0, enable_events = True, disable_number_display = True), sg.Text('0', justification= 'center', key= '_pwm8_')], [sg.Input('0', size = (3,1), key = '_motor8in_')]]

#Sensor Display
sensorCol = [[sg.Text("Temperature:", size = (10, 1), key = '_tempVal_', justification = 'right')], [ sg.Text("Humidity:", size = (10, 1), key = '_humidityVal_', justification = 'right')], [ sg.Text("Wind Speed:", size = (10, 1), key = '_windVal_', justification = 'right')], [sg.Button('Export')]]

layout=[[sg.Col(setreset), sg.Col(col1), sg.Col(col2), sg.Col(col3), sg.Col(col4), sg.Col(col5), sg.Col(col6), sg.Col(col7), sg.Col(col8)],[sg.Col(sensorCol)]]

# Create the window
window=sg.Window("Science Console", layout, size=(1000,600))


# Create an event loop
while True:
    event, values = window.read()

    #updating the values from the slider
    pwmUpdate()
    
    #preparing the pwm values
    pwmInt()
    
    #print(pwm1)

    if event == sg.WIN_CLOSED:
        break

    #send pwm data to microcontroller
    if event == 'Set':
        #update input box
        sliderToIn()
        print("Send PWM packet") # todo: send pwm packet to the approriate motor

    if event == 'Manual':
        #update manual values
        manualIn()


    if event == 'Reset':
        resetAll()
        
window.close()