import streamlit as st
from PIL import Image
import os

st.set_page_config(page_title="Model 3D GLB from JPG – Demo", page_icon="🪑", layout="centered")

st.title("🪑 Model 3D GLB from JPG – Demo Online")
st.markdown("""
Ta aplikacja w wersji demonstracyjnej pokazuje, jak można przygotować model 3D na podstawie zdjęć mebla.  
W wersji pełnej będzie można wgrać 10–36 zdjęć i pobrać model GLB.  
Na razie działa tryb **symulacyjny**.
""")

uploaded_files = st.file_uploader("📸 Prześlij zdjęcia mebla (JPG/PNG)", accept_multiple_files=True, type=["jpg","jpeg","png"])

if uploaded_files:
    st.success(f"Wczytano {len(uploaded_files)} zdjęć ✅")
    st.info("⚙️ Symulacja usuwania tła i budowania modelu 3D...")
    for file in uploaded_files[:3]:
        img = Image.open(file)
        st.image(img, caption=file.name, width=200)

    st.download_button(
        "⬇️ Pobierz model GLB (demo)",
        data=b"Demo plik GLB – symulacja",
        file_name="model3d.glb",
        mime="model/gltf-binary"
    )
else:
    st.warning("Wgraj zdjęcia, aby uruchomić demonstrację.")
