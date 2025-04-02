# Generated file by scripts/custom_systems/add_custom_system.py
# Contains configs for all custom systems in code/common/systems/custom_list.py

from . import *
''' 
@ConfigRegistry.register(HarnessType.Custom, AccuracyTarget.k_99, PowerSetting.MaxP)
class HPE_ProLiant_DL380a_L40S_PCIe_48GBx4(ServerGPUBaseConfig):
    system = KnownSystem.HPE_ProLiant_DL380a_L40S_PCIe_48GBx4
    gpu_batch_size = {'clip1': 1 * 2, 'clip2': 1 * 2, 'unet': 1 * 2, 'vae': 1}
    server_target_qps = 0.55*4
    sdxl_batcher_time_limit = 0
    #use_graphs = True
    min_query_count = 6*800

@ConfigRegistry.register(HarnessType.Custom, AccuracyTarget.k_99, PowerSetting.MaxP)
class HPE_ProLiant_DL380a_H100_PCIe_80GBx4(ServerGPUBaseConfig):
    system = KnownSystem.HPE_ProLiant_DL380a_H100_PCIe_80GBx4
    gpu_batch_size = {'clip1': 8 * 2, 'clip2': 8 * 2, 'unet': 8 * 2, 'vae': 8}
    precision = "fp8" #"int8"
    gpu_inference_streams = 1
    gpu_copy_streams = 1
    server_target_qps = 4
    sdxl_batcher_time_limit = 2
    #use_graphs = True
    min_query_count = 6 * 800

@ConfigRegistry.register(HarnessType.Custom, AccuracyTarget.k_99, PowerSetting.MaxP)
class HPE_PROLIANT_DL380A_H100_NVL_94GBX4(ServerGPUBaseConfig):
    system = KnownSystem.HPE_ProLiant_DL380a_H100_NVL_94GBx4
    gpu_batch_size = {'clip1': 8 * 2, 'clip2': 8 * 2, 'unet': 8 * 2, 'vae': 8}
    precision = "fp8" #"int8"
    #gpu_inference_streams = 1
    #gpu_copy_streams = 1
    server_target_qps = 4
    sdxl_batcher_time_limit = 2
    #use_graphs = True
    min_query_count = 6 * 800
 '''
@ConfigRegistry.register(HarnessType.Custom, AccuracyTarget.k_99, PowerSetting.MaxP)
class HPE_CRAY_XD670_H100_SXM_80GBX8(H100_SXM_80GBx8):
    system = KnownSystem.HPE_Cray_XD670_H100_SXM_80GBx8
    gpu_batch_size = {'clip1': 8 * 2, 'clip2': 8 * 2, 'unet': 8 * 2, 'vae': 8}
    precision = "fp8"
    server_target_qps = 16.2 #16 #16.5-invalid #14 #12.8
    use_graphs = True #False
    start_from_device = True
    gpu_inference_streams = 1
    gpu_copy_streams = 1
    vboost_slider = 1
    sdxl_batcher_time_limit = 5

    ### ServerGPUBaseConfig(GPUBaseConfig):
    #precision = "fp8"
    #use_graphs = False
    #gpu_inference_streams = 1
    #gpu_copy_streams = 1
    #sdxl_batcher_time_limit = 2

    ### H100_SXM_80GBx1(ServerGPUBaseConfig):
    #gpu_batch_size = {'clip1': 8 * 2, 'clip2': 8 * 2, 'unet': 8 * 2, 'vae': 8}
    #server_target_qps = 2
    #sdxl_batcher_time_limit = 3
    #use_graphs = False  # disable to meet latency constraint for x1
    #vboost_slider = 1

    ### H100_SXM_80GBx8(H100_SXM_80GBx1):
    #server_target_qps = 16.2
    #sdxl_batcher_time_limit = 5
    #use_graphs = False

@ConfigRegistry.register(HarnessType.Custom, AccuracyTarget.k_99, PowerSetting.MaxP)
class HPE_CRAY_XD670_H200_SXM_141GBX8(H200_SXM_141GBx8):
    system = KnownSystem.HPE_Cray_XD670_H200_SXM_141GBx8
    gpu_batch_size = {'clip1': 8 * 2, 'clip2': 8 * 2, 'unet': 8 * 2, 'vae': 8}
    precision = "fp8"
    server_target_qps = 17 #2.125*8
    use_graphs = True #False
    start_from_device = True
    gpu_inference_streams = 1
    gpu_copy_streams = 1
    vboost_slider = 1
    sdxl_batcher_time_limit = 5

    ### ServerGPUBaseConfig(GPUBaseConfig):
    #precision = "fp8"
    #use_graphs = False
    #gpu_inference_streams = 1
    #gpu_copy_streams = 1
    #sdxl_batcher_time_limit = 2

    ### H200_SXM_141GBx1(ServerGPUBaseConfig):
    #gpu_batch_size = {'clip1': 8 * 2, 'clip2': 8 * 2, 'unet': 8 * 2, 'vae': 8}
    #server_target_qps = 2.1
    #sdxl_batcher_time_limit = 3
    #use_graphs = False
    #vboost_slider = 1

    ### H200_SXM_141GBx8(H200_SXM_141GBx1):
    #server_target_qps = 16.9
    #sdxl_batcher_time_limit = 5
    #use_graphs = False


@ConfigRegistry.register(HarnessType.Custom, AccuracyTarget.k_99, PowerSetting.MaxP)
class HPE_PROLIANT_DL380A_H200_NVL_141GBX8(ServerGPUBaseConfig):
    system = KnownSystem.HPE_PROLIANT_DL380A_H200_NVL_141GBX8
    gpu_batch_size = {'clip1': 8 * 2, 'clip2': 8 * 2, 'unet': 8 * 2, 'vae': 8}
    server_target_qps = 15.7 #16.9
    sdxl_batcher_time_limit = 5
    use_graphs = True
    start_from_device = True
    gpu_inference_streams = 1
    gpu_copy_streams = 1
    vboost_slider = 1
    
@ConfigRegistry.register(HarnessType.Custom, AccuracyTarget.k_99, PowerSetting.MaxP)
class HPE_PROLIANT_DL380A_L40S_PCIE_48GBX8(ServerGPUBaseConfig):
    system = KnownSystem.HPE_ProLiant_DL380a_L40S_PCIe_48GBx8
    # tensor_path: str = ''
    # precision = "int8"
    gpu_batch_size = {'clip1': 1 * 2, 'clip2': 1 * 2, 'unet': 1 * 2, 'vae': 1}
    sdxl_batcher_time_limit = 0
    server_target_qps = 5.05
    use_graphs = False
    min_query_count = 8 * 800

"""     # Applicable fields for this benchmark are listed below. Not all of these are necessary, and some may be defined in the BaseConfig already and inherited.
    # Please see NVIDIA's submission config files for example values and which fields to keep.
    # Required fields (Must be set or inherited to run):

    # Optional fields:
    active_sms: int = 0
    buffer_manager_thread_count: int = 0
    cache_file: str = ''
    gpu_copy_streams: int = 0
    gpu_inference_streams: int = 0
    instance_group_count: int = 0
    model_path: str = ''
    numa_config: str = ''
    performance_sample_count_override: int = 0
    preferred_batch_size: str = ''
    request_timeout_usec: int = 0
    run_infer_on_copy_streams: bool = False
    schedule_rng_seed: int = 0
    sdxl_batcher_time_limit: float = 0.0
    server_num_issue_query_threads: int = 0
    server_target_latency_ns: int = 0
    server_target_latency_percentile: float = 0.0
    server_target_qps: int = 0
    server_target_qps_adj_factor: float = 0.0
    use_graphs: bool = False
    use_jemalloc: bool = False
    use_spin_wait: bool = False
    verbose_glog: int = 0
    workspace_size: int = 0 """



