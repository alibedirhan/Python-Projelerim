import tkinter as tk

arayuz = tk.Tk()

def çikis():

	etiket['text'] = "Hoşçakal Grafik Arayüzü..."
	dügme['text'] = "Lütfen bekleyin..."
	dügme['state'] = "disabled"
	arayuz.after(2000, arayuz.destroy)

etiket = tk.Label(text="Grafik Arayüzü")
etiket.pack()

dügme = tk.Button(text="Çik", command=çikis)
dügme.pack()

arayuz.protocol("WM_DELETE_WINDOW", çikis)

arayuz.mainloop()
