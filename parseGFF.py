#! /usr/bin/env python3

import argparse
import csv
from Bio import SeqIO
from Bio.Seq import Seq

def get_args():
    # create an ArgumentParser object
    parser = argparse.ArgumentParser(description='This script parses and does some \
        neat stuff with a GFF file')

    # add positional arguments (these are the ones that are absolutely essential/required)
    parser.add_argument("gff", help="name of GFF file")
    parser.add_argument("fasta", help="name of FASTA file")

    # add optional arguments
    # if 'store_true', this means assign 'True' if the argument is specified on the command
    # line, so the default for 'store_true' is false
    # parser.add_argument("-v", "--verbose", help="Print verbose output or not", action='store_true')

    # parse the actual arguments
    return parser.parse_args()

def parse_fasta():
    # read and parse the FASTA file
    # read() assumes one sequence only in the FASTA file
    return SeqIO.read(args.fasta, 'fasta')

def revcomp(seq):
    return seq.reverse_complement()

def translate(dna):
    dna = dna.upper()
    rna = dna.replace("T", "U")
    protein = rna.translate()
    return protein

def parse_gff(genome_object):

    # print(genome_object)

    genome_sequence = genome_object.seq

    # read GFF file line by line
    with open(args.gff, 'r') as gff_file:

        # create a csv reader object
        reader = csv.reader(gff_file, delimiter="\t")

        # read the actual lines
        for line in reader:
            organism     = line[0]
            feature_type = line[2]
            start        = int(line[3])
            end          = int(line[4])
            strand       = line[6]
            attributes   = line[-1]

            if feature_type == 'CDS':

                # extract the sequence of this feature from the genome
                feature_seq = genome_sequence[start-1:end]

                if strand == '-':
                    feature_seq = revcomp(feature_seq)

                #print(len(feature_seq)/3)

                # print FASTA nucleotide sequence for this gene
                print('>' + organism + attributes)
                print(translate(feature_seq))




def main():
    genome_sequence = parse_fasta()
    parse_gff(genome_sequence)

# get the command line arguments
args = get_args()


# set the environment for this script
# is it main, or is this a module being called by another script
if __name__ == '__main__':
    main()