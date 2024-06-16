"""
	复杂动作封装
"""


# 点击输入内容
def click_fill(page, local, fills):
	page.locator(local).click()
	page.locator(local).fill(fills)
