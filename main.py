import FreeSimpleGUI as sg

label_compressor = sg.Text("Files to compress")
input_compressor = sg.Input()
choose_button1 = sg.FileBrowse("Choose")

label_destination = sg.Text("Destination Folder")
input_destination = sg.Input()
choose_destination = sg.FolderBrowse("Choose")

compress_button = sg.Button("Compress")

layout = [
    [label_compressor, input_compressor, choose_button1],
    [label_destination, input_destination, choose_destination],
    [compress_button]
]

window = sg.Window("SqueezeIt File Compressor", layout=layout)
window.read()
window.close()