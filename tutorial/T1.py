# %%
import sys
import torch
from torch.nn import Parameter
import torch.nn as nn
import torch.nn.functional as F

import syft as sy

# %%
hook = sy.TorchHook(torch)
x = torch.tensor([1, 2, 3, 4, 5])

y = x + x
print(y)
# %%


