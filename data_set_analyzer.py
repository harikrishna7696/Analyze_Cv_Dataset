from data_gradients.managers.detection_manager import DetectionAnalysisManager
from data_gradients.datasets.detection import YoloFormatDetectionDataset
import os
from analyzer_utility import analyze_data
import argparse
import logging

fmt = '%(asctime)s: %(message)s'

logging.basicConfig(format=fmt)

def run_analyzer(dir, title):
    classes_names = []
    if os.path.isfile(dir+'classes.txt'):
        with open(dir+'classes.txt', 'r') as f:
            for i in f.readlines():
                classes_names.append(i.strip())
    else:
        logging.error('{} is not Found. Please Make user classes.txt is present and include class names.'.format(dir+'classes.txt'))
        return

    ret = analyze_data(dir)
    if ret and classes_names:
        train_data = YoloFormatDetectionDataset(root_dir=dir, images_dir=os.path.join(dir, 'train', 'images'), labels_dir=os.path.join(dir, 'train', 'labels'), ignore_invalid_labels=True)
        test_data = YoloFormatDetectionDataset(root_dir=dir, images_dir=os.path.join(dir, 'val', 'images'),labels_dir=os.path.join(dir, 'val', 'labels'), ignore_invalid_labels=True)
        analyzer = DetectionAnalysisManager(report_title=title, train_data=train_data, val_data=test_data, class_names=classes_names, is_label_first=True, bbox_format='cxcywh')
        analyzer.run()

if __name__ == '__main__':
    parser = argparse.ArgumentParser()
    parser.add_argument('--root_dir', '-r', required=True, type=str, help='Give the folder where train, val and classes.txt is present')
    parser.add_argument('--title', '-t', required=True, type=str, help='Give the title name result will store in title folder')
    # parser.add_argument('')

    opt = parser.parse_args()
    run_analyzer(opt.root_dir, opt.title)