_base_ = './fcos_r50_caffe_fpn_gn-head_4x4_1x_coco.py'
model = dict(
    pretrained='open-mmlab://resnet101_caffe_bgr', backbone=dict(depth=101))
