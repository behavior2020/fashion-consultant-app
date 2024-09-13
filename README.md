# Fashion Consultant Using RAG!
A Streamlit application that uses OpenAI's GPT-4 to suggest matching shirt colors based on a provided shorts color. The app leverages a language model to act as a fashion consultant, providing users with stylish and compatible outfit combinations.

### Type in the color of the shorts you want to wear today and watch your personal Fashion Consultant suggest matching shirt colors!

<img width="885" alt="Screenshot 2024-07-30 at 18 13 23" src="https://github.com/user-attachments/assets/c81e5c1b-740e-485c-b164-f004620740db">

## Setup

### 1. Clone the repository
```sh
git clone https://github.com/your-repo/fashion-consultant-app.git
cd fashion-consultant-app
pip install -r requirements.txt
```
### 2. Set up the `.env` file
The application requires an OpenAI API key to function. You need to create a `.env` file in the root directory of the project and add your OpenAI API key.

Create a `.env` file and add the following:
```sh
echo 'OPENAI_KEY=your_openai_api_key_here' > .env
```
### 3. Run the app
Start the Streamlit app by running the following command:
```sh
streamlit run app.py
```
### Usage
Type in the color of your shorts and the app will suggest matching shirt colors using the power of GPT-4!
