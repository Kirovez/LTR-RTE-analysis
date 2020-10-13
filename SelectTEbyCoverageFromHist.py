import sys
from collections import defaultdict

def estimateTEsByCoverageFromHist(hist_file, ok_cov_fraction = 1):
    d_cov = defaultdict(int) #TEid:fraction covered by min number of reads
    with open(hist_file) as hist:
        for lines in hist:
            if not lines.startswith("all"):
                chrom, startTE, endTE, covReads, bpCovered, TElength, fraction = lines.rstrip().split("\t")
                unique_TE_id = "{0}:{1}..{2}".format(chrom, startTE, endTE)
                if int(covReads) > ok_cov_fraction:
                    d_cov[unique_TE_id] += float(fraction)

    return d_cov

def selectTEsByCoverage(outFilename, d_cov, fraction = 0.7):
    cnt = 0
    with open(outFilename, "w") as outFile:
        for TEs in d_cov:
            if d_cov[TEs] > fraction:
                outFile.write(TEs + "\n")
                cnt += 1

    print("Number of TE selected by minimum coverage:", cnt)


def main(hist_file, ok_cov_fraction, fraction ):
    outFile = "{0}.selectedBy_mr{1}_mc{2}Cov".format(hist_file, minRead, minFraction)
    d_cov = estimateTEsByCoverageFromHist(hist_file, ok_cov_fraction = ok_cov_fraction)
    selectTEsByCoverage(outFile, d_cov, fraction = fraction)

hist_file, minRead, minFraction = sys.argv[1], int(sys.argv[2]), float(sys.argv[3])
main(hist_file, minRead, minFraction)