# Python library used in this code 
import qrcode as qr
import PySimpleGUI as sg 
import os 
# setup the theme 
sg.theme('Material2')
font =('Verdana', 12)
# Object orientated of the methode image 
qr_image = [sg.Image('', key = 'QRCODE')]

# the layout of the application  
index = 0
index_1= 1
color = {0: ("Salmon", "Teal"), 1: ("white", "Navy")}
layout = [
    [sg.Text('Enter URL:'), sg.Input(text_color= 'black', key= 'URL', font = ('Times') )],
    [sg.Button('Create', key='Submit',  mouseover_colors= color[index], use_ttk_buttons=True, size= (7,1)),  sg.Button('Close', key='CLOSE',mouseover_colors= color[index_1], use_ttk_buttons=True, size= (7,1))],
    [sg.Column([qr_image], justification= 'center')],
]

 # Create the Window
window = sg.Window('QR coode Generator', layout, font= font)

# Event loop  
while True:
    # close windows loop 
    event , values = window.read()
    if event == sg.WIN_CLOSED or event == 'CLOSE':
        break
    # Event manipulation 
    elif event == 'Submit':
        url = values['URL']
        if url:
            qr_code = qr.QRCode(
                version=1,
                error_correction=qr.constants.ERROR_CORRECT_L,
                box_size=20,
                border=4,
                )
            qr_code.add_data('Some data')
            qr_code.make(fit=True)
            img = qr_code.make_image(fback_color=(128, 0, 0), fill_color=(222, 49, 99))
            file_name= 'qr_code'+'.png'
            path = os.path.join(os.getcwd(), file_name)
            img.save(path)
            window['QRCODE'].update(file_name)
window.close()