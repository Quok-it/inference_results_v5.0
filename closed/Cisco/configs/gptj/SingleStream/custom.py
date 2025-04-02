# Generated file by scripts/custom_systems/add_custom_system.py
# Contains configs for all custom systems in code/common/systems/custom_list.json

from . import *


@ConfigRegistry.register(HarnessType.Custom, AccuracyTarget.k_99, PowerSetting.MaxP)
class C245M8_H100NVL_94GBX2(SingleStreamGPUBaseConfig):
    system = KnownSystem.C245M8_H100NVL_94GBx2

    # Applicable fields for this benchmark are listed below. Not all of these are necessary, and some may be defined in the BaseConfig already and inherited.
    # Please see NVIDIA's submission config files for example values and which fields to keep.
    # Required fields (Must be set or inherited to run):
    gpu_batch_size: Dict = {}
    tensor_path: str = ''
    trtllm_build_flags: parse_cli_flags = {}
    trtllm_checkpoint_flags: parse_cli_flags = {}
    trtllm_runtime_flags: parse_cli_flags = {}

    # Optional fields:
    active_sms: int = 0
    cache_file: str = ''
    checkpoint_dir: str = ''
    enable_sort: bool = False
    engine_dir: str = ''
    llm_gen_config_path: str = ''
    single_stream_expected_latency_ns: int = 0
    single_stream_target_latency_percentile: float = 0.0
    use_token_latencies: bool = False
    vboost_slider: int = 0
    workspace_size: int = 0


@ConfigRegistry.register(HarnessType.Custom, AccuracyTarget.k_99_9, PowerSetting.MaxP)
class C245M8_H100NVL_94GBX2_HighAccuracy(C245M8_H100NVL_94GBX2):
    pass


