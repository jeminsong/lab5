
# Automatically generated by /Users/mshafae/github/cpsc120/cpsc-120-solution-lab-05/.action/ccsrcutilities.py on 2023-10-01 16:43:28

TOPTARGETS = all clean spotless format lint header test unittest

SUBDIRS = $(wildcard part-?/.)

default all: all

$(TOPTARGETS): $(SUBDIRS)

$(SUBDIRS):
	$(MAKE) -f Makefile -C $@ $(MAKECMDGOALS)

.PHONY: $(TOPTARGETS) $(SUBDIRS)
