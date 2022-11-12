
notebooks =  $(shell find . -type f -name '*.ipynb' -not -name '*checkpoint*' -printf "%f ")

run:
	@for p in $(notebooks); do jupyter-nbconvert --to notebook --execute $$p; done

clean: $(notebooks:%=clean/%)

clean/%.ipynb: %.ipynb
	+@-jupyter-nbconvert --clear-output --inplace $<

run/%.ipynb: %.ipynb
	+@-jupyter-nbconvert --to notebook --execute $<
