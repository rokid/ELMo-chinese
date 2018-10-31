

import argparse

from bilm.training import dump_weights as dw


if __name__ == '__main__':
    parser = argparse.ArgumentParser()
    parser.add_argument('--save_dir', default="../log/", help='Location of checkpoint files')
    parser.add_argument('--outfile', default="../dump_weights.hdf5",help='Output hdf5 file with weights')

    args = parser.parse_args()
    dw(args.save_dir, args.outfile)

