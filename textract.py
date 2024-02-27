import tkinter as tk
from tkinter import filedialog
from PIL import Image, ImageTk
import boto3

def upload_file():
    filename = filedialog.askopenfilename(filetypes=[('Jpg Files', '*.jpg')])
    if filename:
        img = Image.open(filename)
        img = img.resize((450,200))
        img_photo = ImageTk.PhotoImage(img)
        image_label.config(image=img_photo)
        image_label.image = img_photo
        global img_bytes
        img_bytes = get_image_byte(filename)
        display_button.pack()  # Display the "Display Text" button after uploading the image

def display_text():
    aws_con = boto3.session.Session(profile_name='text_user')
    client = aws_con.client(service_name='textract', region_name='ap-south-1')
    response = client.detect_document_text(Document={'Bytes': img_bytes})
    scanned_text = ""
    for item in response['Blocks']:
        if item['BlockType'] == 'LINE':
            scanned_text += item['Text'] + "\n"
    if scanned_text:
        scanned_text_label.config(text="Information in document:",font=('Arial', 10, 'bold'))
        output_label.config(text=scanned_text)
        scanned_text_label.pack()
        output_label.pack()
        upload_another_button.pack()
        switch_to_second_layout()

def get_image_byte(filename):
    with open(filename, 'rb') as imgfile:
        return imgfile.read()

def switch_to_first_layout():
    second_layout_frame.pack_forget()
    first_layout_frame.pack()

def switch_to_second_layout():
    first_layout_frame.pack_forget()
    second_layout_frame.pack()

root = tk.Tk()
root.geometry("550x550")
root.title("AWS Textract")

first_layout_frame = tk.Frame(root)
first_layout_frame.pack()

label_text_extraction = tk.Label(first_layout_frame, text="Analysis of Document", font=('Arial', 16, 'bold'))
label_text_extraction.pack(pady=10)

upload_button = tk.Button(first_layout_frame, text="Select Document for Text Extraction", command=upload_file)
upload_button.pack()

image_label = tk.Label(first_layout_frame, width=400, height=200)
image_label.pack()

display_button = tk.Button(first_layout_frame, text="Display Text", command=display_text)

second_layout_frame = tk.Frame(root)

label_scanned_text = tk.Label(second_layout_frame, text="Document Analysis Results", font=('Arial', 16, 'bold'))
label_scanned_text.pack(pady=10)

scanned_text_label = tk.Label(second_layout_frame, text="", wraplength=450, justify='left', font=('Arial', 10))
scanned_text_label.pack()

output_label = tk.Label(second_layout_frame, text="", wraplength=450, justify='left', font=('Arial', 10))

upload_another_button = tk.Button(second_layout_frame, text="Upload Another File", command=switch_to_first_layout)


root.mainloop()

