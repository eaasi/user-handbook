# Minimal makefile for Sphinx documentation
#

# You can set these variables from the command line.
SPHINXBUILD   = sphinx-build
SPHINXPROJ    = eaasi
SOURCEDIR     = source
BUILDDIR      = build

# For additional options/flags see:
# http://www.sphinx-doc.org/en/stable/invocation.html#invocation-of-sphinx-build
SPHINXOPTS    = -n -j 4

version:
	@$(SPHINXBUILD) --version

clean:
	rm -v -rf "$(BUILDDIR)"

.PHONY: version Makefile

# Catch-all target: route all unknown targets to Sphinx using the new
# "make mode" option.  $(O) is meant as a shortcut for $(SPHINXOPTS).
%: Makefile
	@$(SPHINXBUILD) -b $@ $(SPHINXOPTS) $(O) "$(SOURCEDIR)" "$(BUILDDIR)"
