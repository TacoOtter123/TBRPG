from flask import Flask, render_template, send_file
from PIL import Image, ImageDraw, ImageFont
import random

app = Flask(__name__)

@app.route('/haiku')
def hello():
    fives=["An old silent pond...", "Autumn moonlight shines", "In the twilight rain", "For love and for hate", "A mountain village", "Night; and once again,", "The summer river:", "A lightning flash", "Plum flower temple", "A little boy sings", "meteor shower", "a gentle wave", "The crow flies again", "Slowly dripping down", "Won't you take me to", "Three hundred seven", "It's like poetry", "'yooooooooooooooo' she swiftly said", "I ate burritos", "O distant night help", "A can of soda", "Silent in the dark", "Twelve red kangaroos", "Jotaro stops time", "JOSEPHU JOESTAR", "ROADROLLERDADAH", "He is menacing", "In the wind there is ", "we can see you to ", "I know where you live ", "The zonk is not real ","Making white blankets ", 'intimidating', 'Miracle is weird', 'Allyu is dumb', 'Fortnite is so cool', 'Fortnite is so bright', "Story of my life", "There's always next year", "California", "Come back right away", "Give me some of it", "I will go with you", "This is all for now", "Winter and summer","Trigonometry", "Intimidating", "Abominable", "Illuminati", "Abracadabra", "A can of soda", "Two orange staplers", "A dog chasing cats", "A cat chasing dogs", "A dog chasing cats", "Joon sits on toilet", "Refrigerator", "Isaac likes to poo", "Michael's poo smells bad", "It is all my fault", "Before every meal", "Dont talk about it", "Do you believe it", "Watch television", "Michael loves fortnite", "Joon likes miracles", "I like Alia ", "Yet I am content.", "How Can You Sleep?", "Are You Frightened Yet?", "ILLUMINATI", "Now I will Show You.", "Take The Shot, James Bond!", "illuminati", "abracadabra", "california", "i have lost my quiche", "right across the street", "before every meal", "a good policeman", "great oak and tori", "trigonometry", "louisiana", "i made a mistake", "play the piano", "i brought the dab back", "Nancy Pelosi", "Intimidating", "Philson Ho is fast", "Photosynthesis", "Electricity", "Serendipity", "China number one", "Philson is so smart", "Canada is bomb", "China Number one", "Donald Trump MAGA", "I like it a lot", "An old silent pond","Mathematical", "Obligatory", "In the April wind", "Blix Hadell-Florin", "Error 404", "Like, run Scooby Doo", "Who wants a scooby snack", "Easter bunny hides" ]
    sevens=["perpetually funky", "a worm digging silently", "I swat a fly and offer", "Under the piled-up snow", "Abracadabracadab", "Swaying in the evening sun", "balancing its tomato", "Tragedy of Darth Plagueis", "on a terrace, eyes aglow,", "Drops fall and flow into one", "The spreadsheet stares back in awe", "There in perpetuity", "I am riding a pony", "Given dull and vapid names", "Pastapocalypse, again?", "Bootleg Sharknado remakes", "Kirby is unoptimized", "JoJo stands menacingly", "SONO CHINO SADAME", "Sunglasses with no lenses", "A chair people don't sit on", "Bruh sound effect one hundred ten", "Communist Propoganda", "That's against my religion", "PRESS A TO RECHARGE HAIKU", "Easter eggs are out of sight ","I am in you dark basement ","I hear you taking at night ","White lily and rose bouquet ","I like to eat them daily", 'leaves falling in the moonlight', 'Fortnite is the very best', 'moon rising during midnight', 'Fornite is important', 'Chanyu Kim is dangerous', "Curiosity is good", "All the very best to you", "The story ends with a kiss", "Well she was just seventeen", "It was raining cats and dogs", "Water will kill you one day", "Some assembly requires", "I'll alert the media", "I can't take it anymore", "No purchase necessary", "Chicken tastes just like chicken", "Alexander Hamilton", "The second line has seven", "Study harder Xiangbo QI", "Please stop pooing Xiangbo Qi", "Your brown poo stinks Michael Qi", "How Alone I truly Feel", "This Haiku Is Real Depressing,", "I had to do it to 'Em.", "Memes Are My Only Purpose", "Communist Propaganda,", "Sowing Madness In Our Brains", "Tennis Is not A Real Sport", "If you Listen, You Will Hear.", "Why Must You Torment Me so?", "autobiographical", "always take care of your health", "learn the art of listening", "heterogeneity", "conceptualization", "the winter season is good", "i like to eat too much grass", "look, i have some persimmons", "let's agree to disagree", "getting there is half the fun", "learn the art of listening", "i will tell you why later", "what is the soup of the day?", "it works on my computer", "dot the i's and cross the t's", "Cross country is not a sport", "Philson Ho thinks he is smart", "It's easy if you just try", "If I tell you then you're' dead", "Baby you can drive my car", "This sentance has seven beats", "Canadians are so great", "Baby you can drive my car", "I really did not do it", "America number one","A frog jumps into the pond", "Autobiographical", "Olimar is a top tier", "David give me all your items", "Biggie Cheese is the true god", "death is inevitable" ]
    fives2=["The roads take me home.", "splash! Silence again.", "into the chestnut.", "Here in funkytown", "A lovely sunset", "Seems so far away", "Go climb Mount Fuji!", "But slowly, slowly!", "pricks like a bramble.", "in the cold of night!", "Oh, Oklahoma!", "the sound of water", "a very mad fish.", "it turns into rain", "The beds are burning", "goes through the water", "I have seen water", "Natural objects", "Don't have to be that.", "My clock is melting", "The window frame.", "I have seen foothills", "a leafless tree beckons.", "Faint sounds of a flute", "I nod, while sighing", "on the garden fence", "blowing on the line.", "To the bourgeoisie", "Perfectly balanced.", "They are stubborn throes.", "Bruh Sound Effect 2", "Roblox V. Minecraft", "Abracadabra", "End of the Haiku", "Haiku is finished", "I have no idea", "FROM COLORAMA", "No more haiku left", "Fingers are tired", "Haiku is over", "Illuminati ","Opportunity ", "Where is the zonk now ","Super Smash Flash 2 ", "I like to drink blood ", "Pediatrician ", "Perpendicular ", "Unbelievable ", "Your in the bathroom ", 'intimidating', 'Miracle is weird', 'Allyu is dumb', 'Fortnite is so cool', 'Fortnite is so bright', "Oh, give me a break", 'We are not alone', "Something smells fishy", "I meant to do that", "Is it Friday yet?", "No pun intended", "You want fries with that", "How can I help you?", "I might know a guy", "appreciation", "abnominable", "illuminati", "generosity", "abracadabra", "creativity", "no one's laughing now", "electricity", "cold,chilly autumn", "snow, hail, rain, winter", "there's no place like home", "whichever comes first", "oh sure, you laugh now", "i am what i am", "something smells fishy", "Give it to me please", "I have lost my keys", "He has a good job", "There is enough room", "government shutdown","Give it to me please", "I have lost my keys", "He has a good job", "There is enough room", "government shutdown", "Let's get this bread", "We got the Bread", "bag the baguette", "latching the loaf", "splash! Silence again", "Nightfall in autumn", "Egan is bad at Smash", "Sand scatters the beach", "I like to eat rats","danny devito"]
    line1=(random.choice(fives))
    line2=(random.choice(sevens))
    line3=(random.choice(fives2))
    background = ["/home/TacoOtter/flower.jpeg", "/home/TacoOtter/fall of water.jpg", "/home/TacoOtter/walkway.jpeg"]
    font = ImageFont.truetype("Pillow/Tests/fonts/FreeMono.ttf", 30)
    mocked = Image.open(random.choice(background))
    d = ImageDraw.Draw(mocked)
    d.text((8,12), line1, font=font, fill=(0,0,0,126))
    d.text((8,62), line2, font=font,fill=(0,0,0,126))
    d.text((8,112), line3, font=font, fill=(0,0,0,126))
    d.text((10,10), line1, font=font, fill=(255,255,255,256))
    d.text((10,60), line2, font=font,fill=(255,255,255,256))
    d.text((10,110), line3, font=font, fill=(255,255,255,256))
    mocked.save("mocked.jpg")
    return render_template('about.html')

@app.route('/download')
def download():
    return send_file("/home/TacoOtter/mocked.jpg", as_attachment=True, attachment_filename='haiku.png')

@app.route('/meme')
def yobama():
    return send_file("/home/TacoOtter/yobama.jpg", as_attachment=True, attachment_filename='funny.png')
    
@app.route('/')
def home():
    return render_template('home.html')

# @app.route("/mock", methods=["GET", "POST"])
# @app.route("/spongebot", methods=["GET", "POST"])
# def sponge_index():
#     if request.method == "GET":
#         return render_template("spongebot.html")
#     if request.method == "POST":
#         mock(request.form['url'])
#         return send_file("mocked.png", as_attachment=True, attachment_filename='mocked.png')

