if __name__ == "__main__":
    temp_string = '%-15s%-15s%-11s%-10s'

    print(temp_string % ('SHIP NAME', 'CLASS', 'DEPLOYMENT', 'IN SERVICE'))
    print(temp_string % ('N2 Bomber',  'Heavy Fighter', 'Limited', "21"))
    print(temp_string % ('J-Type 327',  'Light Combat', 'Unlimited', "1"))
    print(temp_string % ('NX Cruiser',  'Medium Fighter', 'Limited', "18"))
    print(temp_string % ('N1 Starfighter',  'Medium Fighter', 'Unlimited', "25"))
    print(temp_string % ('Royal Cruiser',  'Light Combat', 'Limited', "4"))

