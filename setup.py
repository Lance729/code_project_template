from setuptools import setup, find_packages
# run `pip install -e .` if you want to install the project in editable mode
setup(
    # 项目名称,根目录的名
    name='code_XXX',
    # 项目版本
    version='0.1',
    # 自动查找项目中的包
    packages=find_packages(),
    # 项目依赖，列出运行项目所需的第三方库
    # install_requires=[
    #     'numpy',
    #     'torch',
    # ],
    # 项目描述
    description='XXXX',

)