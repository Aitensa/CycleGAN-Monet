# Pytorch-CycleGAN
A clean and readable Pytorch implementation of CycleGAN (https://arxiv.org/abs/1703.10593)

## Prerequisites
Code is intended to work with ```Python 3.6.x```, it hasn't been tested with previous versions

### [PyTorch & torchvision](http://pytorch.org/)
### [Visdom](https://github.com/facebookresearch/visdom)
```
pip install visdom
pip install -r requirements.txt # install relative packages
```

### 1.  dataset structure
dataset by setting up the following directory structure:

    .
    ├── datasets                   
    |   ├── gan-getting-started
    |   |   ├── train              # Training
    |   |   |   ├── A              # Contains domain A images 
    |   |   |   └── B              # Contains domain B images 
    |   |   └── test               # Testing
    |   |   |   ├── A              # Contains domain A images 
    |   |   |   └── B              # Contains domain B images 



### 2. Train

```
python train.py --cuda 
```

### 3. Test	

```python
python test --cuda  # cmd mode
python Ui.py # Ui mode
```

### 4.Others

##### The structure of the CycleGAN has been plotted and stored in the /structure folder. Also you can plot it by 

```
python netplt.py
```

###### The /output folder stores the transformed image and the training *.pth. 

##### Implement basic linear interpolation to realize gradient change from initial image to transformed image .

### 5. Summary

##### The current project achieved basic monet-style-transformation, it remains much to do.