# Photo gallery dictionary
photo_gallery = {
    1: "beach.png",
    2: "mountain.jpg",
    3: "party1.jpg",
    4: "selfie.png",
    5: "birthday.png",
    6: "concert.jpg",
    7: "sunset.png",
    8: "trip1.jpg"
}

for i in photo_gallery:
    print(f'{i}: {photo_gallery[i]}')
l = set(map(int, input("Enter the indexes: ").split(',')))

for i in l:
    if i in photo_gallery:
        print(f"{photo_gallery[i]}")
