import stimupy

resolution = {
    "visual_size": (10, 20),
    "ppd": 32,
}

target_size = resolution["visual_size"][1] / 10

intensity_background = 0.3

__all__ = ["checkerboard", "bullseye"]
#__all__ = ["bullseye"]

def checkerboard(intensity_target, intensity_left, intensity_right):
    return stimupy.stimuli.checkerboards.checkerboard(
        visual_size=resolution["visual_size"],
        ppd=resolution["ppd"],
        target_indices=((1, 2), (1, 7)),
        intensity_target=intensity_target,
        intensity_backgrounds=(intensity_left, intensity_right)
    )

def bullseye(intensity_target, intensity_left, intensity_right):
    return stimupy.stimuli.bullseyes.rectangular_two_sided(
        visual_size=resolution["visual_size"],
        ppd=resolution["ppd"],
        #target_size=target_size,
        intensity_target=intensity_target,
        intensity_frames=(intensity_left, intensity_right),
        n_frames=4,

    )

# %% SBC
'''
def sbc(intensity_target, intensity_left, intensity_right):
    return stimupy.stimuli.sbcs.two_sided(
        **resolution,
        target_size=target_size,
        intensity_target=intensity_target,
        intensity_backgrounds=(intensity_left, intensity_right)
    )
'''

# %% WHITE'S
'''
def whites(intensity_target, intensity_left, intensity_right):
    return stimupy.stimuli.whites.white(
        **resolution,
        bar_width=target_size,
        target_indices=(2, -3),
        target_heights=target_size,
        intensity_bars=(intensity_left, intensity_right),
        intensity_target=intensity_target
    )
'''