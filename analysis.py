from lib import sars_cov_2_2020_Wuhan
from Bio.Seq import Seq
from Bio.Alphabet import IUPAC

# Reference sequence: https://www.ncbi.nlm.nih.gov/nuccore/NC_045512
c = Seq(sars_cov_2_2020_Wuhan(), IUPAC.unambiguous_rna)
print(c)