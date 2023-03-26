def convert_date(date):
    y,m,d = map(int, date.split('.'))
    date = (y*12 + m) * 28 + d
    return date

def solution(today, terms, privacies):
    answer = []
    rules = {}
    for term in terms:
        name, period = term.split()
        period = int(period)
        rules[name] = period * 28

    today = convert_date(today)

    for i, privacy in enumerate(privacies):
        date, rule = privacy.split()
        date = convert_date(date)
        date += rules[rule]
        if date <= today:
            answer.append(i+1)

    return answer