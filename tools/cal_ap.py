import argparse
import os

import mmcv
import torch
from mmcv import Config, DictAction
from mmcv.parallel import MMDataParallel, MMDistributedDataParallel
from mmcv.runner import get_dist_info, init_dist, load_checkpoint
from tools.fuse_conv_bn import fuse_module

from mmdet.apis import multi_gpu_test, single_gpu_test
from mmdet.core import wrap_fp16_model
from mmdet.datasets import build_dataloader, build_dataset
from mmdet.models import build_detector

'''
export PYTHONPATH=${PWD}:$PYTHONPATH
python3 tools/cal_ap.py tools/cal_ap_config.py --user_json submits/atss_r50_fpn_ms12_results.bbox.json --eval bbox
'''

def parse_args():
    parser = argparse.ArgumentParser(
        description='MMDet test (and eval) a model')
    parser.add_argument('config', help='test config file path')
    parser.add_argument('--user_json', help='user json')
    parser.add_argument(
        '--eval',
        type=str,
        nargs='+',
        help='evaluation metrics, which depends on the dataset, e.g., "bbox",'
        ' "segm", "proposal" for COCO, and "mAP", "recall" for PASCAL VOC')
    args = parser.parse_args()
    return args


def main():
    args = parse_args()

    cfg = Config.fromfile(args.config)
    # set cudnn_benchmark
    cfg.data.test.test_mode = True

    # build the dataloader
    # TODO: support multiple images per gpu (only minor changes are needed)
    dataset = build_dataset(cfg.data.test)

    print(args.user_json)

    #with open(args.user_json, 'r') as f:
    #outputs = mmcv.load(args.user_json)
    outputs = args.user_json

    kwargs = {}
    res = dataset.evaluate_json(outputs, args.eval, **kwargs)
    print(res)

    print(res['bbox_mAP'])

if __name__ == '__main__':
    main()
