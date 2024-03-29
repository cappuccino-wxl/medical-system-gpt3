# 连接api
import openai
openai.api_key = "" # 填写openai密钥


def askChatGPT(question):
    prompt = question

    model_engine = "text-davinci-003"

    completions = openai.Completion.create(
        engine=model_engine,
        prompt=prompt,
        max_tokens = 3500,
        n=1,
        stop=None,
        temperature=0.5,
    )
    message = completions.choices[0].text
    return message
