from decouple import config
from openai import OpenAI
import streamlit as st
from closet import clothes

# Read the "OPENAI_KEY" value from .env file and store it in the OPENAI_KEY variable.
OPENAI_KEY = config("OPENAI_KEY")
client = OpenAI(api_key=OPENAI_KEY)


def build_prompt(query, closet):
    """
    Constructs a prompt for the language model to suggest matching shirt colors
    based on the provided shorts color from the clothes database.
    """
    closet_str = " ".join(
        [f"{item['color']} {item['style']} - {item['type']}".title() for item in closet]
    )
    prompt = f"""
You're a fashion consultant. Based on the given SHORTS COLOR, suggest two matching items from the CLOSET.
Ensure the two items in the CLOSET match well in color. Ensure the two items show in the format COLOR STYLE - TYPE.
Use only items in the CLOSET when making your suggestions and DO NOT repeat items.

SHORTS COLOR: {query}

CLOSET: 
{closet_str}

The two best matching outfits for your {query} shorts are:
1. [Shirt 1]
2. [Shirt 2]

These colors complement {query} nicecly, creating a 
""".strip()

    return prompt


def llm(prompt):
    """Gets a response from the language model based on the prompt."""
    response = client.chat.completions.create(
        model="gpt-4o-mini", messages=[{"role": "user", "content": prompt}]
    )
    return response.choices[0].message.content


def rag(query):
    """Performs a Retrieval-Augmented Generation (RAG) process."""
    prompt = build_prompt(query, clothes)
    answer = llm(prompt)
    return answer


def main():
    """The main function for the Streamlit app."""

    st.title("Fashion Conultant")

    user_input = st.text_input("What color are your shorts?")

    if st.button("Find Matching Outfit"):
        with st.spinner("Processing..."):
            output = rag(user_input)
            st.success("Completed!")
            st.write(output)


if __name__ == "__main__":
    main()
