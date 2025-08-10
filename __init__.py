print("\n\033[32mInitializing RM Nodes\033[0m")  # Fixed green reset

from .rm_flux_sampler_node import RmFluxSampler

NODE_CLASS_MAPPINGS = {
    "RmFluxSampler": RmFluxSampler,
}

NODE_DISPLAY_NAME_MAPPINGS = {
    "RmFluxSampler": "RM Flux Sampler",
}

# Tell ComfyUI where to find JavaScript files
# WEB_DIRECTORY = "./web"

__all__ = ["NODE_CLASS_MAPPINGS", "NODE_DISPLAY_NAME_MAPPINGS"]