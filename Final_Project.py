#FINAL

def final():
    #Welcome and introduction can always add more if I need more lines
    welcome = 'Welcome to the McCord Player Analysis!'
    x = welcome.center(220)
    print(x)
    line = ('----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------')
    y = line.center(220)
    print(y)
    intro1 = 'This analysis is designed to help you as a player figure out what exactly you need to work on to become the greatest you can be!'
    a = intro1.center(220)
    print(a)
    print(' ')
    intro2 = 'During this analysis, I am going to ask you a number of questions with listed options. Please choose the option that relates most to you when prompted by copying that exact option. After you have answered all of the questions, you will be given advice on how to get better at that certain aspect as well as links to youtube videos to help.'
    b = intro2.center(220)
    print(b)
    print(' ')
    intro3 = 'Feel free to take this questionnaire as many times as you like. We recommend that you do this so you can get the most out of the program. If you have any questions or feedback contact me at connor.mccord04@gmail.com.'
    c = intro3.center(220)
    print(c)
    line2 =  ('----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------')
    c = line2.center(220)
    print(c)
    

    #Chatbot portion
    #1st
    print(" ")
    first = input('How long have you been playing lacrosse? -> 0-2 years   2-5 years   6+ years [Answer Here->]   ')
    print(first)
    if first == "0-2 years":
        print("So you're just getting started. That's great!")
    elif first == "2-5 years":
        print("So you're experienced. Very good!")
    elif first == "6+ years":
        print("Ah a veteran, very nice!")
    #2nd
    print(" ")
    second = input('What position do you play? -> Attack   Midfield   Dmiddie   LSM   Close   Goalie   FOGO [Answer Here->]   ')
    print(second)
    if second == "Attack" or second == "Midfield":
        attack1 = input('Are you a scorer or feeder? -> Scorer   Feeder [Answer Here->]   ')
        print(attack1)
        if attack1 == "Scorer":
            scorer1 = input('What is your greatest weakness as a scorer? -> Dodging   Shooting   Finishing [Answer Here->]   ')
            print(scorer1)
            if scorer1 == "Dodging":
                dodging1 = input('What dodge do you struggle with the most? -> Split Dodge   Roll Dodge   Swim Dodge [Answer Here->   ')
                print(dodging1)
                if dodging1 == "Split Dodge":
                    print("For split dodges, I would recommend ")
                    print("Copy and paste this link to learn more about split dodges! (https://www.youtube.com/watch?v=M4Tvpgv1RA0)")
                    new = input("Would you like to learn another dodge? Yes")
                    if input == "yes":
                       print(dodging1)
                elif dodging1 == "Roll Dodge":
                    print("Copy and paste this link to learn more about roll dodges! (https://www.youtube.com/watch?v=xsAaGA0Yl8Y)")
                elif dodging1 == "Swim Dodge":
                    print("Copy and paste this link to learn more about swim dodges! (https://www.youtube.com/watch?v=s8tphBZKPc0)")
            elif scorer1 == "Shooting":
                shooting1 = input('Where do you prefer to shoot from? -> Up top   Wings [Answer Here->]   ')
                print(shooting1)
                if shooting1 == "Up top":
                    up_top = input('When you are shooting from up top, which do you prefer? -> Shooting on the run   Step downs [Answer Here->]   ')
                    print(up_top)
                    if up_top == "Shooting on the run":
                       on_run = input('If you are struggling to shoot on the run, try watching this video! (https://www.youtube.com/watch?v=WG6TBAAq7UE) . Would you also like a video for a shooting practice routine? -> Yes   No [Answer Here->]   ')
                       print(on_run)
                       if on_run == "Yes":
                           routine = ("Here you go! Now go get some work in! (https://www.youtube.com/watch?v=hU0aOLGF9p0)")
                           print(routine)
                       elif on_run == "No":
                            come_on = input('Are you sure? This routine was made by a legititmate d1 player and is a great way to get better at shooting! -> I am ok   Sure [Answer Here->]   ')
                            print(come_on)
                            if come_on == "I'm ok":
                               print("Ok if you say so.")
                            elif come_on == "Sure":
                                 print("Glad you changed your mind! Here it is. Now go get some work in! (https://www.youtube.com/watch?v=hU0aOLGF9p0)")       
                elif shooting1 == "Wings":
                    wings = input('What do you struggle with most while shooting from the wings? -> Getting it on cage   Getting my hands free [Answer Here->]   ')
                    print(wings)
                    if wings == "Getting it on cage":
                       on_cage = input('If you are having trouble getting the ball on cage, watch this video! (https://www.youtube.com/watch?v=12endL4Wr5M) . Would you also like a video for a full shooting practice routine> -> Yes   No [Answer Here->]   ')
                       print(on_cage)
                       if on_cage == "Yes":
                           routine = ("Here you go! Now go get some work in! (https://www.youtube.com/watch?v=hU0aOLGF9p0)")
                           print(routine)
                       elif on_cage == "No":
                            come_on1 = input('Are you sure? This routine was made by a legititmate d1 player and is a great way to get better at shooting! -> I am ok   Sure [Answer Here->]   ')
                            print(come_on1)
                            if come_on1 == "I am ok":
                               print("Ok if you say so.")
                            elif come_on1 == "Sure":
                                 print("Glad you changed your mind! Here it is. Now go get some work in! (https://www.youtube.com/watch?v=hU0aOLGF9p0)")
                    elif wings == "Getting my hands free":
                         hands_free = input("If you are having trouble getting your hands free on the wing, try watching this video! (https://www.youtube.com/watch?v=zrH3OnA96Y0).")
            elif scorer1 == "Finishing":
                 finishing = input('What is your biggest weakness when finishing? -> Finishing Cross Crease   Finishing in tight [Answer Here->]   ')
                 print(finishing)
                 if finishing == "Finishing Cross Crease":
                    cross_crease = input('If you are having trouble finishing cross crease, watch this video! (https://www.youtube.com/watch?v=UK3PMoUXNYA). Would you also like a video for a finishing practice routine> -> Yes   No [Answer Here->]   ')
                    if cross_crease == "Yes":
                       print('Awesome! Here it is. Now go get some work in! (https://www.youtube.com/watch?v=duDhBa-v-mI).')
                    elif cross_crease == "No":
                         
                         print(come_on2)
                         if come_on2 == "I am ok":
                               print("Ok if you say so.")
                         elif come_on2 == "Sure":
                              print("Glad you changed your mind! Here it is. Now go get some work in! (https://www.youtube.com/watch?v=duDhBa-v-mI).")
                 if finishing == ("Finishing in tight"):
                    in_tight = input('If you are having trouble finishing in tight, watch this video! (https://www.youtube.com/watch?v=oZF8dNUIcIM). Would you also like a video for a finishing practice routine> -> Yes   No [Answer Here->]   ')
                    print(in_tight)
                    if in_tight == "Yes":
                       print("Awesome! Here it is. Now go get some work in! (https://www.youtube.com/watch?v=duDhBa-v-mI).")
                    elif in_tight == "No":
                         come_on3 = input("Are you sure? It's great for practice! -> I am ok   Sure [Answer Here->]   ")
                         print(come_on3)
                         if come_on3 == "I am ok":
                               print("Ok if you say so.")
                         elif come_on3 == "Sure":
                              print("Glad you changed your mind! Here it is. Now go get some work in! (https://www.youtube.com/watch?v=duDhBa-v-mI).")
        elif attack1 == "Feeder":
            feeder1 = input('What is your greatest weakness as a feeder? -> Getting away from the defender  Getting it on target [Answer Here->]')
            print(feeder1)
            if feeder1 == "Getting away from the defender":
               print('If you are having trouble getting away from your defender, dodging is the best way to get this done! Here are videos on some of our favorite dodges! Roll Dodge(https://www.youtube.com/watch?v=xsAaGA0Yl8Y) , Split Dodge(https://www.youtube.com/watch?v=M4Tvpgv1RA0) , Swim Dodge(https://www.youtube.com/watch?v=s8tphBZKPc0).') 
            elif feeder1 == "Getting it on target":
               print('The best way to find tune your passing skills is wall ball! Here is one of our favorite wallball routines! (https://laxlibrary.com/lacrosse-content/300-college-lacrosse-wall-ball-workout/).')

            
    elif second == "Dmiddie" or second == "LSM":
         dmiddie1 = input('What do you struggle with most? -> Clearing   Strength   Speed [Answer Here->]   ')
         print(dmiddie1)
         if dmiddie1 == "Clearing":
            clearing = input('If you are having trouble with clearing, here is a great video on how to do so! (https://www.youtube.com/watch?v=KpPgzEGNNGE) . Would you also like a video to help practice this? -> Yes   No [Answer Here->]  ')
            print(clearing)
            if clearing == "Yes":
               print('Awesome, here it is! (https://www.youtube.com/watch?v=b3aNQyHH1w8).')
         elif dmiddie1 == "Strength":
              lift2 = input("Do you lift regularyly? -> Yes   No [Answer Here->]   ")
              if lift2 == "Yes":
                  print('Awesome! If your current workout routine is working for you great! Please check out the strength maxes portion of this analysis! If your workout does not currently work for you, check out the strength workout portion of this analysis!')
              elif lift2 == "No":
                   lifthuh2 = input("Well if you want to build strength, I suggest you start lifting soon. Would you like a workout plan to help you get started? Yes   No [Answer Here->]   ")
                   print(lifthuh2)
                   if lifthuh2 == "Yes":
                      print("Awesome! Please refer to the strength workout function at the bottom!")
                   elif lifthuh2 == "No":
                       nolift2 = input("Okkkkk but its the only way you will build strength. Are you sure?-> I want it   I am ok [Answer Here->]")
                       print(nolift2)
                       if nolift2 == "I want it":
                          print("Awesome, head to the strength workout function at the bottom!")
                       elif nolift2 == "I am ok":
                            print("That's ok")

         elif dmiddie1 == "Speed":
              run2 = input("Do you run regularyly? -> Yes   No [Answer Here->]   ")
              if run2 == "Yes":
                 print('Awesome! If your current running routine is working for you great! Please check out the speed maxes portion of this analysis! If your workout does not currently work for you, check out the speed workout portion of this analysis!')
              elif run2 == "No":
                   runhuh2 = input("Well if you want to improve speed, I suggest you start training soon. Would you like a workout plan to help you get started? Yes   No [Answer Here->]   ")
                   print(runhuh2)
                   if runhuh2 == "Yes":
                      print("Awesome! Please refer to the speed workout function at the bottom!")
                   elif runhuh2 == "No":
                        norun2 = input("Okkkkk but its the only way you will improve your speed. Are you sure?-> I want it   I am ok [Answer Here->]")
                        print(norun2)
                        if norun2 == "I want it":
                            print("Awesome, head to the speed workout function at the bottom!")
                        elif norun2 == "I am ok":
                             print("That's ok")
                      
               
         



    elif second == "Close":
         close1 = input("What do you struggle with most? -> IQ   1v1   Strength   Speed [Answer Here->]   ")
         print(close1)
         if close1 == "IQ":
            close_iq = input('What exactly do you have the most trouble understanding? -> Slides   Position   Man Down [Answer Here->]   ')
            print(close_iq)
            if close_iq == "Slides":
               slides = input('If you are having trouble understanding slides, here is a great video for that! (https://www.youtube.com/watch?v=rbL9yXyCXtQ) . Would you also like a drill to help practice this? -> Yes   No [Answer Here->]   ')
               print(slides)
               if slides == "Yes":
                  print("Awesome! Here it is. Now go get some work in! (https://www.youtube.com/watch?v=59N9iblxI08).")
               elif slides == "No":
                    come_on4 = input("Are you sure? It's great for practice! -> I am ok   Sure [Answer Here->]   ")
                    print(come_on4) 
                    if come_on4 == "I am ok":
                       print("Ok if you say so.")
                    elif come_on4 == "Sure":
                         print("Glad you changed your mind! Here it is. Now go get some work in! (https://www.youtube.com/watch?v=duDhBa-v-mI).")      
            elif close_iq == "Position":
                 pos = input('Are you having trouble more with posistioning on ball or off ball? -> On ball   Off ball [Answer Here->]   ')
                 print(pos)
                 if pos == "On ball":
                    on_ball = input('If you are having trouble with on ball positioning, heresi a great video! (https://www.youtube.com/watch?v=IF0wQWryalc) . Would you also like a drill to help practice this? -> Yes   No [Answer Here->]   ')
                    if on_ball == "Yes":
                       print("Awesome! Here it is. Now go get some work in! (https://www.youtube.com/watch?v=54n9CVGaums).")
                    elif on_ball== "No":
                         come_on4 = input("Are you sure? It's great for practice! -> I am ok   Sure [Answer Here->]   ")
                         print(come_on4)
                         if come_on4 == "I am ok":
                            print("Ok if you say so.")
                         elif come_on4 == "Sure":
                              print("Glad you changed your mind! Here it is. Now go get some work in! (https://www.youtube.com/watch?v=54n9CVGaums).")
                 elif pos == "Off ball":
                      print("Here is a great video on to help with offball! (https://www.youtube.com/watch?v=8pRxEibPq_0) .")

            elif close_iq == "Man Down": 
                 print('Here is a great video that explains man down thoroughly! (https://www.youtube.com/watch?v=OQN-m20q8Lw).')
                
                
         elif close1 == "1v1":
              onev1 = input('What part of 1v1s do you struggle with the most?-> Checks   Playing the man [Answer Here]->   ')
              print(onev1)
              if onev1 == "Checks":
                 checks = input('If you are struggling with checks, here is a great video! (https://www.youtube.com/watch?v=p-ezV0a4p2g) . Would you like a video on how to practice these as well? -> Yes   No [Answer Here->]   ') 
                 print(checks)
                 if checks == 'Yes':
                    print('Here it is! Now go get some work in! (https://www.youtube.com/watch?v=mochLy2dRnY)')
                 elif checks == 'No':
                      come_on5 = input("Are you sure? It's great for practice! -> I am ok   Sure [Answer Here->]   ")
                      print(come_on5)
                      if come_on5 == "I am ok":
                         print("Ok if you say so.")
                      elif come_on5 == "Sure":
                           print('Here it is! Now go get some work in! (https://www.youtube.com/watch?v=mochLy2dRnY)')

              elif onev1 == "Playing the man":
                   man = input('If you are struggling with playing the man, here is a great video! (https://www.youtube.com/watch?v=iWtEUWJqOUE) . Would you like a video on how to practice these as well? -> Yes   No [Answer Here->]   ') 
                   print(man)
                   if man == 'Yes':
                      print('Awesome here it is! Now get go get work in! (https://www.youtube.com/watch?v=BY7K0IaDNMM) .')
                   elif man == 'No':
                        come_on6 = input("Are you sure? It's great for practice! -> I am ok   Sure [Answer Here->]   ")
                        print(come_on6)
                        if come_on6 == "I am ok":
                           print("Ok if you say so.")
                        elif come_on6 == "Sure":
                             print('Here it is! Now go get some work in! (https://www.youtube.com/watch?v=BY7K0IaDNMM)')
                            
              if onev1 == 'Yes':
                 print('Awesome here it is! No go get some work in! (https://www.youtube.com/watch?v=q7aV6yDXpZM).')
              elif onev1 == 'No':
                   come_on7 = input("Are you sure? It's great for practice! -> I am ok   Sure [Answer Here->]   ")
                   print(come_on7)
                   if come_on7 == "I am ok":
                      print("Ok if you say so.")
                   elif come_on7 == "Sure":
                        print("Glad you changed your mind! Here it is. Now go get some work in! (https://www.youtube.com/watch?v=54n9CVGaums).")
                      
         elif close1 == "Strength":
              lift = input("Do you lift regularyly? -> Yes   No [Answer Here->]   ")
              if lift == "Yes":
                  print('Awesome! If your current workout routine is working for you great! Please check out the strength maxes portion of this analysis! If your workout does not currently work for you, check out the strength workout portion of this analysis!')
              elif lift == "No":
                 nolift = input("Well if you want to build strength, I suggest you start lifting soon. Would you like a workout plan to help you get started? Yes   No [Answer Here->]   ")
                 print(lifthuh)
                 if lifthuh == "Yes":
                    print("Awesome! Please refer to the strength workout function at the bottom!")
                 elif lifthuh == "No":
                     nolift = input("Okkkkk but its the only way you will build strength. Are you sure?")
                     print(nolift)
                     if nolift == "I want it":
                         print("Awesome, head to the strength workout function at the bottom!")
                     elif nolift == "I am ok":
                         print("That's ok")

         elif close1 == "Speed":
              run = input("Do you run regularyly? -> Yes   No [Answer Here->]   ")
              if run == "Yes":
                  print('Awesome! If your current running routine is working for you great! Please check out the speed maxes portion of this analysis! If your workout does not currently work for you, check out the speed workout portion of this analysis!')
              elif run == "No":
                 norun = input("Well if you want to improve speed, I suggest you start training soon. Would you like a workout plan to help you get started? Yes   No [Answer Here->]   ")
                 print(runhuh)
                 if runhuh == "Yes":
                    print("Awesome! Please refer to the speed workout function at the bottom!")
                 elif runhuh == "No":
                     norun = input("Okkkkk but its the only way you will improve your speed. Are you sure?-> I want it   I am ok [Answer Here->]5")
                     print(norun)
                     if norun == "I want it":
                         print("Awesome, head to the speed workout function at the bottom!")
                     elif norun == "I am ok":
                         print("That's ok")
                      
                      
            
              

         
            


        
    elif second == "Goalie":
         goalie1 = input('What is your greatest weakness as a goalie? -> Low   Hip   Fivehole   Bouncers   Clearing [Answer Here->]   ')
         print(goalie1)
         if goalie1 == "Low":
            low = input('If you are struggling with low saves, here is a great video! (https://www.youtube.com/watch?v=bleLLpYxHXo) . Would you also like a full workout for saves? -> Yes   No [Answer Here->]   ')
            print(low)
            if low == 'Yes':
               print('Awesome here it is! Now get go get work in! (https://www.youtube.com/watch?v=VkjieJiUeyk) .')
            elif low == 'No':
                 come_on7 = input("Are you sure? It's great for practice! -> I am ok   Sure [Answer Here->]   ")
                 print(come_on7)
                 if come_on7 == "I am ok":
                    print("Ok if you say so.")
                 elif come_on7 == "Sure":
                      print('Here it is! Now go get some work in! (https://www.youtube.com/watch?v=VkjieJiUeyk)')
                     
         elif goalie1 == "Hip":
              hip = input('If you are struggling with hip saves, here is a great a great video! (https://www.youtube.com/watch?v=IU5vh_2E0fY) . Would you also like a full workout for saves? -> Yes   No [Answer Here->]   ')   
              print(hip)
              if hip == 'Yes':
               print('Awesome here it is! Now get go get work in! (https://www.youtube.com/watch?v=VkjieJiUeyk) .')
              elif hip == 'No':
                   print(come_on)
                   if come_on == "I am ok":
                      print("Ok if you say so.")
                   elif come_on == "Sure":
                        print('Here it is! Now go get some work in! (https://www.youtube.com/watch?v=VkjieJiUeyk)')
         elif goalie1 == "Fivehole":
              fivehole = input('If you are struggling with five hole saves, here is a great video! (https://www.youtube.com/watch?v=_kJ_LiRFrHA) . Would you also like a full workout for saves? -> Yes   No [Answer Here->]   ')
              print(fivehole)
              if fivehole == 'Yes':
                 print('Awesome here it is! Now get go get work in! (https://www.youtube.com/watch?v=VkjieJiUeyk) .')
              elif fivehole == 'No':
                   come_on8 = input("Are you sure? It's great for practice! -> I am ok   Sure [Answer Here->]   ")
                   print(come_on8)
                   if come_on8 == "I am ok":
                      print("Ok if you say so.")
                   elif come_on8 == "Sure":
                        print('Here it is! Now go get some work in! (https://www.youtube.com/watch?v=VkjieJiUeyk)')

         elif goalie1 == "Bouncers":
              bouncers = input('If you are struggling with bouncers, here is a great video! (https://www.youtube.com/watch?v=Cyo-6Q4PMm4) . Would you also like a full workout for saves? -> Yes   No [Answer Here->]   ')
              print(bouncers)
              if bouncers == 'Yes':
                 print('Awesome here it is! Now get go get work in! (https://www.youtube.com/watch?v=VkjieJiUeyk) .')
              elif bouncers == 'No':
                   come_on9 = input("Are you sure? It's great for practice! -> I am ok   Sure [Answer Here->]   ")
                   print(come_on9)
                   if come_on9 == "I am ok":
                      print("Ok if you say so.")
                   elif come_on9 == "Sure":
                        print('Here it is! Now go get some work in! (https://www.youtube.com/watch?v=VkjieJiUeyk)')
            

         elif goalie1 == "Clearing": 
              clearing = input('If you are struggling with clearing, here is a great video! (https://www.youtube.com/watch?v=SXNmDdGym1U) . Would you also like a full workout for clearing? -> Yes   No [Answer Here->]   ')
              if clearing == 'Yes':
                 print('Awesome here it is! Now get go get work in! (https://www.youtube.com/watch?v=Iq8nheX9rT8) .')
              elif clearing == 'No':
                   come_on10 = input("Are you sure? It's great for practice! -> I am ok   Sure [Answer Here->]   ")
                   print(come_on10)
                   if come_on10 == "I am ok":
                      print("Ok if you say so.")
                   elif come_on10 == "Sure":
                        print('Here it is! Now go get some work in! (https://www.youtube.com/watch?v=Iq8nheX9rT8)')

    elif second == "FOGO":
         fogo1 = input("What is your greatest weakness as a FOGO? -> Exits   Countering   Clamping   Stance   Scoring [Answer Here->]   ")
         print(fogo1)
         if fogo1 == "Exits":
            exits = input("Here is a great video on exits for faceoffs. Would you also like a video for practice?-> Yes   No [Answer Here->]   ")
            print(exits)
            if exits == "Yes":
               print("Awesome! Here it is! (https://www.youtube.com/watch?v=cg-WcXTtUGc) .")
            elif exits == "No":
                 print("If you say so.")
            

         elif fogo1 == "Countering":
              countering = input("What do you struggle with countering? -> Basics   Execution   [Answer Here->]   ")
              print(countering)
              if countering == "Basics":
                 basics = input("Here is a video for the basics! (https://www.youtube.com/watch?v=516vDY3W6KI) Would you also like a video for practice?-> Yes   No [Answer Here->]   ")
                 print(basics)
                 if basics == "Yes":
                     print("Awesome! Here it is! (https://www.youtube.com/watch?v=cg-WcXTtUGc) .")
                 elif basics == "No":
                      print("If you say so.")


                   
              elif countering == "Execution":
                   execution = input("Here is a video for execution! (https://www.youtube.com/watch?v=tPE7PchL4m8) Would you also like a video for practice-> Yes   No [Answer Here->]   ")
                   print(execution)
                   if execution == "Yes":
                     print("Awesome! Here it is! (https://www.youtube.com/watch?v=cg-WcXTtUGc) .")
                   elif execution == "No":
                        print("If you say so.")

         elif fogo1 == "Clamping":
              clamping = input("What are you mainly struggling on with clamping? -> Speed   Strength [Answer Here->]   ")
              print(clamping)
              if clamping == "Speed":
                 print("Refer to the speed section of the analysis at the bottom of the page!")
              elif clamping == "Strength":
                   print("Refer to the strength section of the analysis at the bottom of the page!")

         elif fogo1 == "Stance":
              stance = input("Here is a video on stance! (https://www.youtube.com/watch?v=iAS-CA4Kvu0) Would you also like a video for practice-> Yes   No [Answer Here->]   ")
              print(stance)
              if stance == "Yes":
                 print("Awesome! Here it is! (https://www.youtube.com/watch?v=cg-WcXTtUGc) .")
              elif execution == "No":
                   print("If you say so.")
              
         elif fogo1 == "Scoring":
              scoring = input("What do you struggle with most when trying to score? -> Shooting   Getting to the cage [Answer Here->]   ")
              print(scoring)
              if scoring == "Shooting":
                 shooting = input("Here is a video for shooting on the run! (https://www.youtube.com/watch?v=PHhXTGHhoKg) . Would you also like a video for practice-> Yes   No [Answer Here->]   ")
                 print(shooting)
                 if shooting == "Yes":
                     print("Awesome! Here it is! (https://www.youtube.com/watch?v=gfhsBLk_wx0) .")
                 elif shooting == "No":
                      print("If you say so.")
                      
    print()
    end = "Thank you for taking part in the question portion of this analysis!"
    ab = end.center(220)
    print(ab)
    more = "If you were instructed to try out the strength and/or speed functions or if you would just like to try them for fun, those are located below!"
    bc = more.center(220)
    print(bc)
    line7 =  ('----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------')
    cd = line7.center(220)
    print(cd)
    

                      
                              
def strength_intro():
    first = "So you need to work on your strength huh?"
    g = first.center(220)
    print(g)
    second = "We got you covered!"
    h = second.center(220)
    print(h)
    third = "For the strength portion of this analysis, you will have to write your maxes for various lifts."
    j = third.center(220)
    print(j)
    fourth = "These lifts include, bench, deadlift, and squat!"
    k = fourth.center(220)
    print(k)
    fifth = "The program will output what your max should be after a six month period"
    l = fifth.center(220)
    print(l)
    linee = ('----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------')
    m = linee.center(220)
    print(m)
    

#this is the how I used my list
def strength_maxes(maxes):
    '''Reference function for strength'''
    for i in range(len(maxes)):
        maxes[i]+=35
    print("These weights should be your goal weight in the next 6=8 months. Refer to the next function to recieve your workout plan!")
    return "For bench: " + str(maxes[0]) + " For squat: " + str(maxes[1]) + " For deadlift: " + str(maxes[2])#how to put each on its own line
        
   


   
   

def strength_workout():
    '''Gives a workout to reach the maxes'''
    sets = 3
    reps = 4
    percent = 50
    exercises = ["Bench", "Squat", "Deadlift"]
    
    for exercise in exercises:
        for rep in range(3, reps+3): 
            print(f"{exercise} - rep {rep} - percent {percent}")
        print()
        
    
    

      
class Speed(object):
    '''Gages the players speed'''
    def __init__(self, mile, forty,  threemile):
        '''Players speed inputs'''
        self.mile = mile
        self.forty = forty
        self.threemile = threemile

    def __str__(self):
        '''Prints Player speed'''
        end_string=''
        end_string+="[Your mile time is: "
        end_string+=str(self.mile)
        end_string+= "]"
        end_string+= ' '
        end_string+="[Your forty time is: "
        end_string+=str(self.forty)
        end_string+= "]"
        end_string+=' '
        end_string+="[Your three mile time is: "
        end_string+=str(self.threemile)
        end_string+= "]"
        return end_string

    def mile_amount(self):
        '''Gives mile amount for the week'''
        if self.mile>7.30:
            times = "4"
        else:
            times = "3"

        print("You should run 1 mile " + times + " days a week.")

    def forty_amount(self):
        '''Gives forty amount for the week'''
        if self.forty>5.2:
            times1 = "5"
        else:
            times1 = "3"
        print("You should run " + times1 + " days a week.")

            

    def threemile_amount(self):
        '''Gives 3 mile amount for the week'''
        if self.threemile>24:
            times2 = "2"
        else:
            times2 = "1"
        print("You should run " + times2 + " days a week when you are not running the mile.")
             
        
        
