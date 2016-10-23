**Try that:**

´´´python
message = "swag yolo" #9
anzahl_threads = 1

for i in range(0, anzahl_threads):
	start = i * (len(message)/anzahl_threads) #0
	stop = start + (len(message)/anzahl_threads) #9
´´´
