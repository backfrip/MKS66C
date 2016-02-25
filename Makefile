.PHONY: clean run

all: runstatement
	python main.py

nodisplay: runstatement
	python main.py --no-display

runstatement:
	@printf "\033[36m> Running \"main.py\"...\n\033[0m"

clean:
	@rm -f *.ppm
	@rm -f *.png
	@printf "\033[32m> Directory scrubbed of PPMs and PNGs.\033[0m\n"
