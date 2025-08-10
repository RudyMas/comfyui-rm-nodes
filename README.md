# ComfyUI RM Nodes

This repository contains **modified nodes** designed for the [ComfyUI](https://github.com/comfyanonymous/ComfyUI) framework, focusing on fixing errors and workflow incompatibilities I encountered in my own workflows.  

> ⚠ **Note:** If you do not have issues with the original nodes, please use the extensions created by the **original authors** instead.  
These modifications are personal adaptations and may differ from the intended behavior of the original versions.

---

## 📂 Nodes

### Flux

#### RM Flux Sampler
##### Initial code from: https://github.com/gseth/ControlAltAI-Nodes

The **RM Flux Sampler** node combines the functionality of the `CustomSamplerAdvance` node and its input nodes into a single, streamlined component.

**Key Features:**
- **CFG Setting:** Fixed at `1.0` for simplicity and to match my workflow needs.
- **Conditioning Input:** Only **positive conditioning** is supported.
- **Compatibility:** Only samplers and schedulers compatible with the **Flux** model are included.
- **Latent Compatibility:** Must be used with **SD3 Empty Latent Image**. The standard empty latent image node is **not** compatible.

---

## 📦 Installation

Clone this repository into your ComfyUI `custom_nodes` folder:

```bash
cd path/to/ComfyUI/custom_nodes
git clone https://github.com/RudyMas/comfyui-rm-nodes.git
```