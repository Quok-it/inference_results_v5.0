# Generated file by scripts/custom_systems/add_custom_system.py
# Contains configs for all custom systems in code/common/systems/custom_list.py

from . import *

''' 
@ConfigRegistry.register(HarnessType.LWIS, AccuracyTarget.k_99, PowerSetting.MaxP)
class HPE_ProLiant_DL380a_L40S_PCIe_48GBx4(ServerGPUBaseConfig):
    system = KnownSystem.HPE_ProLiant_DL380a_L40S_PCIe_48GBx4
    gpu_copy_streams = 4
    use_deque_limit = True
    deque_timeout_usec = 30000
    gpu_batch_size = {'retinanet': 8}
    gpu_inference_streams = 1*4
    server_target_qps = 2800
    workspace_size = 70000000000

@ConfigRegistry.register(HarnessType.LWIS, AccuracyTarget.k_99, PowerSetting.MaxP)
class HPE_ProLiant_DL380a_H100_PCIe_80GBx4(H100_PCIe_80GBx1):
    system = KnownSystem.HPE_ProLiant_DL380a_H100_PCIe_80GBx4
    gpu_copy_streams = 4
    use_deque_limit = True
    deque_timeout_usec = 30000
    gpu_batch_size = {'retinanet': 8}
    gpu_inference_streams = 2
    server_target_qps = 1075*4

@ConfigRegistry.register(HarnessType.LWIS, AccuracyTarget.k_99, PowerSetting.MaxP)
class HPE_PROLIANT_DL380A_H100_NVL_94GBX4(ServerGPUBaseConfig):
    system = KnownSystem.HPE_ProLiant_DL380a_H100_NVL_94GBx4
    gpu_copy_streams = 4
    use_deque_limit = True
    deque_timeout_usec = 30000
    gpu_batch_size = {'retinanet': 16} #8
    gpu_inference_streams = 2
    server_target_qps = 1250 * 4 #1150 * 4
    workspace_size = 60000000000

@ConfigRegistry.register(HarnessType.Triton, AccuracyTarget.k_99, PowerSetting.MaxP)
class HPE_PROLIANT_DL380A_H100_NVL_94GBX4_Triton(HPE_PROLIANT_DL380A_H100_NVL_94GBX4):
    use_triton = True
 '''
@ConfigRegistry.register(HarnessType.LWIS, AccuracyTarget.k_99, PowerSetting.MaxP)
class HPE_CRAY_XD670_H100_SXM_80GBX8(H100_SXM_80GBx8):
    system = KnownSystem.HPE_Cray_XD670_H100_SXM_80GBx8
    start_from_device = True
    #numa_config = "0,1:0-23,96-119&2,3:24-47,120-143&4,5:48-71,144-167&6,7:72-95,168-191"
    server_target_qps = 1720 * 8 #1730 * 8 #1610 * 8 #1750 * 8 #1710 * 8 #1700 * 8
    gpu_batch_size = {'retinanet': 16} #8
    active_sms = 100
    use_graphs = False
    use_cuda_thread_per_device = True
    gpu_copy_streams = 4
    use_deque_limit = True
    deque_timeout_usec = 30000
    gpu_inference_streams = 2
    workspace_size = 60000000000


@ConfigRegistry.register(HarnessType.Triton, AccuracyTarget.k_99, PowerSetting.MaxP)
class HPE_CRAY_XD670_H100_SXM_80GBX8_Triton(HPE_CRAY_XD670_H100_SXM_80GBX8):
    use_triton = True

@ConfigRegistry.register(HarnessType.LWIS, AccuracyTarget.k_99, PowerSetting.MaxP)
class HPE_CRAY_XD670_H200_SXM_141GBX8(H200_SXM_141GBx8):
    system = KnownSystem.HPE_Cray_XD670_H200_SXM_141GBx8
    start_from_device = True
    server_target_qps = 1800 * 8
    gpu_batch_size = {'retinanet': 16} #8
    gpu_inference_streams = 2
    gpu_copy_streams = 4 # <== try to improve this next
    use_deque_limit = True
    deque_timeout_usec = 30000
    workspace_size = 60000000000

@ConfigRegistry.register(HarnessType.Triton, AccuracyTarget.k_99, PowerSetting.MaxP)
class HPE_CRAY_XD670_H200_SXM_141GBX8_Triton(HPE_CRAY_XD670_H200_SXM_141GBX8):
    use_triton = True

@ConfigRegistry.register(HarnessType.LWIS, AccuracyTarget.k_99, PowerSetting.MaxP)
class HPE_PROLIANT_DL380A_H200_NVL_141GBX8(ServerGPUBaseConfig):
    system = KnownSystem.HPE_PROLIANT_DL380A_H200_NVL_141GBX8
    start_from_device = True
    server_target_qps = 12000 #12500 #1800 * 8
    gpu_batch_size = {'retinanet': 16} #8
    gpu_copy_streams = 4 # <== try to improve this next
    use_deque_limit = True
    deque_timeout_usec = 30000
    workspace_size = 60000000000

@ConfigRegistry.register(HarnessType.Triton, AccuracyTarget.k_99, PowerSetting.MaxP)
class HPE_PROLIANT_DL380A_H200_NVL_141GBX8_Triton(HPE_PROLIANT_DL380A_H200_NVL_141GBX8):
    use_triton = True
    
@ConfigRegistry.register(HarnessType.LWIS, AccuracyTarget.k_99, PowerSetting.MaxP)
class HPE_ProLiant_DL380a_L40S_PCIe_48GBx8(ServerGPUBaseConfig):
    system = KnownSystem.HPE_ProLiant_DL380a_L40S_PCIe_48GBx8
    gpu_copy_streams = 4
    use_deque_limit = True
    deque_timeout_usec = 30000
    gpu_batch_size = {'retinanet': 8}
    gpu_inference_streams = 2
    server_target_qps = 6100
    workspace_size = 70000000000

@ConfigRegistry.register(HarnessType.Triton, AccuracyTarget.k_99, PowerSetting.MaxP)
class HPE_ProLiant_DL380a_L40S_PCIe_48GBx8_Triton(HPE_ProLiant_DL380a_L40S_PCIe_48GBx8):
    use_triton = True

"""
    # Applicable fields for this benchmark are listed below. Not all of these are necessary, and some may be defined in the BaseConfig already and inherited.
    # Please see NVIDIA's submission config files for example values and which fields to keep.
    # Required fields (Must be set or inherited to run):
    gpu_batch_size: Dict = {}
    input_dtype: str = ''
    input_format: str = ''
    map_path: str = ''
    precision: str = ''
    tensor_path: str = ''

    # Optional fields:
    active_sms: int = 0
    assume_contiguous: bool = False
    batch_triton_requests: bool = False
    buffer_manager_thread_count: int = 0
    cache_file: str = ''
    complete_threads: int = 0
    deque_timeout_usec: int = 0
    disable_beta1_smallk: bool = False
    energy_aware_kernels: bool = False
    gather_kernel_buffer_threshold: int = 0
    gpu_copy_streams: int = 0
    gpu_inference_streams: int = 0
    instance_group_count: int = 0
    max_queue_delay_usec: int = 0
    model_path: str = ''
    nms_type: str = ''
    num_concurrent_batchers: int = 0
    num_concurrent_issuers: int = 0
    numa_config: str = ''
    output_pinned_memory: bool = False
    performance_sample_count_override: int = 0
    preferred_batch_size: str = ''
    request_timeout_usec: int = 0
    run_infer_on_copy_streams: bool = False
    schedule_rng_seed: int = 0
    server_num_issue_query_threads: int = 0
    server_target_latency_ns: int = 0
    server_target_latency_percentile: float = 0.0
    server_target_qps: float = 0.0
    server_target_qps_adj_factor: float = 0.0
    use_batcher_thread_per_device: bool = False
    use_concurrent_harness: bool = False
    use_cuda_thread_per_device: bool = False
    use_deque_limit: bool = False
    use_graphs: bool = False
    use_jemalloc: bool = False
    use_same_context: bool = False
    use_spin_wait: bool = False
    vboost_slider: int = 0
    verbose_glog: int = 0
    warmup_duration: float = 0.0
    workspace_size: int = 0
"""


@ConfigRegistry.register(HarnessType.LWIS, AccuracyTarget.k_99, PowerSetting.MaxP)
class HPE_HAWKS_3200_H100_NVL_94GBX4(ServerGPUBaseConfig):
    system = KnownSystem.HPE_Hawks_3200_H100_NVL_94GBx4

    # Applicable fields for this benchmark are listed below. Not all of these are necessary, and some may be defined in the BaseConfig already and inherited.
    # Please see NVIDIA's submission config files for example values and which fields to keep.
    # Required fields (Must be set or inherited to run):
    gpu_copy_streams = 4
    use_deque_limit = True
    deque_timeout_usec = 30000
    gpu_batch_size = {'retinanet': 16} #8
    gpu_inference_streams = 2
    server_target_qps = 1250 * 4 #1150 * 4
    workspace_size = 60000000000


@ConfigRegistry.register(HarnessType.Triton, AccuracyTarget.k_99, PowerSetting.MaxP)
class HPE_HAWKS_3200_H100_NVL_94GBX4_Triton(HPE_HAWKS_3200_H100_NVL_94GBX4):
    use_triton = True

