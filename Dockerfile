FROM busybox

ADD edge-detector /bin

CMD [ "edge-detector" ]