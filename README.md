# Traffic Accusation

```bash
usage: main.py [-h] [-f [file]] [-s [start_time]] [-d [duration]] [-l [license]]

A tool can parse videos and images to report a traffic violation.

optional arguments:
  -h, --help            show this help message and exit
  -f [file], --file [file]
                        Which video file to create a subclip
  -s [start_time], --start [start_time]
                        When to start cutting the clip
  -d [duration], --duration [duration]
                        How long does it take to play
  -l [license], --license [license]
                        Which car license to report
```

* `docker exec -ti CONTAINER_ID bash` (`docker ps`)
* `python main.py -f ./videos/xxxxx.MP4 -s 128 -l AAAA-0000`
