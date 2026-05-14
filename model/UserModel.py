"""
这个类用来刻画用户形象以及用户的基本信息 TODO: 这部分信息应该从db中获取, 目前py访问db不会, 会了再说先模拟
"""


class UserModel:
    def __init__(self, user_id, user_name, user_api_key, balance, user_model_name='qwen-plus', user_output_status=None,
                 user_prompt_template=None, agent_name=None, agent_personality=None):
        self.user_id = user_id
        self.user_name = user_name
        self.user_api_key = user_api_key
        self.balance = balance
        self.user_model_name = user_model_name
        self.user_output_status = user_output_status
        self.user_prompt_template = user_prompt_template
        self.agent_name = agent_name
        self.agent_personality = agent_personality

    def set_balance(self, balance):
        self.balance = balance
        return self

    def set_user_model_name(self, user_model_name):
        self.user_model_name = user_model_name

    def set_user_output_status(self, user_output_status):
        self.user_output_status = user_output_status
        return self

    def set_user_prompt_template(self, user_prompt_template):
        self.user_prompt_template = user_prompt_template
        return self

    def set_agent_name(self, agent_name):
        self.agent_name = agent_name
        return self

    def set_agent_personality(self, agent_personality):
        self.agent_personality = agent_personality
        return self
