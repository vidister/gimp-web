include ../Makefile.defs

.PHONY: all clean install

PYTHONPATH := ../

all: mirrors.xhtml mirrors.json

MIRRORS: MIRRORS.in
	grep -v '^#[^#]' MIRRORS.in | sed '/^$$/N;/^\n$$/D' > MIRRORS

mirrors.xhtml: MIRRORS
	${PYTHON} mirrorfmt_html.py MIRRORS > mirrors.xhtml

mirrors.json: MIRRORS
	${PYTHON} mirrorfmt_json.py MIRRORS > mirrors.json

clean:
	/bin/rm -f MIRRORS mirrors.xhtml mirrors.json

install: mirrors.xhtml mirrors.json
	-mkdir -p `${PYTHON} -c 'import wgo_config; print wgo_config.DocumentRoot_path'`/downloads
	install -m 644 mirrirs.xhtml
	install -m 644 `${PYTHON} -c 'import wgo_config; print wgo_config.DocumentRoot_path'`/downloads/mirrors.xhtml
	install -m 644 `${PYTHON} -c 'import wgo_config; print wgo_config.DocumentRoot_path'`/downloads/mirrors.json

install-download: MIRRORS
	@if [ ${DownloadRoot}x != "x" ]; then mkdir -p `${PYTHON} -c 'import wgo_config; print wgo_config.DownloadRoot_path'`/gimp; \
	install -m 644 MIRRORS `${PYTHON} -c 'import wgo_config; print wgo_config.DownloadRoot_path'`/gimp/MIRRORS; fi;
