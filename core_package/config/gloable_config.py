


class Env_config:
    """
    The global configuration for environment.
    """
    global_epsilon: float = 0.1
    global_random_seed: int = 55
    worker_num: int = 5 # selected workers number
    server_num: int = 1  # 服务器数量 ❓ 这个参数好像没用上，后续可以删除
    task_num: int = 100  # 任务数量

    bandwidth: float = 50.0  # The bandwidth of the network, unit is MHz or Hz
    commu_throughput_discount: float = 0.1     # The communication rate discount factor of the device, the actual communication rate is bandwidth * commu_throughput_discount
    with_power: bool = False  # Whether to consider the communication power consumption
    comp_power: float = 5.0    # The communication power between devices, unit is Ws
    
    commu_radius: float = 100.0   # The distance between devices, unit is m
    device_computing_capacity: float = 472.0  # unit is GFlops/s. The device computing capacity refers the NVIDIA Jetson Nano, 128-core NVIDIA Maxwell™ architecture GPU
    comp_ability_discount: float = 0.5  # The discount factor of the computing ability of the device, the actual computing ability is device_computing_capacity * comp_ability_discount
    force_last_task: bool = False  # Whether to last device to take the last task, for MCS system, the last device is always the user receiving final result, who does not take on any computation task.

    path_to_llama: str = "related_dataset/llama3_1B_workload.json"

    # 从数据集dataset_tsmc2014中获取用户信息的方式，有三种方式：
    # extract_from_dataset_randomly、extract_from_dataset_sequentially。
    # 或者按照我们自己的规则生成generate_randomly
    the_way_to_get_user_info: str = "extract_from_dataset_sequentially"  

    task_type: str = "Llama_1B" # "Llama_1B", or "VGG16"

    CNN_model_name: str = 'VGG16'
    CNN_dataset_name: str = 'ImageNet'

    # if the impl_model is "Evaluating_model", the program will print more detail info, which will help users develope; otherwise, when it is in "Distribution_mode", only core function will be impl, only necessary details will be printed.
    impl_model: str = "Evaluating_model" 

    def __init__(self):
        # The __init__ will test if the input parameters are valid.
        self._validate()

    def _validate(self):
        valid_impl_models = {"Evaluating_model", "Distribution_mode"}
        if self.impl_model not in valid_impl_models:
            raise ValueError(
                f"impl_model must be one of {valid_impl_models}, got '{self.impl_model}'"
            )
        if not (0.0 <= self.global_epsilon <= 1.0):
            raise ValueError("global_epsilon must be between 0 and 1.")
        

        
        valid_user_info_methods = {
            "extract_from_dataset_randomly", 
            "extract_from_dataset_sequentially", 
            "generate_randomly"
        }
        if self.the_way_to_get_user_info not in valid_user_info_methods:
            raise ValueError(f"the_way_to_get_user_info must be one of {valid_user_info_methods}, got '{self.the_way_to_get_user_info}'")

