import streamlit as st
from PIL import Image
import cv2
import os
from vehicle_detector import detect_vehicles

st.set_page_config(page_title="Vehicle Detection", page_icon="🚗")

st.title("🚗 Vehicle Detection using YOLOv8")
st.write("Upload an image to detect vehicles.")

uploaded_file = st.file_uploader(
    "Choose an Image",
    type=["jpg", "jpeg", "png"]
)

if uploaded_file is not None:

    # Create uploads folder if it doesn't exist
    os.makedirs("uploads", exist_ok=True)

    image_path = os.path.join("uploads", uploaded_file.name)

    # Save uploaded image
    with open(image_path, "wb") as f:
        f.write(uploaded_file.getbuffer())

    st.subheader("Original Image")
    st.image(image_path, use_container_width=True)

    # Detect vehicles
    result_image, vehicle_count = detect_vehicles(image_path)

    st.subheader("Detected Image")

    # Convert BGR to RGB
    result_image = cv2.cvtColor(result_image, cv2.COLOR_BGR2RGB)

    st.image(result_image, use_container_width=True)

    st.success(f"Total Vehicles Detected: {vehicle_count}")