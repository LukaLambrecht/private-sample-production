# Basic file readability checks of privately produced NanoAOD


import os
import sys
import numpy as np
import awkward as ak
from coffea.nanoevents import NanoEventsFactory, NanoAODSchema
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
            events = NanoEventsFactory.from_root(
               {inputfile: 'Events'},
               schemaclass=NanoAODSchema).events()
            nevents = ak.num(events.run.compute(), axis=0)
        except:
            failed.append(inputfile)
    print()

    # print results
    print('Read {} files, of which {} seem to have failed.'.format(len(args.inputfiles), len(failed)))
    if len(failed)>0: print(failed)
