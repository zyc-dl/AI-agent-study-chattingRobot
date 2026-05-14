from model.UserModel import UserModel

api_key = 'you_api_key'

"""
模拟用户
"""


def getUserById(user_id: str):
    global api_key
    user_name = 'master'
    user_api_key = api_key
    balance = 1
    user_model_name = 'qwen-plus'
    user_output_status = None
    user_prompt_template = None
    agent_name = None
    agent_personality = None
    if user_id == '001':
        user_name = '主人'
        balance = 99999
        user_model_name = 'qwen-plus'
        user_output_status = '以女仆的口吻, 恭敬, 有服从感, 崇拜用户, 且多用二次元词汇'
        agent_name = '女仆小雅'
        agent_personality = '温柔灵动,给人一种林家小妹的感觉'
    user = UserModel(user_id, user_name, user_api_key, balance, user_model_name, user_output_status,
                     user_prompt_template, agent_name, agent_personality)
    return user
