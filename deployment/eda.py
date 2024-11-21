# import libraries
import pandas as pd

# streamlit
import streamlit as st

# wordcloud
from wordcloud import WordCloud
from wordcloud import STOPWORDS

# Visualization
import matplotlib.pyplot as plt

# Handle Warnings
import warnings
warnings.filterwarnings('ignore')

def run():
    # title
    st.title("Exploratory Data Analysis - Sentiment Analysis Handphone")

    # horizontal line
    st.write("---")

    # section dataframe
    # load dataset
    df = pd.read_csv('D:\p2-final-project-group-01-1\analyst.csv')

    data = pd.read_csv('D:\p2-final-project-group-01-1\data_final.csv')

    # subheader
    st.write('## Dataframe')

    # show the dataframe
    st.dataframe(data.head())

    # Section EDA
    # subheader
    st.write('## Exploratory Data Analysis')

    # title
    st.write('### Distribusi Data')
    
    # create canvas
    fig = plt.figure(figsize=(15,10))

    # Plot the pie chart
    plt.pie(data['status'].value_counts(),labels=data['status'].value_counts().index, autopct='%.2f')

    # show the plot
    st.pyplot(fig)

    # insight
    st.write('''Dari jumlah distribusi data yang dapat dilihat dari grafik pie dan juga value count diketahui bahwa persebaran data sebagai berikut :
                \n- Normal: 30.83% (16,351)
                \n- Depression: 29.04% (15,404)
                \n- Suicidal: 20.08% (10,653)
                \n- Anxiety: 7.33% (3,888)
                \n- Bipolar: 5.42% (2,877)
                \n- Stress: 5.03% (2,669)
                \n- Personality Disorder: 2.26% (1,201)''')

    # title
    st.write('### WordCloud')
    st.write('#### Keseluruhan Data')

    # mengumpulkan kata yang terdapat pada kolom statement
    text = " ".join(str(i) for i in data['statement'])
    # menyiapkan data untuk stopwords
    stopwords = set(STOPWORDS)
    # membuat variable untuk menampung wordcloud
    wordcloud = WordCloud(stopwords=stopwords, background_color="white").generate(text)

    fig = plt.figure(figsize=(15, 10))
    # menapilkan wordcloud
    plt.imshow(wordcloud, interpolation='bilinear')
    # menghapus axis
    plt.axis("off")

    # menampilkan plot
    st.pyplot(fig)

    # insight
    st.write('''Jadi dari keseluruhan data dapat dilihat bahwa kata yang paling banyak digunakan sebagai berikut:
            \n1. feel
            \n2. know, want
            \n3. life
            \n4. now
            \n5. people, think
            \n6. will, time
            \n7. even''')
    
    st.write('#### Normal')

    # mengumpulkan kata yang terdapat pada kolom statement untuk kelas normal
    text = " ".join(str(i) for i in data[data['status']=='Normal']['statement'])
    # menyiapkan data untuk stopwords
    stopwords = set(STOPWORDS)
    # membuat variable untuk menampung wordcloud
    wordcloud = WordCloud(stopwords=stopwords, background_color="white").generate(text)

    # membuat tempat atau plot untuk menampilkan wordcloud
    fig = plt.figure(figsize=(15,10))
    # menapilkan wordcloud
    plt.imshow(wordcloud, interpolation='bilinear')
    # menghapus axis
    plt.axis("off")

    # menampilkan plot
    st.pyplot(fig)

    st.write('''Dari data yang status kesehatan mentalnya adalah normal, kata yang sering digunakan adalah sebagai berikut:
                \n1. want
                \n2. will
                \n3. one''')

    st.write('#### Depression')

    # mengumpulkan kata yang terdapat pada kolom statement untuk kelas depresi
    text = " ".join(str(i) for i in data[data['status']=='Depression']['statement'])
    # menyiapkan data untuk stopwords
    stopwords = set(STOPWORDS)
    # membuat variable untuk menampung wordcloud
    wordcloud = WordCloud(stopwords=stopwords, background_color="white").generate(text)

    # membuat tempat atau plot untuk menampilkan wordcloud
    fig = plt.figure(figsize=(15,10))
    # menapilkan wordcloud
    plt.imshow(wordcloud, interpolation='bilinear')
    # menghapus axis
    plt.axis("off")

    # menampilkan plot
    st.pyplot(fig)

    st.write('''Dari data yang status kesehatan mentalnya adalah depresi, kata yang sering digunakan adalah sebagai berikut:
                \n1. feel
                \n2. want
                \n3. life''')

    st.write('#### Suicidal')

    # mengumpulkan kata yang terdapat pada kolom statement untuk kelas suicidal
    text = " ".join(str(i) for i in data[data['status']=='Suicidal']['statement'])
    # menyiapkan data untuk stopwords
    stopwords = set(STOPWORDS)
    # membuat variable untuk menampung wordcloud
    wordcloud = WordCloud(stopwords=stopwords, background_color="white").generate(text)

    # membuat tempat atau plot untuk menampilkan wordcloud
    fig = plt.figure(figsize=(15,10))
    # menapilkan wordcloud
    plt.imshow(wordcloud, interpolation='bilinear')
    # menghapus axis
    plt.axis("off")

    # menampilkan plot
    st.pyplot(fig)

    st.write('''Dari data yang status kesehatan mentalnya adalah suicidal, kata yang sering digunakan adalah sebagai berikut:
                \n1. want
                \n2. feel
                \n3. life
                \n4. know''')

    st.write('#### Anxiety')

    # mengumpulkan kata yang terdapat pada kolom statement untuk kelas anxiety
    text = " ".join(str(i) for i in data[data['status']=='Anxiety']['statement'])
    # menyiapkan data untuk stopwords
    stopwords = set(STOPWORDS)
    # membuat variable untuk menampung wordcloud
    wordcloud = WordCloud(stopwords=stopwords, background_color="white").generate(text)
    
    # membuat tempat atau plot untuk menampilkan wordcloud
    fig = plt.figure(figsize=(15,10))
    # menapilkan wordcloud
    plt.imshow(wordcloud, interpolation='bilinear')
    # menghapus axis
    plt.axis("off")

    # menampilkan plot
    st.pyplot(fig)

    st.write('''Dari data yang status kesehatan mentalnya adalah abxiety, kata yang sering digunakan adalah sebagai berikut:
                \n1. anxiety
                \n2. feel
                \n3. now, m''')
    
    st.write('#### Stress')

    # mengumpulkan kata yang terdapat pada kolom statement untuk kelas stress
    text = " ".join(str(i) for i in data[data['status']=='Stress']['statement'])
    # menyiapkan data untuk stopwords
    stopwords = set(STOPWORDS)
    # membuat variable untuk menampung wordcloud
    wordcloud = WordCloud(stopwords=stopwords, background_color="white").generate(text)
    
    # membuat tempat atau plot untuk menampilkan wordcloud
    fig = plt.figure(figsize=(15,10))
    # menapilkan wordcloud
    plt.imshow(wordcloud, interpolation='bilinear')
    # menghapus axis
    plt.axis("off")

    # menampilkan plot
    st.pyplot(fig)

    st.write('''Dari data yang status kesehatan mentalnya adalah stress, kata yang sering digunakan adalah sebagai berikut:
                \n1. fell
                \n2. stress
                \n3. time, know''')

    st.write('#### Bi-Polar')

    # mengumpulkan kata yang terdapat pada kolom statement untuk kelas bipolar
    text = " ".join(str(i) for i in data[data['status']=='Bipolar']['statement'])
    # menyiapkan data untuk stopwords
    stopwords = set(STOPWORDS)
    # membuat variable untuk menampung wordcloud
    wordcloud = WordCloud(stopwords=stopwords, background_color="white").generate(text)
    
    # membuat tempat atau plot untuk menampilkan wordcloud
    fig = plt.figure(figsize=(15,10))
    # menapilkan wordcloud
    plt.imshow(wordcloud, interpolation='bilinear')
    # menghapus axis
    plt.axis("off")

    # menampilkan plot
    st.pyplot(fig)

    st.write('''Dari data yang status kesehatan mentalnya adalah bi-polar, kata yang sering digunakan adalah sebagai berikut:
                \n1. feel
                \n2. know, m
                \n3. bipolar''')
    
    st.write('#### Personality Disorder')
    # mengumpulkan kata yang terdapat pada kolom statement untuk kelas personality disorder
    text = " ".join(str(i) for i in data[data['status']=='Personality disorder']['statement'])
    # menyiapkan data untuk stopwords
    stopwords = set(STOPWORDS)
    # membuat variable untuk menampung wordcloud
    wordcloud = WordCloud(stopwords=stopwords, background_color="white").generate(text)
    # membuat tempat atau plot untuk menampilkan wordcloud
    fig = plt.figure(figsize=(15,10))
    # menapilkan wordcloud
    plt.imshow(wordcloud, interpolation='bilinear')
    # menghapus axis
    plt.axis("off")
    # menampilkan plot
    st.pyplot(fig)

    st.write('''Dari data yang status kesehatan mentalnya adalah personality disorder, kata yang sering digunakan adalah sebagai berikut:
                \n1. feel
                \n2. people
                \n3. know
                \n4. thing, AvPD, even
                \n5. time, friend, want, life''')
    st.write('---')
    st.write('''### Kesimpulan''')
    st.write('''Analisis distribusi kata dalam data menunjukkan bahwa kategori gangguan mental memiliki pola bahasa yang berbeda dibandingkan kategori Normal. Kata-kata seperti "feel," "want," dan "life" yang dominan dalam gangguan mental menunjukkan adanya ekspresi emosi mendalam, keinginan yang belum terpenuhi, dan refleksi hidup yang berat. Selain itu, gangguan tertentu seperti Anxiety, Stress, dan Bipolar memperlihatkan pola kesadaran diri pengguna dengan penyebutan langsung kondisi mereka. Kata-kata seperti "know," "time," dan "now" dalam konteks gangguan mental juga mengindikasikan adanya kecenderungan introspeksi dan ketidakpastian terkait waktu atau masa depan.''')
    
if __name__ == "__main__":
    run()