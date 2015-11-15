> "Needs more computer science, less noise."
> --Nick Szabo

Bitcoin Notebook connects Rusty Russell's `bitcoin-iterate` to the Jupyter iPython Notebook to enable fast and easy queries against the blockchain history which can then be processed and graphed in a way that is reproduceable and literate.

Check out the [example notebook](./notebooks/Bitcoin Notebook Hello World.ipynb) which contains a couple of demonstration queries, and a [PDF "paper" export](./notebooks/Bitcoin Notebook Hello World.pdf) of the same results.

Install
-------

Run `make` to generate the Python virtualenv environment and compile `bitcoin-iterate`.

Run
---

`./bitcoin-notebook` will launch the Jupyter server with the paths all configured correctly and automatically open a browser window pointing at the notebook list.

Probably the most important thing to remember for people new to Jupyter is that pressing `shift-Enter` will re-run the code in the highlighted section.

Dependencies
------------

You can run `make dependencies` if you're on a Debian based system. Otherwise the packages you will need before the virtualenv will deploy are:

	* libfreetype6-dev
	* liblapack-dev
	* gfortran
	* libpng12-dev

Run `make dependencies-pdf` to install the packages required for exporting to PDF. Here are the packages that will be installed:

	* texlive-latex-base
	* texlive-latex-extra
	* texlive-fonts-recommended
	* pandoc
	* http://ctan.mackichan.com/macros/plain/contrib/misc/ulem.sty

