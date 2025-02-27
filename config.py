class Config:
    # MySQL 配置
    SQLALCHEMY_DATABASE_URI = 'mysql+pymysql://webdemoAdmin:Admin,123@localhost/webdemo'
    SQLALCHEMY_TRACK_MODIFICATIONS = False  # 禁用事件系统，避免警告

    # Flask 配置
    SECRET_KEY = 'webDemoSecretKey'  # 用于加密会话数据
    DEBUG = True  # 开启调试模式
    TESTING = False  # 不开启测试模式