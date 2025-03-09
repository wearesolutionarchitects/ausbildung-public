import winsound, time
for i in range(600, 1500, 200):
    winsound.Beep(i, 500)

time.sleep(3)
winsound.PlaySound("SystemQuestion", winsound.SND_ALIAS)
winsound.PlaySound("GAkkord.wav", winsound.SND_FILENAME)
print("Ende")
