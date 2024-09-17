# %% IMPORTS
from moviepy.editor import VideoFileClip

# %% CONVERT
videoClip = VideoFileClip("./assets/images/537_arm.mp4")
videoClip.write_gif("./assets/images/537_arm.gif")
# %%
videoClip.speedx(2).to_gif("./assets/images/537_arm2.gif")
# %%
