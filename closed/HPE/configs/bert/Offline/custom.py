# Generated file by scripts/custom_systems/add_custom_system.py
# Contains configs for all custom systems in code/common/systems/custom_list.py

from . import *

''' 
@ConfigRegistry.register(HarnessType.Custom, AccuracyTarget.k_99, PowerSetting.MaxP)
class HPE_ProLiant_DL380a_L40S_PCIe_48GBx4(OfflineGPUBaseConfig):
    system = KnownSystem.HPE_ProLiant_DL380a_L40S_PCIe_48GBx4
    use_small_tile_gemm_plugin = True
    gpu_batch_size = {'bert': 32}
    offline_expected_qps = 3300*4
    workspace_size = 7516192768

@ConfigRegistry.register(HarnessType.Custom, AccuracyTarget.k_99_9, PowerSetting.MaxP)
class HPE_ProLiant_DL380a_L40S_PCIe_48GBx4_HighAccuracy(HPE_ProLiant_DL380a_L40S_PCIe_48GBx4):
    precision = "fp16"
    use_fp8 = True
    offline_expected_qps = 3300*4
    gpu_batch_size = {'bert': 32}

@ConfigRegistry.register(HarnessType.Custom, AccuracyTarget.k_99, PowerSetting.MaxP)
class HPE_ProLiant_DL380a_H100_PCIe_80GBx4(H100_PCIe_80GBx1):
    system = KnownSystem.HPE_ProLiant_DL380a_H100_PCIe_80GBx4
    #start_from_device = True
    run_infer_on_copy_streams = True
    use_small_tile_gemm_plugin = False
    gpu_batch_size = {'bert': 1280}
    offline_expected_qps = 5750*4
    workspace_size = 7516192768

@ConfigRegistry.register(HarnessType.Custom, AccuracyTarget.k_99_9, PowerSetting.MaxP)
class HPE_ProLiant_DL380a_H100_PCIe_80GBx4_HighAccuracy(HPE_ProLiant_DL380a_H100_PCIe_80GBx4):
    offline_expected_qps = 5150*4
    precision = "fp16"
    use_fp8 = True
    use_graphs = False
    gpu_batch_size = {'bert': 1024}

@ConfigRegistry.register(HarnessType.Custom, AccuracyTarget.k_99, PowerSetting.MaxP)
class HPE_PROLIANT_DL380A_H100_NVL_94GBX4(H100_NVL_94GBx1):
    system = KnownSystem.HPE_ProLiant_DL380a_H100_NVL_94GBx4
    #use_small_tile_gemm_plugin = False
    gpu_batch_size = {'bert': 1344} #1280-valid #1536-error
    offline_expected_qps = 6800 * 4 #6600*4 -valid #max 6750
    #workspace_size = 7516192768
    #run_infer_on_copy_streams = True

@ConfigRegistry.register(HarnessType.Custom, AccuracyTarget.k_99_9, PowerSetting.MaxP)
class HPE_PROLIANT_DL380A_H100_NVL_94GBX4_HighAccuracy(HPE_PROLIANT_DL380A_H100_NVL_94GBX4):
    precision = "fp16"
    use_fp8 = True
    offline_expected_qps = 6100 * 4 #6000*4 -valid #max 6000
    #use_graphs = False
    gpu_batch_size = {'bert': 1280} #1024 #1344

@ConfigRegistry.register(HarnessType.Triton, AccuracyTarget.k_99, PowerSetting.MaxP)
class HPE_PROLIANT_DL380A_H100_NVL_94GBX4_Triton(HPE_PROLIANT_DL380A_H100_NVL_94GBX4):
    use_triton = True

@ConfigRegistry.register(HarnessType.Triton, AccuracyTarget.k_99_9, PowerSetting.MaxP)
class HPE_PROLIANT_DL380A_H100_NVL_94GBX4_HighAccuracy_Triton(HPE_PROLIANT_DL380A_H100_NVL_94GBX4_HighAccuracy):
    use_triton = True
 '''
@ConfigRegistry.register(HarnessType.Custom, AccuracyTarget.k_99, PowerSetting.MaxP)
class HPE_CRAY_XD670_H100_SXM_80GBX8(H100_SXM_80GBx8):
    system = KnownSystem.HPE_Cray_XD670_H100_SXM_80GBx8
    start_from_device = True
    run_infer_on_copy_streams = True
    gpu_batch_size = {'bert': 1280} #1280 #1344 
    offline_expected_qps = 9400 * 8 #8875*8 #11000 * 8 #10500 * 8 # <<< new
    gpu_copy_streams = 2
    gpu_inference_streams = 4 # <<< new
    vboost_slider = 1 # <<< new

@ConfigRegistry.register(HarnessType.Custom, AccuracyTarget.k_99_9, PowerSetting.MaxP)
class HPE_CRAY_XD670_H100_SXM_80GBX8_HighAccuracy(HPE_CRAY_XD670_H100_SXM_80GBX8):
    offline_expected_qps = 8200 * 8 #9400 *8
    start_from_device = True
    run_infer_on_copy_streams = True
    gpu_batch_size = {'bert': 1024} #1024 #1280 #1344-compliancetest-OOM

    gpu_copy_streams = 8
    gpu_inference_streams = 4
    #vboost_slider = 1 # <<< new

    #from H100_SXM_80GBx1_HighAccuracy(H100_SXM_80GBx1):
    precision = "fp16"
    use_fp8 = True
    use_graphs = False


@ConfigRegistry.register(HarnessType.Triton, AccuracyTarget.k_99, PowerSetting.MaxP)
class HPE_CRAY_XD670_H100_SXM_80GBX8_Triton(HPE_CRAY_XD670_H100_SXM_80GBX8):
    use_triton = True

@ConfigRegistry.register(HarnessType.Triton, AccuracyTarget.k_99_9, PowerSetting.MaxP)
class HPE_CRAY_XD670_H100_SXM_80GBX8_HighAccuracy_Triton(HPE_CRAY_XD670_H100_SXM_80GBX8_HighAccuracy):
    use_triton = True

#H200
@ConfigRegistry.register(HarnessType.Custom, AccuracyTarget.k_99, PowerSetting.MaxP)
class HPE_CRAY_XD670_H200_SXM_141GBX8(H200_SXM_141GBx8):
    system = KnownSystem.HPE_Cray_XD670_H200_SXM_141GBx8
    start_from_device = True
    run_infer_on_copy_streams = True
#    precision = "fp16" #<== do not use here
#    use_fp8 = True #<== do not use here
    use_graphs = False
    gpu_batch_size = {'bert': 1280} 
    offline_expected_qps = 11750 * 8
    gpu_copy_streams = 2
    gpu_inference_streams = 1
    vboost_slider = 1
    use_small_tile_gemm_plugin = False
    workspace_size = 158000000000 #128000000000

@ConfigRegistry.register(HarnessType.Custom, AccuracyTarget.k_99_9, PowerSetting.MaxP)
class HPE_CRAY_XD670_H200_SXM_141GBX8_HighAccuracy(HPE_CRAY_XD670_H200_SXM_141GBX8):
    gpu_batch_size = {'bert': 1024}
    precision = "fp16"
    use_fp8 = True
    offline_expected_qps = 8200 * 8

@ConfigRegistry.register(HarnessType.Triton, AccuracyTarget.k_99, PowerSetting.MaxP)
class HPE_CRAY_XD670_H200_SXM_141GBX8_Triton(HPE_CRAY_XD670_H200_SXM_141GBX8):
    use_triton = True

@ConfigRegistry.register(HarnessType.Triton, AccuracyTarget.k_99_9, PowerSetting.MaxP)
class HPE_CRAY_XD670_H200_SXM_141GBX8_HighAccuracy_Triton(HPE_CRAY_XD670_H200_SXM_141GBX8_HighAccuracy):
    use_triton = True

"""
    # Applicable fields for this benchmark are listed below. Not all of these are necessary, and some may be defined in the BaseConfig already and inherited.
    # Please see NVIDIA's submission config files for example values and which fields to keep.
    # Required fields (Must be set or inherited to run):
    gpu_batch_size: Dict = {}
    input_dtype: str = ''
    input_format: str = ''
    precision: str = ''
    tensor_path: str = ''

    # Optional fields:
    active_sms: int = 0
    batch_triton_requests: bool = False
    bert_opt_seqlen: int = 0
    buffer_manager_thread_count: int = 0
    cache_file: str = ''
    coalesced_tensor: bool = False
    deque_timeout_usec: int = 0
    energy_aware_kernels: bool = False
    gather_kernel_buffer_threshold: int = 0
    gemm_plugin_fairshare_cache_size: int = 0
    gpu_copy_streams: int = 0
    gpu_inference_streams: int = 0
    graph_specs: str = ''
    graphs_max_seqlen: int = 0
    instance_group_count: int = 0
    max_queue_delay_usec: int = 0
    model_path: str = ''
    num_concurrent_batchers: int = 0
    num_concurrent_issuers: int = 0
    numa_config: str = ''
    offline_expected_qps: float = 0.0
    output_pinned_memory: bool = False
    performance_sample_count_override: int = 0
    preferred_batch_size: str = ''
    request_timeout_usec: int = 0
    run_infer_on_copy_streams: bool = False
    soft_drop: float = 0.0
    use_concurrent_harness: bool = False
    use_fp8: bool = False
    use_graphs: bool = False
    use_jemalloc: bool = False
    use_small_tile_gemm_plugin: bool = False
    use_spin_wait: bool = False
    vboost_slider: int = 0
    verbose_glog: int = 0
    workspace_size: int = 0
"""

