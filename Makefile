BASE = rai

target: build bin

DEPEND = Core Optim Algo Geo Plot Gui Kin KOMO ry

build: $(DEPEND:%=inPath_makeLib/%)

bin:
	+make -C rai bin

installUbuntuAll: $(DEPEND:%=inPath_installUbuntu/%)

printUbuntuAll: $(DEPEND:%=inPath_printUbuntu/%) printUbuntu

clean: $(DEPEND:%=inPath_clean/%)

dependAll: cleanLocks cleanDepends $(DEPEND:%=inPath_depend/%)

include $(BASE)/build/generic.mk

.NOTPARALLEL:
