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
        command = [
             "python",
             "main.py",
             "--run",
             "branch",
             "--obj_path",
             obj_file,
             "--output_dir",
             output_dir,
             "--prompt",
             prompt
         ]

        # Run the command using subprocess
        subprocess.run(command, check=True)
        st.success("Text2Mesh complete")

        # Display the resulting images
        for i in range(0, n_iter, 100):
            img_path = os.path.join(output_dir, f"iter_{i}.jpg")
            if os.path.isfile(img_path):
                img = cv2.imread(img_path)
                st.image(img, caption=f"Iteration {i}")
