import subprocess
import pysrt
import os
from .models import Subtitle
import shutil
from datetime import timedelta
import logging

# Configure logging
logger = logging.getLogger(__name__)

def extract_and_save_subtitles(video_instance):
    """
    Extracts subtitles from a video file using ffmpeg and saves them to the database.
    :param video_instance: Video instance for which subtitles will be extracted.
    """
    video_file = video_instance.video_file.path
    video_dir = os.path.dirname(video_file)  # Get the directory of the video file
    output_srt = os.path.join(video_dir, 'subtitles.srt')  # Save SRT file in the same directory

    if not os.path.isfile(video_file):
        logger.error(f"Video file does not exist: {video_file}")
        return

    # Construct the ffmpeg command to extract subtitles
    command = f'ffmpeg -i "{video_file}" -map 0:s:0 "{output_srt}"'

    logger.info(f"Running command: {command}")

    try:
        # Run the command and capture output
        result = subprocess.run(command, shell=True, check=True, text=True, capture_output=True)
        logger.info(f"ffmpeg output: {result.stdout}")
        if result.stderr:
            logger.error(f"ffmpeg error: {result.stderr}")

        # Check if the SRT file was created and has content
        if not os.path.exists(output_srt):
            logger.warning(f"No subtitles were extracted. Output file {output_srt} does not exist.")
            return

        if os.path.getsize(output_srt) == 0:
            logger.warning("The SRT file is empty. No subtitles extracted.")
            return

        # Parse and save subtitles
        logger.info(f"Parsing SRT file: {output_srt}")
        subs = pysrt.open(output_srt)

        if not subs:
            logger.warning("No subtitles found in the SRT file.")
            return

        logger.info(f"Number of subtitles: {len(subs)}")

        for sub in subs:
            logger.info(f"Saving subtitle: {sub.text}")
            try:
                start_time = timedelta(milliseconds=sub.start.ordinal)
                end_time = timedelta(milliseconds=sub.end.ordinal)

                Subtitle.objects.create(
                    video=video_instance,
                    start_time=start_time,  # Save as timedelta
                    end_time=end_time,      # Save as timedelta
                    subtitle=sub.text       # Subtitle text
                )
            except Exception as e:
                logger.error(f"Error saving subtitle: {e}")

        # Cleanup
        os.remove(output_srt)

    except subprocess.CalledProcessError as e:
        logger.error(f"An error occurred during subtitle extraction: {e}")

    except Exception as e:
        logger.error(f"An unexpected error occurred: {e}")
