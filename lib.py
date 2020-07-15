# encoding: utf-8
import re

def sars_cov_2_2020_Wuhan (U=True):
	seq = open("sars_cov_2.txt").read()
	s = " ".join(re.findall("[a-zA-Z]+", seq))
	s = s.replace(" ", "")
	if not U: return s
	if U: return s.replace("t", "u")

