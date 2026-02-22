def calculate_risk(findings):

    score = 0

    for f in findings:

        score += f["severity"]

    if score > 80:
        level = "HIGH RISK"    
    elif score > 40:
        level = "MEDIUM RISK"
    else:
        level = "LOW RISK"

    return {
        "score": score,
        "level": level
    }