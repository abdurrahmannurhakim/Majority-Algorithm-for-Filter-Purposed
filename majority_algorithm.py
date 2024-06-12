#============================================================================
# Name        : majority_algorithm.py
# Author      : Abdurrahman Nurhakim
# Version     : 1.0
# Copyright   : Your copyright notice
# Description : Majority and minority selection for filtering purposed
#============================================================================
 

import time

def average(data):
    total = sum(data)
    rata_rata = total / len(data)
    return rata_rata


def constant(real_value, raw_value):
    return (real_value / raw_value)


def detect_outliers(data, threshold):
    #Deteksi nilai mayoritas dan minoritas berdasarkan threshold setelah pengurutan.
   
    sorted_data = sorted(data)
    majorities = []
    minorities = []
    major_indices = []
    minor_indices = []

    # Cari kelompok mayoritas
    temp_majorities = [sorted_data[0]]
    for i in range(1, len(sorted_data)):
        if abs(sorted_data[i] - sorted_data[i - 1]) <= threshold:
            temp_majorities.append(sorted_data[i])
        else:
            if len(temp_majorities) > len(majorities):
                majorities = temp_majorities
            temp_majorities = [sorted_data[i]]
    if len(temp_majorities) > len(majorities):
        majorities = temp_majorities

    # Tentukan nilai minoritas berdasarkan nilai mayoritas
    for i, value in enumerate(data):
        if value in majorities:
            major_indices.append(i)
        else:
            minorities.append(value)
            minor_indices.append(i)

    return majorities, minorities, major_indices, minor_indices


def replace_minorities(data, majorities, minor_indices):
   # Ganti nilai minoritas dengan rata-rata nilai mayoritas.
    if not majorities:
        return data

    major_avg = average(majorities)

    for index in minor_indices:
        data[index] = major_avg

    return data


def read_minority(window_size, threshold):
    data = [508614, 127466, 1011823, 509614, 509785]

    majorities, minorities, major_indices, minor_indices = detect_outliers(
        data, threshold)

    print("raw measure: ", data)
    print("Majorities: ", majorities)
    print("Minorities: ", minorities)
    print("Majority indices: ", major_indices)
    print("Minority indices: ", minor_indices)

    #ganti minoritas dengan dummy value dari rata2 nilai mayoritas
    filtered_measures = replace_minorities(data, majorities, minor_indices)
    #rata2kan kelima nilai array
    total_measures = average(filtered_measures)

    print("Raw measures: ", data)
    print("Filtered measures: ", filtered_measures)
    print("average value: ", total_measures)

    return total_measures


# Contoh penggunaan
if __name__ == "__main__":
    filtered_value = read_minority(window_size=10, threshold=5000)
    print("Filtered value (mode filter):", filtered_value)
