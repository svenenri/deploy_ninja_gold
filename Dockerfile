FROM python:2-onbuild

COPY start.sh /start.sh
COPY editjson.sh /editjson.sh
COPY editjson.py /editjson.py

EXPOSE 8000

CMD ["/start.sh"]
CMD ["/editjson.sh"]
