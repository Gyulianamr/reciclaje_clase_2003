import json
from pathlib import Path
import numpy as np
import streamlit as st
import tensorflow  as tf
from PIL import Image

st.set_page_config(page_title="Reciclaje IA-ISC", layout="centered")
st.title("Modelo predictivo de reciclaje clase de IA-ISC-campus Comayagua-2026-Genesis Medina")
st.write("Suba una imagen para clasificar con el modelo MobileNetV2 pre-entrenada")


