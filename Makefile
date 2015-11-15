all: bitcoin-iterate/bitcoin-iterate

bitcoin-iterate:
	git submodule init
	git submodule update

bitcoin-iterate/bitcoin-iterate: bitcoin-iterate
	make -C bitcoin-iterate

