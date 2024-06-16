import allure
from playwright.sync_api import Page

"""
	结果处理动作封装
	readAttach：入参（page, 路径[./log/screenshot/], 文件名[test_playwright])
"""


# 结果截图与Allure提取
def readAttach(page: Page, paths, fileName):
	page.screenshot(path=paths + fileName + ".png")
	with open(paths + fileName + ".png", "rb") as file:
		allure.attach(file.read(), name=fileName, attachment_type=allure.attachment_type.PNG)
