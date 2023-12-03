import streamlit as st
from langchain.llms import GooglePalm
from langchain.prompts import PromptTemplate
import requests
import io
from PIL import Image
from pytrends.request import TrendReq

# AIzaSyDnA2sHb-KnieA-7l24NVfuQuRe9xg6SrA
# Split content into sections
def divide_content(content):
    # Split the content into sections based on the specified headers
    sections = {
        "Title": "",
        "Abstract": "",
        "Introduction": "",
        "History": "",
        "Content": "",
        "Conclusion": "",
        "References": "",
        "Further Reading": ""
    }

    current_section = None  # Title, Introduction, Conclusion
    for line in content.splitlines():
        # Check if the line is a header
        if line.startswith("##"):
            # Extract the header name and strip leading/trailing whitespaces
            header_line = line[2:].strip()
            # Handle an additional colon after the header
            if ':' in header_line:
                current_section = header_line.split(':', 1)[0].strip()
            else:
                current_section = header_line
        elif current_section is not None:
            # Append the line to the current section
            sections.setdefault(current_section, "")  # Ensure the key exists
            sections[current_section] += line + "\n"
 
    return sections


# Image Generation
API_URL = "https://api-inference.huggingface.co/models/goofyai/3d_render_style_xl"
headers = {"Authorization": "Bearer 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"}

def query(payload):
	response = requests.post(API_URL, headers=headers, json=payload)
	return response.content


# SEO Keywords
def get_seo_keywords(topic, timeframe='today 5-y', geo='US'):
    pytrends = TrendReq(hl='en-US', tz=360)

    # Build payload
    pytrends.build_payload([topic], cat=0, timeframe=timeframe, geo=geo, gprop='')
    # Get related queries
    related_queries_dict = pytrends.related_queries()
    # Extract top queries from the dictionary
    top_queries = related_queries_dict[topic]['top']
    # Get only the top five query names
    top_five_queries = top_queries['query'].head(5).tolist()

    return top_five_queries



# Streamlit App

# Page Config
st.set_page_config(page_title='📝 AI Text and Image Generation', page_icon='📝', layout='wide', initial_sidebar_state='auto')


# Title
st.sidebar.title('📝 AI Blog Writer')



# Sidebar
st.sidebar.write('This app generates a blog post about a topic of your choice. The app generates the blog post using the Google Palm Language Model. The text generated using SEO Keywords Optimization .The app also generates images using the 3D Render Style XL model. The app is powered by Hugging Face and Streamlit.')
st.sidebar.caption('Made by [Abdalrahman Ali Elnashar](https://www.linkedin.com/in/abdalrahman-ali-el-nashar)')
st.sidebar.divider()
palm_api_key = st.sidebar.text_input('Enter your Google API Key:', key='PaLM_api_key', type='password')
st.sidebar.link_button('Get Google PaLM API key', url='https://makersuite.google.com/app/apikey')

#st.sidebar.write("[Get Google PaLM API key](https://makersuite.google.com/app/apikey)")



# Main Page
col1, col2, col3 = st.columns((1, 3, 1), gap='large')
with col2:

    st.title('🦜🔗 AI Blog Writer using SEO')

    with st.form('myform'):
        st.header('What is the topic of your blog post?')
        topic_text = st.text_input('Topic:', placeholder='Example: Generative AI')
        submitted = st.form_submit_button('Submit')
    

    if submitted:
        if not palm_api_key:
            st.error('Please enter your Google API key in the sidebar.')
            st.stop()
        
        try:
            st.write('Generating blog post about', topic_text, '...')
            st.write('This may take a few minutes.')

            # SEO Keywords
            topic_query = topic_text
            try:
                seo_keywords = get_seo_keywords(topic_query)
            except:
                seo_keywords = ["No keywords found"]


            # LLMS
            palm = GooglePalm(google_api_key='AIzaSyDnA2sHb-KnieA-7l24NVfuQuRe9xg6SrA', temperature=0.6)

            # PromptTemplate
            PT_topic = PromptTemplate(
                template="Generate a blog post about {topic}. The blog format must contain the following sections: Title, Abstract, Introduction, History, Content, Conclusion, References, and Further Reading. Each section must start with '##'.\
                Expand the content of the Abstract and Introduction \
                the number of words of Introduction section should be about 100 words. \
                the blog post should be SEO optimized for the following keywords: {seo_keywords}.",
                input_variables= ['topic'])

            prompt = PT_topic.format(topic=topic_text, seo_keywords=seo_keywords)

            # Palm
            result = palm(prompt)
            blog = divide_content(result)
            
            # -------------------------------------

            # Streamlit Display

            # Title
            title = None
            for line in result.splitlines():
                if line.startswith("## Title"):
                    title = line[10:]
                    if len(title) == 0:
                        title = topic_text + " Blog Post"
                    else:
                        pass
            st.header(title)

            # Abstract
            st.write(blog['Abstract'])
            try:
                image_prompt = blog['Abstract'].splitlines()[1]
            except:
                image_prompt = blog['Abstract'].splitlines()[0]
            image_bytes = query({
                "inputs": image_prompt,
                })
            image = Image.open(io.BytesIO(image_bytes))
            st.image(image=image, use_column_width=True)
            st.divider()
        
            # Introduction
            intro = blog['Introduction'].split('\n\n')
            col1, col2 = st.columns(2, gap='medium')
            with col1:
                st.header('Introduction')
                if len(intro) == 1:
                    st.write(intro[0])
                elif len(intro) == 2:
                    st.write(intro[0])
                    st.write(intro[1])
                elif len(intro) == 3:
                    st.write(intro[0])
                    st.write(intro[1])
                    st.write(intro[2])
                else:
                    st.write(intro[0])
                    st.write(intro[1])
                    st.write(intro[2])        

            with col2:
                try:
                    image_prompt = blog['Introduction'].splitlines()[1]
                except:
                    image_prompt = blog['Introduction'].splitlines()[0]
                
                image_bytes = query({
                    "inputs": image_prompt,
                })
                image = Image.open(io.BytesIO(image_bytes))
                st.image(image=image, use_column_width=True)
                
            # History
            st.header('History')
            st.write(blog['History'])

            # Content
            st.header('Main Content')            
            st.write(blog['Content'])
            try:
                image_prompt = blog['Content'].splitlines()[1]
            except:
                image_prompt = blog['Content'].splitlines()[0]
            
            image_bytes = query({
                "inputs": image_prompt,
            })
            image = Image.open(io.BytesIO(image_bytes))
            st.image(image=image, use_column_width=True)
            
                
            # Conclusion
            st.header('Conclusion')
            st.write(blog['Conclusion'])

            # References
            st.header('References')
            st.write(blog['References'])

            # Further Reading
            st.header('Further Reading')
            st.write(blog['Further Reading'])
        
        except:
            st.error('Something went wrong. Please try again.')
            st.stop()
# End of App
