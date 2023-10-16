"""This module defines the actual experimental design of [this] experiment.

It needs to _at least_ define these functions, which are called by `run_experiment.py`
- run_trial: how to run a single trial of this experiment
- generate_session: how to generate a new session's worth of design (files)

It can define additional functions to help manage the control flow.

"""
'''
import data_management
import numpy as np
import pandas as pd
import stimuli

LUMINANCES = [0, 0.10, 0.25, 0.33, 0.5, 0.66, 0.75, 0.90, 1]

STIM_NAMES = stimuli.__all__


def generate_session(Nrepeats=5):
    for i in range(Nrepeats):
        for stim_name in STIM_NAMES:
            block = generate_block(stim_name)
            block_id = f"{stim_name}-{i}"

            # Save to file
            filepath = data_management.design_filepath(block_id)
            block.to_csv(filepath)


def generate_block(stim_name):
    # Combine all variables into full design
    trials = [
        (stim_name, int_target, int_left, int_right)
        for int_target in LUMINANCES
        for int_left in LUMINANCES
        for int_right in LUMINANCES
    ]

    # Convert to dataframe
    block = pd.DataFrame(
        trials,
        columns=["stim", "intensity_target", "intensity_left", "intensity_right"],
    )

    # Shuffle trial order
    block = block.reindex(np.random.permutation(block.index))
    block.reset_index(drop=True, inplace=True)
    block.index.name = "trial"

    return block

    def generate_block():
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
        line = [t1[0], t1[1], t2[0], t2[1]]
        trials.append(line)

    # creates dataframe with all trials
    block = pd.DataFrame(
        trials,
        columns=['l1', 'bg1', 'l2', 'bg2'],
    )    
    

    # Shuffle trial order
    block = block.reindex(np.random.permutation(block.index))
    block.reset_index(drop=True, inplace=True)
    block.index.name = "trial"

    return block

'''

import data_management
import numpy as np
import pandas as pd
import stimuli
import itertools
import random

DEBUG = False

nl = 10
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
    # Combine all variables into full design
    '''
    trials = [
        (stim_name, target_left, target_right, context_left, context_right)
        for target_left in luminances
        for target_right in luminances
        for context_left in backgrounds
        for context_right in backgrounds
        if not(target_left == target_right and context_left == context_right)
    ]
    
    trials = []
    seen = set()
    for t in trials1:
        s = frozenset(t)
        if s not in seen:
            trials.append(t)
    
    print(trials)
    print(len(trials))
    '''

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
        line = [stim_name, t1[0], t2[0], t1[1], t2[1]]
        trials.append(line)

    #print(trials)
    #print(len(trials))

    # Convert to dataframe
    block = pd.DataFrame(
        trials,
        columns=["stim", "intensity_target_left", "intensity_target_right", "intensity_context_left", "intensity_context_right"],
    )

    # Shuffle trial order
    block = block.reindex(np.random.permutation(block.index))
    block.reset_index(drop=True, inplace=True)
    block.index.name = "trial"

    return block


if __name__ == "__main__":
    
    generate_session()
