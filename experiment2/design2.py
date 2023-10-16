import data_management
import numpy as np
import pandas as pd
import stimuli
import itertools
import random

DEBUG = False

nl = 8
luminances = np.linspace(0.1, 0.9, nl).round(3)
backgrounds=(0.0, 1.0)
STIM_NAMES = stimuli.__all__

if DEBUG:
    print('luminances: ', luminances)
    print('backgrounds: ', backgrounds)

def generate_session(Nrepeats=5):
    for i in range(Nrepeats):
        for stim_name in STIM_NAMES:
            block = generate_block(stim_name)
            block_id = f"{stim_name}-{i}"

            # Save to file
            filepath = data_management.design_filepath(block_id)
            block.to_csv(filepath)

def generate_block(stim_name):
    """ 
    Experimental design for one block of trials. 
    Here you define how many trials one block will contain, which
    will depend on the number of conditions you have. 
    """
    
    targets = [(l, b) for b in backgrounds for l in luminances]
    stimuli_design = list(itertools.combinations(targets, 2))
    
    trials = []
    for t in stimuli_design:
        
        t = list(t)
        # Randomy shuffle order L-R-Down
        if DEBUG:
            print()
            print(t)
        
        random.shuffle(t)
        
        if DEBUG:
            print(t)
        
        # Flatten
        t1, t2 = t
        line = [stim_name, t1[0], t1[1], t2[0], t2[1]]
        trials.append(line)

    # creates dataframe with all trials
    block = pd.DataFrame(
        trials,
        columns=['stim', 'l1', 'bg1', 'l2', 'bg2'],
    )    
    

    # Shuffle trial order
    block = block.reindex(np.random.permutation(block.index))
    block.reset_index(drop=True, inplace=True)
    block.index.name = "trial"

    return block


if __name__ == "__main__":
    
    generate_session()
