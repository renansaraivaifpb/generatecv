# langchain_pipeline.py
from langchain_openai import OpenAI
from langchain_core.prompts import ChatPromptTemplate
from langchain_core.output_parsers import StrOutputParser
from langchain_core.runnables import RunnableMap
import os

api_key = "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"  # Ou substitua diretamente pela chave

llm = OpenAI(temperature=0.7, api_key=api_key)

# Prompts
step_one = ChatPromptTemplate.from_template("Translate the following resume to English:\n\n{Resume}") | llm | StrOutputParser()
step_two = ChatPromptTemplate.from_template("Improve this resume:\n\n{English_Resume}") | llm | StrOutputParser()
step_three = ChatPromptTemplate.from_template("Choose two main programming languages for this resume:\n\n{Resume_improved}") | llm | StrOutputParser()
step_four = ChatPromptTemplate.from_template(
    "Write technical skills for the following resume, based on the selected languages:\n\nResume:\n{Resume_improved}\n\nLanguages:\n{languages}"
) | llm | StrOutputParser()

# Pipeline
chain = (
    RunnableMap({"Resume": lambda x: x["Resume"]})
    | RunnableMap({
        "English_Resume": step_one,
        "Resume": lambda x: x["Resume"]
    })
    | RunnableMap({
        "Resume_improved": step_two,
        "English_Resume": lambda x: x["English_Resume"],
        "Resume": lambda x: x["Resume"]
    })
    | RunnableMap({
        "languages": step_three,
        "Resume_improved": lambda x: x["Resume_improved"],
        "English_Resume": lambda x: x["English_Resume"]
    })
    | RunnableMap({
        "Resume_final": step_four,
        "Resume_improved": lambda x: x["Resume_improved"],
        "languages": lambda x: x["languages"],
        "English_Resume": lambda x: x["English_Resume"]
    })
)

def process_resume(resume_text):
    return chain.invoke({"Resume": resume_text})
