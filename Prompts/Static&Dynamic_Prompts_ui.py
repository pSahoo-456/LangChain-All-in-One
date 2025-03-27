

from langchain_openai import OpenAI,ChatOpenAI
from dotenv import load_dotenv
import streamlit as st
from langchain_core.prompts import PromptTemplate


'''This an example of Static prompts
load_dotenv()

st.header("Research Tool")

user_input=st.text_input('Enter your Prompt')

if st.button('Summarize'):
    result=model.invoke(user_input)
    st.write(result.content)'''
    
#Dynamic prompts
load_dotenv()
model=ChatOpenAI()
st.header("Research Tool")

paper_input=st.selectbox("Select Research Paper Name",["Select...", "Attention is All you Need",
                                                       "BERT:Pre-training of Deep Bidirectional Transformers","GPT-3:Language Models are few-short Learners",
                                                       "Diffusion Models Beat GANs on Image Synthesis"])

style_input=st.selectbox("Select Explanation style",["Beginner-Friendly","Technical","Code-Oriented","Mathematical"])

length_input=st.selectbox("Select Explanation Length",["short(1-2 paragraphs)","Medium(3-5 paragraphs)","Long(Detailed Explanation)"])


#Template
template=PromptTemplate(
    template=""" Please summarize the research paper titled "{paper_input}with the following specifications:
    Explanation Style:{Style_input}
    Explanation Length:{length_input}
    1.Mathematical Explanation:
    -Include relevant mathematical concepts and equations if present in the paper.
    -Explain the mathematical concepts using simple , intuitive code snippets where applicable
    2.Analogies:
    -use relatable analogies to simplyfy complex idea.
    If certain information is not available in the paper , respond with:"Insufficient Information" instead of guessing.
    Ensure the summary is clear , accurate and aligned with the provided style and length.""",

input_variables=["paper_input","Style_input","length_input"],
validate_template=True
)
prompt=template.invoke({   
    'paper_input':paper_input,
    'Style_input':style_input,
    'length_input':length_input
}
)


if st.button('Summarize'):
   result= model.invoke(prompt)
   st.write(result.content)
   
    