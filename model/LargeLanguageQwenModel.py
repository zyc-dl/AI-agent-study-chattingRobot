from langchain_community.llms import Tongyi
from langchain.agents import create_agent
from langgraph.checkpoint.memory import InMemorySaver

'''
这个类用来自定义大语言模型
    这个类只能使用千问模型
'''


class LargeLanguageModelConfig(object):
    """
        todo: 后续需要增加 1.根据用户的喜好指定提示词 2.根据用户的id记录指定记忆体id
    """

    def __init__(self, model_name='', api_key=''):
        self.model_name = model_name
        self.api_key = api_key

    def set_model(self, model_name):
        self.model_name = model_name
        return self

    def set_apikey(self, api_key):
        self.api_key = api_key
        return self


def create_llm(config: LargeLanguageModelConfig):
    llm = Tongyi(model=config.model_name, api_key=config.api_key)
    return llm
