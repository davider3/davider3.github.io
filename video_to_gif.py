# %% IMPORTS
from moviepy.editor import VideoFileClip

# %% CONVERT
videoClip = VideoFileClip("./assets/images/test_drive.mp4")
videoClip.write_gif("./assets/images/test_drive.gif")
# %%
