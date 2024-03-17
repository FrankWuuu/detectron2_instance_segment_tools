#!/usr/bin/env python
# Copyright (c) Facebook, Inc. and its affiliates.
# copy from detectron2/tools/visualize_data.py
# visualize the annotation json to images
import argparse
import os
from itertools import chain

import cv2
import tqdm

from detectron2.config import get_cfg
from detectron2.data import (
    build_detection_train_loader,
    DatasetCatalog,
    detection_utils as utils,
    MetadataCatalog,
)
from detectron2.data.build import filter_images_with_few_keypoints
from detectron2.utils.logger import setup_logger
from detectron2.utils.visualizer import Visualizer


def setup(args):
    cfg = get_cfg()
    if args.config_file:
        cfg.merge_from_file(args.config_file)
    cfg.merge_from_list(args.opts)
    cfg.DATALOADER.NUM_WORKERS = 0
    cfg.freeze()
    return cfg


def parse_args(in_args=None):
    parser = argparse.ArgumentParser(description="Visualize ground-truth data")
    # parser.add_argument(
    #     "--source",
    #     choices=["annotation", "dataloader"],
    #     required=True,
    #     help="visualize the annotations or the data loader (with pre-processing)",
    # )
    # parser.add_argument("--config-file", metavar="FILE", help="path to config file")
    parser.add_argument("--output-dir", default="tooth_ins_out/test_bi", help="path to output directory")
    parser.add_argument("--KEYPOINT_ON", default=False, help="KEYPOINT on or not")
    parser.add_argument("--show", action="store_true", help="show output in a window")
    parser.add_argument(
        "opts",
        help="Modify config options using the command-line",
        default=None,
        nargs=argparse.REMAINDER,
    )
    return parser.parse_args(in_args)


def main() -> None:
    global img
    args = parse_args()
    logger = setup_logger()
    logger.info("Arguments: " + str(args))
    # cfg = setup(args)

    dirname = args.output_dir
    # dirname = cfg.OUTPUT_DIR

    os.makedirs(dirname, exist_ok=True)
    # metadata = MetadataCatalog.get(cfg.DATASETS.TRAIN[0])
    # metadata = MetadataCatalog.get(cfg.DATASETS.TEST[0])
    metadata = MetadataCatalog.get("UESB_t_test")

    def output(vis, fname):
        if args.show:
            print(fname)
            cv2.imshow("window", vis.get_image()[:, :, ::-1])
            cv2.waitKey()
        else:
            filepath = os.path.join(dirname, fname)
            print("Saving to {} ...".format(filepath))
            vis.save(filepath)

    scale = 1.0

    dicts = list(
        # chain.from_iterable([DatasetCatalog.get(k) for k in cfg.DATASETS.train])
        chain.from_iterable([DatasetCatalog.get(k) for k in ("UESB_t_test",)])
    )
    # if cfg.MODEL.KEYPOINT_ON:
    if args.KEYPOINT_ON:
        dicts = filter_images_with_few_keypoints(dicts, 1)
    for dic in tqdm.tqdm(dicts):
        img = utils.read_image(dic["file_name"], "RGB")
        visualizer = Visualizer(img, metadata=metadata, scale=scale)
        vis = visualizer.draw_dataset_dict(dic)
        output(vis, os.path.basename(dic["file_name"]))


# if your dataset is in COCO format, this cell can be replaced by the following three lines:
from detectron2.data.datasets import register_coco_instances
register_coco_instances("UESB_t_train", {}, "tooth_ins/UESB_t/annotations/train.json", "tooth_ins/UESB_t/train")
register_coco_instances("UESB_t_test", {}, "tooth_ins/UESB_t/annotations/test.json", "tooth_ins/UESB_t/test")


if __name__ == "__main__":
    main()  # pragma: no cover
