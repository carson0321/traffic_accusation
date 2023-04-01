import os
import sys
import argparse

from moviepy.editor import VideoFileClip


def handle(file, license, start_time, duration):
    file_name = file.split('/')[-1].split(".")[0]
    video = VideoFileClip(file)

    # image
    video.save_frame(f"./reports/{license.upper()}_{file_name}.jpg", t=start_time)

    # video
    output = video.subclip(start_time - duration/2, start_time + duration/2)
    output.write_videofile(
        f"./reports/{license.upper()}_{file_name}.mp4",
        temp_audiofile=f"./videos/temp_{file_name}.m4a",
        remove_temp=True,
        codec="libx264",
        audio_codec="aac"
    )
    # duration       = video.duration
    # fps            = video.fps
    # width, height  = video.size

    # print(duration)
    print("Done")


if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="A tool can parse videos and images to report a traffic violation.",
                                     formatter_class=argparse.RawTextHelpFormatter)
    parser.add_argument("-f",
                        "--file",
                        nargs="?",
                        type=str,
                        metavar="file",
                        dest="file",
                        help=("Which video file to create a subclip"))

    parser.add_argument("-s",
                        "--start",
                        nargs="?",
                        type=float,
                        metavar="start_time",
                        dest="start_time",
                        help=("When to start cutting the clip"))

    parser.add_argument("-d",
                    "--duration",
                    nargs="?",
                    type=int,
                    default=6,
                    metavar="duration",
                    dest="duration",
                    help=("How long does it take to play"))

    parser.add_argument("-l",
                    "--license",
                    nargs="?",
                    type=str,
                    default="NONE",
                    metavar="license",
                    dest="license",
                    help=("Which car license to report"))

    args = parser.parse_args()
    if not args.file or not args.start_time:
        parser.print_help()
        sys.exit(0)

    if not os.path.exists(args.file):
        print("Video file doesn't exist")

    handle(args.file, args.license, args.start_time, args.duration)
