from langchain_core.prompts import PromptTemplate

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

template.save("template.json")