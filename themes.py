def calculate_trip_cost(num_people, num_days, num_twin_rooms, num_sgl_rooms):
    # Ціни
    twin_price = 190  # ціна за номер TWIN на добу
    sgl_price = 150   # ціна за номер SGL на добу
    transfer_airport = 800  # трансфер готель-аеропорт
    transfer_pool = 250     # трансфер готель-басейн-готель
    lunch_price = 35        # обід на людину
    dinner_price = 45       # вечеря на людину
    gym_price = 200         # спортзал за сесію
    pool_price = 35         # басейн за доріжку на годину

    # Розрахунки
    accommodation_twin = num_twin_rooms * twin_price * num_days
    accommodation_sgl = num_sgl_rooms * sgl_price * num_days

    transfers_airport = transfer_airport * 2  # два трансфери
    transfers_pool = 23 * transfer_pool       # 23 дні трансферів

    lunch = lunch_price * 14 * num_people     # 14 днів обідів
    dinner = dinner_price * 15 * num_people   # 15 днів вечерь

    gym = 9 * gym_price                      # 9 сесій спортзалу
    pool = 5 * 23 * pool_price * 2           # 5 годин, 23 дні, 2 доріжки

    # Загальна вартість послуг
    services_total = transfers_airport + transfers_pool + lunch + dinner + gym + pool

    # Вартість на людину за добу
    cost_per_person_per_day = services_total / num_days / num_people

    # Вартість подорожі на людину за добу
    sgl_cost_per_day = sgl_price + cost_per_person_per_day
    twin_cost_per_day = (twin_price / 2) + cost_per_person_per_day

    return {
        "accommodation_twin": accommodation_twin,
        "accommodation_sgl": accommodation_sgl,
        "services_total": services_total,
        "cost_per_person_per_day": cost_per_person_per_day,
        "sgl_cost_per_day": sgl_cost_per_day,
        "twin_cost_per_day": twin_cost_per_day,
    }

def print_trip_cost(result, num_people):
    print("=" * 50)
    print(f" Вартість поїздки для {num_people} осіб ")
    print("=" * 50)
    print(f"Проживання в TWIN: {result['accommodation_twin']:,} грн")
    print(f"Проживання в SGL: {result['accommodation_sgl']:,} грн")
    print(f"Загальна вартість послуг: {result['services_total']:,} грн")
    print("-" * 50)
    print(f"Вартість послуг на 1 людину/день: {result['cost_per_person_per_day']:.2f} грн")
    print(f"Вартість проживання в SGL за добу: {result['sgl_cost_per_day']:.2f} грн")
    print(f"Вартість проживання в TWIN за добу (1 особа): {result['twin_cost_per_day']:.2f} грн")
    print("=" * 50, "\n")

# Приклад 1: 20 осіб (15 спортсменів, 5 тренерів)
result_1 = calculate_trip_cost(20, 15, 7, 5)
print_trip_cost(result_1, 20)

# Приклад 2: 24 особи (18 спортсменів, 6 тренерів)
result_2 = calculate_trip_cost(24, 15, 9, 6)
print_trip_cost(result_2, 24)
