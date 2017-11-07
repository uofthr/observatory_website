#!/bin/bash
if [ $# -lt 1 ]; then
    MESSAGES=( "Live view from the #UTSC Observatory. 📷" "Live view from weather camera at the @UTSCObservatory. #UofT #Toronto #ScarbTO" "Current conditions at the UTSC Observatory. #UofT" "Live image from the astronomical observatory at #UTSC. 🔭" "Current view from #UTSC towards Highland Creek. #ScarbTO 🏞🌳" "Current sky conditions at the #UTSC Observatory. 🌌🔭" )
    i=$(( RANDOM % ${#MESSAGES[@]} ))
    DATE=`date +"%B %d %Y, %H:%M"`
    MESSAGE="${MESSAGES[i]} ($DATE)"
else
    MESSAGE="$1"
fi 

if [ $# -lt 2 ]; then
    FILENAME="latest.jpg"
else
    FILENAME="$2"
fi 

if [ `stat --format=%Y latest.jpg` -ge $(( `date +%s` - 600 )) ] || [ $# -gt 2 ]; then
    MEDIAJSON=`/usr/local/bin/twurl -H upload.twitter.com -X POST '/1.1/media/upload.json' --file "$FILENAME" --file-field 'media'`
    #echo "$MEDIAJSON"
    MEDIAID=`echo "$MEDIAJSON" | sed -rn 's/\{\"media_id\":(.*)\,\"media_id_string.*/\1/p'`
    echo "$MEDIAID"
    /usr/local/bin/twurl "/1.1/statuses/update.json" -d "media_ids=$MEDIAID&status=$MESSAGE."
    #echo "$MESSAGE"
else
    echo "Image too old."
fi
