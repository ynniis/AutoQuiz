# Authors:
# Ynniis
# NKRIDev
# 11/04/2025

# Librarys
import streamlit as st
from youtube_transcript_api import YouTubeTranscriptApi
import os
from openai import OpenAI
import json

# Creation of the JSON quiz via ChatGPT
def createQuizz(video_id):
    ytt_api = YouTubeTranscriptApi()
    fetched_transcript = ytt_api.fetch(video_id, languages=['en'])	

    scriptArray = []

    for snippet in fetched_transcript:
        scriptArray.append(snippet.text)

    # Create an OpenAI object with API key (do not share it)
    private_key = st.secrets["PRIVATE_KEY"]
    client = OpenAI(
        api_key=private_key
    )     

    json_fomat =  {"quiz":{"title":"","description":"","questions":[{"id":1,"question":"","options":["","","",""],"id_answer":""}]}}

    # Ask something to ChatGPT bot
    completion = client.chat.completions.create(
        model="gpt-4o-mini",
        max_tokens=500,
        messages=[
            {
                "role": "system",
                "content": "You are an english teacher"
            },
            {
                "role": "user",
                "content": f"Do a 5 question quizz in json format with this youtube script video : {scriptArray}. The JSON needs to be in the following format : {json_fomat} and we need only JSON please remove ``` and json. id_answer is the index of the correct answer in options."
            }
        ]
    )

    jsonQuizz = completion.choices[0].message.content
    return jsonQuizz

# Retrieve the video ID of a YouTube URL
def extraire_id(tag_video):
    if "youtu.be/" in tag_video:
        video_id = tag_video.split("youtu.be/")[1].split("?")[0]
    elif "youtube.com/watch?v=" in tag_video:
        video_id = tag_video.split("v=")[1].split("&")[0]
    else:
        raise ValueError("Invalid YouTube video tag format")
    return video_id

# Displaying the quiz on the page
def quiz_display(quiz_object):
    title = quiz_object['quiz']['title']
    description = quiz_object['quiz']['description']
    questions = quiz_object['quiz']['questions']
    
   # We removed the video because there was an error between streamlit and Youtube (access problem)
   # st.video(st.session_state.get('url_video', ''))

    st.subheader(title)
    st.text(description)

    for question in questions:
        key = f"question_{question['id']}"
        options = question['options']
        selected = st.session_state.get(key, None)

        index = options.index(selected) if selected in options else None

        st.radio(
            f"**{question['id']}. {question['question']}**",
            options=options,
            index=index,
            key=key
        )

# Logic
st.title("Automatic Quiz Generator")
url_video = st.text_input("Enter the youtube video tag (ex: :rainbow[youtu.be/xvFZjo5PgG0?si=eI9Z1KIbARmMMbiJ])")
is_clicked = st.button("Choose this video tag !")

if is_clicked:
    if url_video:
        st.session_state['url_video'] = url_video
        tag_video = extraire_id(url_video)
        quizz_json = createQuizz(tag_video)
        st.session_state['quiz_object'] = json.loads(quizz_json)
        st.balloons()
    else:
        st.error("Please enter a valid youtube video tag.")

if 'quiz_object' in st.session_state:
    quizz_model = st.session_state['quiz_object']
    quiz_display(quizz_model)

    send_button = st.button("Send !")
    if send_button:
        score = 0
        total = len(quizz_model["quiz"]["questions"])

        for question in quizz_model["quiz"]["questions"]:
            user_answer = st.session_state.get(f"question_{question['id']}")

            if user_answer == question["options"][int(question["id_answer"])]:
                score += 1
            
        st.success(f"Score: {score}/{total}")

        if score == total:
            st.balloons()
