import pytest
import logging
from core_package.config.gloable_config import Env_config

def test():
    print("hello world")
    if Env_config.impl_model == "Evaluating_model":
        logging.debug(f"\n Total Latency: {123.45} ms \n")


if __name__ != "__main__":
    print("✅ Env impl module <env_impl.py> is imported successfully! ") 



@pytest.mark.testsubmodule
def test_env_impl():
    '''
    测试Env_impl类的基本功能
    🚀 运行`pytest -m testsubmodule -k test_env_impl core_package/example.py`测试一下吧

    预计输出：
        configfile: pytest.ini
        collecting ... ✅ Env impl module <env_impl.py> is imported successfully! 
        collected 1 item                                                                                                                                                
        core_package/example.py::test_env_impl hello world

        -------- live log call ----------------------------------------------
        DEBUG    root:example.py:8 
        Total Latency: 123.45 ms 

        PASSED

        ================================== 1 passed in 0.01s ============
    '''
    test()
