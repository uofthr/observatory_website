#!/bin/bash

#./make_hour.bash

MESSAGES=( "A time-lapse showing the view from #UTSC during the last 40 minutes. 🎥" "This video shows a time-lapse of the last 40 minutes as seen from #UTSC observatory. #ScarbTO" "The last 40 minutes as seen from the @UTSCObservatory. #timelapse 🍿" "The observatory at the University of Toronto Scarborough recorded this time-lapse of the last 40 minutes. #UofT #UTSC" "This is an automated post showing the last 40 minutes as a timelapse. #ScarbTO #UofT" )
i=$(( RANDOM % ${#MESSAGES[@]} ))
MESSAGE="${MESSAGES[i]}"

bash ./uploadNightVideoToTwitter.bash "$MESSAGE"
