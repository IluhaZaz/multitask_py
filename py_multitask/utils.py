import sys
import time
import random
import concurrent.futures


def is_inside_circle(radius: float, x: float, y: float) -> bool:

    """Проверяет, находится ли точка внутри окружности"""

    if y**2 <= (radius**2 - x**2):
        return True
    return False


def count_pi(num_of_points: int, radius: int) -> float:

    """Считает число пи методом Монте-Карло"""

    x = []
    y = []
    in_circle: int = 0
    for i in range(num_of_points):
        x.append(random.uniform(-1 * radius, 1 * radius))
        y.append(random.uniform(-1 * radius, 1 * radius))
    for i in range(num_of_points):
        if is_inside_circle(radius, x[i], y[i]):
            in_circle += 1
    return float(in_circle) / num_of_points * 4


def concurent_count_pi(num_of_points: int, radius: int) -> float:

    """Считает число пи методом Монте-Карло c применением параллельных вычислений"""

    x = []
    y = []
    in_circle: int = 0
    for i in range(num_of_points):
        x.append(random.uniform(-1 * radius, 1 * radius))
        y.append(random.uniform(-1 * radius, 1 * radius))
    with concurrent.futures.ProcessPoolExecutor() as executor:
        res = [
            executor.submit(is_inside_circle, radius, xi, yi) for xi, yi in zip(x, y)
        ]
        for future in concurrent.futures.as_completed(res):
            in_circle += int(future.result())
    return float(in_circle) / num_of_points * 4


def main():

    num_of_points = int(sys.argv[1])
    radius = float(sys.argv[2])

    t0 = time.time()
    res = concurent_count_pi(num_of_points, radius)
    print(
        f"Для функции с параллельными вычислениями: пи =  {res}, время = {time.time() - t0}"
    )

    t0 = time.time()
    res = count_pi(num_of_points, radius)
    print(f"Для обычной функции: пи =  {res}, время = {time.time() - t0}")
