# CarDetectionExample

Fresh Challenge

## Installation

Please refer to [install.md](docs/install.md) for installation and dataset preparation.


## Get Started

Please see [getting_started.md](docs/getting_started.md) for the basic usage of MMDetection.


## Quick Example of ATSS baseline for Car Detection

Link the dataset to the folder "./data/" under this repo.
```
ln -s path/to/dataset data
```

### Train

```
./tools/dist_train.sh local_config/atss_r50_fpn_ms12.py 8
```
Note that the model of this example is trained under 8-GPU settings. If you donot have enough GPU cards, try to adjust some related settings for efficient training.

Run `test_example.ipynb` to see detected results (see as follows) of pretrained baseline model. The baseline model is relatively weak, try your best to improve it~!

![car_detection](https://github.com/implus/CarDetectionExample/blob/master/car.png)

### Complexity Check

Pay attention to the constraints of the complexity for your detectors. The following commands are used for official judgements, with 640x400 images for inference.
```
python3 ./tools/get_flops.py local_config/atss_r50_fpn_ms12.py --shape 640 400
python3 ./tools/benchmark.py local_config/atss_r50_fpn_ms12.py pretrain_model/atss_r50_fpn_ms12.model --fuse-conv-bn
```

## About MMDetection Framework

MMDetection is an open source project that is contributed by researchers and engineers from various colleges and companies. The technical report is on [ArXiv](https://arxiv.org/abs/1906.07155).

Documentation: https://mmdetection.readthedocs.io/

The branch works with **PyTorch 1.3 to 1.5**.

This project is released under the [Apache 2.0 license](LICENSE).


## 此前比赛队伍记录

截止7.28提交队伍的成绩如下，经代码核验成绩均有效。

| 排名 | 队伍英文名    |  性能    | 测速(fps) | Flops(GMac) | Params (M) |
| ---: | ----------    |  :-----: | :-------: | :---------: | :--------: |
| 1    | Faster_Better |  80.4    | 99.3      | 19.05       | 10.72      |
| 2    | xitianqujing  |  80.2    | 51.7      | 33.03       | 26.30      |
| 3    | flying        |  79.0    | 27.2      | 19.04       | 14.65      |

## 0708 Record

截止7.8提交队伍的成绩如下，经代码核验成绩均有效。

| 排名 | 队伍英文名    |  性能    | 测速(fps) | Flops(GMac) | Params (M) |
| ---: | ----------    |  :-----: | :-------: | :---------: | :--------: |
| 1    | Faster_Better |  76.7    | 98.5      | 16.88       | 10.66      |
| 2    | xitianqujing  |  75.7    | 51.4      | 10.32       |  6.58      |
| 3    | flying        |  39.0    | 52.4      | 9.93        |  6.35      |
