import os
import pytest

if __name__ == '__main__':
    json_dir_path = "json_path"
    html_dir_path = "html_path"
    args_list = ["-s", "-v", "--alluredir", json_dir_path]
    pytest.main(args_list)

    # 使用allure命令，生产测试报告
    cmd = f"allure generate {json_dir_path} -o {html_dir_path} -c"
    os.system(cmd)
