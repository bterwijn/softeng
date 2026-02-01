include ${SOFTENG_HOME}/softeng/MasterMakefile

PLOT_PY := $(wildcard plot_*.py)
PLOT_PNG := $(patsubst %.py,%.png,$(PLOT_PY))

%.png : %.py
	bash make_plot.sh $< $@

all	: $(PLOT_PNG)

print:
	@echo ${PLOT_PY}
	@echo $(PLOT_PNG)
