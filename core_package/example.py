import pytest


def test():
    print("hello world")


if __name__ != "__main__":
    print("✅ Env impl module <env_impl.py> is imported successfully! ") 



@pytest.mark.testsubmodule
def test_env_impl():
    # 测试Env_impl类的基本功能
    
    test()
