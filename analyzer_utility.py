import os
import logging

fmt = '%(asctime)s: %(message)s'

logging.basicConfig(format=fmt)

def check_dir(root_dir, dir_path):
    try:
        for root, dir, files in os.walk(root_dir):
            if dir_path in dir:
                logging.info('Directory Found at {}'.format(root_dir+dir_path))
                return True
            else:
                logging.debug('Please make sure path is correct or not: {}'.format(root_dir+dir_path))
                return False
    except Exception as err:
        logging.error('In check_dir function: {}'.format(err.__str__()))


def check_images(path):
    try:
        images = [img for img in os.listdir(path) if img.endswith('.jpg')]
        if len(images) > 0:
            logging.info('{} Images Found at {}.'.format(len(images), path))
            return len(images), True
        else:
            logging.info('{} Images Found at {}, Please add Images.'.format(len(images), path))
            return len(images), False    
    except Exception as err:
        logging.error('In the check_images {}'.format(err.__str__()))


def check_labels(path):
    try:
        labels = [txt for txt in os.listdir(path) if txt.endswith('.txt')]

        if len(labels) > 0:
            logging.info('{} Labels Found at {}.'.format(len(labels), path))
            return len(labels), True
        else:
            logging.info('{} Labels Found at {}, Please add labels.'.format(len(labels), path))
            return len(labels), False 

    except Exception as err:
        logging.error('In the check_labels {}'.format(err.__str__()))




def analyze_data(root_dir):

    try:
        if os.path.isdir(root_dir):
            train_dir = check_dir(root_dir, 'train')
            val_dir = check_dir(root_dir, 'val')

            if train_dir and val_dir:
                logging.info('Train and Val Found.')
                train_images_dir = os.path.join(root_dir, 'train')
                val_images_dir = os.path.join(root_dir, 'val')

                train_images = check_dir(train_images_dir, 'images')
                val_images = check_dir(val_images_dir, 'images')
                if train_images and val_images:
                    train_img_len, train_images = check_images(train_images_dir+'/images')
                    val_img_len, val_images = check_images(val_images_dir+'/images')

                    if train_images and val_images:
                        logging.info('Found images in both train and val images folder.')
                        train_labels_dir = os.path.join(root_dir, 'train')
                        val_labels_dir = os.path.join(root_dir, 'val')

                        train_labels = check_dir(train_labels_dir,'labels')
                        val_labels = check_dir(val_labels_dir,  'labels')

                        if train_labels and val_labels:
                            train_label_len, train_labels = check_labels(train_labels_dir+'/labels')
                            val_label_len, val_labels = check_labels(val_labels_dir+'/labels')

                            if train_labels and val_labels:
                                if train_label_len == train_img_len:
                                    return True
                                else:
                                    logging.error('Length of train images and labels are not Matched, Please Make Sure length need to same images: {} and labels{}'.format(train_img_len, val_label_len))
                                    return False
                            else:
                                logging.error('One of this labels are empty check train: {} and labels: {}'.format(train_label_len, val_label_len))
                                return False
                        else:
                            logging.error('One of this Folder is Missing, Check both folder are available or not at locations, train_labels: {} and val_labels: {}'.format(train_labels_dir, val_labels_dir))
                            return False

                    else:
                        logging.error('No Images Found. One of this Directory is empty, Check train_imges folder: {} and val_images folder: {}'.format(train_images_dir, val_images_dir))
                        return False

                else:
                    logging.error('Please Make sure images folder available in train and val Floder.')
                    return False

            else:
                logging.error('Make sure both train and val need to present in the root dir: {}'.format(root_dir))
                return False


    except Exception as err:
        logging.error('In the analyze_data {}'.format(err.__str__()))
        return False
        