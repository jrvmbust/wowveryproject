                                        ###########################################################################
                                        #######          Project Sweg- DONT FORGET TO ADD CHARACTERS         ######
                                        ###################    Coded by Rovic Vargas IV - James=    ###############
                                        ###########################################################################

                                                        #version 2 (dont also forget to change ver number)
                                                        #running the RenPy engine, you might need to install
                                                        #python to edit this codez
                                                        #edited using Editra
                                                        
                                                                    #####################
                                                                    #Scriptwriter notes:#
                                                                    #####################
                                                         
#                                                                    MORAL OF THE STORY:
#                                                                    2D IS SUPERIOR TO 3D
#                                                                
#                                                                    Moral of the Story:
#            You may have different ways to approach things but if it is justified then it’s fine. I don’t know okay. I just pulled that out from my ass.
#                                    P.S. don’t forget scene where Pygmalion comments on some of the most popular waifus around:
#                

init:
    $ slow_dissolve = Dissolve(2.0)
    $ flashbulb = Fade(0.2, 0.0, 0.8, color='#fff')
    $ deadbulb= Fade(0.2, 0.0, 0.8, color='#000')

    $ circleirisout = ImageDissolve("id_circleiris.png", 1.0, 8)
    $ circleirisin = ImageDissolve("id_circleiris.png", 1.0, 8, reverse=True)
    $ circlewipe = ImageDissolve("id_circlewipe.png", 1.0, 8)
    $ dream = ImageDissolve("id_dream.png", 2.0, 64)
    $ teleport = ImageDissolve("id_teleport.png", 1.0, 0)
    
    $ end = Character(None,
                          what_size=50, #Font size
                          what_xalign=0.5, #Centers text within the window
                          window_xalign=0.5, #Centers the window horizontally
                          window_yalign=0.5, #Centers the window vertically
                          what_text_align=0.5, #Centers text within the window, just in case
                          window_background=None,#Removes the window, so only the text shows
                          what_slow_cps=50 #Speed at which the text appears (slow)
                          )

    
image bg sc1 = im.Scale("images/sc1.png", 800, 600)
image bg sc2 = im.Scale("images/sc2.png", 800, 600)
image bg sc3 = im.Scale("images/sc3.png", 900, 700)
image bg sc4 = im.Scale("images/sc4.png", 800, 600)
image bg sc5 = im.Scale("images/sc5.png", 800, 600)
image bg sc6 = im.Scale("images/sc6.png", 800, 600)
image bg sc7 = im.Scale("images/sc7.png", 800, 600)
image bg sc8 = im.Scale("images/sc8.png", 800, 600)
image bg bbg = im.Scale("images/bbg.png", 800, 600)
image bg sctrans = im.Scale("images/sctrans.png", 800, 600)
image gala norm = im.Scale("images/gd.png", 400, 600)
image gala ivor = im.Scale("images/gdi.png", 400, 600)
image aph norm = im.Scale("images/aphnorm.png", 400, 600)
image aph dismay = im.Scale("images/aphsad.png", 400, 600)
image adv norm = im.Scale("images/adv.png", 400, 500)
image adv dismay = im.Scale("images/advdis.png", 400, 500)
image ovid norm = im.Scale("images/ovi.png", 400, 500)
image pig pig:
    im.Scale("images/pig.png", 220, 210)
    xalign .5
    yalign .5
    
image doge doge:
     anim.Blink(Image("images/doge.jpeg"))
     xalign .5
     yalign .5




# characters.
define pyg = Character(_("Pygmalion"),
                        color="#c8ffc8",
                        what_slow_cps=50)
define pyg = Character(_("Pygmalion"),
                        color="#c8ffc8",
                        what_slow_cps=50)
define adv = Character(_("Adviser"),
                        color="#c8ffc8",
                        what_slow_cps=50)
define ovi = Character(_("Ovid"),
                        color="#c8ffc8",
                        what_slow_cps=50)
define aph = Character(_("Aphrodite"),
                        color="#c8ffc8",
                        what_slow_cps=50)
define gal = Character(_("Galatea"),
                         color="#c8ffc8",
                         what_slow_cps=50)
define wow = Character(None, what_outlines=[(3, "#000000", 2, 2), (3, "#282", 0, 0)], what_size = 40, what_style="centered_text", window_style="centered_window")

# main script.
label start:

    scene bg sc1
    with dissolve
    
    pyg "A new day dawns over my house."
    pyg "The sun shining,{w} birds singing,{w} bees buzzing…"
    pyg "…and I’m here, complaining about it all. Too bad people ruin it. By {b}people{/b} I mean people like myself who scrutinize every wrong anyone or anything offers."
    pyg "Oh Olympus! I should just busy myself with something I actually like…"
    
    with dissolve
    scene bg bbg
    with dissolve
    scene bg sc2
    with dissolve
    
    show adv norm
    adv "My Lord, the ladies have been waiting for you."
    pyg "Forgive me, but I don’t want to attend to them."
    show adv dismay
    adv "*sigh* {w} Here we go again. I’ve told you countless of times, a man must settle down with someone, if otherwise that man is more than a coward-afraid of his destiny."
    pyg "Tsk… *facepalm*"
    #pyg transform to left with alpha key
    
    with dissolve
    scene bg bbg
    with dissolve
    scene bg sc3
    with dissolve
    
    show gala ivor
    with dissolve
    pyg "Oh my dear Galatea! Forgive me for wasting time with such fools! It is equivalent to death! Alas! Who will admire your perfection and bathe you with riches?"
    
    with dissolve
    scene bg bbg
    with dissolve
    scene bg sc4
    with dissolve
    
    show ovid norm
    with dissolve
    ovi "My Lord, the coming festival for Aphrodite is fast approaching, what must we do?"
    with dissolve
    pyg "Aphrodite, that’s right! The Goddess of Love! If I make her festival worthy for her, she might make Galatea worthy of love for me!"
    pyg "To wish a goddess to do such a humiliating thing… breathing life to a statue of all things… how embarrassing."
    pyg "I digress, as they say: “Do all you can for the one you love.”"
    pyg "Let’s make the offering the best we’ve ever gave, Ovid."
    
    with dissolve
    scene bg bbg
    with dissolve
    scene bg sc5
    with dissolve
    
    show pig pig
    with dissolve
    play fire "fire.wav" fadein 2 fadeout 2
    pyg "{i}Oh, I bellow how I can place{/i}"
    pyg "{i}Feelings on such lifeless things taste{/i}"
    pyg "{i}Hear too, Goddess, pleadings should trace{/i}"
    pyg "{i}Please make Love One human, none nays{/i}"
    stop fire
    
    with dissolve
    scene bg bbg
    with dissolve
    scene bg sc6
    with dissolve
    
    show aph norm
    with dissolve
    aph "Pygmalion, your prayer has been heard. How pathetic to lone for a flawless craft of the same being you truly despise, a woman."
    show aph dismay
    with dissolve
    aph "I pity you, dear Pygmalion, *sigh*{w} and for that, I shall grant your righteous desperation. Good thing too, I would probably get a good laugh while I’m at it."
    play fire "chime.wav" fadein 2 fadeout 2
    stop fire
    
    with dissolve
    scene bg bbg
    with dissolve
    scene bg sc7
    with dissolve
    
    #*TOUCHES GALATEA IN THE SFW WAY, LIKE SERIOUSLY, BRO, NOT EVEN GIVING A RAPE JOKE HERE*
    #huehue
    
    pyg "My love, you look rather different today. Your radiance, it’s glowing better than ever."
    pyg "*sigh*{w} It’s probably the light, there’s no way that the Goddess heard my cry. If she saw my heart’s true content, she would surely find it quite ironic..."
    pyg "Why did I make you anyway…? {w}Carving the pinnacle of beauty while disdaining the very thing I’m making…"
    pyg "I’m such a fool, really- {w}moping around and suffering the pain of loving something that can never love me back…"
    pyg "It’s such a pain to keep in the desire to correct the wrongdoings of others. It’s evident that no one can change for the better by himself…"
    pyg "Alas, I cannot let myself go, not now. Quite righteous, yet desperate…"
    show gala norm
    with dissolve
    gal "D-Desperate for what…?"
    pyg "Y-You can talk! You’re…alive!"
    gal "*laughs and hugs Pygmalion again*"
    pyg "I-I’m speechless…"
    show gala smile
    with dissolve
    gal "Then you do not have to talk…"
    
    with dissolve
    scene bg bbg
    with dissolve
    scene bg sc8
    with dissolve
    
    show aph norm
    with dissolve
    pyg "Thankful am I of the aid, {w}Humbly you have my life changed"
    aph "The pleasure is all mine."
    pyg "How can I ever thank you?"
    aph "Nothing that I require… just let the proper merit go in its place."
    pyg "I shall bathe you then with riches and more offerings."
    aph "Whatever you wish to do, just please… no more boars…"
    
    with dissolve
    scene bg bbg
    with dissolve
    
    centered "And thus, Galatea and I wed, always thanked Aphrodite, and in return, she never failed to bless our lives."
    centered "Who would’ve thought that I would marry the very thing that I despised. I guess in the end, the gods have the final say."
    centered "Not long after, we had another blessing, our son, Paphos."
    with dissolve
    centered "To Te’los"
    with dissolve
    
    centered "Thanks for Playing!"
    
    with dissolve
    
    menu:
        "What do you want to do?"
        
        "Restart the Game.":
            jump start
        "End the Game.":
            return
        "pls dont click":
            jump easteregg

label easteregg:
    
    scene bg bbg
    show doge doge
    with dissolve
    play music "wow.mp3" fadein 2
    
    with dissolve
    wow "This was Greek Retold: Pygmalion and Aphrodite"
    with dissolve
    wow "GROUPMATES:"
    with dissolve
    wow "Rovic Vargas"
    with dissolve
    wow "Clyde Tapales"
    with dissolve
    wow "Justin Carcacta" #huehuehuehuehue
    with dissolve
    wow "Angelika Bais"
    with dissolve
    wow "Earl Regalado"
    with dissolve
    wow "Thanks for Playing!"
    
    stop music fadeout 1
    jump menu1
    
label menu1:
    
    menu:
        "What do you want to do?"
        
        "Restart the Game.":
            jump start
        "End the Game.":
            return
        "u just clicked it, dont click this again":
            jump easteregg1
            
label easteregg1:
    
    scene bg bbg
    show doge doge
    with dissolve
    play music "wow2.mp3" fadein 2
    
    with dissolve
    wow "This was Greek Retold: Pygmalion and Aphrodite"
    with dissolve
    wow "GROUPMATES:"
    with dissolve
    wow "Rovic Vargas"
    with dissolve
    wow "Clyde Tapales"
    with dissolve
    wow "Justiniano Caracta" #huehuehuehuehue2xmorehuehue
    with dissolve
    wow "Angelika Bais"
    with dissolve
    wow "Earl Regalado"
    with dissolve
    wow "Thanks for Playing!"
    
    stop music fadeout 1
    jump menu2
    
label menu2:
    
    menu:
        "What do you want to do?"
        
        "Restart the Game.":
            jump start
        "End the Game.":
            return
        "u cant click dis anymore":
            jump menu3

label menu3:
    
    menu:
        "What do you want to do?"
        
        "Restart the Game.":
            jump start
        "End the Game.":
            return
        "pls dont":
            jump menu2
    
    
    
    


    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
