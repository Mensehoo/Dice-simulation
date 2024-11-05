import random

def dice_simulation():
    print("Selamat datang di simulasi lempar dadu!")
    
    while True:
        roll = input("Ketik 'y' untuk lempar dadu atau 'n' untuk keluar: ").lower()
        
        if roll == 'y':
            dice_result = random.randint(1, 6)
            print(f"Anda mendapat angka: {dice_result}")
        elif roll == 'n':
            print("Terima kasih telah menggunakan simulasi dadu. Sampai jumpa!")
            break
        else:
            print("Input tidak valid. Silakan ketik 'y' untuk lempar dadu atau 'n' untuk keluar.")

dice_simulation()
