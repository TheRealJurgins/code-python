import webbrowser as wb
import pyautogui as pg

name = pg.prompt("What's your name?")
pg.alert("Hello " + name)

food = pg.prompt("What's your favorite food?")
pg.alert(name + " likes to eat " + food)

sport = pg.prompt("What's your favorite sport?")
pg.alert(name + " likes to play " + sport)

age = pg.prompt("What's your age?")
pg.alert(name + " likes to eat " + food + ", likes to play " + sport + ", and is " + age + ".")

fteam = pg.prompt("What's your favorite football team?")
if fteam == "Patriots":
    pg.alert("Youre dumb.")
    wb.open("https://www.youtube.com/watch?v=a6GGZ68mOZA")
elif fteam == "Texans":
    pg.alert("Yee")
    wb.open("https://www.youtube.com/watch?v=SdK80l6eC1o")
elif fteam == "Panthers":
    pg.alert("k")
elif fteam == "Steelers":
    pg.alert("yur garbage")
    wb.open("https://www.youtube.com/watch?v=cp2TkF4uek4")
elif fteam == "Jaguars":
    pg.alert("look at this.")
    wb.open("https://www.youtube.com/watch?v=FVg41m4vHV4")
else:
    pg.alert(name + " likes the " + fteam)

bteam = pg.prompt("What's your favorite baseball team?")
if bteam == "Yankees":
    pg.alert("enjoy")
    wb.open("https://www.youtube.com/watch?v=I4xmwL94sqE")
    wb.open("https://www.youtube.com/watch?v=I4xmwL94sqE")
    wb.open("https://www.youtube.com/watch?v=I4xmwL94sqE")
    wb.open("https://www.youtube.com/watch?v=I4xmwL94sqE")
    wb.open("https://www.youtube.com/watch?v=I4xmwL94sqE")
    wb.open("https://www.youtube.com/watch?v=I4xmwL94sqE")
    wb.open("https://www.youtube.com/watch?v=I4xmwL94sqE")
    wb.open("https://www.youtube.com/watch?v=I4xmwL94sqE")
    wb.open("https://www.youtube.com/watch?v=I4xmwL94sqE")
elif bteam == "I hate baseball":
    pg.alert("basketball sucks")
elif bteam == "Phillies":
    pg.alert("k")
elif bteam == "Red Sox":
    pg.alert("congladuration")
elif bteam == "Orioles":
    pg.alert("okay")
else:
    pg.alert(name + " likes the " + bteam)

movie = pg.prompt("What's your favorite movie?")
if movie == "finding dory":
    pg.alert("k")
elif movie == "Up":
    pg.alert("classic")
elif movie == "Vulture 3":
    pg.alert("what is that")
elif movie == "Jumanji":
    pg.alert("youre sick")
    wb.open("https://www.youtube.com/watch?v=c8CHDTpbh5w")
elif movie == "whitman":
    pg.alert("yees")
else:
    pg.alert(name + " likes to watch " + movie)
    


    
    
