# install/update dependencies
dev:
	uv pip install -r requirements.txt --refresh --upgrade

# package valohai-utils for distribution
# makes current development version available in an execution environment
valohai-utils.tgz: valohai-utils ../valohai-utils/valohai/*
	# use GNU tar to get rid of extra header attributes added by macOS tar
	gtar czf $@ valohai-utils/*

valohai-utils:
	ln -s ../valohai-utils $@