import os

import pytest

if __name__ == "__main__":
    pytest.main()
    os.system("allure generate ./reports/tmp -o ./reports/UIReport --clean")
    # ����������Allure����HTML
    os.system("allure serve ./reports/tmp")
    # os.system('allure open -h 127.0.0.1 -p 8083 ./reports/UIReport')
