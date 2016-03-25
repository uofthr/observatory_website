#!/bin/bash
if [ $# -lt 1 ]; then
    MESSAGE="Live view from the #UTSC Observatory"
else
    MESSAGE="$1"
fi 

if [ `stat --format=%Y latest.jpg` -ge $(( `date +%s` - 600 )) ]; then
    MEDIAJSON=`/usr/local/bin/twurl -H upload.twitter.com -X POST '/1.1/media/upload.json' --file 'latest.jpg' --file-field 'media'`
    #echo "$MEDIAJSON"
    MEDIAID=`echo "$MEDIAJSON" | sed -rn 's/\{\"media_id\":(.*)\,\"media_id_string.*/\1/p'`
    echo "$MEDIAID"
    DATE=`date +"%B %d %Y, %H:%M"`
    /usr/local/bin/twurl "/1.1/statuses/update.json" -d "media_ids=$MEDIAID&status=$MESSAGE ($DATE)."
    #echo "$MESSAGE"
else
    echo "Image too old."
fi
