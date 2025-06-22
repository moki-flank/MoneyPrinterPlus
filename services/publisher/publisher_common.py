import time
import selenium
import subprocess
import os
from selenium import webdriver
from tools.utils import get_must_session_option


def init_driver():
    driver_type = get_must_session_option('video_publish_driver_type', "请设置驱动类型")
    driver_location = get_must_session_option('video_publish_driver_location', "请设置驱动位置")
    debugger_address = get_must_session_option('video_publish_debugger_address', "请设置debugger地址")
    
    if driver_type == 'chrome':
        # 启动浏览器驱动服务
        service = selenium.webdriver.chrome.service.Service(driver_location)
        # Chrome 的调试地址
        debugger_address = debugger_address
        # 创建Chrome选项，重用现有的浏览器实例
        options = selenium.webdriver.chrome.options.Options()
        options.page_load_strategy = 'normal'  # 设置页面加载策略为'normal' 默认值, 等待所有资源下载,
        options.add_experimental_option('debuggerAddress', debugger_address)
        # 使用服务和选项初始化WebDriver
        driver = webdriver.Chrome(service=service, options=options)
        driver.implicitly_wait(10)  # 设置隐式等待时间为10秒
        return driver
        
    elif driver_type == 'firefox':
        # 移除subprocess.Popen部分，只用webdriver启动
        firefox_binary = r"C:\Program Files\Mozilla Firefox\firefox.exe"
        
        # 创建service
        service = selenium.webdriver.firefox.service.Service(driver_location)
        
        # 配置options
        options = selenium.webdriver.firefox.options.Options()
        options.page_load_strategy = 'normal'
        
        # 指定Firefox二进制文件位置
        if os.path.exists(firefox_binary):
            options.binary_location = firefox_binary
        
        # 启动Firefox（只启动一个实例）
        driver = webdriver.Firefox(service=service, options=options)
        driver.implicitly_wait(10)
        return driver