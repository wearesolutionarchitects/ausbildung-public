import statistics as sta

pa = [5, 2, 4, 17]
print("Liste:", pa)
print("Arithmetischer Mittelwert:", sta.mean(pa))
print("Geometrischer Mittelwert:", sta.geometric_mean(pa))
print("Harmonischer Mittelwert:", sta.harmonic_mean(pa))
print("Median:", sta.median(pa))
print("Unterer Median:", sta.median_low(pa))
print("Oberer Median:", sta.median_high(pa))
print()

pb = [5, 2, 4, 17, 3]
print("Liste:", pb)
print("Median:", sta.median(pb))
print("Unterer Median:", sta.median_low(pb))
print("Oberer Median:", sta.median_high(pb))
print()

pc = [3, 5, 5, 12, 17, 17]
print("Modus:", sta.mode(pc))
print("Multimodus:", sta.multimode(pc))
print()

print("Arithm. Mittelwert aus Tupel:", sta.mean((5, 2, 4, 17)))
pe = {'D':5, 'NL':2, 'CH':4, 'F':17}
print("Arithm. Mittelwert aus Dictionary:", sta.mean(pe.values()))
