def calculate_meeting_time(distance, speed1, speed2):

  if speed1 <= 0 or speed2 <= 0:
    return None  

  relative_speed = speed1 + speed2  
  meeting_time = distance / relative_speed
  return meeting_time


try:
  distance = float(input("Введите расстояние между автомобилями (км): "))
  speed1 = float(input("Введите скорость первого автомобиля (км/ч): "))
  speed2 = float(input("Введите скорость второго автомобиля (км/ч): "))
except ValueError:
  print("Ошибка: Некорректный ввод. Пожалуйста, введите числа.")
  exit()


meeting_time = calculate_meeting_time(distance, speed1, speed2)

if meeting_time is not None:
  print(f"Автомобили встретятся через {meeting_time:.2f} часа(ов).")
else:
  print("Встреча невозможна, так как один или оба автомобиля не движутся.")

