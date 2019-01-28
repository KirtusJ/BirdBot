def conversion(inp):
    try:
        if not '°' in inp:
            degree = float(inp[:-1]) 
        else:
            degree = float(inp[:-2])
    except Exception as e:
        return e
    opt = ['c','C','f','F'] 
    if inp.endswith(opt[0]) or inp.endswith(opt[1]):
        return f"{round(float(9 * degree / 5 + 32),2)}°F"
    elif inp.endswith(opt[2]) or inp.endswith(opt[3]):
        return f"{round(float((degree - 32) * 5 / 9),2)}°C"
    return "Invalid input"