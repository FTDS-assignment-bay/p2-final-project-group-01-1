# import libraries
import pandas as pd

# streamlit
import streamlit as st

# wordcloud
from wordcloud import WordCloud

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

    st.image('logo.jpg')

    # section dataframe
    # load dataset
    df = pd.read_csv('D:/p2-final-project-group-01-1/analyst.csv')
    df = df.drop_duplicates()
    df = df.dropna()

    data = pd.read_csv('D:\p2-final-project-group-01-1\data_final.csv')
    
    # Hapus simbol '+' dan tulisan 'terjual' lalu ganti tipe data ke integer
    data['Rating'] = data['Rating'].str.replace('bintang ', '')
    data['Rating'] = data['Rating'].astype(int)

    # subheader
    st.write('## Dataframe')

    # show the dataframe
    st.dataframe(data.head())

    # Section EDA
    # subheader
    st.write('## Exploratory Data Analysis')

    # title
    st.write('### Distribusi Brand Varian')
    
    brand_counts = df['brand'].value_counts()

    # create canvas
    fig = plt.figure(figsize=(15,10))

    plt.pie(brand_counts, labels=brand_counts.index, autopct='%1.1f%%', startangle=90, colors=plt.cm.Paired.colors)
    plt.title('Distribution of Brands')
    plt.axis('equal') 

    # show the plot
    st.pyplot(fig)

    # insight
    st.write('''
                \n- Infinix: 4%
                \n- Xiaomi: 7.7%
                \n- Vivo: 13%
                \n- Asus: 13.8%
                \n- Samsung: 17%
                \n- Realme: 20.2%
                \n- Oppo: 24.3%
             ''')

    # title
    st.write('### Bar Chart')
    st.write('#### Most Sold Brand')

    # Group the data by brand and sum the sold quantities
    brand_sales = df.groupby('brand')['sold'].sum()

    # Plot the bar chart
    fig2 = plt.figure(figsize=(10, 6))
    brand_sales.sort_values().plot(kind='bar', color='skyblue', edgecolor='black')

    # Add titles and labels
    plt.title('Total Sales by Brand', fontsize=16)
    plt.xlabel('Brand', fontsize=12)
    plt.ylabel('Total Sales', fontsize=12)
    plt.xticks(rotation=45, ha='right')  # Rotate brand names for better visibility
    plt.tight_layout()

    # show the plot
    st.pyplot(fig2)

    # insight
    st.write('''
                \n- Xiaomi: 66100
                \n- Vivo: 18135
                \n- Asus: 1957
                \n- Samsung: 37785
                \n- Realme: 6269
                \n- Oppo: 29529
             ''')
    
    # title
    st.write('### Bar Chart')
    st.write('#### Average Price')

    # Group the data by brand and calculate the average price
    average_price_by_brand = df.groupby('brand')['price'].mean()

    # Plot the bar chart
    fig3 = plt.figure(figsize=(10, 6))
    average_price_by_brand.sort_values().plot(kind='bar', color='lightgreen', edgecolor='black')

    # Add titles and labels
    plt.title('Average Price of Products by Brand', fontsize=16)
    plt.xlabel('Brand', fontsize=12)
    plt.ylabel('Average Price', fontsize=12)
    plt.xticks(rotation=45, ha='right')  # Rotate brand names for better visibility
    plt.tight_layout()

     # show the plot
    st.pyplot(fig3)

      # insight
    st.write('''
                \n- Xiaomi: Rp 3.464.789,00
                \n- Vivo: Rp 3.325.562,00
                \n- Asus: Rp 10.307.820,00
                \n- Samsung: Rp 9.472.238,00
                \n- Realme: Rp 10.214.440,00
                \n- Oppo: Rp 4.735.667,00
             ''')
    
    # title
    st.write('### Bar Chart')
    st.write('#### Most Sold Ram')

    # Group the data by brand and calculate the average price
    sold_ram = df.groupby('ram')['sold'].sum()

    # Plot the bar chart
    fig4 = plt.figure(figsize=(10, 6))
    sold_ram.sort_values().plot(kind='bar', color='lightgreen', edgecolor='black')

    # Add titles and labels
    plt.title('Most Sold RAM', fontsize=16)
    plt.xlabel('RAM', fontsize=12)
    plt.ylabel('Units', fontsize=12)
    plt.xticks(rotation=45, ha='right')  # Rotate brand names for better visibility
    plt.tight_layout()

     # show the plot
    st.pyplot(fig4)

     # insight
    st.write('''
                \n- The most sold brand with 8GB RAM is 'samsung' with a total quantity of 21564 units.
             ''')
    
    # title
    st.write('### Bar Chart')
    st.write('#### Most Sold Rom')

    # Group the data by brand and calculate the average price
    sold_rom = df.groupby('rom')['sold'].sum()

    # Plot the bar chart
    fig5 = plt.figure(figsize=(10, 6))
    sold_rom.sort_values().plot(kind='bar', color='lightgreen', edgecolor='black')

    # Add titles and labels
    plt.title('Most Sold ROM', fontsize=16)
    plt.xlabel('ROM', fontsize=12)
    plt.ylabel('Units', fontsize=12)
    plt.xticks(rotation=45, ha='right')  # Rotate brand names for better visibility
    plt.tight_layout()

     # show the plot
    st.pyplot(fig5)

     # insight
    st.write('''
                \n- The most sold brand with 128GB ROM is 'xiaomi' with a total quantity of 66100 units.
             ''')




    # title
    st.write('### WordCloud')
    st.write('#### Rating = 1')

   # Filter rows where rating < 3
    low_rating_reviews = data[data['Rating'] == 1]

    # Combine all review text into a single string
    text_data = " ".join(low_rating_reviews['Review'].dropna().astype(str))

    # Generate the word cloud
    wordcloud = WordCloud(width=800, height=400, background_color='white').generate(text_data)

    # Plot the word cloud
    fig6 = plt.figure(figsize=(10, 5))
    plt.imshow(wordcloud, interpolation='bilinear')
    plt.axis('off')  # Hide the axes for a cleaner look
    plt.title("Word Cloud for Reviews with Rating 1", fontsize=16)
    plt.show()

    # menampilkan plot
    st.pyplot(fig6)

    # insight
    st.write('''
            Words such "tidak", "kurang", "kurir", "proses" are mention in the 1 rating wordclouds. This indicates variety of reasons, often driven by dissatisfaction or frustration with a product or service such as poor product quality or misleading product descriptions.
             ''')
    
    st.write('#### Very Bad')

    st.write('#### Rating = 2')

   # Filter rows where rating < 3
    low_rating_reviews = data[data['Rating'] == 2]

    # Combine all review text into a single string
    text_data = " ".join(low_rating_reviews['Review'].dropna().astype(str))

    # Generate the word cloud
    wordcloud = WordCloud(width=800, height=400, background_color='white').generate(text_data)

    # Plot the word cloud
    fig7 = plt.figure(figsize=(10, 5))
    plt.imshow(wordcloud, interpolation='bilinear')
    plt.axis('off')  # Hide the axes for a cleaner look
    plt.title("Word Cloud for Reviews with Rating 2", fontsize=16)
    plt.show()

    # menampilkan plot
    st.pyplot(fig7)

    # insight
    st.write('''
            Words such "tidak", "barang", "pengiriman", "proses" are mention in the 2 rating wordclouds. This indicates variety of reasons, often driven by dissatisfaction or frustration with a product or service such as poor product quality or misleading product descriptions.
            ''')
    
    st.write('#### Bad')

    st.write('#### Rating = 3')

   # Filter rows where rating < 3
    low_rating_reviews = data[data['Rating'] == 3]

    # Combine all review text into a single string
    text_data = " ".join(low_rating_reviews['Review'].dropna().astype(str))

    # Generate the word cloud
    wordcloud = WordCloud(width=800, height=400, background_color='white').generate(text_data)

    # Plot the word cloud
    fig8 = plt.figure(figsize=(10, 5))
    plt.imshow(wordcloud, interpolation='bilinear')
    plt.axis('off')  # Hide the axes for a cleaner look
    plt.title("Word Cloud for Reviews with Rating 3", fontsize=16)
    plt.show()

    # menampilkan plot
    st.pyplot(fig8)

    # insight
    st.write('''
            Words such "tidak", "kurang", "lama", "proses" are mention in the 3 rating wordclouds. This indicates variety of reasons, often driven by dissatisfaction or frustration with a product or service such as misleading product descriptions, poor customer services, or delivery issues.
            ''')
    
    st.write('#### Bad')

    st.write('#### Rating = 4')

   # Filter rows where rating < 3
    low_rating_reviews = data[data['Rating'] == 4]

    # Combine all review text into a single string
    text_data = " ".join(low_rating_reviews['Review'].dropna().astype(str))

    # Generate the word cloud
    wordcloud = WordCloud(width=800, height=400, background_color='white').generate(text_data)

    # Plot the word cloud
    fig9 = plt.figure(figsize=(10, 5))
    plt.imshow(wordcloud, interpolation='bilinear')
    plt.axis('off')  # Hide the axes for a cleaner look
    plt.title("Word Cloud for Reviews with Rating 4", fontsize=16)
    plt.show()

    # menampilkan plot
    st.pyplot(fig9)

    # insight
    st.write('''
            Words such "bagus", "aman", "barang", "proses" are mention in the 4 rating wordclouds. This indicates variety of reasons, often driven by customer satisfaction with a product or service such as good product quality or fast delivery service.
            ''')
    
    st.write('#### Good')

    st.write('#### Rating = 5')

   # Filter rows where rating < 3
    low_rating_reviews = data[data['Rating'] == 5]

    # Combine all review text into a single string
    text_data = " ".join(low_rating_reviews['Review'].dropna().astype(str))

    # Generate the word cloud
    wordcloud = WordCloud(width=800, height=400, background_color='white').generate(text_data)

    # Plot the word cloud
    fig10 = plt.figure(figsize=(10, 5))
    plt.imshow(wordcloud, interpolation='bilinear')
    plt.axis('off')  # Hide the axes for a cleaner look
    plt.title("Word Cloud for Reviews with Rating 5", fontsize=16)
    plt.show()

    # menampilkan plot
    st.pyplot(fig10)

    # insight
    st.write('''
            Words such "cepat", "aman", "awet", "sesuai", "mantap" are mention in the 5 rating wordclouds. This indicates variety of reasons, often driven by customer satisfaction with a product or service such as good product quality, fast delivery service, value of money, and or user experience.
            ''')
    
    st.write('#### Very Good')

if __name__ == "__main__":
    run()