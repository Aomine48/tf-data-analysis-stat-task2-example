import pandas as pd
import numpy as np

from scipy.stats import norm


chat_id = 515069313 # Ваш chat ID, не меняйте название переменной

def solution(p: float, x: np.array) -> tuple:
    # Измените код этой функции
    # Это будет вашим решением
    # Не меняйте название функции и её аргументы
    alpha = 1 - p
    loc = x.mean()/(86*86)
    scale = np.sqrt(np.var(x))/(86*86) / np.sqrt(len(x))
    t_value = norm.ppf(1 - alpha / 2, len(x) - 1)
    ci_lower = loc - t_value * scale / np.sqrt(x.mean() ** 2)
    ci_upper = loc + t_value * scale / np.sqrt(x.mean() ** 2)
    return ci_lower, ci_upper
