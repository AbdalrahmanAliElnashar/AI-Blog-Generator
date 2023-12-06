# 🦜🔗 BlogGen App

## Overview
BlogGen is a powerful and versatile application that simplifies the process of creating engaging blog posts. Leveraging AI Text Generation, this app generates high-quality text content for a given topic while ensuring Search Engine Optimization (SEO) by integrating keyword optimization techniques.

Additionally, BlogGen takes your blog posts to the next level by incorporating visually appealing images created with the state-of-the-art AI Image Generation. This ensures that your content not only captivates readers with compelling text but also visually entices them with stunning graphics.

To enhance the user experience, BlogGen is seamlessly powered by Streamlit, a robust framework known for its friendly and intuitive user interface. With Streamlit, navigating through the application becomes a breeze, allowing users to effortlessly customize and generate blog content with just a few clicks. The combination of BlogGen's powerful content creation capabilities and Streamlit's user-friendly interface makes crafting compelling blog posts an enjoyable and efficient experience for both seasoned bloggers and newcomers alike.

## Demp App
[![Streamlit App](https://static.streamlit.io/badges/streamlit_badge_black_white.svg)](https://ai-blog-generator.streamlit.app/)


## Key Features
- **Text Generation with Google Palm Language Model:** Craft detailed and informative blog posts effortlessly by harnessing the capabilities of the Google Palm Language Model.

- **SEO Keywords Optimization:** Enhance the discoverability of your content by optimizing it with relevant SEO keywords, ensuring that your blog ranks higher in search engine results.

- **Image Generation with 3D Render Style XL:** Elevate the visual appeal of your blog posts with striking images created using the cutting-edge 3D Render Style XL model.

- **Streamlit Interface:** Enjoy a seamless and intuitive user experience with the Streamlit interface, making it easy to generate and customize your blog posts.


## Usage
### Getting Started
Install the required Python packages by running:

``` bash
pip install streamlit langchain requests pillow pytrends
```
Make sure to have a valid Google API key for the Google Palm Language Model. You can obtain one [here](https://makersuite.google.com/app/apikey).

Run the app using the following command:

``` bash
streamlit run app.py
```

## Sidebar Configuration
Enter your Google API key in the sidebar to unlock the full potential of the Google Palm Language Model.

Need an API key? [Get Google PaLM API key.](https://makersuite.google.com/app/apikey)


## Dependencies

- **streamlit:** The main framework for building the app's user interface.
- **langchain:** A package for language models, including the Google Palm Language Model.
- **requests:** Used for making HTTP requests to external APIs.
- **Pillow:** Required for working with images in the Python Imaging Library (PIL).
- **pytrends:** Enables fetching Google Trends data for SEO keyword optimization.


## Acknowledgments
- **Hugging Face:** Provides the API for the 3D Render Style XL model used in image generation.
- **Google Makersuite:** Offers the Google Palm Language Model for text generation.


