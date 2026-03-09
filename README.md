# Project Template Initialization Guide

## Overview
This guide provides instructions on how to clone a programming template from Git, remove existing user information and links, and initialize the project for your own use.

## Prerequisites
- Git installed on your machine
- Basic command line knowledge

## Steps

### 1. Clone the Project
Open your terminal or command prompt and run the following command to clone the project:
git clone <project-url>
Replace `<project-url>` with the actual URL of the Git repository.

### 2. Navigate to the Project Directory
Change your current directory to the newly cloned project folder:
cd <project-name>
Replace `<project-name>` with the actual name of the project.

### 3. Remove Existing User Information
To remove any existing user information and links, follow these steps:

- Remove user-specific files (e.g., `.gitconfig`, `.gitignore`, `README.md`, etc.):
rm -rf .git

- Initialize a new Git repository:
`git init`

- Set your own user information for Git:

    `git config --global user.name "Your Name"`

    `git config --global user.email "your.email@example.com"`

### 4. Initialize the Project
Depending on the project's requirements, you may need to install dependencies, set up environment variables, or perform other initialization tasks. Please refer to the project's documentation for specific instructions.

- Add a new remote repository: `git remote add origin new-url`



# 中文版

步骤1: 安装setup.py，并安装组件
步骤2: 设置引用成功提示
步骤3: 安装pytest
步骤4: 设置全局参数
步骤5: 画图页面和画图工具分开
步骤6: 设置python的虚拟环境，miniconda，python自带的虚拟环境工具venv(好像是这个名)
步骤7: 用git管理版本