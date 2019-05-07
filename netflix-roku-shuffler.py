from roku import Roku; 
import time;
roku = Roku('192.168.60.65');
# identify hulu app, switch launcher to hulu
netflix = roku['Netflix'];
netflix.launch();
# roku.current_app --> potential future while loop; if loop = expected app, end

# Wait for profile screen.
time.sleep(3);
# Select first profile.
roku.select();
# land on last show, go back to main menu
time.sleep(10);
roku.back();
# navigate to left nav bar
time.sleep(.5);
roku.left();
# go up to search
time.sleep(.5);
roku.up();
# select search
time.sleep(.5);
roku.select();
# enter search term
time.sleep(.5);
roku.literal('word');
# Navigate to movie/show
time.sleep(.5);
roku.right();
time.sleep(.5);
roku.right();
time.sleep(.5);
roku.right();
time.sleep(.5);
roku.right();
time.sleep(.5);
roku.right();
time.sleep(.5);
roku.right();
# play movie
time.sleep(.5);
roku.play();

# from random import choice
# word = choice("josh jeremy peter paul mary".split())


# roku.apps --> identify hulu
# python library --> random
# from random import choice https://stackoverflow.com/questions/306400/how-to-randomly-select-an-item-from-a-list
# Define an array --- vairable = [a,b,x]
# string split method --> vairable = "jeremy josh isl table book"
# variable.split ---> will output array