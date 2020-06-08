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
