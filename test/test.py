from model.LargeLanguageQwenModel import LargeLanguageModel, invokeByUser
from utils.SimulatedUserUtils import getUserById


def test_01():
    llm = LargeLanguageModel(model_name='qwen-plus', api_key='you_api_key')
    while True:
        input_message = input('请输入')
        print(llm.invoke(input_message))


def test_02():
    user = getUserById('001')
    while True:
        input_message = input('请输入')
        print(invokeByUser(user, input_message))


if __name__ == "__main__":
    test_02()
