#!/usr/bin/python3
import os

import torchvision.transforms as transforms
from torchvision.utils import save_image
from torch.utils.data import DataLoader
from torch.autograd import Variable
import torch

from models import Generator
from datasets import ImageDataset

class transfer(object):
    def __init__(self, path, update=None,prameter=0):
        self.batchSize = 1
        self.dataroot = path
        self.input_nc = 3
        self.output_nc = 3
        self.size = 256
        self.cuda = True
        self.n_cpu = 0
        self.update=update
        self.generator_A2B = 'output/netG_A2B.pth'
        self.generator_B2A = 'output/netG_B2A.pth'
    
    def run(self):
        if torch.cuda.is_available() and not self.cuda:
            print("WARNING: You have a CUDA device, so you should probably run with --cuda")
        
        
        ###### Definition of variables ######
        # Networks
        netG_A2B = Generator(self.input_nc, self.output_nc)
        netG_B2A = Generator(self.output_nc, self.input_nc)

        if self.cuda:   
            netG_A2B.cuda()
            netG_B2A.cuda()

            # Load state dicts
        netG_A2B.load_state_dict(torch.load(self.generator_A2B))
        netG_B2A.load_state_dict(torch.load(self.generator_B2A))
        #print('successfully load in net!')

        # Set model's test mode
        netG_A2B.eval()
        netG_B2A.eval()

        #   Inputs & targets memory allocation
        Tensor = torch.cuda.FloatTensor if self.cuda else torch.Tensor
        input_A = Tensor(self.batchSize, self.input_nc, self.size, self.size)
        input_B = Tensor(self.batchSize, self.output_nc, self.size, self.size)

        #     Dataset loader
        transforms_ = [ transforms.ToTensor(),
                        transforms.Normalize((0.5,0.5,0.5), (0.5,0.5,0.5)) ]
        dataloader = DataLoader(ImageDataset(self.dataroot, transforms_=transforms_, mode='test'),
                                batch_size=self.batchSize, shuffle=False, num_workers=self.n_cpu)
        ###################################

        ###### Testing######

        # Create output dirs if they don't exist
        if not os.path.exists('output/A'):
            os.makedirs('output/A')
        if not os.path.exists('output/B'):
            os.makedirs('output/B')

        for i, batch in enumerate(dataloader):
            # Set model input
            real_A = Variable(input_A.copy_(batch['A']))
            real_B = Variable(input_B.copy_(batch['B']))

             # Generate output
            fake_B = 0.5*(netG_A2B(real_A).data + 1.0)
            fake_A = 0.5*(netG_B2A(real_B).data + 1.0)
                
            # Save image files
            save_image(fake_A, 'output/A/s%4d.png' % (i+1))
            save_image(fake_B, 'output/B/s%4d.png' % (i+1))

            self.update(real_A,fake_B,path='output',tag=(i+1))
            
            
            #sys.stdout.write('\rGenerated images %04d of %04d' % (i+1, len(dataloader)))

            #sys.stdout.write('\n')
            ###################################




