# CarDetectionExample
Sinovation Ventures Challenge

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

### Test & Submit Result

```
./tools/dist_test.sh local_config/atss_r50_fpn_ms12.py pretrain_model/atss_r50_fpn_ms12.model 8 --format-only --options "jsonfile_prefix=./submit_atss_r50_fpn_ms12_results"
```

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

## Submit 

每支队伍将如下文件夹用tar打包：
```
tar -zcvf team_english_name.tar.gz team_english_name
```
并将 team_english_name.tar.gz 于7月28日12:00前发送至 xiangli@momenta.ai, 注意team_english_name替换为真实的队伍英文名
文件命名格式如下(#号后为说明，不包括在名字中)

```
team_english_name           # 更新为真实的队伍英文名字
├── CarDetectionExample     # 能够复现本队伍较紧T1条件下模型的代码, 供主办方复现及T1条件核查
├── submit_T0_results       # T0条件下模型在testA上的预测结果
├── submit_T1_results       # T1条件下模型在testA上的预测结果
├── T1.model                # T1条件下的训练好的模型，用于生成submit_T1_results
├── README.md               # README必须包含如下内容，具体的超参数配置可以有变化
│   ├── Training Cmd: 
│   │   ├── ./tools/dist_train.sh local_config/team_english_name.py 8
│   ├── Submit Cmd:
│   │   ├── ./tools/dist_test.sh local_config/team_english_name.py ../T1.model 8 --format-only --options "jsonfile_prefix=./submit_T1_results"
│   ├── Complexity Check Cmd
│   │   ├── python3 ./tools/get_flops.py local_config/team_english_name.py --shape 640 400
│   │   ├── python3 ./tools/benchmark.py local_config/team_english_name.py ../T1.model --fuse-conv-bn
```

## 0728 Final Record

截止7.28提交队伍的成绩如下，经代码核验成绩均有效。

| 排名 | 队伍英文名    |  T1 性能 | 测速(fps) | Flops(GMac) | Params (M) | T0 性能 |
| ---: | ----------    |  :-----: | :-------: | :---------: | :--------: | :-----: |
| 1    | Faster_Better |  80.4    | 99.3      | 19.05       | 10.72      |   80.4  |
| 2    | xitianqujing  |  80.2    | 51.7      | 33.03       | 26.30      |   83.0  |
| 3    | flying        |  79.0    | 27.2      | 19.04       | 14.65      |   79.0  |

## 0708 Record

截止7.8提交队伍的成绩如下，经代码核验成绩均有效。

| 排名 | 队伍英文名    |  T1 性能 | 测速(fps) | Flops(GMac) | Params (M) | T0 性能 |
| ---: | ----------    |  :-----: | :-------: | :---------: | :--------: | :-----: |
| 1    | Faster_Better |  76.7    | 98.5      | 16.88       | 10.66      |   --    |
| 2    | xitianqujing  |  75.7    | 51.4      | 10.32       |  6.58      |   77.7  |
| 3    | flying        |  39.0    | 52.4      | 9.93        |  6.35      |   --    |


