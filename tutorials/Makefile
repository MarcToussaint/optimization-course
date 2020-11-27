
ipynb_paths =  $(shell find . -type f -name '*.ipynb' -not -name '*checkpoint*' -printf "%f ")

run_paths = how_to_query_an_NLP.ipynb opt-1.ipynb

run:
	@for p in $(run_paths); do jupyter-nbconvert --execute $$p --to python; done

clean: $(ipynb_paths:%=clean/%)

clean/%.ipynb: %.ipynb
	+@-jupyter-nbconvert --ClearOutputPreprocessor.enabled=True --inplace $<
#jupyter-nbconvert --clear-output --inplace $<

run/%.ipynb: %.ipynb
	+@-jupyter-nbconvert --execute $< --to python
