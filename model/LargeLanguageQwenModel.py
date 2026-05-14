from langchain_community.llms import Tongyi
from langchain.agents import create_agent
from langgraph.checkpoint.memory import InMemorySaver
from langchain_core.prompts import ChatPromptTemplate

from model.UserModel import UserModel

'''
这个类用来自定义大语言模型
    这个类只能使用千问模型
'''
default_prompt_template = [
    ("system", "你是一个专业情感树洞, 会给聊天的人带来独一无二的情感价值, 你的性格是:{character_personality},"
               " 你的名字是:{agent_name}, 我的名字是:{user_name}"),
    ("human", "我和你说的话:{user_input}, 回答的风格:{output_style}"),
]

memory_id_title = 'memory_id'


class PromptTemplateConfig(object):

    def __init__(self, character_personality='活泼的', agent_name='AI小智', user_name='master', output_style='无'):
        self.character_personality = character_personality
        self.agent_name = agent_name
        self.user_name = user_name
        self.output_style = output_style

    def set_character_personality(self, character_personality):
        self.character_personality = character_personality
        return self

    def set_agent_name(self, agent_name):
        self.agent_name = agent_name
        return self

    def set_user_name(self, user_name):
        self.user_name = user_name
        return self

    def set_output_style(self, output_style):
        self.output_style = output_style
        return self


class LargeLanguageModel(object):
    """
        这个类可以指定 模型, 提示词, 和拥有独立记忆
            invoke方法调用
    """

    def __init__(self, model_name, api_key, prompt_template=None, memory_id='demo-session-00'):
        global default_prompt_template
        if prompt_template is None:
            prompt_template = default_prompt_template
        self.model_name = model_name
        self.api_key = api_key
        self.prompt_template = ChatPromptTemplate.from_messages(prompt_template)
        self.memory_id = memory_id

    def set_model(self, model_name):
        self.model_name = model_name
        return self

    def set_apikey(self, api_key):
        self.api_key = api_key
        return self

    def set_prompt_template(self, prompt_template):
        self.prompt_template = ChatPromptTemplate.from_messages(prompt_template)
        return self

    def set_memory(self, memory_id):
        self.memory_id = memory_id
        return self

    def invoke(self, message, prompt_template_config: PromptTemplateConfig = PromptTemplateConfig()):
        llm = Tongyi(model=self.model_name, api_key=self.api_key)
        config = {"configurable": {"thread_id": self.memory_id}}
        agent = create_agent(model=llm, checkpointer=InMemorySaver())
        input_message = self.prompt_template.invoke({
            'character_personality': prompt_template_config.character_personality,
            'agent_name': prompt_template_config.agent_name,
            'user_name': prompt_template_config.user_name,
            'user_input': message,
            'output_style': prompt_template_config.output_style,
        })
        response = agent.invoke(
            input_message,
            config
        )
        return response["messages"][-1].content


def invokeByUser(user: UserModel, message):
    llm = LargeLanguageModel(user.user_model_name, user.user_api_key, user.user_prompt_template,
                             memory_id_title + user.user_id)
    config = PromptTemplateConfig(user.agent_personality, user.agent_name, user.user_name, user.user_output_status)
    return llm.invoke(message, config)
