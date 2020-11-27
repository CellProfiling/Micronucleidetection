from hpacellseg import cellsegmentator
import os.path
import numpy as np
import scipy.ndimage as ndi
import skimage.transform as transform
import imageio
import click
from utils import download_with_url

NMODEL = 'nuclei_model.pth'
CMODEL = 'cell_model.pth'
CURL = "https://kth.box.com/shared/static/he8kbtpqdzm9xiznaospm15w4oqxp40f.pth"
NURL = "https://kth.box.com/shared/static/l8z58wxkww9nn9syx9z90sclaga01mad.pth"


@click.command()
@click.argument('image', required=True, type=str)
@click.argument('output', required=True, type=str)
@click.option('--binarize', is_flag=True)
def main(image, output, binarize):
    segmentator = cellsegmentator.CellSegmentator(NMODEL, CMODEL)
    in_image = imageio.imread(image)
    n_labels = segmentator.label_nuclei([in_image])[0]
    n_labels = transform.resize(
            n_labels,
            (n_labels.shape[0]*4, n_labels.shape[1]*4))

    subgreen = n_labels[..., 2] * np.logical_not(n_labels[..., 1] > 0)
    labels = ndi.label(subgreen)[0]

    if binarize:
        labels = (labels > 0).astype(np.uint8)
        labels *= 255
    imageio.imsave(output, labels)


if __name__ == '__main__':
    if not os.path.exists(CMODEL):
        print('Downloading cell model')
        print('May take a few moments')
        download_with_url(CURL, CMODEL)
    if not os.path.exists(NMODEL):
        print('Downloading nuclei model')
        print('May take a few moments')
        download_with_url(NURL, NMODEL)
    main()
