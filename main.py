from wordcloud import WordCloud
import matplotlib.pyplot as plt

def generate_word_cloud(text):
    # Generate a word cloud image
    wordcloud = WordCloud(width =800, height=400, background_color='white').generate(text)

    # Display the generated image using matplotlib
    plt.figure(figsize=(10, 5))
    plt.imshow(wordcloud, interpolation='bilinear')
    plt.axis('off') #Turn off axis labels
    plt.show()

if __name__ == "__main__":
    #Replace the sample text with your own
    sample_text = """
    Python is an amazing programming language that is widely used for various applications.
    It has a simple syntax and is easy to learn. Python is used in web development, data science,
    artificial intelligence, and many other fields. It has a large and active community that
    contributes to its growth and development.
    """

    generate_word_cloud(sample_text)