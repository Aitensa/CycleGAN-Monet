# Copyright 2021 anonymity
# 
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
# 
#     http://www.apache.org/licenses/LICENSE-2.0
# 
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.


import torchvision.transforms as transforms
from torch.utils.data import DataLoader
from torch.autograd import Variable
from PIL import Image
from torchvision.utils import save_image, make_grid
import torch

from models import *
from utils import *
from datasets import *

import torch.nn as nn
import torch.nn.functional as F
import torch
from torchviz import make_dot 

G = Generator(3,3)
D=Discriminator(3)

G.apply(weights_init_normal)
D.apply(weights_init_normal)


x=Variable(torch.randn(1,3,128,128))
y=D(x)
z=G(x)
g= make_dot(y)
d=make_dot(z)
d.render(filename='Generator',directory='structure/',format='png',view=False)
g.render(filename='Discriminator',directory='structure/',format='png',view=False)