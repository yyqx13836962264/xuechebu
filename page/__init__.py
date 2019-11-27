from selenium.webdriver.common.by import By

# 主页面
mine = By.XPATH, '//*[contains(@text, "我的")]'  # 我的

# 我的页面
login = By.XPATH, '//*[contains(@text, "登录")]'  # 登录/注册

# 登录页面
# name = By.XPATH, '//*[contains(@text, "账号")]'  # 账号
name = By.ID, 'com.bjcsxq.chat.carfriend:id/login_phone_et'  # 账号
# pwd = By.XPATH, '//*[contains(@text, "密码")]'  # 密码
pwd = By.ID, 'com.bjcsxq.chat.carfriend:id/login_pwd_et'  # 密码
login_btn = By.ID, 'com.bjcsxq.chat.carfriend:id/login_btn'  # 登录按钮
com_btn = By.XPATH, '//*[contains(@text, "确定")]'  # 登录提示框确定按钮
