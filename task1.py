def solution(molar_mass1, molar_mass2, given_mass1, given_mass2, volume, temp):
    return ((given_mass1/molar_mass1 + given_mass2/molar_mass2) * 0.082 * (temp+273.15)) / volume

print(solution(44, 30, 3, 2, 5, 50))
print(solution(60, 20, 10, 30, 10, 100))