from PIL import Image

def trim_edges_gif(input_path, output_path, pixels):
    # Open the GIF
    im = Image.open(input_path)
    frames = []
    
    # Calculate new bounds
    width, height = im.size
    box = (pixels, pixels, width-pixels, height-pixels)
    
    try:
        while True:
            # Copy and crop current frame
            frame = im.copy()
            frames.append(frame.crop(box))
            # Go to next frame
            im.seek(im.tell() + 1)
    except EOFError:
        pass

    # Save the cropped frames
    frames[0].save(
        output_path,
        save_all=True,
        append_images=frames[1:],
        duration=im.info['duration'],
        loop=0
    )

# Usage - trim 10 pixels from each edge:
trim_edges_gif('input.gif', 'output.gif', 5)
