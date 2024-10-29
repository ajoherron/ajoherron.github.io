from PIL import Image
import os


def reduce_gif_frames(input_path, output_path, nth_frame=3):
    """
    Creates a new GIF using every nth frame from the input GIF.

    Args:
        input_path (str): Path to input GIF file
        output_path (str): Path where the new GIF will be saved
        nth_frame (int): Keep every nth frame (default: 10)
    """
    # Open the GIF file
    with Image.open(input_path) as img:
        # Get basic info about the GIF
        n_frames = img.n_frames
        duration = img.info.get("duration", 100)  # Duration between frames in ms

        # Extract every nth frame
        frames = []
        for i in range(0, n_frames, nth_frame):
            img.seek(i)
            frames.append(img.copy())

        if frames:
            # Save the new GIF with the same frame duration
            frames[0].save(
                output_path,
                save_all=True,
                append_images=frames[1:],
                duration=duration,
                loop=0,
                optimize=True,
            )
            print(f"Created new GIF with {len(frames)} frames")
        else:
            print("No frames were extracted")


# Example usage
if __name__ == "__main__":
    input_gif = "input.gif"
    output_gif = "output_faster.gif"

    if os.path.exists(input_gif):
        reduce_gif_frames(input_gif, output_gif)
    else:
        print(f"Could not find {input_gif}")
