from langchain_huggingface import ChatHuggingFace,HuggingFacePipeline
from dotenv import load_dotenv
import os

os.environ[HF_HOME]="D:/HuggingFace"

llm=HuggingFacePipeline.from_model_id(
    model_id="TinyLlama/TinyLlama-1.1B-Chat-v1.0",
    task="Text-generation",
    pipeline_kwargs=dict(
        temperature=0.5,
        max_new_token=100
        
    )
    
)

model=ChatHuggingFace(llm=llm)
result=model.invoke("What is the capital of India")
print(result.content)