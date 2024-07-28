import streamlit as st
from openai import OpenAI
from config import personal_api_key

# Add your own OpenAI API key
client = OpenAI(api_key=personal_api_key)

# Hard-coded shirt colors (adjust as needed)
shirt_colors = [
    "cerulean",
    "navy",
    "white",
    "black",
    "gray",
    "dark green",
]


def build_prompt(query, shirt_colors):
    """
    Constructs a prompt for the language model to suggest matching shirt colors
    based on the provided shorts color from the clothes database.
    """
    prompt_template = """
You're a fashion consultant. Based on the given SHORTS COLOR, suggest two matching shirt colors from the closet.
Use only the shirt colors in the closet when making your suggestions and DO NOT repeat colors.

SHORTS COLOR: {shorts_color}

CLOSET: 
{closet}

The two best matching shirt colors for the SHORTS COLOR are
""".strip()
    closet = "\n".join([f"color: {color}" for color in shirt_colors])
    prompt = prompt_template.format(shorts_color=query, closet=closet).strip()
    return prompt


def llm(prompt):
    """Gets a response from the language model based on the prompt."""
    response = client.chat.completions.create(
        model="gpt-4o-mini", messages=[{"role": "user", "content": prompt}]
    )
    return response.choices[0].message.content


def rag(query):
    """Performs a Retrieval-Augmented Generation (RAG) process."""
    prompt = build_prompt(query, shirt_colors)
    answer = llm(prompt)
    return answer


def main():
    """The main function for the Streamlit app."""

    st.title("Fashion Conultant")

    user_input = st.text_input("What color are your shorts?")

    if st.button("Find Matching Shirt Colors"):
        with st.spinner("Processing..."):
            output = rag(user_input)
            st.success("Completed!")
            st.write(output)


if __name__ == "__main__":
    main()
