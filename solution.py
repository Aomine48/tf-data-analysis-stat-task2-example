import pandas as pd
import numpy as np

from scipy.stats import norm


chat_id = 515069313 # Ваш chat ID, не меняйте название переменной

def solution(p: float, x: np.array) -> tuple:
    # Измените код этой функции
    # Это будет вашим решением
    # Не меняйте название функции и её аргументы
    alpha = 1 - p
    loc = (x.mean() - 0.5) / 3698.0
    scale = 1 / (3698.0 * len(x))
    return gamma.ppf(alpha / 2, len(x), loc=loc, scale=scale), \
           gamma.ppf(1 - alpha / 2, len(x), loc=loc, scale=scale)
