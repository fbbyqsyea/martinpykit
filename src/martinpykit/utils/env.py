import os
from dotenv import load_dotenv


class EnvConfig:
    """动态读取环境变量配置"""

    def __init__(self, env_file: str = ".env"):
        """初始化时加载 .env 文件"""
        self.env_file = env_file
        self._load_env()

    def _load_env(self):
        """加载 .env 文件中的环境变量"""
        load_dotenv(self.env_file)

    def __getattr__(self, name):
        """动态获取环境变量的值"""
        value = os.getenv(name.upper())  # 将属性名转换为大写，匹配环境变量名
        if value is not None:
            return value
        else:
            raise AttributeError(f"env {name} not defined")
