

# How to change the map
Mac gayver Laby is using a simple text file to generate the map, as so, it is very easy for you to create
new maps, let's go throught the steps together :

- First of all, create a file with the name of your choosing (ex : map2.txt) and don't forget the ".txt"
- Inside your file use x15 col and x15 lines
- The laby used simple patterns to tell the game what is a path, a wall, the start and the end, 
here is the code related :
    # = Wall (Hero cannot go)
    . = Path (Hero can go)
    S = Where hero starts 
    X = The end 
- Finally update the map here : models/laby and find the line 31, change map1.txt to your new one

That's all !

