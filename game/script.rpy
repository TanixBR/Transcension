# You can place the script of your game in this file.

# Declare images below this line, using the image statement.
# eg. image eileen happy = "eileen_happy.png"
init python:
  def eyewarp(x):
    return x**1.33
  eye_open = ImageDissolve("fx/eye.png", .5, ramplen=128, reverse=False, time_warp=eyewarp)
  eye_shut = ImageDissolve("fx/eye.png", .5, ramplen=128, reverse=True, time_warp=eyewarp)
image black = '#000000'
image white = '#FFFFFF'
image class 1 = "Classroom_01_day.jpg"
image front gate = "school_gate_2.jpg"
image school grounds 1 = "school_grounds_1.jpg"
image walking_crowd:
    "crowds/crowd1.png" with Dissolve(.06, alpha=True) #shows the image with a transition
    0.6 #A pause of 0.6 sec before the next image
    "crowds/crowd2.png" with Dissolve(0.6, alpha = True) #alpha=True to preserve transparency
    0.6
    "crowds/crowd3.png" with Dissolve(0.6, alpha = True)
    0.6
    repeat #creates a loop
# Declare characters used by this game.
define k = Character('Kyoko', color="#008000")
define n = Character(None, kind=nvl)
define hu = Character( '???', color="#8B4513")
define h = Character('Hisashi', color="#8B4513")

# The game starts here.
label splashscreen:

    scene black
    with Pause(1)
    
    show text "ViSwan Studios Presents..." with dissolve
    with Pause(2)
    
    hide text with dissolve
    with Pause(1)
    return
    
label start:
stop music 
play music "music/Pre-chapter Jingle.mp3" noloop fadein 2.0 fadeout 2.0
scene black with dissolve
show text "Prologue" with Pause(4.2)
with dissolve
scene black with dissolve
play music "music/Beginnings (Prologue).mp3" loop fadein 2.0
n "I always knew I was different"
n "Ever since I was a child, I just knew SOMETHING was different"
n "Unfortunately, I couldn't quite put my finger on it until I was 13"
nvl clear
n "The term \"transgender\" comes to mind for many."
n "Although to me, it's just another thing to add on the pile of things that make up me as a person"
nvl clear
n "Let's see..."
n "I suffer from fairly bad social anxiety."
n "As a result, I could be considered \"shy\" by many."
n "This led to me being kind of a \"shut-in\"." 
nvl clear
n "However..."
nvl clear
n "This also gave me time to figure out what I like to do."
n "I dabbled quite a bit in the arts, and figured out that my \"thing\", so to speak, was music."
n "Before long, My parents took note of this, and figured the best course of action was to send me to a school for \"gifted\" individuals."
n "No, I don't mean mentally or physically disabled."
n "I mean, people who are talented in the arts and related topics."
nvl clear
n "Chiaharu Academy, it's called."
n "Located in a quaint little town in Northern Japan."
n "It would be there that I would spend two years of my life, improving my artistic skills, while at the same time hopefully improving my social skills."
n "This is my story"
nvl clear

stop music
play music "music/Pre-chapter Jingle.mp3" noloop fadein 2.0 fadeout 2.0
scene black with dissolve 
show text "Act 1\nNew Beginnings" with Pause(4.2)
with dissolve
scene front gate with dissolve
play music "music/Excitement.mp3" loop fadein 2.0
k "Well, here goes nothing. First day at Chiaharu Academy."
"I close my eyes, quickly reflecting on my existence"
scene black with eye_shut
n "I'd be lying if I said I wasn't at least a little nervous"
n "I've never exactly had good experiences with schooling, be it due to me being bullied all throughout school, or some other thing, I will never know."
n "Regardless, I've never exactly been the type to easily socialize."
n "I'm just hoping that my time here will change that."
nvl clear
scene white with eye_open
scene front gate
"I let out a fairly long sigh"
k "Let's do this."
scene school grounds 1 with dissolve
show walking_crowd
"There is a surprisingly large amount of students milling about the school grounds"
k "Come on Kyoko, don't panic, don't panic, breathe...."
hide walking_crowd
scene black with eye_shut
python:
    renpy.music.set_volume(0, delay=2, channel='music')
n "I tend to have panic attacks when in areas with a lot of people"
n "As such, I tend to keep to myself"
n "Breathe in."
n "Breathe out."
nvl clear
"I repeat this a few more times until I feel adequately comfortable"
python:
    renpy.music.set_volume(1, delay=2, channel='music')
scene white with eye_open
scene school grounds 1
show walking_crowd
hu "Hey, uh, are you ok?"
"I quickly realize that someone, a boy, is talking to me."
n "He appears to be about 5 foot 6, with dark glasses and short brown hair"
nvl clear
k "Uh, yeah, sorry. I'm ok. Just kinda zoned out for a second there."
h "Hey, it's ok! Happens to me every so often. My name's Hisashi, what's your name?"
k "Kyoko. Kyoko Ashitaru"
h "Well, nice to meet you, Kyoko! Is this your first day at Chiaharu?"
k "Yeah, I guess you could say that. I transferred here from my other school"
