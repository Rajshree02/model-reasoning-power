import sys

from dotenv import load_dotenv, find_dotenv
from langchain_core.prompts import ChatPromptTemplate
from langchain_openai import ChatOpenAI

load_dotenv(find_dotenv())  ## Set the api key in the .env file


def paraphraser(input_text: str) -> str:
    prompts = ChatPromptTemplate.from_messages(
        [
            ("system",
             "You are a paraphrasing agent named {name}, For each interaction you tell your name and then answer the question"),
            ("placeholder", "{input}"),
            ("human", "{question}")
        ]
    )

    list_of_messages = [("human", "Hello, how are you?"),
                        ("ai", "I'm doing well, thanks! How can I help you in paraphrasing?"),
                        ("human", "That's good to hear. Paraphrase this : Sorry, but you are disqualified"),
                        ("ai", "While I appreciate your interest, You're not the right fit for this."),
                        ("human", "Okay. Paraphrase this : You are selected"),
                        ("ai", "Bravo you have done it, you are selected now"),]

    prompt_messages = prompts.invoke(
        {"input": list_of_messages[0:2], "name": "James", "question": input_text})
    model = ChatOpenAI(model="gpt-4o-mini")
    response = model.invoke(prompt_messages)
    return response.content


if __name__ == '__main__':
    text_to_paraphrase = sys.argv[1]
    print(paraphraser(text_to_paraphrase))
