open_hw
connect_hw_server
open_hw_target
current_hw_device [lindex [get_hw_devices] 0]
refresh_hw_device -update_hw_probes false [lindex [get_hw_devices] 0]


# set_property PROGRAM.FILE {/home/xx/Work/MDT_TDC_ver1_evaluation-MMCM_test/MMCM_hit_gen/MMCM_TOP.bit} [lindex [get_hw_devices] 0]
# set_property PROBES.FILE {/home/xx/Work/MDT_TDC_ver1_evaluation-MMCM_test/MMCM_hit_gen/debug_nets.ltx} [lindex [get_hw_devices] 0]
set_property PROBES.FILE {/home/junjie-lab-admin/Work/Resolution_auto/debug_nets.ltx} [lindex [get_hw_devices] 0]
set_property PROGRAM.FILE {/home/junjie-lab-admin/Work/Resolution_auto/MMCM_TOP.bit} [lindex [get_hw_devices] 0]
current_hw_device [lindex [get_hw_devices] 0]
refresh_hw_device [lindex [get_hw_devices] 0]






proc psen {} {
	startgroup
	set_property OUTPUT_VALUE 1 [get_hw_probes psen_0_vio -of_objects [get_hw_vios -of_objects [get_hw_devices xc7k325t_0] -filter {CELL_NAME=~"vio_phase_control_inst"}]]
	commit_hw_vio [get_hw_probes {psen_0_vio} -of_objects [get_hw_vios -of_objects [get_hw_devices xc7k325t_0] -filter {CELL_NAME=~"vio_phase_control_inst"}]]
	endgroup

	startgroup
	set_property OUTPUT_VALUE 0 [get_hw_probes psen_0_vio -of_objects [get_hw_vios -of_objects [get_hw_devices xc7k325t_0] -filter {CELL_NAME=~"vio_phase_control_inst"}]]
	commit_hw_vio [get_hw_probes {psen_0_vio} -of_objects [get_hw_vios -of_objects [get_hw_devices xc7k325t_0] -filter {CELL_NAME=~"vio_phase_control_inst"}]]
	endgroup
	puts "Psen once!" 
}


proc psincdec_set1 {} {
	set_property OUTPUT_VALUE 1 [get_hw_probes psincdec_0_vio -of_objects [get_hw_vios -of_objects [get_hw_devices xc7k325t_0] -filter {CELL_NAME=~"vio_phase_control_inst"}]]
	commit_hw_vio [get_hw_probes {psincdec_0_vio} -of_objects [get_hw_vios -of_objects [get_hw_devices xc7k325t_0] -filter {CELL_NAME=~"vio_phase_control_inst"}]]
	puts "psincdec_set1" 
}

proc psincdec_set0 {} {
	set_property OUTPUT_VALUE 0 [get_hw_probes psincdec_0_vio -of_objects [get_hw_vios -of_objects [get_hw_devices xc7k325t_0] -filter {CELL_NAME=~"vio_phase_control_inst"}]]
	commit_hw_vio [get_hw_probes {psincdec_0_vio} -of_objects [get_hw_vios -of_objects [get_hw_devices xc7k325t_0] -filter {CELL_NAME=~"vio_phase_control_inst"}]]
	puts "psincdec_set0" 
}

psincdec_set0



set edge r
set run_name 0204_chnl18_chnl00_$edge
puts $run_name
exec mkdir $run_name
cd ./$run_name
for {set i 0} {$i < 136} {incr i} {
	after 300
	puts "======================== Receiving run: $i ================================"
	set env(LD_LIBRARY_PATH) "/usr/local/lib:/usr/lib:/usr/local/lib64:/usr/lib64"
	exec ../../../ethernet_cap/mac_daq -r $run_name -d 1000000 -e $edge -b $i
	set env(LD_LIBRARY_PATH) "/home/junjie-lab-admin/Vivado/2016.2/lib/lnx64.o:/home/junjie-lab-admin/Vivado/2016.2/tps/lnx64/jre/lib/amd64:/home/junjie-lab-admin/Vivado/2016.2/tps/lnx64/jre/lib/amd64/server:/usr/local/lib:/usr/lib:/usr/local/lib64:/usr/lib64:/home/junjie-lab-admin/Vivado/2016.2/bin/../lnx64/tools/dot/lib"
	puts "======================== Finished run: $i ================================"
	psen
}


# for {set i 15} {$i < 53} {set i i+3} {
# 	after 1500
# 	puts "======================== Receiving run: $i ================================"
# 	set env(LD_LIBRARY_PATH) "/usr/local/lib:/usr/lib:/usr/local/lib64:/usr/lib64"
# 	exec ./mac_daq $run_name$i -verbose off 1000000 >>output.log 2>> output.csv
# 	# exec ./mac_daq 1229_res_001 -verbose off 10000
# 	set env(LD_LIBRARY_PATH) "/home/junjie-lab-admin/Vivado/2016.2/lib/lnx64.o:/home/junjie-lab-admin/Vivado/2016.2/tps/lnx64/jre/lib/amd64:/home/junjie-lab-admin/Vivado/2016.2/tps/lnx64/jre/lib/amd64/server:/usr/local/lib:/usr/lib:/usr/local/lib64:/usr/lib64:/home/junjie-lab-admin/Vivado/2016.2/bin/../lnx64/tools/dot/lib"
# 	puts "======================== Finished run: $i ================================"
# 	psen
# 	psen
# 	psen
# }

# for {set i 53} {$i < 83} {incr i} {
# 	after 1500
# 	puts "======================== Receiving run: $i ================================"
# 	set env(LD_LIBRARY_PATH) "/usr/local/lib:/usr/lib:/usr/local/lib64:/usr/lib64"
# 	exec ./mac_daq $run_name$i -verbose off 1000000 >>output.log 2>> output.csv
# 	# exec ./mac_daq 1229_res_001 -verbose off 10000
# 	set env(LD_LIBRARY_PATH) "/home/junjie-lab-admin/Vivado/2016.2/lib/lnx64.o:/home/junjie-lab-admin/Vivado/2016.2/tps/lnx64/jre/lib/amd64:/home/junjie-lab-admin/Vivado/2016.2/tps/lnx64/jre/lib/amd64/server:/usr/local/lib:/usr/lib:/usr/local/lib64:/usr/lib64:/home/junjie-lab-admin/Vivado/2016.2/bin/../lnx64/tools/dot/lib"
# 	puts "======================== Finished run: $i ================================"
# 	psen
# }

# for {set i 83} {$i < 122} {set i i+3} {
# 	after 1500
# 	puts "======================== Receiving run: $i ================================"
# 	set env(LD_LIBRARY_PATH) "/usr/local/lib:/usr/lib:/usr/local/lib64:/usr/lib64"
# 	exec ./mac_daq $run_name$i -verbose off 1000000 >>output.log 2>> output.csv
# 	# exec ./mac_daq 1229_res_001 -verbose off 10000
# 	set env(LD_LIBRARY_PATH) "/home/junjie-lab-admin/Vivado/2016.2/lib/lnx64.o:/home/junjie-lab-admin/Vivado/2016.2/tps/lnx64/jre/lib/amd64:/home/junjie-lab-admin/Vivado/2016.2/tps/lnx64/jre/lib/amd64/server:/usr/local/lib:/usr/lib:/usr/local/lib64:/usr/lib64:/home/junjie-lab-admin/Vivado/2016.2/bin/../lnx64/tools/dot/lib"
# 	puts "======================== Finished run: $i ================================"
# 	psen
# 	psen
# 	psen
# }

# for {set i 122} {$i < 138} {incr i} {
# 	after 1500
# 	puts "======================== Receiving run: $i ================================"
# 	set env(LD_LIBRARY_PATH) "/usr/local/lib:/usr/lib:/usr/local/lib64:/usr/lib64"
# 	exec ./mac_daq $run_name$i -verbose off 1000000 >>output.log 2>> output.csv
# 	# exec ./mac_daq 1229_res_001 -verbose off 10000
# 	set env(LD_LIBRARY_PATH) "/home/junjie-lab-admin/Vivado/2016.2/lib/lnx64.o:/home/junjie-lab-admin/Vivado/2016.2/tps/lnx64/jre/lib/amd64:/home/junjie-lab-admin/Vivado/2016.2/tps/lnx64/jre/lib/amd64/server:/usr/local/lib:/usr/lib:/usr/local/lib64:/usr/lib64:/home/junjie-lab-admin/Vivado/2016.2/bin/../lnx64/tools/dot/lib"
# 	puts "======================== Finished run: $i ================================"
# 	psen
# }

exit