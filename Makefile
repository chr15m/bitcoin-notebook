all: bitcoin-iterate/bitcoin-iterate virtualenv/lib/python2.7/site-packages

.PHONY: clean

bitcoin-iterate:
	git submodule init
	git submodule update

bitcoin-iterate/bitcoin-iterate: bitcoin-iterate
	make -C bitcoin-iterate

virtualenv/bin/activate:
	virtualenv virtualenv

virtualenv/lib/python2.7/site-packages: requirements.txt virtualenv/bin/activate
	. ./virtualenv/bin/activate && pip install -r requirements.txt && touch virtualenv/lib/python2.7/site-packages

clean:
	make -C bitcoin-iterate clean
	rm -rf virtualenv
