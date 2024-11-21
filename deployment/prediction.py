# import libraries
import streamlit as st
import re
import json
# Handle Warnings
import warnings
warnings.filterwarnings('ignore')

import google.generativeai as genai

genai.configure(api_key="AIzaSyAjLiSDpzE6H50bu2vXgi2Lju-Z2sIxWKI")

model = genai.GenerativeModel("gemini-1.5-flash")

# membuat fungsi untuk melakukan text processing
def clean_text(text):
  # Remove special characters and punctuation
  text = re.sub(r"[^\w\s]", " ", text)

  # Remove single characters
  text = re.sub(r"\b[a-zA-Z]\b", " ", text)

  # Remove HTML tags
  text = re.sub(r"<[^>]*>", " ", text)

  # Lowercase the text
  text = text.lower()

  # Remove extra whitespace
  text = re.sub(r"\s+", " ", text)

  # Trim leading and trailing spaces
  text = text.strip()

  return text

def run():
    # title
    st.title('Sentiment Analysis')

    # horizontal line
    st.write("---")

    st.image('logo.jpg')

    # description
    st.write('''This page will allows user to detect review sentiment''')

    # form
    with st.form(key='form parameter'):
        text = st.text_area('Masukkan text:')       

        submit = st.form_submit_button('Predict')

    # predict
    if submit:
        try:
            texts = clean_text(text)
            prompt = f"""
                    Anda adalah seorang ahli linguistik yang pandai mengklasifikasikan sentimen ulasan pelanggan ke dalam label Positif/Negatif.
                    Bantu saya mengklasifikasikan ulasan pelanggan ke dalam: Positif dan Negatif.
                    Ulasan pelanggan diberikan di antara dua backticks.
                    Dalam output Anda, hanya kembalikan kode Json sebagai output - yang disediakan di antara dua backticks.
                    Tugas Anda adalah memperbarui label yang diprediksi di bawah 'pred_label' dalam kode Json.
                    Hanya memberikan output Positif atau Negatif.
                    Jangan mengubah format kode Json.

                    ```
                    ['"clean_reviews":{texts},"pred_label":""']
                    ```
                    """
            
            response = model.generate_content(prompt)

            # Bersihkan string JSON
            json_data = response.text.replace("`", "").strip().replace('json', '').replace('\n', '')  # Buang backticks dan spasi ekstra

            # Parse JSON dan konversi ke DataFrame
            data = json.loads(json_data)
            first_entry = data[0]

            st.write(f"Text: '{texts}'")
            st.write(f"Predicted Class: {first_entry['pred_label']}")

        except:
            st.write('Terjadi kesalahan coba input ulang.')

if __name__ == "__main__":
    run()