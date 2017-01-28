import numpy as np
import sys
import argparse


print "Starting script..."


def main(argv):
#    pycaffe_dir = os.path.dirname(__file__)

    parser = argparse.ArgumentParser()
    # Required arguments: input and output files.
    parser.add_argument(
        "input_results_file",
        help="Results to load"
    )
    parser.add_argument(
        "width",
        help="width of the video file"
    )
    parser.add_argument(
        "height",
        help="height of the video file"
    )

    args = parser.parse_args()

    label_file = np.loadtxt(args.input_results_file)

    print('min width ', np.min(label_file[:, 3]))
    print('max width ', np.max(label_file[:, 3]))

    print('min height ', np.min(label_file[:, 4]))
    print('max height ', np.max(label_file[:, 4]))

    # close to the left edge
    adjacent_to_left = label_file[:, 1] <= 1
    adjacent_to_top = label_file[:, 2] <= 1

    adjacent_to_right = ((label_file[:, 1] + label_file[:, 3]) >= (int(args.width))-1)
    adjacent_to_bottom = ((label_file[:, 2] + label_file[:, 4]) >= (int(args.height))-1)

    print('np.count_nonzero(adjacent_to_top): ', np.count_nonzero(adjacent_to_top))
    print('np.count_nonzero(adjacent_to_left): ', np.count_nonzero(adjacent_to_left))
    print('np.count_nonzero(adjacent_to_right): ', np.count_nonzero(adjacent_to_right))
    print('np.count_nonzero(adjacent_to_bottom): ', np.count_nonzero(adjacent_to_bottom))

if __name__ == '__main__':
    main(sys.argv)

