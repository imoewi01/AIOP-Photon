This repo contains my contributions to the AI Optimized Polarization project at Jefferson Lab. The AIOP_CoherentEdgePosition.pdf is a technical note that has a more detailed summary of the results. 




In order to replicate this analysis, you need access to the Jefferson Lab servers. 

1) The .txt files in myGetCommands are the commands I use to access the archived EPICS data for the Spring 2020 run period. These must be run on one of the gluon machines. gluons150-155 are for general use. Instructions on accessing the gluons is given in Appendix C of the technical note.

2) cleanAndConvertData_txt_to_csv.py converts each of the .txt files to .csv files. The .csv files contain two variables, the new setpoint of the variable of interest, as well as the Date-Time when the new value was set. 

3) merge_all_csv.ipynb is used to merge the resulting csv files for all the variables. This is where the majority of the data manipulation occurs, including fixing the run numbers and defining the nudge sequences. 

4) add_beam_up_time_combined.ipynb adds a variable for the amount of time since the electron beam dropped. This information is only used for nonudge-study_combined.ipynb, so information about the nudges are removed to save space.


The remaining notebooks are used to visualize the output of the .csv files produced by the steps above. They can be run in any order.

a) multinudge_combined.ipynb is used to measure the average energy change for each "nudge" of the gear system.

b) backlash_study_combined.ipynb displays time series data that shows how the photon beam energy changes when the gears are "nudged" in one direction followed by the opposite direction. When this occurs, there will be a small amount of backlash during which no change in energy will occur.

c) nonudge-study_combined.ipynb contains data where no user inputs were given. This is used to determine how the electron beam properties impact the properties of our photon beam.

d) singlenudge-study.ipynb shows rough estimates of the energy change for each "nudge", as well as an estimate for how long it takes for the beam energy to update after a "nudge" occurs. 