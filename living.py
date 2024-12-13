import streamlit as s
from PIL import Image
img=Image.open('hello.jpg')
s.set_page_config(page_icon=img,page_title='LIVING DREAM GROUP')
s.title('We Will Back Soon ! 🦉')
