# BasketballGAN
### Generate the ghosting defensive strategies given offensive sketch.
![](https://drive.google.com/uc?export=view&id=1lmxvBG-PTLg4vhEF_hmG1IS20vDEyvyv)
<img align="right" src="https://drive.google.com/uc?export=view&id=1QWN9BtFgaAKA1tvx_ePQku934CeCWIRl" width="400" title="A Generated Play"/>

## [Paper](TODO) | [Video](https://drive.google.com/open?id=1HD7-L2MKX8f0Xp6jhSBgJtr7Ui9ReiUE) | [Supplemental](https://drive.google.com/a/nvidia.com/file/d/1dXMA_1AjpPu7J4_Iw1yb6pp-9d9Lp2uN/view?usp=sharing)

### BasketballGAN: Generating Basketball Play Simulation through Sketching

Hsin-Ying Hsieh<sup>1</sup>, Chieh-Yu Chen<sup>2</sup>, Yu-Shuen Wang<sup>1</sup> and Jung-Hong Chuang<sup>1</sup>

<sup>1</sup>National Chiao Tung University, <sup>2</sup>NVIDIA Corporation

In [ACMMM 2019](https://www.acmmm.org/2019/).

## Prerequisites
- OS: Linux
- [NVIDIA Dokcer](https://github.com/NVIDIA/nvidia-docker)
- [NVIDIA NGC Tensorflow Docker Image](https://ngc.nvidia.com/catalog/containers/nvidia:tensorflow)
- NVIDIA GPU (V100 16GB)

### Dataset

## Getting Stated # TODO
```bash
~$ git clone https://gitlab-master.nvidia.com/dl/sae-taiwan/nctu_cgvlab_bballgan.git
~$ cd nctu_cgvlab_bballgan
nctu_cgvlab_bballgan$ docker login nvcr.io
nctu_cgvlab_bballgan$ docker pull nvcr.io/nvidia/tensorflow:19.06-py2
nctu_cgvlab_bballgan$ docker run --runtime=nvidia -it --rm -v $PWD:$PWD nvcr.io/nvidia/tensorflow:19.06-py2 bash
```

### Download Dataset 
- create 'data' folder
- save [dataset](https://drive.google.com/a/nvidia.com/file/d/1955WfjX2xtHVb6QAJ70zLQH65V0JD_e3/view?usp=sharing) under folder 'data'
```bash
nctu_cgvlab_bballgan$ mkdir data
```

### Training
```bash
nctu_cgvlab_bballgan$ cd src
nctu_cgvlab_bballgan/src$ python Train_Triple.py --folder_path='tmp' --data_path='data'
```

### Monitoring
```bash
nctu_cgvlab_bballgan/src$ tensorboard --logdir='tmp/Log'
```

### Logs/Samples/Checkpoints
- nctu_cgvlab_bballgan/src/tmp/Log: training summary for tensorboard
- nctu_cgvlab_bballgan/src/tmp/Samples: generated videos sampled on different iterations
- nctu_cgvlab_bballgan/src/tmp/Checkpoints: tensorflow checkpoints on different iterations

## Citation (TODO)
If you find this useful for your research, please use the following.

``` 
@inproceedings{hsieh2019basketballgan,
  title={BasketballGAN: Generating Basketball Play Simulation through Sketching},
  author={Hsin-Ying Hsieh, Chieh-Yu Chen, Yu-Shuen Wang and Jung-Hong Chuang},  
  booktitle={2019 ACM Multimedia Conference on Multimedia Conference},
  year={2019}
}
```