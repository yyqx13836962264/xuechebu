from appium import webdriver


def init_driver():
    """驱动获取方法"""
    capabilities = {
        "platformName": "Android",  # 平台类型
        "platformVersion": "5.1",  # 系统版本
        "deviceName": "模拟器",  # 设备名称
        "appPackage": "com.bjcsxq.chat.carfriend",  # 待测引用的包名
        "appActivity": ".MainActivity",  # 待测应用的启动名
        # "noReset": True # 不重置应用
    }
    driver = webdriver.Remote('http://127.0.0.1:4723/wd/hub', desired_capabilities=capabilities)
    return driver


# 学车不(旧版) 包名/启动名
# com.bjcsxq.chat.carfriend/.MainActivity

if __name__ == '__main__':
    init_driver()
