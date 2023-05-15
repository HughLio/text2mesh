import streamlit as st
import subprocess
import tempfile
import os

# Set Streamlit app title
st.title("Text to 3D Model with Text2Mesh")

# Streamlit interface to upload mesh
st.header("Upload Mesh")
obj_file = st.file_uploader("Upload OBJ file", type=["obj"])

prompt = st.text_input("Enter prompt")

# Streamlit interface to run Text2Mesh
if st.button("Run Text2Mesh"):
    with tempfile.TemporaryDirectory() as temp_dir:
        output_dir = temp_dir
        n_iter = 750
        st.write("Running Text2Mesh...")
        command = f"python main.py --run branch --obj_path {obj_file.name} --output_dir {output_dir} --prompt \"{prompt}\" --sigma 12.0 --clamp tanh --n_normaugs 4 --n_augs 1 --normmincrop 0.1 --normmaxcrop 0.4 --geoloss --colordepth 2 --normdepth 2 --frontview --frontview_std 4 --clipavg view --lr_decay 0.9 --clamp tanh --normclamp tanh --maxcrop 1.0 --save_render --seed 29 --n_iter {n_iter} --learning_rate 0.0005 --normal_learning_rate 0.0005 --standardize --no_pe --symmetry --background 1 1 1"
        subprocess.run(command, shell=True)
        st.success("Text2Mesh complete")

        # Display the resulting images
        for i in range(0, n_iter, 100):
            img_path = os.path.join(output_dir, f"iter_{i}.jpg")
            if os.path.isfile(img_path):
                st.image(img_path, caption=f"Iteration {i}")
