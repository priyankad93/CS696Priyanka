"""
Homework 01
DO NOT RENAME THIS FILE OR ANY DEFINITIONS!
Place this file in your github repo inside of a folder titled "Homework".
"""
import os

# String Functions
def fast_complement(dna):
    """
    Uses a dictionary to convert a DNA sequence into the complement strand.  C <--> G,  T <--> A
    :param dna: a string containing only the characters C, T, A, and G
    :return: a string containing only the characters C, T, A, and G
    """
    a = {'A': 'T', 'T': 'A', 'C': 'G', 'G': 'C'}
    fastComplement = ''
    for eachCharInDNA in dna:
        fastComplement+= a.get(eachCharInDNA) #used to be of complexity O(n2) now its O(n) Cpython
    return fastComplement

def remove_interval(s, start, stop):
    """
    Removes the interval of characters from a string or list inclusively, 0 based
    EX: remove_intervals('ABCDEFGHI', 2, 5) will return 'ABGHI'.
    :param s: a string
    :param start: a non-negative integer
    :param stop: a non-negative integer greater than the start integer.
    :return: a string
    """
    # count=0
    # substringOfS=''
    # for eachCharInString in s :
    #     if count>=start and count<=stop:
    #         count+=1
    #         continue
    #     substringOfS+=eachCharInString
    #     count+=1
    # return substringOfS

    return s[:start] + s[stop + 1:]

def kmer_list(s, k):
    """
    Generates all kmers of size k for a string s and store them in a list
    :param s: any string
    :param k: any integer greater than zero
    :return: a list of strings
    """
    listOfKmers=[]
    possibleKmers = len(s)-k+1
    for i in range(0,possibleKmers):
        listOfKmers.append(s[i:i+k])
    return listOfKmers

def kmer_set(s, k):
    """
    Generates all kmers of size k for a string s and store them in a set
    :param s: any string
    :param k: any integer greater than zero
    :return: a set of strings
    """
    listOfKmers = set()
    possibleKmers = len(s) - k + 1
    for i in range(0, possibleKmers):
        listOfKmers.add(s[i:i + k])
    return listOfKmers


def kmer_dict(s, k):
    """
    Generates all kmers of size k for a string s and store them in a dictionary with the
    kmer(string) as the key and the number of occurances of the kmer as the value(int).
    :param s: any string
    :param k: any integer greater than zero
    :return: a set of strings
    """
    listOfKmers = {}
    possibleKmers = len(s) - k + 1
    for i in range(0, possibleKmers):
        kmer = s[i:i + k]
        listOfKmers[kmer] = listOfKmers.get(kmer,0)+1
    return listOfKmers


# Reading Files
def head(file_name):
    """
    Prints the FIRST 10 lines of a file
    :param file_name: a string
    :return: None
    """

    with open(file_name) as file:
        print(''.join(file.readlines()[0:10]).rstrip())
    return

def tail(file_name):
    """
    Prints the LAST 10 lines of a file
    :param file_name: a string
    :return: None
    """

    with open(file_name) as file:
        print(''.join(file.readlines()[-10:]).rstrip())
    return

def print_even(file_name):
    """
    Prints the even numbered lines of a file
    :param file_name: a string
    :return: None
    """


    with open(file_name) as file:
        print(''.join(file.readlines()[1::2]).rstrip())
    return

def csv_list(file_name):
    """
    Read in a CSV file to a 2D array (In python it is a list of lists)
    :param file_name: a string
    :return: a list of lists
    """

    mylist=[]
    with open(file_name) as f:
        for i in f:
            mylist.append(i.rstrip().split(','))
    return mylist

def get_csv_column(file_name, column):
    """
    Reads in a CSV file and returns a list of values belonging to the column specified
    :param file_name: a string
    :param column: a positive integer
    :return: a list
    """
    mylist = []
    with open(file_name) as f:
        for i in f:
            mylist.append(i.rstrip().split(','))
    csv_column=[]
    for i in mylist:
        csv_column.append(i[column-1]) #since list start with 0
    return csv_column

def fasta_seqs(file_name):
    """
    Reads in a FASTA file and returns a list of only the sequences
    :param file_name: a string
    :return: a list of strings
    """
    mylist=[]
    with open(file_name) as fastaFile:
        text=fastaFile.read().split('>')
        for i in text[1:]:
            mylist.append(i.split('\n',1)[1].replace('\n',''))
    return mylist

def fasta_headers(file_name):
    """
    Reads in a FASTA file and returns a list of only the headers (Lines that start with ">")
    :param file_name: a string
    :return: a list of strings
    """
    mylist = []
    with open(file_name) as fastaFile:
        text = fastaFile.read().split('>')
        for i in text[1:]:
            mylist.append(i.split('\n', 1)[0].replace('\n', ''))
    return mylist


def fasta_dict(file_name):
    """
    Reads in a FASTA file and returns a dictionary of the format {header: sequence, ...}, where
    the sequence headers are keys and the sequence is the value
    :param file_name: a string
    :return: a dictionary
    """
    mydict = {}
    with open(file_name) as fastaFile:
        text = fastaFile.read().split('>')
        for i in text[1:]:
            mydict[i.split('\n', 1)[0].replace('\n', '')]=i.split('\n', 1)[1].replace('\n', '')
    return  mydict


def fastq_to_fasta(file_name, new_name=None):
    """
    Reads in a FASTQ file and writes it to a new FASTA file. This definition should also
    keep the same file name and change the extension to from .fastq to .fasta if new_name is not specified.
    EX: fastq_to_fasta('ecoli.fastq') should write to a new file called ecoli.fasta
    :param file_name: a string
    :param new_name: a string
    :return: None
    """

    newFileName=new_name
    # print(newFileName)
    # print(file_name)
    if new_name!='None':
        newFileName=file_name.replace('.fastq','.fasta')
    with open(file_name,'r') as fastqFile:
        text=fastqFile.read().split('@')
    with open(newFileName,"w+") as fastaFile:
        for i in text[1:]:
            fastaFile.write('>'+i.split('+')[0])


# Transcription and Translation
def reverse_complement(dna):
    """
    Returns the strand of DNA that is the reverse complement of the sequence given
    :param dna: a string containing only the characters C, T, A, and G
    :return: a string containing only the characters C, T, A, and G
    """
    return fast_complement(dna)[::-1]

def transcribe(dna):
    """
    Transcribes a string of DNA into RNA
    :param dna: a string containing only the characters C, T, A, and G
    :return: a string containing only the characters C, U, A, and G
    """
    return dna.replace('T','U')

def translate(rna):
    """
    Translates the strand of RNA given into its amino acid composition.
    DO NOT INCLUDE * IN YOUR RETURN STRING
    :param rna: a string containing only the characters C, U, A, and G
    :return: a string containing only the characters G, A, L, M, F, W, K, Q, E, S, P, V, I, C, Y, H, R, N, D, and T
    """
    RNA_CODON_TABLE = {"UUU": "F", "UUC": "F", "UUA": "L", "UUG": "L",
           "UCU": "S", "UCC": "S", "UCA": "S", "UCG": "S",
           "UAU": "Y", "UAC": "Y", "UAA": "*", "UAG": "*",
           "UGU": "C", "UGC": "C", "UGA": "*", "UGG": "W",
           "CUU": "L", "CUC": "L", "CUA": "L", "CUG": "L",
           "CCU": "P", "CCC": "P", "CCA": "P", "CCG": "P",
           "CAU": "H", "CAC": "H", "CAA": "Q", "CAG": "Q",
           "CGU": "R", "CGC": "R", "CGA": "R", "CGG": "R",
           "AUU": "I", "AUC": "I", "AUA": "I", "AUG": "M",
           "ACU": "T", "ACC": "T", "ACA": "T", "ACG": "T",
           "AAU": "N", "AAC": "N", "AAA": "K", "AAG": "K",
           "AGU": "S", "AGC": "S", "AGA": "R", "AGG": "R",
           "GUU": "V", "GUC": "V", "GUA": "V", "GUG": "V",
           "GCU": "A", "GCC": "A", "GCA": "A", "GCG": "A",
           "GAU": "D", "GAC": "D", "GAA": "E", "GAG": "E",
           "GGU": "G", "GGC": "G", "GGA": "G", "GGG": "G"}

    returnString=''
    for i in range(0,len(rna),3):
        seq=rna[i:i+3]
        seqCodon = RNA_CODON_TABLE.get(seq)
        if(seqCodon!='*'):
            returnString += seqCodon
    return returnString


def reading_frames(dna):
    """
    Generates a list of all 6 possible reading frames for a given strand of DNA
    For the non-biologists: https://en.wikipedia.org/wiki/Open_reading_frame
    :param dna: a string containing only the characters C, T, A, and G
    :return: a list of 6 strings containing only C, T, A, and G
    """
    my_list=[]
    for i in range(3):
        my_list.append(dna[i:])
    dna1=reverse_complement(dna)
    for i in range(3):
        my_list.append(dna1[i:])
    return my_list

