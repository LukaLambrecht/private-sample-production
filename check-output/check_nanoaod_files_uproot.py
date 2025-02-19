# Basic file readability checks of privately produced NanoAOD


import os
import sys
import uproot
import argparse


if __name__=='__main__':

    # read command line arguments
    parser = argparse.ArgumentParser()
    parser.add_argument('-i', '--inputfiles', required=True, type=os.path.abspath, nargs='+',
      help='Path to NanoAOD file(s) to check')
    args = parser.parse_args()

    # read input files
    failed = []
    for idx, inputfile in enumerate(args.inputfiles):
        print('Reading file {} / {}...'.format(idx+1, len(args.inputfiles)), end='\r')
        try:
            with uproot.open(f'{inputfile}:Events') as tree:
                nevents = tree.num_entries
        except:
            failed.append(inputfile)
    print()

    # print results
    print('Read {} files, of which {} seem to have failed.'.format(len(args.inputfiles), len(failed)))
    if len(failed)>0: print(failed)
