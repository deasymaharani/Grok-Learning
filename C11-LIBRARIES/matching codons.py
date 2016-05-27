def matching_codons(complements, poolA, poolB):
    pairs = ()
    result= []
    for i in range(0, len(poolA)):
        for j in range(0, len(poolB)):
            flag = 0
            for k in range(0, len(poolA[i])):
                if poolA[i][k] in complements.keys() and poolB[j][k] == complements[poolA[i][k]]:
                    flag = flag+1
            if flag == 3:
                pairs = (poolA[i], poolB[j])    
                result.append(pairs)
    return result
    