import streamlit as st
import trimesh
import argparse
#import cv2
import os
import matplotlib.pyplot as plt
import importlib
import PIL
from IPython.display import display, HTML
import subprocess


st.title("Text to 3D Model with Text2Mesh")

# Function to remesh input mesh


# Streamlit interface to upload and remesh mesh
st.header("Upload and Remesh Mesh")
obj_file = st.file_uploader("Upload OBJ file", type=["obj"])
if obj_file is not None:
        # Save the uploaded file
        file_path = os.path.join("./input_obj/", obj_file.name)
        with open(file_path, "wb") as f:
            f.write(obj_file.getvalue())
        
        st.success("File saved successfully!")
prompt = st.text_input("Enter prompt")
#n_iter = st.number_input("Enter number of iterations", min_value=1, value=750, step=1)
#remeshed_path = obj_path
#st.success("Remeshing complete")

# Streamlit interface to run text2mesh
if st.button("Run Text2Mesh"):
#if os.path.isfile(file_path):
    output_dir = "results/"
    st.write("Running Text2Mesh...")
    n_iter=750
    command = ["python", "main.py", "--run", "branch", "--obj_path", file_path, "--output_dir", output_dir, "--prompt", prompt, "--sigma", "12.0", "--clamp", "tanh", "--n_normaugs", "4", "--n_augs", "1", "--normmincrop", "0.1", "--normmaxcrop", "0.4", "--geoloss", "--colordepth", "2", "--normdepth", "2", "--frontview", "--frontview_std", "4", "--clipavg", "view", "--lr_decay", "0.9", "--clamp", "tanh", "--normclamp", "tanh", "--maxcrop", "1.0", "--save_render", "--seed", "29", "--n_iter", str(n_iter), "--learning_rate", "0.0005", "--normal_learning_rate", "0.0005", "--standardize", "--no_pe", "--symmetry", "--background", "1", "1", "1"]
    subprocess.run(command, check=True)
    st.success("Text2Mesh complete")
'''
# Streamlit interface to display results
st.header("Display Results")
if os.path.isdir(output_dir):
    frames = []
    for i in range(0, n_iter, 100):
        img = cv2.imread(os.path.join(output_dir, f"iter_{i}.jpg"))
        frames.append(img)
        plt.figure(figsize=(20, 4))
        plt.imshow(cv2.cvtColor(img, cv2.COLOR_BGR2RGB))
        plt.axis("off")
        plt.title(f"Iteration {i}")
        st.pyplot()
else:
    st.warning("No output directory found.")'''
