from marvel import Marvel
from keys import PRIVATE_KEY, PUBLIC_KEY

marvel = Marvel(PUBLIC_KEY=PUBLIC_KEY, PRIVATE_KEY=PRIVATE_KEY)

comics = marvel.comics

all_comics = comics.all()["data"]["results"]

print(all_comics[0]["thumbnail"])
