# Εισάγουμε τη βιβλιοθήκη sense_hat για να επικοινωνήσουμε με τα εξαρτήματά του sense HAT.
from sense_emu import SenseHat

# Εισάγουμε την sleep από την βιβλιοθήκη time, για να δώσουμε χρόνο στα απεικονιζόμενα μηνύματα
from time import sleep

# Δίνουμε το όνομα s στην συσκευή μας.
s=SenseHat()

# Με την show_letter απεικονίζουμε ένα χαρακτήρα στην συστοιχία LED.
s.show_letter("a")
sleep(2) # περιμένουμε 2 δευτερόλεπτα για να προλάβουμε να δούμε τον χαρακτήρα m
# Εκχωρούμε το λευκό χρώμα στην μεταβλητή w (white), και
# κανένα χρώμα (μαύρο) στην μεταβλητή b (black):
w = (255,255,255)
b = (0,0,0)
# Σχεδιάζουμε την εικόνα μας, ως μια λίστα 64 στοιχείων (8x8)
smiley = [
b, w, w, w, w, w, w, b,
w, b, b, b, b, b, b, w,
w, b, w, b, b, w, b, w,
w, b, b, b, b, b, b, w,
w, b, w, b, b, w, b, w,
w, b, b, w, w, b, b, w,
w, b, b, b, b, b, b, w,
b, w, w, w, w, w, w, b
]
# εμφανίζουμε την εικόνα μας στην οθόνη:
s.set_pixels(smiley)
sleep(2) # περιμένουμε 2 δευτερόλεπτα για να προλάβουμε να δούμε την εικόνα μας.
# Τέλος εμφανίζουμε το μήνυμα alexandros με πράσινα γράμματα και γκρίζο φόντο:
s.show_message("alexandros",scroll_speed=0.1,text_colour=(0,255,0),back_colour=(100,100,100))

# Το πρόγραμμα τερματίζεται.


# Με την clear() σβήνουμε τυχόν παλιές τιμές
# που έχει δεχθεί η LED συστοιχία
s.clear()

# Αποθηκεύουμε τις τιμές των αισθητήρων θερμοκρασίας,
# υγρασίας και ατμοσφαιρικής πίεσης στις μεταβλητές
# temp, humid και pressure αντίστοιχα.
temp = s.temperature
humid = s.humidity
pressure = s.pressure

# στρογγυλοποιούμε τις παραπάνω τιμές στο πρώτο δεκαδικό:
temp = round(temp,1)
humid = round(humid ,0)
pressure= round(pressure,1)

# Εκτυπώνουμε τις τιμές στην κονσόλα
# προσθέτοντας στο τέλος και τις μονάδες:
print("Θερμοκρασία: ", temp, "C")
print("Υγρασία: ", humid,"%")
print("Ατμοσφαιρική πίεση: ", pressure, "mbar")

# Εμφανίζουμε τις τιμές στη συστοιχία LED:
s.show_message("Temp:"+str(temp)+"C")
s.show_message("Humid:"+str(humid)+"%")
s.show_message("Humid:"+str(s.humidity)+"%")
s.show_message("Pressure:"+str(pressure)+"mbar")


# O Βρόχος while True θα εκτελείται μέχρι να διακόψουμε το πρόγραμμά μας.
while True:
    # Το sense-Hat επιστρέφει ένα λεξικό, που είναι μια 
    # δομή δεδομένων στην python και  περιλαμβάνει τους τίτλους
    # των τριών αξόνων μαζί με τις τιμές τους
    orient=s.orientation
    print(orient)
    # προσθέτουμε μια μικρή παύση 0.1 του δευτερολέπτου στην επανάληψη του βρόχου
    sleep(0.1)
