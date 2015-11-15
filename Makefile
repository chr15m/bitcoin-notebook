all: bitcoin-iterate/bitcoin-iterate

.PHONY: clean

bitcoin-iterate:
	git submodule init
	git submodule update

bitcoin-iterate/bitcoin-iterate: bitcoin-iterate
	make -C bitcoin-iterate

clean:
	make -C bitcoin-iterate clean
