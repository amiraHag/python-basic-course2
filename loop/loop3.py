# ----------------------------
# -- Loop => While Training --
# -- Simple Bookmark Manage --
# ----------------------------


myFavouriteWebs = []
maximumWebs = 5

while maximumWebs > 0:

  web = input("PLease enter the website name you want:")

  myFavouriteWebs.append(f"https://{web.strip().lower()}")
  maximumWebs -= 1

  print(f"Website Added, {maximumWebs} Places Left")
  print(myFavouriteWebs)

else:

  print("Bookmark Is Full, You Cant Add More")

if len(myFavouriteWebs) > 0:
  myFavouriteWebs.sort()
  index = 0
  print("Printing The List Of Websites in Your Bookmark")

  while index < len(myFavouriteWebs):
    print(myFavouriteWebs[index])
    index += 1
