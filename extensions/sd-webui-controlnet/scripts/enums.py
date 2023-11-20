from enum import Enum


class StableDiffusionVersion(Enum):
    """The version family of stable diffusion model."""

    UNKNOWN = 0
    SD1x = 1
    SD2x = 2
    SDXL = 3

    @staticmethod
    def detect_from_model_name(model_name: str) -> "StableDiffusionVersion":
        """Based on the model name provided, guess what stable diffusion version it is.
        This might not be accurate without actually inspect the file content.
        """
        if any(f"sd{v}" in model_name.lower() for v in ("14", "15", "16")):
            return StableDiffusionVersion.SD1x

        if "sd21" in model_name or "2.1" in model_name:
            return StableDiffusionVersion.SD2x

        if "xl" in model_name.lower():
            return StableDiffusionVersion.SDXL

        return StableDiffusionVersion.UNKNOWN


class ControlModelType(Enum):
    """
    The type of Control Models (supported or not).
    """

    ControlNet = "ControlNet, Lvmin Zhang"
    T2I_Adapter = "T2I_Adapter, Chong Mou"
    T2I_StyleAdapter = "T2I_StyleAdapter, Chong Mou"
    T2I_CoAdapter = "T2I_CoAdapter, Chong Mou"
    MasaCtrl = "MasaCtrl, Mingdeng Cao"
    GLIGEN = "GLIGEN, Yuheng Li"
    AttentionInjection = "AttentionInjection, Lvmin Zhang"  # A simple attention injection written by Lvmin
    StableSR = "StableSR, Jianyi Wang"
    PromptDiffusion = "PromptDiffusion, Zhendong Wang"
    ControlLoRA = "ControlLoRA, Wu Hecong"
    ReVision = "ReVision, Stability"
    IPAdapter = "IPAdapter, Hu Ye"
    Controlllite = "Controlllite, Kohya"


# Written by Lvmin
class AutoMachine(Enum):
    """
    Lvmin's algorithm for Attention/AdaIn AutoMachine States.
    """

    Read = "Read"
    Write = "Write"
