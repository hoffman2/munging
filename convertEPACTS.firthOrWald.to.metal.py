#This script takes EPACTS logistic score test results and returns a format for performing a p-value based meta anlysis in METAL.
#Direction based on magnitude of score test
import sys
import gzip
import re
def main(inputfile, outputfile):
	infh = gzip.open(inputfile,"r")
	with open(outputfile,"w") as outfh:
		for line in infh:
			if line[0] == "#":
				outfh.write("MARKER\tREF_ALLELE\tEFFECT_ALLELE\tSAMPLESIZE\tEFFECT_FREQ\tMAF\tP_VALUE\tBETA\tSEBETA\tDIRECTION\n")
			else:
				elements = line.strip().split("\t")
				testMarker = elements[3]
				MAF = elements[7]
				PVALUE = elements[8]
				MAGNITUDE = elements[9]
				SEBETA = elements[10]
				SAMPLESIZE = elements[4]
				SAMPLESIZE= int(SAMPLESIZE)
                                TOTAL_AC = SAMPLESIZE*2
                                EFFECT_AC = elements[5]
                                EFFECT_AC = float(EFFECT_AC)
                                EFFECT_FREQ = EFFECT_AC/TOTAL_AC
                                EFFECT_FREQ = round(EFFECT_FREQ,4)
				if MAGNITUDE == "NA":
					MAGNITUDE = "NaN"
				else:
					 MAGNITUDE = MAGNITUDE
				MAGNITUDE = float(MAGNITUDE)
				if MAGNITUDE < 0:
					DIRECTION = "-"
				elif MAGNITUDE > 0:
					DIRECTION = "+"
				else:
					DIRECTION = "NA"
				otherChrBP,otherREF,otherEFFECT,otherBP = re.split("_|/",testMarker)
				outfh.write(testMarker+"\t"+otherREF+"\t"+otherEFFECT+"\t"+str(SAMPLESIZE)+"\t"+str(EFFECT_FREQ)+"\t"+str(MAF)+"\t"+PVALUE+"\t"+str(MAGNITUDE)+"\t"+str(SEBETA)+"\t"+DIRECTION+"\n")
	infh.close()

if __name__ == "__main__":
	main(sys.argv[1],sys.argv[2])
