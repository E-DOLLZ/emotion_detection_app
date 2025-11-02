import streamlit as st
import os
from model import detect_emotion

os.makedirs("data", exist_ok=True)

st.title("😎 Emotion Detection App")
st.write("Upload an image to detect emotions.")

uploaded_file = st.file_uploader("Upload an image", type=["jpg","jpeg","png"])

if not uploaded_file:
    st.info("Please upload an image.")
else:
    image_path = os.path.join("data", uploaded_file.name)
    with open(image_path, "wb") as f:
        f.write(uploaded_file.getbuffer())
    st.image(image_path, caption="Uploaded Image", use_column_width=True)

    try:
        result = detect_emotion(image_path)
    except Exception as e:
        st.error(f"Error detecting emotion: {e}")
        result = None

    if result:
        emotion = result["dominant_emotion"]
        confidence = max(result["scores"].values())
        st.success(f"Detected Emotion: {emotion.upper()} ({confidence:.2f})")
    else:
        st.warning("No face detected or error occurred.")
