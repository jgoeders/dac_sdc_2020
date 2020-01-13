proj:
	vivado -source ../dac_contest.tcl

clean:
	rm -rf project_1

move_bitstream: ../dac_contest.bit

../dac_contest.bit: project_1/project_1.runs/impl_1/dac_contest_wrapper.bit
	cp $< $@