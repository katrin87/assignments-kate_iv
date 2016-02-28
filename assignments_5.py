#! /usr/bin/env python


from __future__ import division, print_function

NUCLEOTIDES = ["A", "G", "T", "C"]
CODONS = {
        "TTT": "F",
        "TTC": "F",
        "TTA": "L",
        "TTG": "L",
        "CTT": "L",
        "CTC": "L",
        "CTA": "L",
        "CTG": "L",
        "ATT": "I",
        "ATC": "I",
        "ATA": "I",
        "ATG": "M",
        "GTT": "V",
        "GTC": "V",
        "GTA": "V",
        "GTG": "V",
        "TCT": "S",
        "TCC": "S",
        "TCA": "S",
        "TCG": "S",
        "CCT": "P",
        "CCC": "P",
        "CCA": "P",
        "CCG": "P",
        "ACT": "U",
        "ACC": "U",
        "ACA": "U",
        "ACG": "U",
        "GCT": "A",
        "GCC": "A",
        "GCA": "A",
        "GCG": "A",
        "TAT": "Y",
        "TAC": "Y",
        "CAT": "H",
        "CAC": "H",
        "CAA": "Q",
        "CAG": "Q",
        "AAT": "N",
        "AAC": "N",
        "AAA": "K",
        "AAG": "K",
        "GAT": "D",
        "GAC": "D",
        "GAA": "E",
        "GAG": "E",
        "TGT": "C",
        "TGC": "C",
        "TGG": "W",
        "CGT": "R",
        "CGC": "R",
        "CGA": "R",
        "CGG": "R",
        "AGT": "S",
        "AGC": "S",
        "AGA": "R",
        "AGG": "R",
        "GGT": "G",
        "GGC": "G",
        "GGA": "G",
        "GGG": "G",
        "TAA": ".",
        "TAG": ".",
        "TGA": "."

}


def translator(triplet):
    if triplet in CODONS.keys():
        return CODONS[triplet]

def reconstruct_protein_alignment(args):
    """
    "Greedy" Reconstructs the aligned protein sequences on the base of aligned nucleotide sequences.
    Assumptions: nucleotide sequences consist only from coding regions, three gaps in nucleotide
    sequence equal for one gap in protein sequence
    :type args: str
    :param args: aligned DNA sequence
    :return: tuple of aligned protein sequence
    """
    aminoacid_seq_massive = []
    for seq in args:
        if len(seq) % 3:
            raise ValueError ("The length of sequences is not multiple of three")
        GAP = "-"
        triplet = []
        gap_counter = 0
        aminoacid_seq = []
        for char in seq:
            if char == GAP:
                gap_counter += 1
            elif char in NUCLEOTIDES:
                triplet.append(char)
            else:
                raise ValueError ("Incorrect symbol in sequence")
            if gap_counter == 3:
                aminoacid_seq.append(GAP)
                gap_counter = 0
            if len(triplet) == 3:
                aminoacid_seq.append(translator(''.join(triplet)))
                triplet = []
        aminoacid_seq_massive.append(''.join(aminoacid_seq))
    return tuple(aminoacid_seq_massive)

args = ("AAAGGGTTT", "AA-GGGT--", "TAAGGGTTT")
print(reconstruct_protein_alignment(args))