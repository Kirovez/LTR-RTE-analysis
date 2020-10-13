from Bio import SeqIO
import re
pattern = "C..C....H....C"
list_of_GAG_ORFs = r"RTE_ORFs_filtered.tab"
fasta_proteins = r"35K_TE_selected_all_ORFs.fastafiltered.fasta"

with open(list_of_GAG_ORFs) as InTab, open("RBM_ORF_screen.tab", 'w') as out:
    ORFs_id = {}
    for line in InTab:
        ORFs_id[line.split("\t")[0]] = 0
    for seq in SeqIO.parse(fasta_proteins, 'fasta'):
        re_find = re.findall(pattern, str(seq.seq))
        if seq.id in ORFs_id and re_find:
            for motives in re_find:
                out.write(seq.id + "\t" + motives + "\n")

