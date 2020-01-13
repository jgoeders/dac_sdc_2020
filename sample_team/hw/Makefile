proj:
	vivado -source dac_sdc.tcl

clean:
	rm -rf dac_sdc

copy_hw: ../dac_sdc.bit ../dac_sdc.hwh

../dac_sdc.bit: dac_sdc/dac_sdc.runs/impl_1/dac_sdc_wrapper.bit
	cp $< $@

../dac_sdc.hwh: dac_sdc/dac_sdc.srcs/sources_1/bd/sensors96b/hw_handoff/sensors96b.hwh 
	cp $< $@