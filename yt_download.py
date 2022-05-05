from unittest import result
import pytube

# ------------------
import logging
logging.basicConfig(filename='H:\python_unifael\status.log', level=logging.DEBUG,
                    format='%(asctime)s %(levelname)s %(name)s %(message)s')
logger = logging.getLogger(__name__)
# ------------------


SAVE_PATH = "H:\python_unifael"
link = open('YT_links.csv', 'r')

for i in link:
    try:
        yt = pytube.YouTube(i)
    except ZeroDivisionError as err:
        logger.error(err)  # logs

    ys = yt.streams.get_highest_resolution()

    try:
        ys.download(SAVE_PATH)
    except:  # ZeroDivisionError as err:   logger.error(err)
        print = "deu ruim"
