all: bitcoin-iterate/bitcoin-iterate virtualenv/lib/python2.7/site-packages

.PHONY: clean depdendencies dependencies-pdf

bitcoin-iterate:
	git submodule init
	git submodule update

bitcoin-iterate/bitcoin-iterate: bitcoin-iterate
	make -C bitcoin-iterate

virtualenv/bin/activate:
	virtualenv virtualenv

virtualenv/lib/python2.7/site-packages: requirements.txt virtualenv/bin/activate
	. ./virtualenv/bin/activate && pip install -r requirements.txt && touch virtualenv/lib/python2.7/site-packages

# PHONY tasks

dependencies:
	sudo apt-get install python-virtualenv libfreetype6-dev liblapack-dev gfortran libpng12-dev

dependencies-pdf:
	sudo apt-get install texlive-latex-base texlive-latex-extra texlive-fonts-recommended pandoc
	curl http://ctan.mackichan.com/macros/plain/contrib/misc/ulem.sty > ulem.sty

clean:
	make -C bitcoin-iterate clean
	rm -rf virtualenv
