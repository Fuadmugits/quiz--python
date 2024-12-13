def kuis():
    pertanyaan = {
        "Apa ibu kota Prancis?": "Paris",
        "Siapa penemu lampu pijar?": "Edison",
        "Apa planet terdekat dengan matahari?": 
            "Merkurius"
    }
    skor = 0
    for pertanyaan, jawaban in pertanyaan.items():
        jawaban_user = input(pertanyaan + " ")
        if jawaban_user.lower() == jawaban.lower():
            print("Benar!")
            skor += 1
        else:
            print(f"Salah! Jawaban yang benar adalah {jawaban}.")
    print(f"Skor Anda: {skor}/{len(pertanyaan)}")

kuis()