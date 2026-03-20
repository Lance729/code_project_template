# LLMs Research Project

## 项目简介 | Project Overview

这是一个用于大语言模型（LLM）研究的代码项目。

This is a research code project for Large Language Models (LLMs).

---

## 环境配置 | Environment Setup

### 安装 Mamba | Install Mamba

Mamba 是一个快速的 Python 环境管理器，是 Conda 的替代品。

Mamba is a fast Python environment manager, a drop-in replacement for Conda.

#### macOS / Linux 安装 | macOS / Linux Installation

```bash
# 方法一：使用 Miniforge (推荐 / Recommended)
# 下载并安装 Miniforge（包含 Mamba）
curl -Ls https://micro.mamba.pm/api/micromamba/${os:-$(uname -s)}/${arch:-$(uname -m)}/latest | tar -xvj bin/micromamba
./bin/micromamba shell init
source ~/.bashrc  # 或 source ~/.zshrc

# 方法二：使用 brew 安装 mamba
brew --version # 确保 Homebrew 已安装
brew install --cask miniforge # 这一步不知道为什么很慢，还会报错，多试几次就可以了
```


#### 验证安装 | Verify Installation

```bash
# 检查 mamba 是否安装成功
mamba --version
# 输出类似: mamba 1.5.x
```

---

### 使用 Mamba 创建环境 | Create Environment with Mamba



#### 方法一：手动创建环境 | Manually Create Environment

```bash
# 创建新环境（安装最新 Python）
mamba create -n llm_env python


# 如果要查看可用的 Python 版本：
mamba search python


# 或指定 Python 版本
mamba create -n llm_env python=3.12

# 激活环境
mamba activate llm_env

# 安装依赖

mamba install pytest setuptools

# 可选安装：numpy torch jupyter
```

#### 方法二：从 environment.yml 创建 | From environment.yml

```bash
# 激活基础环境
micromamba activate

# 或使用 mamba
mamba env create -f environment.yml

# 激活环境
mamba activate llm_env
```

#### 常用命令 | Common Commands

```bash
# 列出所有环境
mamba env list

# 更新环境
mamba env update -f environment.yml

# 删除环境
mamba env remove -n llm_env

# 导出当前环境配置
mamba env export > environment.yml
```

---

## 项目初始化步骤 | Project Initialization Steps

### 1. 克隆项目 | Clone the Project

```bash
git clone <project-url>
cd LLMs
```

### 2. 创建并激活环境 | Create and Activate Environment

```bash
# 使用 mamba 从 environment.yml 创建环境
mamba env create -f environment.yml

# 激活环境
mamba activate llm_env
```

### 3. 安装项目包 (setup.py) | Install Project Package (setup.py)

`setup.py` 是 Python 项目的标准安装配置文件，用于定义项目的元数据、依赖包和打包信息。

`setup.py` is the standard installation configuration file for Python projects, used to define project metadata, dependencies, and packaging information.

**功能 | Features：**
- 定义项目名称、版本、描述 / Define project name, version, description
- 声明项目依赖 / Declare project dependencies
- 支持可编辑模式安装 (`pip install -e .`) / Support editable mode installation

```bash
# 以可编辑模式安装项目（推荐）
# Install project in editable mode (recommended)
pip install -e .

# 验证安装
python -c "import core_package; print('OK')"
```

### 4. 安装测试框架 (pytest) | Install Testing Framework (pytest)

`pytest` 是 Python 常用的单元测试框架，用于编写和运行测试用例。

`pytest` is a popular Python unit testing framework for writing and running test cases.

**功能 | Features：**
- 简单易用的测试编写语法 / Simple test writing syntax
- 自动发现测试文件 / Automatic test discovery
- 丰富的插件生态 / Rich plugin ecosystem
- 支持日志输出和标记 / Support for logging and markers

```bash
# 使用 mamba 安装 pytest
mamba install pytest

# 或使用 pip
pip install pytest

# 运行所有测试 / Run all tests
pytest

# 运行指定测试文件,‼️这会运行该文件中的所有测试 / Run specific test file
pytest path/to/test_file.py

# 运行特定测试函数 / Run specific test function
pytest -m testsubmodule -k test_function_name path/to/file.py

# 带日志输出运行 / Run with logging output
pytest --log-cli-level=DEBUG
```

### 5. 验证安装 | Verify Installation

```bash
# 运行示例脚本
python core_package/example.py
```

---

## 项目结构 | Project Structure

```
LLMs/
├── core_package/          # 核心代码包
│   ├── config/          # 配置文件
│   ├── benchmarks/      # 基准测试
│   └── *.py            # 核心模块
├── results/             # 结果目录
│   ├── data/           # 数据文件
│   └── images/         # 图片文件
├── environment.yml     # 环境配置
├── setup.py           # 项目安装配置
├── run.py             # 运行入口
└── pytest.ini         # pytest 配置
```

---

## 常用操作 | Common Operations

### 运行代码 | Run Code

```bash
# 激活环境
mamba activate llm_env

# 运行主程序
python run.py
```

### Jupyter Notebook

```bash
# 启动 Jupyter
jupyter notebook
# 或
jupyter lab
```

### 使用 Git 进行版本控制 | Git Version Control

```bash
# 初始化 Git（如果需要）
git init

# 设置用户信息
git config --global user.name "Your Name"
git config --global user.email "your.email@example.com"

# 添加文件并提交
git add .
git commit -m "Initial commit"

# 取消对文件夹的追踪（不删除本地文件夹）
git rm --cached -r folder_name/



```

---

## 依赖项 | Dependencies

主要依赖见 `environment.yml`，核心依赖包括：

- Python 3.x
- NumPy
- PyTorch
- Jupyter

详见 [environment.yml](environment.yml)

---
