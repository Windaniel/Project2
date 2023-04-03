import PySimpleGUI as sg
import pyttsx3 as pt

# Set a theme for the app
sg.theme('DarkTeal5')
font= ('Times', 12)
# the app layout.
index = 1
index_1= 0
color = {0: ("LightCoral", "Olive"), 1: ("DarkSalmon", "Lime")}
layout = [
    [sg.Text(''), sg.Input(text_color= 'Black', key= 'INPUT', font= "Times" ), sg.Button('Speak', key='LISTENER',  mouseover_colors=color[index], use_ttk_buttons=True, size= (7,1)), sg.Text(), sg.Button('Close', key='close',  mouseover_colors=color[index_1], use_ttk_buttons=True, size= (7,1))],
    [sg.Text('Select voice type:'), sg.Radio("Male", "RADIO", default= True, key='MALE'),sg.Radio('Female', 'RADIO', default = False, key ='FEMALE' )],
    [sg.Text( key= 'RESULT')],
]

# Create the Window
window = sg.Window('Text to Speech App', layout, font= font )

# Event loop
while True:
    event , values = window.read()
    if event == sg.WIN_CLOSED or event == 'close':
        break
    elif event == 'LISTENER':
        Text = str(values['INPUT'])
        eng = pt.init() # Initialise the instance
        eng.setProperty('rate', 180)
        eng.setProperty('volume',2.0)
               
        voice = eng.getProperty('voices') # get the available voice 
        Male = values['MALE']
        Female= values['FEMALE']
        # setup voice choice between male and female 
        if Male:
            eng.setProperty('voice', voice[0].id) # for male voices' the index 0 
        elif Female :
            eng.setProperty('voice', voice[1].id) #  for female voices' the index 1 
        result = eng.say(Text)    
        eng.runAndWait()
        window['RESULT'].update(result)
window.close()
