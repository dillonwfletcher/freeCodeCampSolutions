import numpy as np

def calculate(list):
    
    if len(list) != 9:
        raise ValueError("List must contain nine numbers.")

    matrix = np.array(list).reshape((3,3))
    
    mean = [matrix.mean(axis=0).tolist(), matrix.mean(axis=1).tolist(), np.mean(matrix)]
    var = [matrix.var(axis=0).tolist(), matrix.var(axis=1).tolist(), np.var(matrix)]
    std = [matrix.std(axis=0).tolist(), matrix.std(axis=1).tolist(), np.std(matrix)]
    mX = [matrix.max(axis=0).tolist(), matrix.max(axis=1).tolist(), np.max(matrix)]
    mN = [matrix.min(axis=0).tolist(), matrix.min(axis=1).tolist(), np.min(matrix)]
    sM = [matrix.sum(axis=0).tolist(), matrix.sum(axis=1).tolist(), np.sum(matrix)]
    
    return {"mean": mean,
            "variance": var, 
            "standard deviation": std,
            "max": mX, 
            "min": mN,
            "sum": sM}
