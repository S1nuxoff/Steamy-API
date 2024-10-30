# Исходные данные
app_id = 730
market_name = "Glock-18 | AXIA (Field-Tested)"
listing_id = 5250726062740376662
asset_id = 27118964045
context_id = 2

# Список наклеек
stickers = [
    "Sticker | Sphinx",
    "Sticker | Skull Troop",
    "Sticker | FaZe Clan | MLG Columbus 2016",
    "Sticker | Cloud9 (Glitter) | Copenhagen 2024",
]


# Функция для вывода списка наклеек
def display_stickers():
    print("Available Stickers:")
    for i, sticker in enumerate(stickers, 1):
        print(f"{i}. {sticker}")


# Пользователь выбирает наклейку
def choose_sticker():
    display_stickers()
    choice = int(input("Choose a sticker by number: ")) - 1
    if 0 <= choice < len(stickers):
        return stickers[choice]
    else:
        print("Invalid choice. Please try again.")
        return choose_sticker()


# Генерация URL с выбранной наклейкой
def generate_market_url(sticker):
    market_name_encoded = (
        market_name.replace(" ", "%20")
        .replace("|", "%7C")
        .replace("(", "%28")
        .replace(")", "%29")
    )
    sticker_encoded = sticker.replace(" ", "%20").replace("|", "%7C")
    url = f"https://steamcommunity.com/market/listings/{app_id}/{market_name_encoded}?filter={sticker_encoded}#buylisting%7C{listing_id}%7C{app_id}%7C{context_id}%7C{asset_id}"
    return url


# Основной код
chosen_sticker = choose_sticker()
market_url = generate_market_url(chosen_sticker)
print(f"Generated URL: {market_url}")
