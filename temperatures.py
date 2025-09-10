# --- Layer 1: Get user input for location type ---
print("📍 Welcome to the Metro Heat Advisory System")
print("Select your location type:")
print("1. Park / Green Space")
print("2. Downtown / Urban Core")
print("3. Residential Area")
location_choice = input("Enter choice (1/2/3): ")

if location_choice == "1":
    location = "Park"
    print("\n You selected: ",location)

    # --- Layer 2: Get current temperature ---
    temp = float(input("Enter current temperature (°C): "))

    if temp > 35:
        print("   Extreme heat detected in green space.")

        # --- Layer 3: Check if shade/water is available ---
        has_shade = input("   Is shaded seating or water mist available here? (yes/no): ").lower()

        if has_shade == "yes":
            print("      Shade/water available.")

            # --- Layer 4: Check visitor density ---
            density = input("      Is the park currently crowded? (low/medium/high): ").lower()

            if density == "high":
                print("          ADVISORY: Activate additional misting stations and deploy hydration volunteers.")
            elif density == "medium":
                print("         ADVISORY: Monitor crowd and prepare extra water supply.")
            else:  # low
                print("         ADVISORY: Normal operations. No immediate action needed.")

        else:  # no shade/water
            print("      NO SHADE/WATER AVAILABLE.")

            # --- Layer 4: Check visitor density ---
            density = input("      Is the park currently crowded? (low/medium/high): ").lower()

            if density == "high" or density == "medium":
                print("        URGENT ADVISORY: Evacuate visitors or provide emergency cooling tents immediately.")
            else:  # low
                print("          ADVISORY: Post warning signs and advise visitors to leave or stay hydrated.")

    elif temp > 30:
        print("    High heat. Recommend hydration stations open.")
    else:
        print("    Temperature is safe. Enjoy the park!")

elif location_choice == "2":
    location = "Downtown"
    print("\n You selected: ",location)
    temp = float(input("Enter current temperature (°C): "))

    if temp > 38:
        print("    CRITICAL HEAT in urban core.")

        # --- Layer 3: Check if cooling centers are open ---
        cooling_open = input("   Are public cooling centers open? (yes/no): ").lower()

        if cooling_open == "yes":
            print("      Cooling centers available.")

            # --- Layer 4: Check public transport AC status ---
            bus_ac = input("      Is public bus air conditioning operational? (yes/no/partial): ").lower()

            if bus_ac == "no":
                print("          ADVISORY: Deploy free shuttle buses with AC to cooling centers.")
            elif bus_ac == "partial":
                print("          ADVISORY: Increase frequency of AC-equipped buses.")
            else:
                print("          ADVISORY: Normal transit. Monitor for system failures.")

        else:  # cooling centers closed
            print("      NO COOLING CENTERS OPEN.")

            # --- Layer 4: Check if it's a weekend ---
            is_weekend = input("      Is today a weekend? (yes/no): ").lower()

            if is_weekend == "yes":
                print("          URGENT: Open emergency centers in libraries/schools. Activate city-wide alert.")
            else:
                print("          URGENT: Coordinate with employers for early release or remote work.")

    else:
        print("    Heat manageable. Monitor for spikes.")

elif location_choice == "3":
    location = "Residential"
    print("\n You selected: ",location)
    temp = float(input("Enter current temperature (°C): "))

    if temp > 36:
        print("    Dangerous heat in residential zone.")

        # --- Layer 3: Check vulnerable population ---
        has_elderly = input("   Are there known elderly or at-risk residents? (yes/no): ").lower()

        if has_elderly == "yes":
            print("       High-risk population present.")

            # --- Layer 4: Check power grid status ---
            power_status = input("      Is the local power grid stable? (stable/brownout/outage): ").lower()

            if power_status == "outage" or power_status == "brownout":
                print("         EMERGENCY: Deploy mobile generators and wellness checks immediately.")
            else:
                print("          ADVISORY: Conduct door-to-door wellness checks and distribute water.")

        else:
            print("       General population.")

            # --- Layer 4: Check power grid status ---
            power_status = input("      Is the local power grid stable? (stable/brownout/outage): ").lower()

            if power_status == "outage":
                print("          ADVISORY: Prioritize power restoration and open neighborhood cooling spots.")
            else:
                print("          ADVISORY: Send SMS alerts and encourage AC use.")

    else:
        print("    Conditions are acceptable.")

else:
    print(" Invalid selection. Please restart and choose 1, 2, or 3.")