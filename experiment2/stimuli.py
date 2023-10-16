import stimupy

resolution = {
    "visual_size": (10, 20),
    "ppd": 32,
}

target_size = resolution["visual_size"][1] / 10

intensity_background = 0.3

__all__ = ["checkerboard", "bullseye"]
# target_left, target_right, context_left, context_right

def checkerboard(intensity_target, context_left, context_right):
    return stimupy.stimuli.checkerboards.checkerboard(
        visual_size=resolution["visual_size"],
        ppd=resolution["ppd"],
        intensity_target=intensity_target,
        intensity_checks=(context_left,context_right),
        target_indices=((1, 2), (1, 7))
    )

def bullseye(intensity_target, context_left, context_right):
    return stimupy.stimuli.bullseyes.rectangular_two_sided(
        visual_size=resolution["visual_size"],
        ppd=resolution["ppd"],
        n_frames=4,
        intensity_frames=(context_left, context_right),
        intensity_target=intensity_target,
        intensity_background=intensity_background
    )