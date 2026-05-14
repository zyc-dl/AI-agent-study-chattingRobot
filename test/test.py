from model.LargeLanguageQwenModel import LargeLanguageModel

llm = LargeLanguageModel(model_name='qwen-plus', api_key='you_api_key')

while True:
    input_message = input('请输入')
    print(llm.invoke(input_message))
