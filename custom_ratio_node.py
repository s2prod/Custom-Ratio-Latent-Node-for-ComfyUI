import torch

class CustomRatioNode:
    def __init__(self):
        self.resolutions = {
            "1:1 (512×512) square": (512, 512),
            "1:1 (1024×1024) square": (1024, 1024),
            "3:2 (768×512) landscape": (768, 512),
            "4:3 (1216×832) landscape": (1216, 832),
            "4:3 (1152×896) landscape": (1152, 896),
            "16:9 (1344×768) landscape": (1344, 768),
            "21:9 (1536×640) landscape": (1536, 640),
            "16:9 (1920×1080) landscape": (1920, 1080),
            "2:3 (512×768) portrait": (512, 768),
            "3:4 (832×1216) portrait": (832, 1216),
            "3:4 (896×1152) portrait": (896, 1152),
            "9:16 (768×1344) portrait": (768, 1344),
            "9:21 (640×1536) portrait": (640, 1536),
            "9:16 (1080×1920) portrait": (1080, 1920),
        }

    @classmethod
    def INPUT_TYPES(cls):
        temp_instance = cls()
        return {
            "required": {
                "ratio": (list(temp_instance.resolutions.keys()), {"default": "16:9 (1344×768) landscape"}),
                "batch_size": ("INT", {"default": 1, "min": 1, "max": 64}),
            }
        }

    RETURN_TYPES = ("LATENT",)
    RETURN_NAMES = ("latent",)
    FUNCTION = "generate_latent"
    CATEGORY = "Custom/Latent"

    def generate_latent(self, ratio, batch_size):
        width, height = self.resolutions[ratio]
        latent_width = width // 8
        latent_height = height // 8
        latent = torch.zeros([batch_size, 4, latent_height, latent_width])
        
        return ({"samples": latent},)

NODE_CLASS_MAPPINGS = {"CustomRatioNode": CustomRatioNode}
NODE_DISPLAY_NAME_MAPPINGS = {"CustomRatioNode": "Custom Ratio Latent"}
