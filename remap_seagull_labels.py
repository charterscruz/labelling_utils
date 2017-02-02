#!/usr/bin/env python
"""
The goal of this script if to remap ground truth files from a given resolution to another
"""

import numpy as np
import sys
import argparse


def main(argv):
#    pycaffe_dir = os.path.dirname(__file__)

    parser = argparse.ArgumentParser()
    # Required arguments: input and output files.
    parser.add_argument(
        "input_results_file",
        help="Results to load"
    )

    parser.add_argument(
        "output_results_file",
        help="where to write"
    )
    parser.add_argument(
        "old_width",
        help="old width used to create the lebal"
    )
    parser.add_argument(
        "old_height",
        help="old height used to create the lebal"
    )

    parser.add_argument(
        "new_width",
        help="new width used to create the lebal"
    )
    parser.add_argument(
        "new_height",
        help="new height used to create the lebal"
    )

    args = parser.parse_args()

    # Load label
    label_file = np.loadtxt(args.input_results_file)
    print label_file

    # compute scale change
    fx = float(args.new_width) / float(args.old_width)
    fy = float(args.new_height) / float(args.old_height)

    label_file[:, 2] = label_file[:, 2] * fx
    label_file[:, 3] = label_file[:, 3] * fy
    label_file[:, 4] = label_file[:, 4] * fx
    label_file[:, 5] = label_file[:, 5] * fy

    np.savetxt(args.output_results_file, label_file, fmt = '%1.4f')


if __name__ == '__main__':
    main(sys.argv)

