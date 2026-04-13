import streamlit as st
from dotenv import load_dotenv
load_dotenv()

import google.generativeai as genai
from PIL  import Image


st.set_page_config('DEFECT AI',page_icon='🤖',layout='wide')

st.title("AI POWERED DEFECT ANALYZER🤖🧠🇦🇮👾")
st.header(":blue[Prototype of automated structural defect analyzer using AI] 🎯")
st.subheader(f" :red[AI powered structural defect analysis using Streamlit that allows users to upload the image of any structural defects and to get suggestions and recommendations for repair and rebuilt]🚀")


with st.expander(' ➤ About the app'):
    st.markdown(f'''This app helps to detect the defects like cracks, misalligments etc and provide 
                - **Defect Detection**
                - **Recommendation**
                - **Suggestions for improvements** ''')
    
import os

key = os.getenv('GOOGLE_API_KEY')

genai.configure(api_key=key)

input_image = st.file_uploader('Upload your file here ➤', 
                               type =['png','jpeg','jpg'])


img = ''

if input_image:
    
    img = Image.open(input_image).convert('RGB')
    st.image(img, caption="Uploaded Successfully ✅️ ")
    
    
    
prompt = f'''You are an quality engineer and civil engineer. You need to 
analyze the input image and provide neccessary details for the below given quetsions
in bullet points (max 3 points for each questions)

1. Identify the type of structural defect in the given image like cracks, bends,misalligements etc
2. What is the probability of damages caused by the defect detected
3. What is the severity level of the defect as minor, moderate, major 
4. What is the possible causage of the defect considering the material damages, environmental damage 
5. Say whether we can repair the defect or not ? It yes Provide the suggestions
6. Suggest any remedies to be done immediately
7. Say whether the defect cause any damage to the surrouding area? If yes say the probability
8. Say whether we need to monitor this damage ? If yes how long we need to 
9. Give me materials needs to repair this defect
10. Give me repairing cost in Indian Rupees'''

model = genai.GenerativeModel('gemini-2.5-flash')

def generate_result(prompt, img):
    
    result = model.generate_content(f'''Using the given {prompt} 
                           and given image {img}
                           analyze the image and give the
                           results as per the given prompt''')
    
    return result.text

submit = st.button('Analyze the image 🎯')

if submit:
    with st.spinner('Results Loading....👩🏻‍💻'):
        response = generate_result(prompt, img)
        
        st.markdown('## :green[Results]')
        st.write(response)



