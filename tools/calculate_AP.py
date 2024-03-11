#!/usr/bin/env python
# Copyright (c) Facebook, Inc. and its affiliates.

import logging
import torch
import argparse
from detectron2.engine import (
    default_argument_parser,
)
from detectron2.evaluation.coco_evaluation import _evaluate_predictions_on_coco

logger = logging.getLogger("detectron2")

# args = default_argument_parser().parse_args()
args = argparse.ArgumentParser(description="visualize the pth result")
args.add_argument('--pth', default="tooth_ins_out/inference/UESB_t_test/instances_predictions.pth", help="the pred pth path")
# args.add
def main(args):
    path = "tooth_ins_out/inference/UESB_t_test/instances_predictions.pth"
    pth_ = torch.load(path)
    print("pth:",pth_)
    return 0

# # if your dataset is in COCO format, this cell can be replaced by the following three lines:
# from detectron2.data.datasets import register_coco_instances

# register_coco_instances("UESB_t_train", {}, "tooth_ins/UESB_t/annotations/train.json", "tooth_ins/UESB_t/train")
# register_coco_instances("UESB_t_test", {}, "tooth_ins/UESB_t/annotations/test.json", "tooth_ins/UESB_t/test")


if __name__ == "__main__":
    main(args) # pragma: no cover
