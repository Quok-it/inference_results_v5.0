# Generated file by scripts/custom_systems/add_custom_system.py
# Contains configs for all custom systems in code/common/systems/custom_list.json

from . import *


@ConfigRegistry.register(HarnessType.Custom, AccuracyTarget.k_99, PowerSetting.MaxP)
class ESC8000_H200_NVLX8_NVLINK(OfflineGPUBaseConfig):
    system = KnownSystem.ESC8000_H200_NVLx8_NVLink

    # Applicable fields for this benchmark are listed below. Not all of these are necessary, and some may be defined in the BaseConfig already and inherited.
    # Please see NVIDIA's submission config files for example values and which fields to keep.
    # Required fields (Must be set or inherited to run):
    gpu_batch_size: Dict = {}
    tensor_path: str = ''

    # Optional fields:
    active_sms: int = 0
    cache_file: str = ''
    engine_dir: str = ''
    offline_expected_qps: float = 0.0
    vboost_slider: int = 0
    workspace_size: int = 0


