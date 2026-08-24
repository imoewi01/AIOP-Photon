import pandas as pd
# need to change run number, so that run number for setup is same as for the actual data acquisition 
# currently, run number only changes when DAQ:STATUS is 1, which is after radiator setup. Want to apply new run number when DAQ:STATUS goes from 2->0, not 0->1


# new version that should be much faster
def fix_run_numbers_vectorized(df_tmp):
    
    df_out = df_tmp.copy()
    run_numbers = df_tmp['RunNumber'].unique()

    # Pandas series for DAQ:STATUS
    status = df_tmp['DAQ:STATUS']
    run_col = df_tmp['RunNumber']

    # Position (0-based index) of each raw run number within the sorted-by-appearance run_numbers array
    run_pos = pd.Series(range(len(run_numbers)), index=run_numbers)

    # A "2 -> 0" transition marks the true boundary where a new run should start.
    # We also guard against a "1 -> 0" transition, which can happen if the DAQ
    # fails/aborts before ever reaching status 2. Because of the delay in the raw
    # RunNumber increment, a single raw RunNumber can contain MORE THAN ONE such
    # transition (a full 0->1->2->0, or an aborted 0->1->0, cycle can repeat
    # before the raw RunNumber itself changes). Each occurrence should shift the
    # rows that follow it by one additional run number.
    prev_status = status.shift(1)
    off_event = status.eq(0) & (prev_status.eq(2) | prev_status.eq(1))

    # Cumulative count of off_events seen so far within the current raw run (inclusive of the transition row itself)
    shift_amount = off_event.groupby(run_col).cumsum()

    target_pos = (run_col.map(run_pos) + shift_amount).clip(upper=len(run_numbers) - 1)

    df_out['RunNumber'] = target_pos.map(pd.Series(run_numbers)).values
    return df_out



# old version that was very slow
# need to loop through runs. For each run, should see the sequence 0 -> 1 -> 2 for DAQ:STATUS. Once it goes 2->0, next run should start
# (also guard against 1->0, which can happen if the DAQ fails/aborts before ever reaching status 2.
# a raw RunNumber can contain more than one such transition, each of which should shift forward by one more run)

def fix_run_numbers(df_tmp):

    df_out = pd.DataFrame()

    run_list = df_tmp['RunNumber'].unique()
    print(min(run_list),'to',max(run_list))

    for run_idx in range(len(run_list)):
        if run_idx%100==0:
            print(run_list[run_idx])
        runVal = run_list[run_idx]
        df_run = df_tmp[df_tmp['RunNumber']==runVal].copy()

        if runVal == max(run_list): 
            df_out = pd.concat([df_out,df_run])
            continue

        shift_count = 0
        prev_status = None
        for i, row in df_run.iterrows():
            daq_status = row['DAQ:STATUS']

            if daq_status == 0 and prev_status in (1, 2):
                #print("daq turned off (1->0 or 2->0), shifting forward one more run")
                shift_count += 1

            if shift_count > 0:
                # never revert: always assign the run number `shift_count` positions ahead,
                # clamped to the last available run
                target_idx = min(run_idx + shift_count, len(run_list) - 1)
                df_run.at[i,'RunNumber'] = run_list[target_idx]

            prev_status = daq_status
        
        df_out = pd.concat([df_out,df_run])
    return df_out


